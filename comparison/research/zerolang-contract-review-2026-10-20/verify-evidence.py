import json,hashlib
from pathlib import Path
p=Path(__file__).resolve().parent
failed={'source-edit-verify-no-write','strict-stale-check','conflict-check','conflict-run','invalid-source-refresh','invalid-source-import','rollback-type-failure','rollback-unknown-operation','stale-hash-rejection','failing-test','merge-conflicting'}
unchanged=failed|{'clean-status','clean-verify','source-edit-status','dry-run-valid','conflict-status','graph-only-status'}
for file in ['results.json','portable-results.json']:
 rows=json.loads((p/file).read_text());r={x['name']:x for x in rows};assert len(r)==len(rows)==53
 for n,x in r.items():assert x['exit']==(1 if n in failed else 0),(file,n)
 for n in unchanged:assert r[n]['before']==r[n]['after'],(file,n)
 for n in ['source-edit-check-refresh','explicit-import','mtime-independent-refresh','conflict-import-select-source','merge-independent']:
  assert r[n]['before']['zero.graph']!=r[n]['after']['zero.graph'],(file,n)
 expected={'clean-run':'baseline\n','source-edit-run':'human-edit\n','imported-run':'human-edit\n','mtime-independent-run':'human-edit\n','conflict-import-run':'human-edit\n','graph-only-run':'baseline\ngraph-edit\n','conflict-export-run':'baseline\ngraph-edit\n','rollback-original-run':'baseline\n','dry-run-original-run':'baseline\n','merge-independent-run':'left-edit\n','merge-conflicting-original-run':'baseline\n','passing-test':'1 test(s) ok\n'}
 for n,s in expected.items():assert r[n]['stdout']==s,(file,n)
 for n,code in [('strict-stale-check','RGP008'),('conflict-check','RGP006'),('invalid-source-refresh','TYP003'),('invalid-source-import','TYP003'),('merge-conflicting','RGM003')]:
  assert any(d['code']==code for d in json.loads(r[n]['stdout'])['diagnostics']),(file,n)
 assert 'wrong expectation' in r['failing-test']['stderr']
 assert json.loads(r['stale-hash-rejection']['stdout'])['diagnostic']['code']=='GPH002'
s=(p/'merged-projection.0').read_text();assert 'left-edit' in s and 'return left - right' in s
for n,h in json.loads((p/'sha256.json').read_text()).items():assert hashlib.sha256((p/n).read_bytes()).hexdigest()==h,n
print('Verified 53 command observations in each of two runs; rejection cases, file preservation, runtime outputs, diagnostic codes, merged projection and evidence hashes match.')
