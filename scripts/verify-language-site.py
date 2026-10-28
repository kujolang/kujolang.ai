import json,pathlib,re
from html.parser import HTMLParser
r=pathlib.Path('output');c=json.loads(pathlib.Path('examples/catalog.json').read_text());home=(r/'index.html').read_text();sitemap=(r/'sitemap.xml').read_text()
assert home.index('The Kujo programming language') < home.index('data-code-explorer') < home.index('id="ecosystem-title"')
for t in ['Get Started','View Examples','ai_request_hash','ai_chat','home-example']: assert t in home,t
routes=['language','examples','development-workflow','performance']+['examples/'+x['slug'] for x in c['items']]
class Links(HTMLParser):
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  for key in ['href','src']:
   url=d.get(key,'').split('#')[0].split('?')[0]
   if url.startswith('/') and not url.startswith('//'):
    p=r/url.lstrip('/')
    if url.endswith('/'): p=p/'index.html'
    assert p.exists(),url
for route in routes+['']:
 p=r/route/'index.html';html=p.read_text();Links().feed(html)
 assert 'https://kujolang.ai/'+(route+'/' if route else '') in sitemap,route
 assert '&lt;article' not in html,route
 assert '<meta property="og:image"' in html
 if route: assert 'https://kujolang.ai/'+route+'/' in (r/'llms.txt').read_text(),route
for x in c['items']:
 html=(r/'examples'/x['slug']/'index.html').read_text()
 assert 'Pinned source' in html and 'Breadcrumb' in html and x['sha256']
urls=re.findall(r'<loc>(.*?)</loc>',sitemap);assert len(urls)==len(set(urls))
print('Language-first content, all example routes, internal links, sitemap and static fallback passed')
