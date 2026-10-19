import pathlib,subprocess,json,hashlib,platform
r=pathlib.Path(__file__).parent.resolve();d=r/'zero-cases';d.mkdir(exist_ok=True);env={'PATH':'/usr/bin:/bin:/usr/local/bin','HOME':str(r/'home'),'TMPDIR':str(r)};receipts=[]
def run(args,expected=0):
 p=subprocess.run(['/usr/bin/sandbox-exec','-f',str(r/'isolate.sb'),str(r/'zero')]+args,cwd=d,env=env,text=True,capture_output=True,timeout=60);v={'args':args,'exit':p.returncode,'stdout':p.stdout,'stderr':p.stderr,'expected_exit':expected};receipts.append(v);print(json.dumps(v));return p
run(['--version','--json']);run(['init','--json']);run(['patch','--op','addMain','--op','addCheckWrite fn="main" text="hello from zero\\n"','--json']);run(['check','--json']);run(['test']);run(['run']);run(['export','--json']);run(['verify-projection','--json']);run(['patch','--op','help'])
(r/'zero-receipts.json').write_text(json.dumps({'platform':platform.platform(),'machine':platform.machine(),'binary_sha256':hashlib.sha256((r/'zero').read_bytes()).hexdigest(),'cases':receipts},indent=2)+'\n')
