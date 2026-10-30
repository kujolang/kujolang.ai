#!/usr/bin/env python3
"""Package complete, reproducible applications; verify every archived file."""
import io
import json
from pathlib import Path
import sys
import zipfile
root = Path(__file__).resolve().parents[1]
base = root/'public/workflows'
catalog = json.loads((root/'workflows/catalog.json').read_text())
all_files = {}

def bundle(path, files):
    if '--check' in sys.argv:
        with zipfile.ZipFile(path) as archive:
            assert sorted(archive.namelist()) == sorted(files), str(path)
            for name, value in files.items():
                assert archive.read(name) == value, (str(path), name)
    else:
        data = io.BytesIO()
        with zipfile.ZipFile(data, 'w', zipfile.ZIP_DEFLATED) as archive:
            for name, value in sorted(files.items()):
                entry = zipfile.ZipInfo(name, (1980,1,1,0,0,0))
                entry.external_attr = 0o644 << 16
                entry.compress_type = zipfile.ZIP_DEFLATED
                archive.writestr(entry, value)
        path.write_bytes(data.getvalue())

for item in catalog['items']:
    directory = base/item['slug']
    files = {p.name: p.read_bytes() for p in directory.iterdir() if p.is_file() and (p.name in {'main.kujo', 'common.kujo', 'input.json', 'schema.json', 'README.md', 'draft.txt'} or (p.name.startswith('responses') and p.suffix == '.json'))}
    bundle(base/(item['slug']+'.zip'), files)
    all_files.update({item['slug']+'/'+name: value for name, value in files.items()})
bundle(base/'ai-workflows.zip', all_files)
print('Verified' if '--check' in sys.argv else 'Built', len(catalog['items']), 'application ZIPs and the complete bundle')
