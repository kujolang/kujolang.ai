"""Verify scoped public pages and exact social/hero assets against local builds."""
import hashlib
import json
from pathlib import Path
import re
import subprocess

HERE = Path(__file__).resolve().parent
SITE = HERE.parents[1]
TARGETS = [
    (SITE, 'https://kujolang.ai', '/ecosystem/kujo-hermes/'),
    (SITE.parent / 'docs.kujolang.ai', 'https://docs.kujolang.ai', '/tools/kujo-hermes/'),
    (SITE.parent / 'kujo-course-1-8-2', 'https://kujo.robertdevore.com', '/hermes/'),
]

def fetch(url):
    return subprocess.check_output(['curl', '-fsSL', '--max-time', '30', url])

checks = []
for repo, origin, route in TARGETS:
    url = origin + route
    raw = fetch(url)
    html = raw.decode()
    assert 'hermes plugins install kujolang/kujo-hermes' in html, url
    assert len(re.findall(r'<h1(?:\s|>)', html)) == 1, url
    canonical = re.search(r'<link rel="canonical" href="([^"]+)', html).group(1)
    assert canonical == url, canonical
    image = re.search(r'<meta property="og:image" content="([^"]+)', html).group(1)
    assert image.startswith(origin + '/'), image
    asset = fetch(image)
    local = repo / 'output' / image[len(origin) + 1:]
    assert hashlib.sha256(asset).digest() == hashlib.sha256(local.read_bytes()).digest(), image
    assert url.encode() in fetch(origin + '/sitemap.xml'), url
    checks.append({'url': url, 'status': 200, 'canonical': canonical, 'h1': 1,
                   'og_image': image, 'asset_matches_local': True,
                   'html_sha256': hashlib.sha256(raw).hexdigest()})
for route in ['/', '/ecosystem/', '/ecosystem/tooling/', '/.well-known/kujo-site-index.json']:
    assert b'kujo-hermes' in fetch('https://kujolang.ai' + route), route
hero = '/assets/images/ecosystem/hermes-verification-console.webp'
assert hashlib.sha256(fetch('https://kujolang.ai' + hero)).digest() == hashlib.sha256((SITE / 'output' / hero[1:]).read_bytes()).digest()
(HERE / 'production-metadata.json').write_text(json.dumps(checks, indent=2) + '\n')
print('PASS: three live pages, canonicals, H1s, sitemaps, exact OG/hero bytes and marketing discovery links')
