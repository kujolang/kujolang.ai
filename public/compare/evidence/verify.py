#!/usr/bin/env python3
"""Positive/negative artifact verification; no benchmark or model calls."""
import hashlib,json,os,pathlib,platform,shutil,subprocess,sys,tempfile

def valid(text):
    try:
        value=json.loads(text)
        return isinstance(value,dict) and type(value.get('total')) is int and value['total']==42
    except (ValueError,TypeError):
        return False

def main():
    kujo=os.environ.get('KUJO_BIN','kujo')
    version=subprocess.run([kujo,'--version'],capture_output=True,text=True,check=True).stdout.strip()
    if version!='kujo 1.8.1':
        raise SystemExit('This exercise is pinned to kujo 1.8.1; observed '+version)
    source=pathlib.Path(__file__).with_name('produce.kujo')
    command=[kujo,'run',str(source.resolve())]
    result=subprocess.run(command,capture_output=True,text=True,timeout=30)
    # Keep output inspection separate from the producer's process exit.
    with tempfile.TemporaryDirectory() as tmp:
        artifact=pathlib.Path(tmp)/'result.json';artifact.write_text(result.stdout)
        positive_run=subprocess.run([sys.executable,__file__,'--check',str(artifact)],capture_output=True)
        positive=positive_run.returncode==0
        artifact.write_text('{"total":41}')
        negative_run=subprocess.run([sys.executable,__file__,'--check',str(artifact)],capture_output=True)
        negative=negative_run.returncode==0
    controls={text:valid(text) for text in ['{}','not json','{"total":true}','{"total":"42"}','{"total":42.0}']}
    ok=result.returncode==0 and positive and not negative and not any(controls.values())
    receipt={'scope':'Artifact verification exercise; not comparative performance or agent evaluation',
      'version':version,'environment':{'system':platform.system(),'machine':platform.machine(),'release':platform.release(),'python':platform.python_version()},
      'command':command,'exitCode':result.returncode,'stdout':result.stdout,'stderr':result.stderr,
      'runtimeSha256':hashlib.sha256(pathlib.Path(shutil.which(kujo) or kujo).read_bytes()).hexdigest(),
      'sourceSha256':hashlib.sha256(source.read_bytes()).hexdigest(),
      'artifactSha256':hashlib.sha256(result.stdout.encode()).hexdigest(),
      'positiveVerifierExit':positive_run.returncode,'wrongValueVerifierExit':negative_run.returncode,
      'malformedControlsAccepted':controls,'repetitions':1,'passed':ok}
    pathlib.Path('evidence.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print('PASS: correct artifact accepted; incorrect and malformed artifacts rejected' if ok else 'FAIL')
    return 0 if ok else 1
if __name__=='__main__':
    if len(sys.argv)==3 and sys.argv[1]=='--check':
        sys.exit(0 if valid(pathlib.Path(sys.argv[2]).read_text()) else 1)
    sys.exit(main())
