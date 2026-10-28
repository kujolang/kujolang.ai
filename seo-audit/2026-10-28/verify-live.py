#!/usr/bin/env python3
import json,pathlib,hashlib,urllib.request,concurrent.futures
from bs4 import BeautifulSoup
root=pathlib.Path(__file__).resolve().parents[2];audit=pathlib.Path(__file__).resolve().parent
receipts=json.loads((audit/'raw/after/pages.json').read_text());manifest=json.loads((root/'howl-language-pages.json').read_text());catalog=json.loads((root/'examples/catalog.json').read_text())
for i,r in enumerate(receipts):
 assert r['status']==200 and r['canonical']==r['url'],r
 soup=BeautifulSoup((audit/f'raw/after/page-{i:02}.html').read_text(),'html.parser');blocks=[json.loads(x.string) for x in soup.select('script[type="application/ld+json"]')];nodes=[]
 for b in blocks:nodes.extend(b.get('@graph',[b]))
 route=r['url'].removeprefix('https://kujolang.ai').strip('/')
 if route:assert any(x.get('@type')=='BreadcrumbList' for x in nodes),route
 if route.startswith('examples/'):
  code=next(x for x in nodes if x.get('@type')=='SoftwareSourceCode');assert code['text']==(root/('public/samples/'+route.split('/')[1]+'.kujo')).read_text(),route
 assert soup.select_one('.site-brand')['aria-label']=='Kujo home',route
 if not route:assert soup.select_one('.home-hero__media img').get('srcset'),route

def check(card):
 path='assets/images/social/'+card['id']+'.jpg';url='https://kujolang.ai/'+path
 with urllib.request.urlopen(urllib.request.Request(url,headers={"User-Agent":"KujoSiteAudit/1.0"}),timeout=30) as r:body=r.read();status=r.status
 expected=hashlib.sha256((root/path).read_bytes()).hexdigest();actual=hashlib.sha256(body).hexdigest()
 return {'url':url,'status':status,'expected_sha256':expected,'observed_sha256':actual,'matches':expected==actual}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:images=list(pool.map(check,manifest['cards']))
(audit/'raw/after/social-images.json').write_text(json.dumps(images,indent=2)+'\n');assert all(x['status']==200 and x['matches'] for x in images),[x for x in images if not x['matches']]
print('Live: all 26 pages have current schema/accessibility markup and all 26 social images match local SHA-256.')
