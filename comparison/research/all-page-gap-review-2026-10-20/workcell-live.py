import json,os,subprocess,tempfile,pathlib,shutil
root=pathlib.Path(os.environ['WORKCELL_REVIEW_SOURCE']).resolve();out=pathlib.Path(os.environ['WORKCELL_REVIEW_OUTPUT']).resolve();out.mkdir(parents=True,exist_ok=True);tmp=pathlib.Path(tempfile.mkdtemp(prefix='workcell-comparison-'));rows=[]
def run(name,args,expected=0):
 p=subprocess.run(args,cwd=root,capture_output=True,text=True,timeout=150);r=dict(name=name,args=args,exit=p.returncode,stdout=p.stdout,stderr=p.stderr);rows.append(r);(out/'results.json').write_text(json.dumps(rows,indent=2));assert p.returncode==expected,r;return r
run('runtime',[os.environ['KUJO'],'--version']);run('docker',['docker','version','--format','{{.Server.Version}}']);repo=tmp/'repo';repo.mkdir()
for args in [['git','init','-q',str(repo)],['git','-C',str(repo),'config','user.email','fixture@example.invalid'],['git','-C',str(repo),'config','user.name','Comparison fixture']]:subprocess.run(args,check=True)
(repo/'README.md').write_text('# Fixture\n');subprocess.run(['git','-C',str(repo),'add','.'],check=True);subprocess.run(['git','-C',str(repo),'commit','-qm','fixture'],check=True)
w=str(root/'bin/workcell')
run('hello',[w,'run','--file','examples/hello/workcell.json','--repo',str(repo),'--output',str(tmp/'hello'),'--no-pull'])
f=next((tmp/'hello').glob('*/receipt.json'));receipt=json.loads(f.read_text());assert receipt['schema_version']=='workcell-receipt/v1';assert (f.parent/'artifacts/hello.txt').read_text()=='hello from Workcell\n';shutil.copy2(f,out/'hello-receipt.json')
v=run('verify-intact',[w,'verify','--run',str(f.parent),'--json']);assert json.loads(v['stdout'])['ok'] is True
with (f.parent/'stdout.log').open('a') as stream:stream.write('changed fixture\n')
v=run('verify-modified',[w,'verify','--run',str(f.parent),'--json'],8);assert json.loads(v['stdout'])['ok'] is False
failure=json.loads((root/'examples/failure/workcell.json').read_text());failure['cleanup']['keep_failed']=False;(tmp/'failure.json').write_text(json.dumps(failure))
run('failed-workload',[w,'run','--file',str(tmp/'failure.json'),'--repo',str(repo),'--output',str(tmp/'failure'),'--no-pull'],7)
f=next((tmp/'failure').glob('*/receipt.json'));shutil.copy2(f,out/'failure-receipt.json')
run('source-unchanged',['git','-C',str(repo),'diff','--exit-code']);shutil.rmtree(tmp);print('Workcell Docker execution, artifact, integrity and failed-workload controls passed')
