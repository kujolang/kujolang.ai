"""Read-only generated HTML inventory; preserves comparable metadata and hashes."""
import sys,json,csv,hashlib
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urljoin,urlsplit,unquote
class Page(HTMLParser):
 def __init__(self):
  super().__init__(); self.title='';self.h1=[];self.canonical='';self.description='';self.robots='';self.images=[];self.links=[];self.schema=[];self.errors=[];self.active='';self.buf='';self.lang=''
 def handle_starttag(self,t,a):
  d=dict(a)
  if t=='html':self.lang=d.get('lang','')
  if t in ['title','h1']:self.active=t;self.buf=''
  if t=='meta':
   if d.get('name')=='description':self.description=d.get('content','')
   if d.get('name')=='robots':self.robots=d.get('content','')
  if t=='link' and d.get('rel')=='canonical':self.canonical=d.get('href','')
  if t=='img':self.images.append(d)
  if t=='a' and d.get('href'):self.links.append(d['href'])
  if t=='script' and d.get('type')=='application/ld+json':self.active='schema';self.buf=''
 def handle_data(self,d):
  if self.active:self.buf+=d
 def handle_endtag(self,t):
  if t==self.active or (t=='script' and self.active=='schema'):
   if self.active=='title':self.title=self.buf.strip()
   if self.active=='h1':self.h1.append(self.buf.strip())
   if self.active=='schema':
    try:self.schema.append(json.loads(self.buf))
    except ValueError:self.errors.append('invalid JSON-LD')
   self.active='';self.buf=''
root=Path(sys.argv[1]);origin=sys.argv[2];out=Path(sys.argv[3]);rows=[]
for p in sorted(root.rglob('*.html')):
 rel=str(p.relative_to(root));url=origin+'/'+(rel[:-10] if rel.endswith('index.html') else rel);h=Page();b=p.read_bytes();h.feed(b.decode());broken=[]
 for href in h.links:
  u=urlsplit(urljoin(url,href))
  if u.netloc!=urlsplit(origin).netloc:continue
  q=root/unquote(u.path).lstrip('/');q=q/'index.html' if q.is_dir() or not q.suffix else q
  if not q.exists():broken.append(href)
 rows.append(dict(url=url,title=h.title,meta_description=h.description,canonical=h.canonical,h1=h.h1,lang=h.lang,robots=h.robots,images=h.images,links=h.links,schema=h.schema,schema_errors=h.errors,broken_internal_links=sorted(set(broken)),html_bytes=len(b),content_hash=hashlib.sha256(b).hexdigest()))
out.write_text(json.dumps(rows,indent=2));fields=['phase','url','source_file','page_type','local_status','production_status','indexable','robots_directives','canonical','canonical_target_status','title','title_length','meta_description','description_length','h1','heading_structure','word_count','lang','published_date','modified_date','author','breadcrumbs','schema_types','internal_inbound_links','internal_outbound_links','external_outbound_links','broken_internal_links','broken_external_links','image_count','missing_alt','missing_dimensions','page_depth','orphan','sitemap_included','duplicate_title','duplicate_description','content_hash','issues']
from collections import Counter
from xml.etree import ElementTree
counts=Counter(r['title'] for r in rows);descriptions=Counter(r['meta_description'] for r in rows)
inbound=Counter(urljoin(r['url'],x).split('#')[0] for r in rows for x in r['links'])
sitemap=root/'sitemap.xml';sitemap_urls=set()
if sitemap.exists():sitemap_urls={e.text for e in ElementTree.parse(sitemap).iter() if e.tag.endswith('}loc')}
def types(value):
 if isinstance(value,dict):return ([value['@type']] if isinstance(value.get('@type'),str) else [])+[t for v in value.values() for t in types(v)]
 if isinstance(value,list):return [t for v in value for t in types(v)]
 return []
for r in rows:
 r.update(phase=out.stem,source_file='',page_type='generated HTML',local_status=200,production_status='not individually probed',indexable='noindex' not in r['robots'],robots_directives=r['robots'],canonical_target_status=200 if r['canonical'] in {x['url'] for x in rows} else 'not checked',title_length=len(r['title']),description_length=len(r['meta_description']),heading_structure='see preserved HTML',word_count='',published_date='',modified_date='',author='',breadcrumbs='',schema_types=sorted(set(types(r['schema']))),internal_inbound_links=inbound[r['url']],internal_outbound_links=sum(urlsplit(urljoin(r['url'],x)).netloc==urlsplit(origin).netloc for x in r['links']),external_outbound_links=sum(urlsplit(urljoin(r['url'],x)).netloc not in ['',urlsplit(origin).netloc] for x in r['links']),broken_external_links='not exhaustively probed',image_count=len(r['images']),missing_alt=sum('alt' not in i for i in r['images']),missing_dimensions=sum(not i.get('width') or not i.get('height') for i in r['images']),page_depth='not measured',orphan=inbound[r['url']]==0,sitemap_included=r['url'] in sitemap_urls,duplicate_title=counts[r['title']]>1,duplicate_description=descriptions[r['meta_description']]>1,issues=r['schema_errors']+r['broken_internal_links'])
with out.with_suffix('.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows({k:r[k] for k in fields} for r in rows)
print(json.dumps({'pages':len(rows),'missing_titles':sum(not r['title'] for r in rows),'missing_canonicals':sum(not r['canonical'] for r in rows),'schema_errors':sum(len(r['schema_errors']) for r in rows),'broken_internal_destinations':len(set(x for r in rows for x in r['broken_internal_links']))}))
