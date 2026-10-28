#!/usr/bin/env python3
"""Check semantic metadata against visible source, not a search visibility score."""
import json,pathlib
from bs4 import BeautifulSoup
root=pathlib.Path('output');catalog=json.loads(pathlib.Path('examples/catalog.json').read_text())
routes=['','language','development-workflow','performance','examples']+['examples/'+x['slug'] for x in catalog['items']]
titles=set();descriptions=set()
for route in routes:
 soup=BeautifulSoup((root/route/'index.html').read_text(),'html.parser');url='https://kujolang.ai/'+(route+'/' if route else '')
 assert soup.find('link',rel='canonical')['href']==url,url
 assert len(soup.find_all('h1'))==1,url
 title=soup.title.text;description=soup.find('meta',attrs={'name':'description'})['content']
 assert title and title not in titles,url;assert description and description not in descriptions,url
 titles.add(title);descriptions.add(description)
 blocks=[json.loads(x.string) for x in soup.select('script[type="application/ld+json"]')]
 nodes=[]
 for block in blocks:nodes.extend(block.get('@graph',[block]))
 if route:
  crumb=next(x for x in nodes if x.get('@type')=='BreadcrumbList')
  assert crumb['itemListElement'][-1]['item']==url,url
 if route.startswith('examples/'):
  code=next(x for x in nodes if x.get('@type')=='SoftwareSourceCode')
  source=pathlib.Path('public/samples/'+route.split('/')[1]+'.kujo').read_text()
  assert code['text']==source and soup.select_one('.example-source pre code').get_text()==source,url
  assert catalog['commit'] in code['isBasedOn'],url
 if route=='examples':assert any(x.get('@type')=='CollectionPage' for x in nodes),url
 assert soup.select_one('.site-brand')['aria-label']=='Kujo home',url
print(f'Passed canonical, unique metadata, H1, breadcrumb and source alignment checks for {len(routes)} pages.')
