import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class SiteKitArtifactTests(unittest.TestCase):
    def test_verifies_only_the_requested_output_against_the_vendored_manifest(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / 'site'
            assets = output / 'assets/sitekit'
            shutil.copytree(ROOT / 'assets/sitekit', assets)
            command = [sys.executable, str(ROOT / 'scripts/verify-sitekit.py'), str(output)]

            result = subprocess.run(command, cwd=temporary, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)

            (assets / 'sitekit.css').write_text('incomplete CSS')
            result = subprocess.run(command, cwd=temporary, capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('SiteKit checksum mismatch', result.stderr)

            manifest_file = assets / 'sitekit-manifest.json'
            manifest = json.loads(manifest_file.read_text())
            manifest['files'].pop('sitekit.css')
            manifest_file.write_text(json.dumps(manifest))
            result = subprocess.run(command, cwd=temporary, capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('SiteKit manifest mismatch', result.stderr)
