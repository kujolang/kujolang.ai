import pathlib,subprocess,json,hashlib,shutil,tempfile
r=pathlib.Path(__file__).parent.resolve(); env={'PATH':'/usr/bin:/bin:/usr/local/bin','HOME':str(r/'home'),'TMPDIR':str(r),'DO_NOT_TRACK':'1'}
def call(binary,args,cwd):
 p=subprocess.run(['/usr/bin/sandbox-exec','-f',str(r/'isolate.sb'),str(binary)]+args,cwd=cwd,env=env,text=True,capture_output=True,timeout=90)
 return {'args':args,'exit':p.returncode,'stdout':p.stdout,'stderr':p.stderr}
d=json.load(open(r/'zero-receipts.json'));z=r/'zero-cases';g=z/'zero.graph'
before=g.read_bytes();v=call(r/'zero',['patch','--json','--op','addFunction name="bad" ret="i32"','--op','addReturnExpr fn="bad" expr="true"'],z);v['graphUnchanged']=before==g.read_bytes();d['cases'].append(v);print('typed patch',v['exit'],v['stdout'][-1000:])
t=pathlib.Path(tempfile.mkdtemp(prefix='zero-review-',dir='/private/tmp'));shutil.copytree(z,t/'package');z=t/'package'
for args in [['export','--json'],['verify-projection','--json']]:
 v=call(r/'zero',args,z);d['cases'].append(v);print(args,v['exit'],v['stdout'][-650:])
p=z/'src/main.0'
if p.exists():
 old=p.read_text();p.write_text(old.replace('hello from zero','changed text'))
 v=call(r/'zero',['verify-projection','--json'],z);d['cases'].append(v);print('divergent',v['exit']);p.write_text(old)
(r/'zero-receipts.json').write_text(json.dumps(d,indent=2)+'\n')
d=json.load(open(r/'baml-receipts.json'));z=r/'baml-cases'
v=call(r/'baml/bin/baml-cli',['pack','total','--output','./total-packed'],z);d['cases'].append(v);print('baml pack',v['exit'],v['stderr'][-500:])
if (z/'total-packed').exists():
 v=call(z/'total-packed',[],z);d['cases'].append(v);print('baml executable',v['exit'],v['stdout']);(z/'total-packed').unlink()
(r/'baml-receipts.json').write_text(json.dumps(d,indent=2)+'\n')
