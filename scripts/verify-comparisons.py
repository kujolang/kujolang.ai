#!/usr/bin/env python3
"""Validate the actual static comparison artifact, not just its source."""
import argparse,json,pathlib,re,sys,urllib.parse,xml.etree.ElementTree as ET
parser=argparse.ArgumentParser();parser.add_argument("--origin",default="https://kujolang.ai");parser.add_argument("--output",default="output");args=parser.parse_args();origin=args.origin.rstrip("/")
from html.parser import HTMLParser
root=pathlib.Path(__file__).resolve().parents[1];out=root/args.output;catalog=json.loads((root/'comparison/catalog.json').read_text())
class Page(HTMLParser):
 def __init__(self,text):
  super().__init__();self.meta={};self.links=[];self.ids=set();self.canonical=[];self.h1=0;self.h2=0;self.tables=0;self.schema=[];self.in_json=False;self.buf='';self.feed(text)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id'in a:self.ids.add(a['id'])
  if tag=='h1':self.h1+=1
  if tag=='h2':self.h2+=1
  if tag=='table':self.tables+=1
  if tag=='meta':self.meta[a.get('name',a.get('property',''))]=a.get('content','')
  if tag=='a' and 'href'in a:self.links.append(a['href'])
  if tag=='link' and a.get('rel')=='canonical':self.canonical.append(a.get('href'))
  if tag=='script' and a.get('type')=='application/ld+json':self.in_json=True;self.buf=''
 def handle_data(self,data):
  if self.in_json:self.buf+=data
 def handle_endtag(self,tag):
  if tag=='script' and self.in_json:self.schema.append(json.loads(self.buf));self.in_json=False
errors=[]
def check(ok,msg):
 if not ok:errors.append(msg)
sitemap=ET.parse(out/'sitemap.xml');urls={n.text for n in sitemap.iter() if n.tag.endswith('}loc')}
routes=['compare/']+['compare/'+p['slug']+'/' for p in catalog['pages']]
titles=[];descriptions=[];total_links=0
for route in routes:
 file=out/route/'index.html';check(file.exists(),route+': missing route')
 if not file.exists():continue
 text=file.read_text();p=Page(text);url=origin+'/'+route
 check(p.h1==1,route+': expected one H1');check(p.canonical==[url],route+': canonical mismatch');check(url in urls,route+': absent from sitemap');check(p.meta.get('og:url')==url,route+': OG URL');check(bool(p.meta.get('description')),route+': description missing');check(bool(p.meta.get('og:image')),route+': image missing');check(bool(p.schema),route+': no schema');check('BreadcrumbList' in json.dumps(p.schema),route+': breadcrumb schema missing');check('noindex' not in p.meta.get('robots',''),route+': noindex');check('{{' not in text,route+': unexpanded template');
 titles+=re.findall(r'<title>(.*?)</title>',text);descriptions.append(p.meta.get('description'))
 for link in p.links:
  u=urllib.parse.urlparse(urllib.parse.urljoin(url,link))
  if u.netloc!=urllib.parse.urlparse(origin).netloc:continue
  total_links+=1;target=out/urllib.parse.unquote(u.path).lstrip('/')
  if target.is_dir():target=target/'index.html'
  check(target.is_file(),route+': broken internal link '+link)
  if u.fragment and target.is_file() and target.suffix=='.html':check(u.fragment in Page(target.read_text()).ids,route+': missing anchor '+link)
 if route=='compare/':
  check(p.tables==1,'hub: expected four-language matrix')
  check({'choose','capabilities','architecture','workflow','evidence','guides'}<=p.ids,'hub: missing section anchors')
  check((out/'compare/text/overview.md').read_bytes()==(root/'public/compare/text/overview.md').read_bytes(),'hub: public overview drift')
 if route!='compare/':
  slug=route.strip('/').split('/')[-1];record=next(r for r in catalog['pages'] if r['slug']==slug)
  check(p.h2>=len(record['sections']),slug+': section HTML missing or escaped')
  if record['kind']=='direct':
   check(p.tables==2+bool(record.get('boundaryReview')),slug+': capability, decision or boundary table missing')
   check({'choose','architecture','capabilities','scenarios','evaluation','boundaries','questions','sources'}<=p.ids,slug+': technical section anchors missing')
  else:
   check(p.tables==2,slug+': decision and example tables missing')
   check({'lenses','decision','practice','example','mistakes','detail','questions','sources','continue'}<=p.ids,slug+': guide anchors missing')
  check((out/'compare/text'/f'{slug}.md').read_bytes()==(root/'public/compare/text'/f'{slug}.md').read_bytes(),slug+': public text drift')
  check(url in (out/'llms.txt').read_text(),slug+': missing llms entry')
check(len(titles)==len(set(titles)),'duplicate comparison titles');check(len(descriptions)==len(set(descriptions)),'duplicate comparison descriptions')
receipt={'routes':len(routes),'internalLinksChecked':total_links,'errors':errors,'passed':not errors}
print(json.dumps(receipt,indent=2));sys.exit(bool(errors))
