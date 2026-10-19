import pathlib,subprocess,json,hashlib,platform,re
r=pathlib.Path(__file__).parent.resolve();d=r/'bend-cases';d.mkdir(exist_ok=True);bin=r/'bend/bend/bin/bend'
profile=r/'isolate.sb';profile.write_text('(version 1)\n(allow default)\n(deny network*)\n(deny file-read* (subpath "/Users"))\n(allow file-read* (subpath "'+str(r)+'"))\n(deny file-write*)\n(allow file-write* (subpath "'+str(r)+'") (subpath "/private/tmp"))\n')
env={'PATH':'/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin','HOME':str(r/'home'),'TMPDIR':str(r),'BEND_NO_TELEMETRY':'1','BEND_HOME':str(r/'bend/bend')}
guide=(r/'bend/bend/guide/GUIDE.md').read_text();proof=guide.split('### Laws and Proofs')[1].split('```python')[1].split('```')[0].strip()
files={'good-proof.bend':proof,'bad-proof.bend':proof.replace('case 0n:\n      {==}','case 0n:\n      0n'),'arithmetic.bend':'import Base\n\ndef main() -> U32:\n  (6 * 7 : U32)\n','bad-type.bend':'import Base\n\ndef main() -> U32:\n  "wrong"\n','bad-affine.bend':'import Base\n\ndef twice(x: U32) -> U32:\n  (x + x : U32)\n\ndef main() -> U32:\n  twice(21)\n'}
for n,s in files.items():(d/n).write_text(s+'\n')
receipts=[]
def run(args,expected=None,exe=bin):
 cmd=['/usr/bin/sandbox-exec','-f',str(profile),str(exe)]+args
 try:
  p=subprocess.run(cmd,cwd=d,env=env,capture_output=True,text=True,timeout=60);v={'args':args,'exit':p.returncode,'stdout':p.stdout,'stderr':p.stderr,'expected_exit':expected};print(json.dumps(v));receipts.append(v)
 except Exception as e:receipts.append({'args':args,'error':str(e)});print(str(e))
run(['version'],0)
for n,expected in [('good-proof.bend',0),('bad-proof.bend',1),('arithmetic.bend',0),('bad-type.bend',1),('bad-affine.bend',1)]:run([n,'--check-only'],expected)
run(['good-proof.bend','--verdict'],0);run(['bad-proof.bend','--verdict'],1);run(['arithmetic.bend'],0)
run(['arithmetic.bend','-o','arithmetic.js'],0)
run(['arithmetic.bend','-o','arithmetic-native'],0)
if (d/'arithmetic-native').exists():run([],0,d/'arithmetic-native')
(r/'bend-receipts.json').write_text(json.dumps({'platform':platform.platform(),'machine':platform.machine(),'binary_sha256':hashlib.sha256(bin.read_bytes()).hexdigest(),'archive_sha256':'93eea3f54b7b91f28ea15a1b9f2d825afa58c1fcd417c11024a62f8c3506b813','sandbox':profile.read_text(),'cases':receipts},indent=2)+'\n')
