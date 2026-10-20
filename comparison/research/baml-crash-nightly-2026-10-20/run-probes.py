import argparse,json,subprocess,os
from pathlib import Path
ap=argparse.ArgumentParser();ap.add_argument('--python',required=True);ap.add_argument('--project',required=True);ap.add_argument('--output',required=True);a=ap.parse_args()
cases={
'int':'sdk.echo(42)','string':'sdk.echo("wrong")','numeric-string':'sdk.echo("42")','bool':'sdk.echo(True)','float':'sdk.echo(1.5)','null':'sdk.echo(None)','list-to-int':'sdk.echo([1,"bad"])','async-string':'asyncio.run(sdk.echo_async("wrong"))',
'list-valid':'sdk.items([1,2])','list-invalid-member':'sdk.items([1,"bad"])','optional-invalid':'sdk.optional("bad")','plus-valid':'sdk.plus(41)','plus-invalid':'sdk.plus("bad")',
'missing-arg':'sdk.echo()','unknown-arg':'sdk.echo(1,extra=2)','duplicate-arg':'sdk.echo(1,value=2)','unsupported-object':'sdk.echo(object())','large-int':'sdk.echo(2**80)',
'model-valid':'sdk.Answer(value=42)','model-invalid':'sdk.Answer(value="bad")','model-coercion':'sdk.Answer(value="42")','strict-model':'sdk.Answer.model_validate({"value":"42"},strict=True)',
'class-return-valid':'sdk.answer(sdk.Answer(value=42))','class-return-forged':'sdk.answer(sdk.Answer.model_construct(value="bad"))','field-forged':'sdk.field(sdk.Answer.model_construct(value="bad"))','constructed-return-invalid':'sdk.construct("bad")','class-dict':'sdk.answer({"value":42})',
'parse-valid':'sdk.Extract_spec().parse(\'{"value":42}\')','parse-invalid':'sdk.Extract_spec().parse(\'{"value":"bad"}\')','parse-coercion':'sdk.Extract_spec().parse(\'{"value":"42"}\')','parse-wrong-domain':'sdk.Extract_spec().parse(\'{"value":41}\')',
'strict-host-wrapper':'TypeAdapter(int).validate_python("42",strict=True)'}
results=[]
for name,expr in cases.items():
 code='import json,asyncio,baml_sdk as sdk\nfrom pydantic import TypeAdapter\ntry:\n value='+expr+'\n print(json.dumps({"kind":"return","type":type(value).__name__,"repr":repr(value)}))\nexcept Exception as e:\n print(json.dumps({"kind":"error","type":type(e).__name__,"message":str(e)}))'
 x=subprocess.run([a.python,'-X','faulthandler','-c',code],cwd=a.project,env={'PATH':'/usr/bin:/bin','DO_NOT_TRACK':'1'},capture_output=True,text=True,timeout=25)
 results.append(dict(name=name,expression=expr,exit=x.returncode,stdout=x.stdout,stderr=x.stderr))
 Path(a.output).write_text(json.dumps(results,indent=2)+'\n')
 print(name,x.returncode,flush=True)
