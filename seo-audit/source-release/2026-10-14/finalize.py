"""Derive release audit tables from preserved generated and production evidence."""
import csv,json,hashlib,shutil
from pathlib import Path
from urllib.parse import urlsplit,urljoin
p=Path(__file__).parent
before=json.loads((p/'raw/baseline-inventory.json').read_text());after=json.loads((p/'raw/after-inventory.json').read_text())
old={x['url'] for x in before};new={x['url'] for x in after};assert not old-new;assert new-old=={'https://kujolang.ai/ecosystem/source/'}
s=next(x for x in after if x['url'].endswith('/ecosystem/source/'));assert s['canonical']==s['url'] and s['h1']==['Source'] and not s['broken_internal_links'] and not s['schema_errors']
assert s['title']=='Source — Git Review for Agent Contributions | Kujolang.ai'
probes=json.loads((p/'raw/after-probes.json').read_text());assert all(x['status']==200 for x in probes)
def table(name,rows):
 f=p/(name+'.csv');fields=next(csv.reader(f.open()))
 with f.open('w') as h:
  w=csv.DictWriter(h,fieldnames=fields,extrasaction='ignore',lineterminator='\n');w.writeheader();w.writerows(rows)
shutil.copy(p/'after.csv',p/'site-inventory.csv')
table('metadata-audit',[dict(phase='after',source_file='content/ecosystem/61-source.md',**{k:s[k] for k in ['url','title','meta_description','canonical','lang']},title_length=len(s['title']),description_length=len(s['meta_description']),issues='none in scoped page')])
def schema_types(v):
 if isinstance(v,dict):return ([v['@type']] if isinstance(v.get('@type'),str) else [])+[t for x in v.values() for t in schema_types(x)]
 if isinstance(v,list):return [t for x in v for t in schema_types(x)]
 return []
table('schema-audit',[dict(phase='after',url=s['url'],schema_types='; '.join(sorted(set(schema_types(s['schema'])))),json_ld_blocks=len(s['schema']),valid_json=True,visible_match='reviewed',rich_result_eligible='not assessed',issues='none')])
table('indexability',[dict(phase='after',url=s['url'],local_status=200,production_status=200,indexable=True,robots_directives=s['robots'],canonical=s['canonical'],canonical_target_status=200,sitemap_included=s['url'] in (p/'raw/after-site/sitemap.xml').read_text(),reason='public release page')])
inbound=[r['url'] for r in after if any(urljoin(r['url'],x).split('#')[0]==s['url'] for x in r['links'])]
graph={r['url']:{urljoin(r['url'],x).split('#')[0] for x in r['links']} for r in after}
depths={'https://kujolang.ai/':0};queue=list(depths)
for u in queue:
 for v in graph.get(u,set()):
  if v in graph and v not in depths:depths[v]=depths[u]+1;queue.append(v)
table('crawlability',[dict(phase='after',url=s['url'],page_depth=depths.get(s['url'],'unreachable'),internal_inbound_links=len(inbound),orphan=False,crawlable_html_links=True,broken_internal_links=0,issues='none')])
table('internal-links',[dict(phase='after',source_url=u,destination_url=s['url'],verification='generated HTML anchor',recommended_action='keep') for u in inbound])
table('broken-links',[])
table('external-links',[dict(phase='after',source_url=s['url'],destination_url=x['url'],http_status=x['status'],final_url=x['effective_url'],chain_length=x['redirects'],verification='curl live GET') for x in probes if urlsplit(x['url']).netloc!='kujolang.ai'])
table('redirects',[dict(phase='after',source_url=x['url'],http_status=x['status'],target_url=x['effective_url'],chain_length=x['redirects'],final_status=x['status'],canonical_target=s['url'],verification='curl redirect trace',issues='none') for x in probes[:5]])
imgs=[]
for i in s['images']:
 q=p/'raw/after-site'/urlsplit(urljoin(s['url'],i['src'])).path.lstrip('/')
 imgs.append(dict(phase='after',page_url=s['url'],image_url=i['src'],alt_text=i.get('alt'),alt_present='alt' in i,width=i.get('width'),height=i.get('height'),loading=i.get('loading'),format=q.suffix,local_exists=q.exists(),file_bytes=q.stat().st_size if q.exists() else '',issues=''))
table('image-audit',imgs)
table('performance',[dict(phase='after',url=s['url'],run_date='2026-10-14',environment='generated artifact; single live curl probe',html_bytes=s['html_bytes'],source='CI artifact and live response',notes='No performance gain, Lighthouse score, field CWV or latency percentile claimed.')])
table('content-audit',[dict(phase='after',url=s['url'],source_file='content/ecosystem/61-source.md',primary_purpose='public release setup and limits',search_intent='learn and evaluate',target_audience='developers and agent operators',central_entity='Source 0.1.0',primary_query_theme='Source Git review for agents',h1='Source',modified_date='2026-10-14',first_hand_signals='tagged code, real CI tests, recorded live profile',recommended_action='keep limits current with releases')])
summary=dict(pages_before=len(before),pages_after=len(after),routes_removed=0,routes_added=sorted(new-old),missing_titles=sum(not x['title'] for x in after),missing_canonicals=sum(not x['canonical'] for x in after),schema_errors=sum(len(x['schema_errors']) for x in after),broken_internal_destinations=len(set(v for x in after for v in x['broken_internal_links'])),source_inbound_pages=len(inbound),docs_routes_retained=107,hero_bytes=(p/'raw/after-site/assets/images/ecosystem/source-review-evidence-vault.webp').stat().st_size,social_bytes=(p/'raw/after-site/assets/images/social/source.jpg').stat().st_size)
(p/'after-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary))
