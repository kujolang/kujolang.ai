import csv,json,collections,hashlib,tarfile,datetime
from pathlib import Path
A=Path(__file__).resolve().parent
NA='NOT AVAILABLE — DATA ACCESS REQUIRED'
def rows(n):return list(csv.DictReader((A/n).open()))
def write(n,data,fields=None):
 fields=fields or (list(data[0]) if data else next(csv.reader((A/n).open())))
 with (A/n).open('w') as f:w=csv.DictWriter(f,fields,extrasaction='ignore',lineterminator='\n');w.writeheader();w.writerows(data)
def table(n,values):
 fields=next(csv.reader((A/n).open()));write(n,[dict(zip(fields,v)) for v in values],fields)
base=rows('baseline.csv');ext=rows('external-links.csv');live=json.loads((A/'live-pages.json').read_text());probes=json.loads((A/'external-probes.json').read_text());lookup={r['url']:r for r in live}
for r in base:r['broken_external_links']=sum(x['source_url']==r['url'] and str(x['http_status']) in ['404','410'] for x in ext)
write('baseline.csv',base);write('site-inventory.csv',base)
write('after.csv',[{**r,'phase':'after'} for r in base])
s=json.loads((A/'baseline-summary.json').read_text());s.update(broken_external_destinations=sum(x['status'] in [404,410] for x in probes),external_destinations_checked=len(probes),external_indeterminate=sum(x['status'] in ['',401,403,405,429] for x in probes),p0=0,p1=0)
(A/'baseline-summary.json').write_text(json.dumps(s,indent=2)+'\n');(A/'after-summary.json').write_text(json.dumps({**s,'phase':'after','comparison':'No website changes; identical preserved output verified by SHA-256.'},indent=2)+'\n')
content=rows('content-audit.csv')
for r in content:
 u=r['url'];r['currentness']='Automated inventory plus representative editorial review 2026-10-30; release currency not independently certified for every project';r['citation_worthiness']='First-party source-linked material; actual AI citations unmeasured';r['gap']='No search-demand or cannibalization data';r['action']='Maintain source accuracy; use platform data to choose editorial expansion'
 if '/examples/' in u:
  r.update(purpose='Run and adapt a Kujo example',intent='task-based developer learning',original_evidence='Pinned sample/source checks or application ZIP with authored fixtures, validation and limits',action='Preserve reproducibility and explicit run/check boundaries')
 elif '/compare/' in u:r.update(original_evidence='Dated comparison dimensions and primary-source evidence; no universal speed ranking',action='Review when compared releases materially change')
 elif '/performance/' in u:r.update(original_evidence='Dated ten-run process measurement with source hash and narrow workload boundary',action='Add broader workload evidence only through a separate measured experiment')
 elif '/writing/' in u:r.update(original_evidence='Coming-soon placeholder; no articles',gap='Navigation promises writing but the page has no substantive articles',action='Publish a useful field report or decide whether to remove/noindex the empty listing')
 elif '/ecosystem/skills/' in u:r.update(purpose='Install one released agent skill',intent='technical adoption',original_evidence='Versioned installation and source-backed guidance',action='Retain release boundaries; avoid repetitive keyword expansion')
