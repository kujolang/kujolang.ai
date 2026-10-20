import pathlib,subprocess,json,hashlib,shutil,os
import argparse,tempfile
ap=argparse.ArgumentParser();ap.add_argument('--binary',required=True);ap.add_argument('--output',required=True);a=ap.parse_args()
p=pathlib.Path(a.output).resolve();p.mkdir(parents=True,exist_ok=True);root=pathlib.Path(tempfile.mkdtemp(prefix='zero-contract-review-'));z=str(pathlib.Path(a.binary).resolve());results=[]
(root/'baseline').mkdir();setup=[]
for args in [['init','--json'],['patch','--json','--op','addMain','--op','addCheckWrite fn="main" text="baseline\\n"','--op','addFunction name="add" ret="i32"','--op','addParam fn="add" name="left" type="i32"','--op','addParam fn="add" name="right" type="i32"','--op','addReturnBinary fn="add" name="+" left="left" right="right" type="i32"'],['export','--json']]:
 x=subprocess.run([z]+args,cwd=root/'baseline',capture_output=True,text=True,timeout=45);setup.append(dict(args=args,exit=x.returncode,stdout=x.stdout,stderr=x.stderr));assert x.returncode==0,(x.stdout,x.stderr)
(p/'setup-results.json').write_text(json.dumps(setup,indent=2)+'\n')
(p/'baseline.0').write_bytes((root/'baseline/src/main.0').read_bytes())
(p/'zero.toml').write_bytes((root/'baseline/zero.toml').read_bytes())

def snap(d):
 return {str(f.relative_to(d)):hashlib.sha256(f.read_bytes()).hexdigest() for f in [d/'zero.graph',d/'zero.toml',*sorted((d/'src').glob('*.0'))] if f.exists()}
def fresh(name):
 d=root/name
 if d.exists():shutil.rmtree(d)
 shutil.copytree(root/'baseline',d);return d
def run(name,d,args,env=None):
 before=snap(d);e=dict(os.environ);e.update(env or {});x=subprocess.run([z]+args,cwd=d,env=e,capture_output=True,text=True,timeout=45);r=dict(name=name,args=args,env=env or {},exit=x.returncode,stdout=x.stdout,stderr=x.stderr,before=before,after=snap(d));results.append(r);(p/'results.json').write_text(json.dumps(results,indent=2)+'\n');print(name,x.returncode,x.stdout[-170:].replace('\n',' '),x.stderr[:150].replace('\n',' '),flush=True);return r
def edit(d,old='baseline',new='human-edit'):
 f=d/'src/main.0';s=f.read_text();assert old in s;f.write_text(s.replace(old,new))
def patch(d,name,ops,extra=[]):return run(name,d,['patch','--json',*extra,*sum((['--op',s] for s in ops),[])])
d=fresh('clean');run('clean-status',d,['status','--json']);run('clean-verify',d,['verify-projection','--json']);run('clean-run',d,['run'])
d=fresh('refresh');edit(d);run('source-edit-status',d,['status','--json']);run('source-edit-verify-no-write',d,['verify-projection','--json']);run('source-edit-check-refresh',d,['check','--json']);run('source-edit-run',d,['run']);run('source-edit-final-verify',d,['verify-projection','--json'])
d=fresh('strict');edit(d);run('strict-stale-check',d,['check','--json'],{'ZERO_STALE':'fail'});run('explicit-import',d,['import','--json']);run('imported-run',d,['run']);run('imported-verify',d,['verify-projection','--json'])
d=fresh('graph-only');patch(d,'graph-only-patch',['addCheckWrite fn="main" text="graph-edit\\n"']);run('graph-only-status',d,['status','--json']);run('graph-only-run',d,['run']);run('graph-only-export',d,['export','--json']);run('graph-only-verify',d,['verify-projection','--json'])
d=fresh('conflict');patch(d,'conflict-graph-edit',['addCheckWrite fn="main" text="graph-edit\\n"']);edit(d);run('conflict-status',d,['status','--json']);run('conflict-check',d,['check','--json']);run('conflict-run',d,['run']);run('conflict-export-select-graph',d,['export','--json']);run('conflict-export-run',d,['run']);run('conflict-export-verify',d,['verify-projection','--json'])
d=fresh('invalid-source');edit(d,'return left + right','return true');run('invalid-source-refresh',d,['check','--json']);run('invalid-source-import',d,['import','--json'])
d=fresh('timestamp');edit(d);os.utime(d/'src/main.0',(1,1));os.utime(d/'zero.graph',(2000000000,2000000000));run('mtime-independent-refresh',d,['check','--json']);run('mtime-independent-run',d,['run'])
d=fresh('rollback');patch(d,'rollback-type-failure',['addCheckWrite fn="main" text="must-not-persist\\n"','addFunction name="bad" ret="i32"','addReturnExpr fn="bad" expr="true"']);run('rollback-original-run',d,['run']);patch(d,'rollback-unknown-operation',['addCheckWrite fn="main" text="must-not-persist\\n"','unknownOperation']);patch(d,'stale-hash-rejection',['expect graphHash "graph:0000000000000000"','addCheckWrite fn="main" text="must-not-persist\\n"'])
d=fresh('dry-run');patch(d,'dry-run-valid',['addCheckWrite fn="main" text="dry-run\\n"'],['--check-only']);run('dry-run-original-run',d,['run'])
d=fresh('tests');patch(d,'add-passing-test',['addTest name="addition works" call="add" arg0="40" arg1="2" expect="42" type="i32"']);run('passing-test',d,['test']);patch(d,'add-failing-test',['addTest name="wrong expectation" call="add" arg0="40" arg1="2" expect="41" type="i32"']);run('valid-graph-wrong-expectation',d,['check','--json']);run('failing-test',d,['test'])
d=fresh('conflict-import');patch(d,'import-conflict-graph-edit',['addCheckWrite fn="main" text="graph-edit\\n"']);edit(d);run('conflict-import-select-source',d,['import','--json']);run('conflict-import-run',d,['run']);run('conflict-import-verify',d,['verify-projection','--json'])
left=fresh('merge-left');right=fresh('merge-right');dest=fresh('merge-result')
run('merge-left-edit',left,['patch','--json','--replace-in-fn','main','--old','baseline','--new','left-edit']);run('merge-right-edit',right,['patch','--json','--replace-in-fn','add','--old','left + right','--new','left - right'])
run('merge-independent',dest,['merge','--json','--base',str(root/'baseline/zero.graph'),'--left',str(left/'zero.graph'),'--right',str(right/'zero.graph')]);run('merge-independent-run',dest,['run']);run('merge-independent-export',dest,['export','--json']);run('merge-independent-verify',dest,['verify-projection','--json']);patch(dest,'merged-add-test',['addTest name="merged subtraction" call="add" arg0="40" arg1="2" expect="38" type="i32"']);run('merged-arithmetic-test',dest,['test']);(p/'merged-projection.0').write_bytes((dest/'src/main.0').read_bytes())
left=fresh('merge-conflict-left');right=fresh('merge-conflict-right');dest=fresh('merge-conflict-result')
run('merge-conflict-left-edit',left,['patch','--json','--replace-in-fn','main','--old','baseline','--new','left-edit']);run('merge-conflict-right-edit',right,['patch','--json','--replace-in-fn','main','--old','baseline','--new','right-edit'])
run('merge-conflicting',dest,['merge','--json','--base',str(root/'baseline/zero.graph'),'--left',str(left/'zero.graph'),'--right',str(right/'zero.graph')]);run('merge-conflicting-original-run',dest,['run'])

shutil.rmtree(root)
