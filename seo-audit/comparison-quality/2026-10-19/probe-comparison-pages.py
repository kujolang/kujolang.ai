import pathlib,json,concurrent.futures,urllib.request,datetime,sys,hashlib
from bs4 import BeautifulSoup
R=pathlib.Path(__file__).resolve().parents[3]; A=R/'seo-audit/comparison-quality/2026-10-19';phase=sys.argv[1];raw=A/'raw'/phase;raw.mkdir(parents=True,exist_ok=True)
C=json.load(open(R/'comparison/catalog.json'));urls=['https://kujolang.ai/compare/']+['https://kujolang.ai/compare/'+p['slug']+'/' for p in C['pages']]
def get(u):
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0 (compatible; KujoComparisonAudit/1.0)'}),timeout=25) as r:
   b=r.read();return dict(url=u,status=r.status,final=r.url,headers=dict(r.headers),body=b.decode(errors='replace'))
 except Exception as e:return dict(url=u,error=str(e))
rows=list(concurrent.futures.ThreadPoolExecutor(8).map(get,urls)); links=set()
for i,r in enumerate(rows):
 if 'body' in r:
  (raw/f'page-{i}.html').write_text(r['body']);s=BeautifulSoup(r['body'],'html.parser');links.update(a['href'] for a in s.select('main a[href]') if a['href'].startswith('https://') and not a['href'].startswith('https://kujolang.ai'))
  r['sha256']=hashlib.sha256(r.pop('body').encode()).hexdigest()
external=list(concurrent.futures.ThreadPoolExecutor(8).map(get,sorted(links)))
for r in external:r.pop('body',None)
(raw/'live.json').write_text(json.dumps({'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pages':rows,'external':external},indent=2))
print(json.dumps({'pages':len(rows),'external':len(external),'errors':[r for r in rows+external if r.get('status')!=200]},indent=2))
