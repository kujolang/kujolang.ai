"""Compare deployed catalog counts, ZIPs and new social cards with release sources."""
import hashlib,json,pathlib,urllib.request,urllib.error,time
root=pathlib.Path.cwd()
base=root/'.loop-engineering/example-gaps/evidence'
slugs=['redacted-summary','grounded-analytics','context-packing','intent-routing','response-cache']
attempts=[]
def fetch(path):
 for attempt in range(1,4):
  request=urllib.request.Request('https://kujolang.ai'+path,headers={'User-Agent':'KujoSiteAudit/1.0','Cache-Control':'no-cache'})
  try:
   with urllib.request.urlopen(request,timeout=30) as response:
    assert response.status==200,path
    attempts.append({'path':path,'attempt':attempt,'status':response.status})
    return response.read()
  except urllib.error.HTTPError as error:
   attempts.append({'path':path,'attempt':attempt,'status':error.code})
   if error.code not in [429,500,502,503,504] or attempt==3:raise
   time.sleep(2)
html=fetch('/examples/').decode()
samples=len(json.loads((root/'examples/catalog.json').read_text())['items'])
apps=len(json.loads((root/'workflows/catalog.json').read_text())['items'])
assert f'<strong>{samples+apps}</strong><span>total examples' in html
assert f'<strong>{apps}</strong><span>AI applications' in html
assert f'Download all {apps} applications' in html
results=[]
paths=[('/workflows/ai-workflows.zip','public/workflows/ai-workflows.zip')]
for slug in slugs:
 paths += [(f'/assets/images/social/examples-{slug}.jpg',f'assets/images/social/examples-{slug}.jpg'),(f'/workflows/{slug}.zip',f'public/workflows/{slug}.zip')]
for remote,local in paths:
 data=fetch(remote)
 assert data==(root/local).read_bytes(),remote
 results.append({'path':remote,'sha256':hashlib.sha256(data).hexdigest(),'matches_source':True})
(base/'live-assets.json').write_text(json.dumps({'total':samples+apps,'samples':samples,'applications':apps,'assets':results,'attempts':attempts},indent=2)+'\n')
print('Live counts and 11 archive/image assets match the release.')
