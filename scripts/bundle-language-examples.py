"""Build a reproducible samples archive, or verify its exact contents."""
import gzip
import io
from pathlib import Path
import sys
import tarfile

root = Path(__file__).resolve().parents[1] / 'public' / 'samples'
target = root / 'kujo-examples.tar.gz'
archive = io.BytesIO()
with tarfile.open(fileobj=archive, mode='w', format=tarfile.USTAR_FORMAT) as bundle:
    for path in sorted(root.rglob('*')):
        if not path.is_file() or path == target:
            continue
        data = path.read_bytes()
        entry = tarfile.TarInfo(path.relative_to(root).as_posix())
        entry.size = len(data)
        entry.mode = 0o644
        bundle.addfile(entry, io.BytesIO(data))
output = io.BytesIO()
with gzip.GzipFile(fileobj=output, mode='wb', filename='', mtime=0) as stream:
    stream.write(archive.getvalue())
compressed = output.getvalue()
if '--check' in sys.argv:
    assert gzip.decompress(target.read_bytes()) == archive.getvalue(), 'Samples bundle is stale; run npm run examples:generate'
    print('Samples archive matches every sample and fixture')
else:
    target.write_bytes(compressed)
    print('Built reproducible samples archive')
