from pathlib import Path
import json,hashlib
p=Path(__file__).resolve().parent
read=lambda n:json.loads((p/n).read_text())
a,b=read('stable-results.json'),read('nightly-results.json')
assert len(a)==len(b)==32
assert [(x['name'],x['exit'],x['stdout']) for x in a]==[(x['name'],x['exit'],x['stdout']) for x in b]
assert next(x for x in b if x['name']=='plus-invalid')['exit']==-11
assert all(x['exit']==-11 for x in read('no-handler-results.json'))
for v in ['stable','nightly']:
 c={x['input']:x for x in read('tag-controls.json') if x['version']==v}
 assert c['null']['stdout']=='False\n' and c['false']['stdout']=='True\n'
 assert c['true']['exit']==1 and 'internal omitted argument' in c['true']['stderr']
for c in read('crash-extracts.json'):
 assert c['exception']['signal']=='SIGSEGV'
 assert c['threadState']['r12']['value']&7==2
 assert c['threadState']['rax']['value']==0x0300000000000000
for n,h in read('sha256.json').items():assert hashlib.sha256((p/n).read_bytes()).hexdigest()==h,n
print('Verified: 32 matching boundary outcomes; 2 no-handler crashes; 6 tag controls; 2 native crash extracts. Upstream defect remains unresolved.')
