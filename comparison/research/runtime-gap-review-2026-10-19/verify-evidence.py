from pathlib import Path
import hashlib,json
p=Path(__file__).resolve().parent
checks=[]
def check(name,value):
 checks.append({'name':name,'passed':bool(value)})
 if not value:raise AssertionError(name)
for name,digest in json.loads((p/'sha256.json').read_text()).items():check(name,hashlib.sha256((p/name).read_bytes()).hexdigest()==digest)
for name in ['ci-final/bend.json','baml-client.json']:
 for c in json.loads((p/name).read_text())['cases']:check(c['name'],c['passed'])
check('pack succeeded',json.loads((p/'pack-retry.json').read_text())['exit']==0)
x=json.loads((p/'packed-execution.json').read_text());check('standalone result',x['exit']==0 and x['stdout'].strip()=='42')
for name in ['processes','profiler','spans']:
 x=json.loads((p/f'query-{name}.json').read_text());v=json.loads(x['stdout']);check(name+' query complete',x['exit']==0 and v['outcome']['status']=='complete' and not v['outcome']['diagnostics'] and not v['outcome']['unsealed'])
 if name=='processes':check('success and failure retained',{'success','error'} <= {r[1] for r in v['rows']})
 if name=='profiler':check('profiler outcomes',['user.total',1,0] in v['rows'] and ['user.fail',0,1] in v['rows'])
 if name=='spans':check('return span',any(r[0]=='user.total' and r[1]=='return' for r in v['rows']))
print(json.dumps({'passed':len(checks),'checks':checks},indent=2))