write('content-audit.csv',content)
table('keyword-map.csv',[[r['phase'],r['url'],r['h1'],'Kujo and first-party ecosystem',next(x['intent'] for x in content if x['url']==r['url']),r['title'].replace(' | Kujo',''),'installation; examples; verification','runtime; source; workflows','How can I use '+r['h1']+'?','https://docs.kujolang.ai/','Demand and overlap unmeasured','Keep website adoption examples complementary to full reference documentation'] for r in base])
questions=['What is Kujo and when should I use it?','How do I install Kujo?','How can I replay an AI response offline?','How do I validate structured model output?','How do I keep private values out of an AI request?','How can I resume an interrupted AI batch?','How do I cache model responses safely?','How does Kujo compare with BAML?','What does Kujo performance evidence establish?','How can I make AI workflow results reviewable?']
table('ai-search-benchmark.csv',[[q,platform,'2026-10-30',NA,NA,NA,NA,NA,NA,NA,'No controlled answer captured','data-availability.md','Benchmark plan only; crawler access is not citation evidence'] for q in questions for platform in ['ChatGPT Search','Bing Copilot','Perplexity']])
table('search-rankings.csv',[[q,'Tool search, provider unspecified','2026-10-30','unknown','unknown','Related Kujo docs and creator project pages returned',NA,'docs.kujolang.ai; robertdevore.com',NA,NA,'research-sources.md','Limited result set; neither an index-coverage test nor a controlled rank observation'] for q in ['site:kujolang.ai Kujo programming language','"Kujo" "deterministic" programming language']])
issues=[
 ['SEO-01','baseline','rendering / headings','P2','https://kujolang.ai/ecosystem/muzzle/',1,'code-heading-findings.json; content/ecosystem/23-muzzle.md:48','Preserve copyable shell comments and a single page H1','High','Low / parser regression review','Fix fenced-code handling or safely render this block; add a regression check for headings inside pre/code','Website maintainer','open; report-only audit'],
 ['SEO-02','baseline','external evidence link','P2','https://kujolang.ai/ecosystem/dispatch/',1,'external-probes.json; GitHub contents API and raw URL independently confirm absent v1.4.0 release-audit file','Let readers verify the release and upgrade assertions','High','Low','Replace only after locating the correct version-specific release evidence; do not guess another release URL','Dispatch/site maintainer','open; report-only audit'],
 ['SEO-03','baseline','content usefulness','P2','https://kujolang.ai/writing/',1,'Preserved baseline HTML says Content coming soon','Make the writing navigation lead to useful content','High','Editorial','Publish a real article or choose an appropriate navigation/indexing treatment for the placeholder','Site owner','editorial recommendation'],
 ['SEO-04','baseline','measurement','P3','https://kujolang.ai/',323,'data-availability.md','Measure actual search and AI visibility','High','Owner access','Provide GSC/Bing AI Performance exports, analytics, verified crawler logs and field CWV','Site owner','data access unavailable'],
 ['SEO-05','baseline','edge validator compatibility','P3','https://kujolang.ai/robots.txt',1,'Lighthouse robots-txt audit; robots-live.txt; crawler-access.csv','Interpret the tool warning without weakening owner policy','High','External / optional','Preserve training restrictions; track Content-Signal validator compatibility and verify actual crawler behavior','Site owner','informational; not a demonstrated indexing outage'],
 ['SEO-06','baseline','redirect efficiency','P3','http://www.kujolang.ai/',1,'redirects.csv: two permanent hops to canonical HTTPS apex','Remove one unnecessary round trip if edge settings are later reviewed','High','External','Optional one-hop canonical redirect; retain path/query handling; no urgent change justified','Site owner','optional recommendation']]
table('issues.csv',issues)
perf=rows('performance.csv')
metrics='\n'.join('| '+r['template']+' | '+str(round(float(r['lcp_ms'])/1000,2))+' s | '+format(float(r['cls']),'.5f')+' | '+str(round(float(r['ttfb_ms'])))+' ms |' for r in perf)
scores={}
for f in (A/'raw/performance').glob('*.json'):
 d=json.loads(f.read_text());scores[f.stem.removeprefix('baseline-')]={k:round(v['score']*100) for k,v in d['categories'].items()}
