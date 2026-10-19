import csv,json,pathlib,sys,shutil,collections
R=pathlib.Path(__file__).resolve().parents[3]; A=R/'seo-audit/comparison-quality/2026-10-19'; phase=sys.argv[1];full=A/'raw'/('full-'+phase);full.mkdir(parents=True,exist_ok=True)
urls={'https://kujolang.ai/compare/'}|{'https://kujolang.ai/compare/'+p['slug']+'/' for p in json.load(open(R/'comparison/catalog.json'))['pages']}
for p in A.glob('*.csv'):
 if p.name not in [phase+'.csv','site-inventory.csv','metadata-audit.csv','content-audit.csv','internal-links.csv','external-links.csv','broken-links.csv','image-audit.csv','schema-audit.csv','indexability.csv','crawlability.csv']:continue
 rows=list(csv.DictReader(p.open()));fields=next(csv.reader(p.open()))
 if not rows:continue
 key='url' if 'url' in fields else 'source_url' if 'source_url' in fields else None
 if not key:continue
 shutil.copy2(p,full/p.name);rows=[r for r in rows if r[key] in urls]
 with p.open('w') as f:w=csv.DictWriter(f,fields,lineterminator='\n');w.writeheader();w.writerows(rows)
rows=list(csv.DictReader((A/(phase+'.csv')).open()));meta=list(csv.DictReader((A/'metadata-audit.csv').open()));schemas=list(csv.DictReader((A/'schema-audit.csv').open()));links=list(csv.DictReader((A/'internal-links.csv').open()));imgs=list(csv.DictReader((A/'image-audit.csv').open()))
summary={'phase':phase,'scope':'eight comparison pages; full-site graph used for depth and inbound links','canonical_pages':len(rows),'indexable_pages':sum(r['indexable']=='yes' for r in rows),'missing_titles':sum(not r['title'] for r in rows),'duplicate_titles':sum(r['duplicate_title']=='yes' for r in rows),'missing_descriptions':sum(not r['meta_description'] for r in rows),'duplicate_descriptions':sum(r['duplicate_description']=='yes' for r in rows),'h1_issues':sum(r['h1_count']!='1' for r in meta),'canonical_mismatches':sum(r['canonical']!=r['url'] for r in rows),'orphans':sum(r['orphan']=='yes' for r in rows),'pages_deeper_than_three_clicks':sum(int(r['page_depth'])>3 for r in rows),'broken_internal_links':sum(r['http_status']=='404' for r in links),'missing_alt':sum('missing alt' in r['issues'] for r in imgs),'missing_dimensions':sum('missing intrinsic dimensions' in r['issues'] for r in imgs),'schema_parse_errors':sum(r['parse_state']!='valid JSON' for r in schemas),'sitemap_missing':sum(r['sitemap_included']!='yes' for r in rows),'schema_coverage':sum(bool(r['schema_types']) for r in rows),'issues':{r['url']:r['issues'] for r in rows if r['issues']}}
shutil.copy2(A/(phase+'-summary.json'),full/(phase+'-summary.json'));(A/(phase+'-summary.json')).write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))
