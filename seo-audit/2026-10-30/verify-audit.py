import csv,gzip,hashlib,json,tarfile
from pathlib import Path
A=Path(__file__).resolve().parent;R=A.parents[1]
def rows(n):return list(csv.DictReader((A/n).open()))
base=rows('baseline.csv');after=rows('after.csv');live=json.loads((A/'live-pages.json').read_text());seal=json.loads((A/'baseline-seal.json').read_text())
assert len(base)==len(after)==len(live)==323
assert all(r['status']==200 and r['canonical']==r['url'] for r in live)
assert all({k:v for k,v in a.items() if k!='phase'}=={k:v for k,v in b.items() if k!='phase'} for a,b in zip(base,after))
assert hashlib.sha256((A/'baseline-html.tar.gz').read_bytes()).hexdigest()==seal['archive_sha256']
assert hashlib.sha256((A/'baseline-files.json').read_bytes()).hexdigest()==seal['file_manifest_sha256']
for path,digest in json.loads((A/'baseline-files.json').read_text()).items():assert hashlib.sha256((R/'output'/path).read_bytes()).hexdigest()==digest,path
with tarfile.open(A/'baseline-html.tar.gz') as t:
 for m in t.getmembers():
  if m.isfile():assert t.extractfile(m).read()==(R/'output'/m.name).read_bytes(),m.name
assert len(json.loads((A/'external-probes.json').read_text()))==468
assert len(rows('performance.csv'))==4 and all(r['environment'].startswith('Production') for r in rows('performance.csv'))
assert len(rows('ai-search-benchmark.csv'))==30
assert len(rows('keyword-map.csv'))==len(rows('content-audit.csv'))==323
assert sum(r['severity'] in ['P0','P1'] for r in rows('issues.csv'))==0
assert sum(r['severity']=='P2' for r in rows('issues.csv'))==3
for f in A.glob('*.md'):
 assert f.stat().st_size>50,f
 assert 'TODO' not in f.read_text(),f
with tarfile.open(A/'audit-receipts.tar.gz') as t:
 names=set(t.getnames())
 assert all('raw/full/'+r['receipt'] in names for r in live)
 assert sum(n.startswith('raw/performance/') and n.endswith('.json') for n in names)==4
 assert 'raw/live/baseline-production-diagnostics.json' in names
print('Audit verified: 323 local/live pages, unchanged sealed baseline, 468 external destinations, four production lab receipts and complete report datasets.')
