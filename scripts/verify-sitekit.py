#!/usr/bin/env python3
"""Verify the complete vendored SiteKit release, including runnable assets."""
import hashlib
import json
import sys
from pathlib import Path
root = Path(__file__).resolve().parents[1]
output = Path(sys.argv[1]) if len(sys.argv) > 1 else root / 'output'
source = json.loads((root / 'assets/sitekit-source.json').read_text())
vendored = root / 'assets/sitekit'
published = output / 'assets/sitekit'
manifest = json.loads((vendored / 'sitekit-manifest.json').read_text())
if manifest['version'] != source['version']:
    raise SystemExit(f"SiteKit version mismatch in {vendored}")
if json.loads((published / 'sitekit-manifest.json').read_text()) != manifest:
    raise SystemExit(f"SiteKit manifest mismatch in {published}")
for directory in (vendored, published):
    for name, expected in manifest['files'].items():
        artifact = directory / name
        if hashlib.sha256(artifact.read_bytes()).hexdigest() != expected:
            raise SystemExit(f"SiteKit checksum mismatch: {artifact}")
print(f"SiteKit {source['version']} source/output distribution integrity passed")
