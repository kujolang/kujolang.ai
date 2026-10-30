"""Run the full site build and reuse only byte-verified, unchanged responsive assets."""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile

root=Path.cwd();output=root/'output'
hash_file=lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
variants=[p for p in output.rglob('*.webp') if any(p.name.endswith('-'+str(w)+'.webp') for w in [640,960,1280])]
assert len(variants)==1167, 'Only reuse the complete, passing first-run image set'
originals={str(p.relative_to(output)):hash_file(p) for p in output.rglob('*.webp') if p not in variants}
algorithm=hash_file(root/'scripts/generate-responsive-images.mjs')
with tempfile.TemporaryDirectory(prefix='kujo-verified-images-') as tmp:
    hashes={}
    for p in variants:
        rel=p.relative_to(output);destination=Path(tmp)/rel;destination.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,destination);hashes[str(rel)]=hash_file(p)
    subprocess.run(['kujo','run','./build.kujo','--','--site-url','https://kujolang.ai'],check=True)
    rebuilt={str(p.relative_to(output)):hash_file(p) for p in output.rglob('*.webp')}
    assert rebuilt==originals, 'Image inputs changed; regenerate instead of reusing'
    assert hash_file(root/'scripts/generate-responsive-images.mjs')==algorithm
    for rel,digest in hashes.items():
        assert hash_file(Path(tmp)/rel)==digest
        shutil.copyfile(Path(tmp)/rel,output/rel)
        assert hash_file(output/rel)==digest
(root/'seo-audit/2026-10-30/build-image-receipt.json').write_text(json.dumps({'generator_sha256':algorithm,'originals':originals,'responsive_variants':hashes,'basis':'First iteration completed responsive generation and site image contract; final build image inputs match exactly.'},indent=2)+'\n')
print('Full build completed; 1167 responsive variants reused with unchanged input, algorithm and output hashes.')
