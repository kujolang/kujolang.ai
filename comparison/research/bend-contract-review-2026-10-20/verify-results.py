import json,sys
from pathlib import Path
def verify(path):
 rows=json.loads(Path(path).read_text());r={x['name']:x for x in rows};kernel=any(n.startswith('verdict-') for n in r);assert len(r)==len(rows)==(83 if kernel else 76),len(r)
 rejected={'bad-proof','open-law','unsafe','nondecreasing','affine-invalid','foreign','missing-import/PROOF'}
 for n,x in r.items():
  expected=0
  if n.startswith('check-') and n[6:] in rejected:expected=1
  if n.startswith('verdict-') and n[8:] in rejected:expected=1
  if n.startswith(('run-js-exit-','run-native-exit-')):
   code=int(n.rsplit('-',1)[1]);expected=code if code<=255 else 1
  assert x.get('exit')==expected,(n,x)
 for target in ['eval-','run-js-','run-native-']:
  for n,value in [('copy-valid','42'),('overflow','0'),('underflow','4294967295'),('parallel','4096'),('unsafe','42'),('foreign','42')]:assert r[target+n]['stdout'].strip()==value,(target,n)
 for n in ['check-unsafe','check-foreign']:
  assert 'rely on unsafe or foreign code' in r[n]['stderr']
 assert all(x in r['check-unsafe']['stderr'] for x in ['raw','wrapper','main'])
 assert 'PROOF.bend must import ./LAWS.bend' in r['check-missing-import/PROOF']['stderr']
 assert 'decreasing self-call' in r['check-nondecreasing']['stderr']
 assert 'consumed more than once' in r['check-affine-invalid']['stderr']
 for n in ['nat-negative','nat-fraction','nat-bigint','nat-above-limit','nat-string','nat-null','nat-nan','nat-infinity','curried-invalid']:
  v=json.loads(r[n]['stdout']);assert v['kind']=='error' and 'Nat past' in v['message'],n
 for n,v in [('nat-valid',42),('nat-zero',0),('nat-limit',2**53),('inc-valid',42),('curried-valid',5),('word-valid',42),('word-negative',-1),('word-overflow',2**32),('word-string','42')]:
  obj=json.loads(r[n]['stdout']);assert obj['kind']=='return' and obj['value']==v,n
 if kernel:
  for n in ['verdict-good-proof','verdict-filled/PROOF']:assert 'ALL PROOFS CHECK' in r[n]['stdout'],n
 print(json.dumps({'observations':len(rows),'kernelRequested':kernel,'matchedRecordedContract':True}))
if __name__=='__main__':verify(sys.argv[1])
