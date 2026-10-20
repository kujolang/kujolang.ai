import json,hashlib
from pathlib import Path
p=Path(__file__).resolve().parent
rows={f.stem:json.loads(f.read_text()) for f in (p/'receipts').glob('*.json') if f.stem!='dispatch-state'}
expected={'spec-invalid':1,'eval-invalid':1,'artifact-failed-producer':1,'artifact-wrong-runtime':1,'shipcheck-test-actually-fails':7,'shipcheck-contract':1,'docker-availability':None}
for name,row in rows.items():assert row['exit']==expected.get(name,0),(name,row['exit'])
for n,needle in [('sdk-budget','6 passed, 0 failed'),('sdk-runner','32 passed, 0 failed'),('fence-contract','317 passed, 0 failed'),('runledger-contract','81 passed, 0 failed'),('watchdog-proxy','proxy_integration_stub_suite: PASS')]:assert needle in rows[n]['stdout'],n
assert json.loads(rows['spec-valid']['stdout'])['valid'] is True
assert json.loads(rows['spec-invalid']['stdout'])['valid'] is False
assert json.loads(rows['shipcheck-tests-present']['stdout'])['summary']['gate_passed']==1
assert json.loads((p/'receipts/dispatch-state.json').read_text())['status']=='completed'
w={x['name']:x for x in json.loads((p/'workcell-live/results.json').read_text())}
assert len(w)==7
for n,x in w.items():assert x['exit']=={'verify-modified':8,'failed-workload':7}.get(n,0)
assert json.loads(w['verify-intact']['stdout'])['ok'] is True
assert json.loads(w['verify-modified']['stdout'])['ok'] is False
z=json.loads((p/'zero-results/results.json').read_text());assert len(z)==55
assert next(x for x in z if x['name']=='merged-arithmetic-test')['stdout']=='1 test(s) ok\n'
b=json.loads((p/'baml-nightly/results.json').read_text());old=json.loads((p.parent/'baml-crash-nightly-2026-10-20/nightly-results.json').read_text());assert len(b)==32
assert [(x['name'],x['exit'],x['stdout']) for x in b]==[(x['name'],x['exit'],x['stdout']) for x in old]
assert next(x for x in b if x['name']=='plus-invalid')['exit']==-11
sources=json.loads((p/'source-checks.json').read_text())['sources'];assert len(sources)==45 and all(x['ok'] for x in sources)
for name,digest in json.loads((p/'sha256.json').read_text()).items():assert hashlib.sha256((p/name).read_bytes()).hexdigest()==digest,name
print('Retained ecosystem, Docker, artifact, Zerolang and BAML outcomes and hashes verified')
