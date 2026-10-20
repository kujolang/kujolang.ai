import hashlib,json,runpy
from pathlib import Path
root=Path(__file__).resolve().parent
verify=runpy.run_path(str(root/'verify-results.py'))['verify']
for name in ['macos-results.json','linux-results.json']: verify(root/name)
cases=json.loads((root/'kernel-controls.json').read_text())['cases']
assert len(cases)==12 and all(x['passed'] for x in cases)
for name,digest in json.loads((root/'sha256.json').read_text()).items():
 assert hashlib.sha256((root/name).read_bytes()).hexdigest()==digest,name
print('Evidence hashes and 12 kernel controls passed')