(A/'lab-scores.json').write_text(json.dumps(scores,indent=2)+'\n')
(A/'executive-summary.md').write_text(f'''# Kujo SEO and AI-search audit

**PASS WITH RECOMMENDATIONS — 30 October 2026.** Technical discovery is healthy. The audit found two concrete page defects and one content gap, with no observed P0 or P1 problem. This was a report-only audit: **323 pages audited; zero website pages changed or deployed**.

## What passed

- **323/323 canonical pages returned HTTP 200** and match the 323-entry sitemap. All live canonicals matched their URLs.
- No missing or duplicate titles/descriptions, missing canonicals, broken internal links, orphan pages, or pages more than three clicks from the homepage in the generated link graph.
- Structured data parses on every page. All 63 examples retain source-backed content; parsing does not establish rich-result eligibility.
- **1,206 image occurrences** have alt attributes and intrinsic dimensions; no missing responsive candidates were found. Decorative empty alt is not treated as an error.
- Googlebot, Bingbot, OAI-SearchBot, ChatGPT-User, Claude-SearchBot, Claude-User, PerplexityBot and Perplexity-User passed all sampled robots/home/key-page/sitemap requests. These are synthetic agent tests, not verified provider-IP logs.
- All 13 host/path/feed/error probes behaved as expected. HTTPwww uses two permanent hops; this is optional polish.

## Prioritized findings

| Priority | Finding | Recommended next action |
|---|---|---|
| P2 | [Muzzle](https://kujolang.ai/ecosystem/muzzle/) renders a shell comment as an H1 inside its code block, creating two H1s and altering the displayed command. | Repair fenced-code rendering and add a regression check. Evidence: [code-heading-findings.json](code-heading-findings.json). |
| P2 | [Dispatch](https://kujolang.ai/ecosystem/dispatch/) links to a missing v1.4.0 release/upgrade evidence file. Both GitHub HTML and raw endpoints return 404; the tag's directory listing lacks the file. | Locate the correct version-specific evidence before replacing the link. |
| P2 | [Writing](https://kujolang.ai/writing/) remains a coming-soon page linked in primary navigation. | Publish substantive material or choose a suitable navigation/indexing treatment. This is a usefulness gap, not a proven search penalty. |
| P3 | Actual search and AI citation outcomes are unmeasured. | Obtain owner exports and run the fixed benchmark plan. |

Of **468 unique external destinations**, **466 returned200**, **one returned 404**, and **one npm page returned403**. The npm version exists in the registry (HTTP 200), so the website 403 is an access limitation, not a confirmed broken package. See [external-links.csv](external-links.csv).

## Production performance

Four Lighthouse 13.0.1 mobile simulated runs scored **98–100 performance**, **100 accessibility**, **100 best practices**, and **92 SEO**. The SEO deduction in all four reports is the same unknown `Content-Signal` directive inserted by Cloudflare. Sampled search crawlers are allowed; the warning does not demonstrate an indexing failure. Preserve the existing training policy.

| Template | Lab LCP | Lab CLS | Document response time |
|---|---:|---:|---:|
{metrics}

These are one-run lab observations, not field Core Web Vitals, INP, or a speed guarantee. Minor cache/image/legacy-JS opportunities are optional experiments given the measured performance. Raw receipts are preserved in [audit-receipts.tar.gz](audit-receipts.tar.gz).

## AI-search readiness and content

The strongest citation candidates are the 63 executable/source-linked examples, dated comparisons, explicit failure boundaries, and reproducible performance receipt. The site explains what checks prove and what they do not. Keep these distinctions when adding content. The documentation site is a complementary reference surface; cannibalization is not established without query data.

Comparable BAML, DSPy and PDL documentation emphasizes examples, task-based tutorials, references and debugging/evaluation paths. Kujo's application downloads are useful original evidence. A next editorial investment should be a measured field report showing a real problem, inputs, failures, results and limitations—not additional generic keyword pages. See [research sources](research-sources.md).

`llms.txt` is available but remains an experimental convenience. Search eligibility, crawler access and valid markup do not prove that an AI system cites the site. Google documents that no special AI markup is required for its search features.

## Visibility and limitations

Search Console/Bing indexing, impressions, clicks, CTR, positions, organic conversions, verified bot logs, backlinks, field CWV/INP, and controlled AI-answer citations: **{NA}**. Public tool searches returned related Kujo docs and creator pages, but do not establish main-site index coverage or rankings. No ranking, traffic or AI-citation improvement is claimed.

Internal SEO/AI-readiness scores: **not assigned**, before or after; a composite would obscure unavailable outcome evidence. P0/P1 counts remain **0/0 before and after**. Site inputs and output are unchanged; findings remain open. Report source commit: `ffad82c72423131674733c3f6a02620b08d2d28a`.

## Next measurements

Use the same URL inventory and benchmark questions on **6 November (7 days), 27 November (28 days), 29 December (60 days), and 28 January 2027 (90 days)**. Compare like-for-like country/device filters and date windows. See [recommendations](recommendations.md), [issues](issues.csv), [data availability](data-availability.md), and [methodology](methodology.md).
''')
(A/'data-availability.md').write_text(f'''# Data availability

Available: complete repository/output crawl, 323 live page bodies and headers, 468 external destinations, 13 redirect probes, 10 crawler profiles, four production Lighthouse receipts, baseline archive/hash manifest, source-backed example verification, and limited public search observations.

Search Console, Bing Webmaster Tools/AI Performance, analytics/conversions, verified CDN/origin logs, full error-URL enumeration, backlink data, field CWV/INP, controlled country/device rankings and controlled AI-answer citations: **{NA}**.

No connected tool exposing these private platform datasets was available. Synthetic user-agent strings do not prove access from actual provider IPs. The small public search result set is not a rank or index-coverage test. AI benchmark rows are a planned protocol and explicitly unmeasured.
''')
(A/'methodology.md').write_text('''# Methodology

Scope: full kujolang.ai site, English-language developer adoption, documentation discovery and runnable examples. User requested an audit report; no content, infrastructure, training-policy or production changes were made. The prior October28 audit covered 26 new pages; this audit covers 323 canonical pages. Counts are not a like-for-like remediation comparison with that older scoped audit.

Delivery: source Markdown/catalogs/templates → pinned Kujo 1.9.0 build.kujo → output → responsive image pipeline → GitHub Actions/GitHub Pages → observed Cloudflare edge → browser/crawler. Current deployment evidence is preserved by the preceding release; this audit independently fetched every live canonical page. DNS/edge configuration access and origin logs were unavailable; response headers and DNS probes are observations, not a complete configuration dump.

Untouched source ffad82c rebuilt using the existing pinned runtime. The task-specific rebuild.py reused 1,167 responsive assets only after verifying input, generator and output hashes. baseline-html.tar.gz preserves HTML/XML/text; baseline-files.json hashes the whole output. baseline-seal.json authenticates these artifacts. Raw live HTML is compressed perURL, with headers/metadata in live-pages.json. audit-receipts.tar.gz retains live, redirect and Lighthouse receipts. Do not overwrite this baseline.

scripts/seo_audit.py inventories generated index.html routes, joins sitemap and HTML links, computes reachability, checks files/images, parses JSON-LD and records metadata. probe-full.py fetches all 323 live URLs with six workers and at most one transient retry, then checks deduplicated external destinations. Source and live metadata/canonical differences are reviewed separately. scripts/probe_site.py checks host/slash/query/error/feed and crawler-agent variants. Four production Lighthouse 13.0.1 mobile simulated runs assess representative templates; no field or causal conclusions follow from one run.

Every page receives automated structural/content inventory. Deeper editorial review samples home, language, performance, comparisons, examples, ecosystem detail/skills, ethos/contact and writing. Content-audit.csv combines template classification with these reviewed examples; it is not a claim of a human sentence-by-sentence review or current-release certification for every ecosystem project. No fabricated author/date/keyword volume was added. Structural validation is not Google rich-result certification.

Because this is report-only, after.csv and after-summary.json are unchanged-output comparison snapshots, not a post-remediation crawl. Whole-output hashes are rechecked at closeout. P0/P1 findings are none; P2 issues are openly recorded. Scores are omitted in favor of verifiable counts. No new deployment is needed for audit artifacts; commits use skip-CI.
''')
(A/'changes.md').write_text('# Changes\n\nNo website source, routes, content, assets, crawler policy or infrastructure changed. Only dated audit/report artifacts and a scoped Loop verification configuration were added. No production deployment was triggered.\n')
(A/'before-after.md').write_text('# Before / after\n\nReport-only audit. Both snapshots contain323 canonical/indexable pages; zero missing/duplicate titles or descriptions, zero missing/mismatched canonicals, zero internal broken links/orphans, one extra-H1 page, one broken external destination, zero schema parse errors, and P0=0/P1=0. All323 live pages returned200. No remediation or outcome improvement is claimed. The complete baseline output hashes are checked unchanged at closeout.\n')
(A/'unresolved.md').write_text(f'# Unresolved\n\nP2: Muzzle fenced shell comment renders as an H1; Dispatch release-evidence URL404; Writing remains a placeholder. These remain recommendations because the user requested a report. The two concrete defects are candidates for a small follow-up fix.\n\nPlatform visibility and field measurements: {NA}. npm HTML403 is indeterminate; its registry version returned200. Training-bot restrictions are deliberate policy, not search-access defects. No P0/P1 or deployment blocker was observed.\n')
(A/'recommendations.md').write_text('''# Recommendations and measurement plan

1. Repair Muzzle's code-fence rendering and verify copied code plus single-H1 output. Locate Dispatch's correct 1.4.0 evidence before changing its link. These are small, concrete follow-up fixes.
2. Replace the Writing placeholder with a real field report: problem, source/version, test setup, failure and recovery, raw results, limitations. Alternatively make an explicit navigation/indexing decision while it is empty; no automatic noindex recommendation is treated as permission.
3. Obtain Google Search Console and Bing Webmaster Tools/AI Performance exports. Review page/query dimensions, selected canonicals, indexed status and sitemap ingestion. Add analytics conversion/referral data and verified crawler/error logs when available.
4. Optional: reduce the HTTPwww two-hop redirect and evaluate Lighthouse cache/image suggestions only with repeat measurements. Preserve current training policy; do not optimize a validator score by removing it.

7 days — 2026-11-06: repeat canonical/crawler/error probes, inspect owner URL-indexing samples, and repeat four mobile production lab runs with the same browser/profile. Record deployment changes.
28 days — 2026-11-27: compare 28-day query/page impressions, clicks, CTR, position distributions, conversions and AI referrals against the previous 28 days using identical country/device filters. Run all 10 fixed questions on each named AI-search platform, recording date, model/search mode, locale, full response, citations and competing domains.
60 days — 2026-12-29: repeat and investigate sustained query/intent gaps. Use actual impressions to distinguish useful docs/examples overlap from cannibalization. Check citation factual accuracy.
90 days — 2027-01-28: assess sustained trends, conversion value, release effects and seasonality. Do not infer causality from one before/after change. Preserve numerator/denominator and missing data.

No recurring automation was requested or created. Keep benchmark wording stable. No keyword-stuffed FAQs, invented case studies or AI-only markup are needed.
''')
with tarfile.open(A/'audit-receipts.tar.gz','w:gz') as t:
 for f in sorted((A/'raw').rglob('*')):
  if f.is_file():t.add(f,arcname=f.relative_to(A))
print('Report completed')
