#!/usr/bin/env python3
"""Verify the previously built inputs and outputs have not changed between gates."""
import hashlib,json,pathlib,sys
root=pathlib.Path('.');receipt=pathlib.Path('.loop-engineering/seo-howl-pages/evidence/build-hashes.json')
paths=[pathlib.Path('build.kujo'),pathlib.Path('kujo-ssg.yml')]
for directory in ['assets','templates','content','public','examples','output']:
 paths.extend(p for p in pathlib.Path(directory).rglob('*') if p.is_file())
actual={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
if '--record' in sys.argv:receipt.write_text(json.dumps(actual,indent=2)+'\n')
else:assert actual==json.loads(receipt.read_text()),'Build source/output changed; rebuild before acceptance'
print(f'{len(actual)} build source/output hashes verified')
