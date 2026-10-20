from pathlib import Path
import subprocess,json
p=Path(__file__).resolve().parent;r=p.parent;env={'PATH':'/usr/bin:/bin','HOME':str(r/'home'),'TMPDIR':str(p),'DO_NOT_TRACK':'1'};py=str(r/'gap-review/venv/bin/python');results=[]
for name,code in [('valid-unsandboxed','import baml_sdk as s; print(s.plus(41))'),('crash-unsandboxed','import baml_sdk as s; print(s.plus("bad"))'),('mutated-field','import baml_sdk as s; a=s.Answer(value=42); a.value="bad"; print(repr(s.field(a)))'),('mutated-class-return','import baml_sdk as s; a=s.Answer(value=42); a.value="bad"; print(s.answer(a))'),('strict-wrapper-valid','import baml_sdk as s; from pydantic import TypeAdapter; print(s.plus(TypeAdapter(int).validate_python(41,strict=True)))')]:
 x=subprocess.run([py,'-X','faulthandler','-c',code],cwd=p/'project',env=env,capture_output=True,text=True,timeout=20);results.append(dict(name=name,code=code,exit=x.returncode,stdout=x.stdout,stderr=x.stderr));print(name,x.returncode,x.stdout,x.stderr[:250])
(p/'followup-results.json').write_text(json.dumps(results,indent=2))
for name,body in [('good','echo(42)'),('bad','echo("wrong")')]:
 f=p/(name+'.baml');f.write_text('function echo(value: int) -> int { value }\nfunction main() -> int { '+body+' }\n')
 x=subprocess.run(['/usr/bin/sandbox-exec','-f',str(r/'isolate.sb'),str(r/'baml/bin/baml-cli'),'check','--file',str(f)],cwd=p,env=env,capture_output=True,text=True,timeout=25);results.append(dict(name='baml-check-'+name,exit=x.returncode,stdout=x.stdout,stderr=x.stderr));print(name,x.returncode,x.stderr[:700])
(p/'followup-results.json').write_text(json.dumps(results,indent=2))
