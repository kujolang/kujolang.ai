import pathlib,subprocess,os,json
import argparse,shutil,platform
ap=argparse.ArgumentParser();ap.add_argument('--bend',default=shutil.which('bend'));ap.add_argument('--bend-home',default=os.environ.get('BEND_HOME'));ap.add_argument('--output',required=True);ap.add_argument('--kernel',action='store_true');a=ap.parse_args();assert a.bend and a.bend_home
p=pathlib.Path(__file__).resolve().parent;f=p/'fixtures';o=pathlib.Path(a.output).resolve();o.mkdir(parents=True,exist_ok=True);env=dict(os.environ,BEND_HOME=str(pathlib.Path(a.bend_home).resolve()),BEND_NO_TELEMETRY='1',CC='/usr/bin/clang');b=str(pathlib.Path(a.bend).resolve());rows=[]
(o/'environment.json').write_text(json.dumps({'platform':platform.platform(),'machine':platform.machine(),'kernelRequested':a.kernel,'node':subprocess.check_output(['node','--version'],text=True).strip()},indent=2))
def run(n,args):
 try:
  x=subprocess.run(args,cwd=f,env=env,capture_output=True,text=True,timeout=60);r=dict(name=n,args=args,exit=x.returncode,stdout=x.stdout,stderr=x.stderr)
 except subprocess.TimeoutExpired as x:r=dict(name=n,args=args,timeout=True,stdout=str(x.stdout),stderr=str(x.stderr))
 rows.append(r);(o/'results.json').write_text(json.dumps(rows,indent=2)+'\n');print(n,r.get('exit','timeout'),r.get('stdout','')[:180].replace('\n',' '),r.get('stderr','')[:180].replace('\n',' '),flush=True);return r
run('version',[b,'version'])
for n in ['good-proof','bad-proof','open-law','unsafe','nondecreasing','copy-valid','affine-invalid','foreign','missing-import/PROOF','filled/PROOF']:
 run('check-'+n,[b,str(f/(n+'.bend')),'--check-only'])
for n in ['copy-valid','overflow','underflow','parallel','unsafe','foreign']:
 run('eval-'+n,[b,str(f/(n+'.bend'))])
 for target in ['js','native']:
  artifact=o/(n+('.js' if target=='js' else ''))
  r=run('build-'+target+'-'+n,[b,str(f/(n+'.bend')),'-o',str(artifact)])
  if r.get('exit')==0:run('run-'+target+'-'+n,['node',str(artifact)] if target=='js' else [str(artifact)])
for n in ['exit-0','exit-7','exit-255','exit-256']:
 for target in ['js','native']:
  artifact=o/(n+('.js' if target=='js' else ''));r=run('build-'+target+'-'+n,[b,str(f/(n+'.bend')),'-o',str(artifact)])
  if r.get('exit')==0:run('run-'+target+'-'+n,['node',str(artifact)] if target=='js' else [str(artifact)])
run('build-host',[b,str(f/'host.bend'),'-o',str(o/'host.mjs')])
cases={'nat-valid':'lib.identity(42)','nat-zero':'lib.identity(0)','nat-limit':'lib.identity(2**53)','nat-negative':'lib.identity(-1)','nat-fraction':'lib.identity(1.5)','nat-bigint':'lib.identity(1n)','nat-above-limit':'lib.identity(2**53+2)','nat-string':'lib.identity("42")','nat-null':'lib.identity(null)','nat-nan':'lib.identity(NaN)','nat-infinity':'lib.identity(Infinity)','inc-valid':'lib.inc(41)','curried-valid':'lib.add(2)(3)','curried-invalid':'lib.add(1)(-1)','word-valid':'lib.word(42)','word-negative':'lib.word(-1)','word-overflow':'lib.word(2**32)','word-string':'lib.word("42")'}
for n,expr in cases.items():
 code='import lib from '+json.dumps((o/'host.mjs').as_uri())+';try { const v='+expr+'; console.log(JSON.stringify({kind:"return",type:typeof v,value:v})); } catch(e) { console.log(JSON.stringify({kind:"error",type:typeof e,message:String(e)})); }';run(n,['node','--input-type=module','-e',code])

if a.kernel:
 for n in ['good-proof','bad-proof','open-law','unsafe','foreign','missing-import/PROOF','filled/PROOF']:
  run('verdict-'+n,[b,str(f/(n+'.bend')),'--verdict'])
if any(x.get('timeout') for x in rows):raise SystemExit('A subprocess timed out; inspect receipts')

import sys
subprocess.run([sys.executable,str(p/"verify-results.py"),str(o/"results.json")],check=True)
