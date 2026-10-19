import pathlib,subprocess,json,hashlib,platform
r=pathlib.Path(__file__).parent.resolve();d=r/'baml-cases';env={'PATH':'/usr/bin:/bin:/usr/local/bin','HOME':str(r/'home'),'TMPDIR':str(r),'DO_NOT_TRACK':'1'};receipts=[];src=d/'baml_src/main.baml';good='function total() -> int { 6 * 7 }\n\ntestset "review" {\n test ("correct total") { assert.equal(total(), 42); }\n}\n'
def run(args,expected=0):
 p=subprocess.run(['/usr/bin/sandbox-exec','-f',str(r/'isolate.sb'),str(r/'baml/bin/baml-cli')]+args,cwd=d,env=env,text=True,capture_output=True,timeout=60);v={'args':args,'exit':p.returncode,'stdout':p.stdout,'stderr':p.stderr,'expected_exit':expected};receipts.append(v);print(json.dumps(v));return p
src.write_text(good);run(['check']);run(['run','total']);run(['test'])
src.write_text(good.replace('42);','41);'));run(['test'],1)
src.write_text('function total() -> int { "wrong" }\n');run(['check'],1)
src.write_text('function total( {\n');run(['check'],1)
src.write_text(good);run(['generate','add','python/pydantic2']);run(['generate']);run(['help','pack'])
(r/'baml-receipts.json').write_text(json.dumps({'platform':platform.platform(),'machine':platform.machine(),'binary_sha256':hashlib.sha256((r/'baml/bin/baml-cli').read_bytes()).hexdigest(),'archive_sha256':'a13b4c004ee011b334bfed31439ba8fb61278e4850b0277774328873deb47ddc','checksumVerified':True,'cases':receipts},indent=2)+'\n')
