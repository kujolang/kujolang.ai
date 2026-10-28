#!/usr/bin/env python3
"""Repeat the same scoped inventory and live checks; full-site crawl remains context."""
import csv,json,pathlib,sys,concurrent.futures,urllib.request,urllib.error,hashlib,datetime
from bs4 import BeautifulSoup
root=pathlib.Path(__file__).resolve().parents[2];audit=pathlib.Path(__file__).resolve().parent
phase=sys.argv[1];context=audit/'context'/phase
catalog=json.loads((root/'examples/catalog.json').read_text())
routes=['/','/language/','/development-workflow/','/performance/','/examples/']+['/examples/'+x['slug']+'/' for x in catalog['items']]
urls=['https://kujolang.ai'+r for r in routes]
(audit/'scope.json').write_text(json.dumps({'date':'2026-10-28','baseline_commit':'9a28242f7838a3571f4f847a77757c1e1cd94cb4','urls':urls,'scope':'26 new/refined pages; full generated site crawled as linking context'},indent=2)+'\n')
raw=audit/'raw'/phase;raw.mkdir(parents=True,exist_ok=True)
def fetch(url):
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'KujoSiteAudit/1.0'})
  with urllib.request.urlopen(req,timeout=25) as r:
   body=r.read();return {'url':url,'status':r.status,'final_url':r.geturl(),'headers':dict(r.headers),'body':body.decode('utf8',errors='replace')}
 except urllib.error.HTTPError as e:return {'url':url,'status':e.code,'final_url':e.geturl(),'headers':dict(e.headers),'error':str(e),'body':''}
 except Exception as e:return {'url':url,'status':'unavailable','error':str(e),'body':''}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool: receipts=list(pool.map(fetch,urls))
for i,r in enumerate(receipts):
 body=r.pop('body');(raw/f'page-{i:02}.html').write_text(body)
 soup=BeautifulSoup(body,'html.parser');can=soup.find('link',rel='canonical')
 r['canonical']=can.get('href') if can else '';r['title']=soup.title.get_text() if soup.title else '';r['sha256']=hashlib.sha256(body.encode()).hexdigest()
(raw/'pages.json').write_text(json.dumps(receipts,indent=2)+'\n')
statuses={r['url']:r['status'] for r in receipts}
for file in context.glob('*.csv'):
 with file.open() as f: reader=csv.DictReader(f);fields=reader.fieldnames;rows=list(reader)
 scoped=[r for r in rows if r.get('url',r.get('source_url',r.get('page_url',''))) in urls]
 for row in scoped:
  if 'production_status' in row:row['production_status']=statuses[row['url']]
 target=audit/file.name
 with target.open('w') as f:w=csv.DictWriter(f,fields);w.writeheader();w.writerows(scoped)
rows=list(csv.DictReader((audit/f'{phase}.csv').open()))
summary={'phase':phase,'pages':len(rows),'production_200':sum(r['production_status']=='200' for r in rows),'indexable':sum(r['indexable']=='yes' for r in rows),'missing_titles':sum(not r['title'] for r in rows),'duplicate_titles':sum(r['duplicate_title']=='yes' for r in rows),'missing_descriptions':sum(not r['meta_description'] for r in rows),'duplicate_descriptions':sum(r['duplicate_description']=='yes' for r in rows),'missing_canonicals':sum(not r['canonical'] for r in rows),'orphans':sum(r['orphan']=='yes' for r in rows),'broken_internal_links':sum(int(r['broken_internal_links']) for r in rows),'schema_types':sorted(set(r['schema_types'] for r in rows))}
(audit/f'{phase}-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
# Check each unique external destination once; protected responses remain indeterminate.
external=list(csv.DictReader((audit/'external-links.csv').open()));destinations=sorted(set(r['destination_url'] for r in external if r['destination_url'].startswith('http')))
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool: ext=list(pool.map(fetch,destinations))
for r in ext:r.pop('body',None)
(raw/'external.json').write_text(json.dumps(ext,indent=2)+'\n');byurl={r['url']:r for r in ext}
for r in external:
 probe=byurl.get(r['destination_url'],{});r['http_status']=probe.get('status','');r['final_url']=probe.get('final_url','');r['verification']='indeterminate/access blocked' if str(r['http_status']) in ['401','403','405','429','unavailable'] else 'live GET observed; not a historical-link assertion'
if external:
 with (audit/'external-links.csv').open('w') as f:w=csv.DictWriter(f,external[0].keys());w.writeheader();w.writerows(external)
print(json.dumps(summary,indent=2));print('external unique destinations',len(destinations))
