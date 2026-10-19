import pathlib,subprocess,json,hashlib
r=pathlib.Path(__file__).parent.resolve();d=r/'zero-cases';env={'PATH':'/usr/bin:/bin:/usr/local/bin','HOME':str(r/'home'),'TMPDIR':str(r)};data=json.load(open(r/'zero-receipts.json'));g=d/'zero.graph'
def run(args,expected=0):
 before=hashlib.sha256(g.read_bytes()).hexdigest();p=subprocess.run(['/usr/bin/sandbox-exec','-f',str(r/'isolate.sb'),str(r/'zero')]+args,cwd=d,env=env,text=True,capture_output=True,timeout=60);after=hashlib.sha256(g.read_bytes()).hexdigest();v={'args':args,'exit':p.returncode,'stdout':p.stdout,'stderr':p.stderr,'expected_exit':expected,'graphUnchanged':before==after};data['cases'].append(v);print(args[:3],p.returncode,p.stdout[:180],p.stderr[:200]);return p
run(['patch','--json','--op','expect graphHash "graph:0000000000000000"','--op','addCheckWrite fn="main" text="must not write"'],1)
run(['patch','--json','--op','addFunction name="bad" ret="i32"','--op','addReturnExpr fn="bad" expr="\"wrong\""'],1)
run(['patch','--json','--op','addFunction name="add" ret="i32"','--op','addParam fn="add" name="left" type="i32"','--op','addParam fn="add" name="right" type="i32"','--op','addReturnBinary fn="add" name="+" left="left" right="right" type="i32"','--op','addTest name="addition works" call="add" arg0="40" arg1="2" expect="42" type="i32"'])
run(['test'])
run(['patch','--json','--op','addTest name="wrong expectation" call="add" arg0="40" arg1="2" expect="41" type="i32"'])
run(['test'],1)
run(['export','--json']);projection=d/'src/main.0'
if projection.exists():
 old=projection.read_bytes();projection.write_text(projection.read_text()+'\n// deliberate divergence\n');run(['verify-projection','--json'],1);projection.write_bytes(old)
run(['check','--json'])
(r/'zero-receipts.json').write_text(json.dumps(data,indent=2)+'\n')
