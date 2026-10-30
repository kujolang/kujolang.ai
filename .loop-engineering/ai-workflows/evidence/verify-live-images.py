import concurrent.futures
import hashlib
import json
import pathlib
import subprocess

root = pathlib.Path.cwd()
manifest = json.loads((root/'howl-ai-workflows.json').read_text())

def verify(card):
    path = 'assets/images/social/' + card['id'] + '.jpg'
    remote = subprocess.check_output(['curl', '--fail', '--silent', '--show-error', '--location', '--retry', '2', '--retry-all-errors', '--connect-timeout', '10', '--max-time', '30', '--user-agent', 'KujoSiteAudit/1.0', 'https://kujolang.ai/' + path], timeout=110)
    expected = hashlib.sha256((root/path).read_bytes()).hexdigest()
    assert hashlib.sha256(remote).hexdigest() == expected, path
    return {'path': path, 'sha256': expected, 'status': 200}

with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
    results = list(pool.map(verify, manifest['cards']))
(root/'.loop-engineering/ai-workflows/evidence/live-images.json').write_text(json.dumps(results, indent=2)+'\n')
print(f'{len(results)} live social images match reviewed local assets')
