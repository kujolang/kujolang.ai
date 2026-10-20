import asyncio,json,pathlib,threading,http.server,platform
import baml_sdk as sdk
from baml_sdk import trace
cases=[];requests=[];mode='good'
class Handler(http.server.BaseHTTPRequestHandler):
 def log_message(self,*args):pass
 def do_POST(self):
  body=json.loads(self.rfile.read(int(self.headers['Content-Length'])))
  requests.append(dict(path=self.path,body=body,authorization=self.headers.get('Authorization')))
  if mode=='http-error':status=401;data={'error':{'message':'fixture unauthorized','type':'authentication_error'}}
  else:
   status=200;content='{"value":42}' if mode=='good' else '{"value":"not-an-integer"}'
   data={'id':'fixture-1','object':'chat.completion','model':'review-fixture','choices':[{'index':0,'message':{'role':'assistant','content':content},'finish_reason':'stop'}],'usage':{'prompt_tokens':1,'completion_tokens':1,'total_tokens':2}}
  raw=json.dumps(data).encode();self.send_response(status);self.send_header('Content-Type','application/json');self.send_header('Content-Length',str(len(raw)));self.end_headers();self.wfile.write(raw)
server=http.server.ThreadingHTTPServer(('127.0.0.1',0),Handler);threading.Thread(target=server.serve_forever,daemon=True).start();url=f'http://127.0.0.1:{server.server_port}'
def check(name,fn,expected=None,error=False):
 try:
  got=fn();passed=not error and (expected is None or got==expected);result=str(got)
 except Exception as e:result=type(e).__name__+': '+str(e);passed=isinstance(error,str) and error in result
 cases.append(dict(name=name,passed=passed,result=result));print(name,passed,flush=True)
check('python-sync',sdk.total,42)
check('python-async',lambda:asyncio.run(sdk.total_async()),42)
check('typed-argument',lambda:sdk.echo(37),37)
check('host-type-boundary-observed',lambda:sdk.echo('wrong'),'wrong')
check('declared-error',sdk.fail,error="BamlError: str: 'review failure'")
check('trace-context',lambda:sdk.context(_baml={'trace':trace.span(inputs=True,output=True).context(metadata={'review':'fixture'},distinct_id='local-test')}).metadata,{'review':'fixture'})
check('trace-context-isolation',lambda:sdk.context().metadata,{})
check('provider-typed-output',lambda:sdk.local_provider(url).value,42)
check('provider-request-shape',lambda:requests[-1]['path']=='/chat/completions' and requests[-1]['body']['model']=='review-fixture' and requests[-1]['authorization']=='Bearer local-fixture-only',True)
mode='bad-schema'
check('provider-schema-rejection',lambda:sdk.local_provider(url),error='ai.errors.ParseFailed')
mode='http-error'
check('provider-http-rejection',lambda:sdk.local_provider(url),error='ai.errors.InvalidRequest')
server.shutdown()
pathlib.Path('../baml-client.json').write_text(json.dumps(dict(platform=platform.platform(),cases=cases,requests=requests),indent=2))
raise SystemExit(0 if all(c['passed'] for c in cases) else 1)
