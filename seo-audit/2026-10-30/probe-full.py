"""Read-only full production and outbound-link verification with bounded retries."""
import concurrent.futures,csv,gzip,hashlib,json,time,urllib.request,urllib.error,urllib.parse
from pathlib import Path
from bs4 import BeautifulSoup
A=Path(__file__).resolve().parent
R=A.parents[1]
raw=A/'raw/full';raw.mkdir(parents=True,exist_ok=True)
def rows(n):return list(csv.DictReader((A/n).open()))
def write(n,data,fields=None):
 with (A/n).open('w') as f:
  w=csv.DictWriter(f,fields or list(data[0]),extrasaction='ignore',lineterminator='\n');w.writeheader();w.writerows(data)
def get(url,save=False):
 history=[]
 for attempt in range(2):
  try:
   with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'KujoSiteAudit/1.0'}),timeout=15) as r:
    body=r.read();d={'url':url,'status':r.status,'final_url':r.geturl(),'headers':dict(r.headers),'bytes':len(body)}
    if save:
     key=hashlib.sha256(url.encode()).hexdigest();(raw/(key+'.html.gz')).write_bytes(gzip.compress(body,mtime=0))
     soup=BeautifulSoup(body,'lxml');c=soup.find('link',rel='canonical');m=soup.find('meta',attrs={'name':'robots'})
     d.update(canonical=c.get('href','') if c else '',title=soup.title.get_text() if soup.title else '',robots=m.get('content','') if m else '',h1_count=len(soup.find_all('h1')),body_sha256=hashlib.sha256(body).hexdigest(),receipt=key+'.html.gz')
    break
  except urllib.error.HTTPError as e:d={'url':url,'status':e.code,'final_url':e.geturl(),'error':str(e)}
  except Exception as e:d={'url':url,'status':'','final_url':url,'error':str(e)}
  history.append(d.copy())
  if d['status'] not in ['',429,500,502,503,504]:break
  time.sleep(1)
 d['prior_attempts']=history
 return d
paths=sorted((R/'output').rglob('index.html'))
urls=['https://kujolang.ai/'+str(p.relative_to(R/'output')).removesuffix('index.html') for p in paths]
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:live=list(pool.map(lambda u:get(u,True),urls))
(A/'live-pages.json').write_text(json.dumps(live,indent=2)+'\n')
print('Live pages',len(live),{str(s):sum(r['status']==s for r in live) for s in set(r['status'] for r in live)},flush=True)
page_map={r['url']:r for r in live}
for name in ['baseline.csv','site-inventory.csv','indexability.csv']:
 data=rows(name)
 for r in data:
  p=page_map[r['url']];r['production_status']=p['status'];r['canonical_target_status']=page_map.get(r['canonical'],{}).get('status',r.get('canonical_target_status',''))
 write(name,data)
s=json.loads((A/'baseline-summary.json').read_text());s['production_200_pages']=sum(r['status']==200 for r in live);(A/'baseline-summary.json').write_text(json.dumps(s,indent=2)+'\n')
ext=rows('external-links.csv');destinations=sorted(set(urllib.parse.urldefrag(r['destination_url'])[0] for r in ext))
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:results=list(pool.map(get,destinations))
(A/'external-probes.json').write_text(json.dumps(results,indent=2)+'\n')
lookup={r['url']:r for r in results}
for r in ext:
 p=lookup[urllib.parse.urldefrag(r['destination_url'])[0]];r['http_status']=p['status'];r['final_url']=p['final_url'];r['chain_length']='not recorded'
 r['verification']='unavailable; confirm manually' if p['status'] in [404,410] else 'indeterminate / access or transport blocked' if p['status'] in ['',401,403,405,429] or isinstance(p['status'],int) and p['status']>=500 else 'live GET'
 r['recommended_action']='review destination' if p['status'] in [404,410] else 'none' if p['status']==200 else 'recheck if business-critical'
write('external-links.csv',ext)
broken=rows('broken-links.csv')+[r for r in ext if r['http_status'] in [404,410]]
write('broken-links.csv',broken,list(ext[0]))
print('External destinations',len(results),{str(s):sum(r['status']==s for r in results) for s in set(r['status'] for r in results)},flush=True)
