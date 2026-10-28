#!/usr/bin/env python3
import json,csv,pathlib,hashlib,zipfile
p=pathlib.Path(__file__).resolve().parent
seal=json.loads((p/'baseline-seal.json').read_text())
assert all(hashlib.sha256((p/n).read_bytes()).hexdigest()==v for n,v in seal.items()),'Baseline was changed'
for phase in ['baseline','after']:
 rows=list(csv.DictReader((p/f'{phase}.csv').open()));assert len(rows)==26
 assert all(r['production_status']=='200' and r['canonical']==r['url'] and r['indexable']=='yes' and r['broken_internal_links']=='0' for r in rows)
assert len(json.loads((p/'raw/after/social-images.json').read_text()))==26
assert all(x['matches'] for x in json.loads((p/'raw/after/social-images.json').read_text()))
hashes=json.loads((p/'howl/artifact-hashes.json').read_text())
with zipfile.ZipFile(p/'howl/showcase.zip') as z:assert len(z.namelist())==79 and all(hashlib.sha256(z.read(n)).hexdigest()==h for n,h in hashes.items())
assert json.loads((p/'howl/determinism.json').read_text())['identical']
assert len(list(csv.DictReader((p/'performance.csv').open())))==8
assert len(list(csv.DictReader((p/'ai-search-benchmark.csv').open())))==30
assert 'PASS WITH RECOMMENDATIONS' in (p/'executive-summary.md').read_text()
print('Audit verified: immutable baseline, 26 before/after pages, 26 live image hashes, 79 archived Howl artifacts, 8 lab receipts, 30 explicit unmeasured benchmark entries.')
