#!/usr/bin/env python3
import csv,json,pathlib,datetime
p=pathlib.Path(__file__).resolve().parent
NA='NOT AVAILABLE — DATA ACCESS REQUIRED'
def rows(n):return list(csv.DictReader((p/n).open()))
def write(n,data):
 fields=next(csv.reader((p/n).open()))
 with (p/n).open('w') as f:w=csv.DictWriter(f,fields);w.writeheader();w.writerows(data)
base=rows('baseline.csv');after=rows('after.csv');scope=json.loads((p/'scope.json').read_text())['urls']
def table(n,values):
 fields=next(csv.reader((p/n).open()));write(n,[dict(zip(fields,v)) for v in values])
table('keyword-map.csv',[[r['phase'],r['url'],r['h1'],'Kujo programming language','informational / developer task',r['title'].replace(' | Kujo',''),'install; run; replay; examples','Kujo runtime; language reference',f"How do I use {r['h1']} in Kujo?",'https://docs.kujolang.ai/','No keyword-volume or cannibalization evidence available','Keep examples practical; link to the reference for full API contracts'] for r in base])
table('search-rankings.csv',[[q,'Tool search; provider not disclosed','2026-10-28','unknown','unknown','docs.kujolang.ai returned; target examples absent from limited results',NA,'Kujo documentation: tools/kujo; start-here; quickstart',NA,NA,'research-sources.md; dated query observation','Not a controlled Google/Bing rank; result absence does not prove non-indexing'] for q in ['site:kujolang.ai/examples Kujo programming language','Kujo programming language deterministic AI request hash']])
questions=['What is Kujo?','How do I install Kujo?','How do I run my first Kujo program?','How do Kujo functions work?','How does Kujo hash an AI request?','Can I replay an AI response offline in Kujo?','How do I validate structured output in Kujo?','How do I test a Kujo program?','What does the Kujo performance measurement prove?','How does Loop Engineering record evidence?']
table('ai-search-benchmark.csv',[[q,platform,'2026-10-28',NA,NA,NA,NA,NA,NA,NA,'No controlled answer captured','data-availability.md','Not run; do not infer citation eligibility from crawler access'] for q in questions for platform in ['ChatGPT Search','Bing Copilot','Perplexity']])
issues=[
 ['SEO-01','baseline','structured data','P2','|'.join(scope[1:]),25,'baseline.csv; raw/baseline/; build.kujo','Represent visible page hierarchy','High','Low','Add BreadcrumbList and identify collection','Repository','resolved'],
 ['SEO-02','baseline','structured data','P2','|'.join(u for u in scope if '/examples/' in u and u!='https://kujolang.ai/examples/'),21,'baseline.csv; examples/catalog.json','Identify exact sample and pinned source','High','Low','Add SoftwareSourceCode from canonical samples','Repository','resolved'],
 ['HOWL-01','baseline','showcase provenance','P2','|'.join(scope),26,'Baseline Git commit howl-social.json: file=social-card.txt','Use real examples in showcase HTML/Markdown','High','Low','Sync metadata, reference actual samples, render and inspect','Repository','resolved'],
 ['SEO-03','baseline','accessibility','P2','|'.join(scope),26,'raw/performance/baseline-home.json: label-content-name-mismatch','Match visible Kujo logo text to accessible name','High','Low','Change shared logo label to Kujo home','Repository','resolved'],
 ['SEO-04','baseline','media','P2',scope[0],1,'raw/performance/baseline-home.json; baseline homepage HTML','Let the browser choose an appropriately sized hero','High','Low','Add srcset using existing generated image variants','Repository','resolved'],
 ['SEO-05','intermediate','performance','P2',scope[0],1,'raw/performance-intermediate/after-home.json','Avoid loading a hidden video poster alongside the responsive hero','High','Low','Load poster on video-open and use preload=none','Repository','resolved'],
 ['OBS-01','after','measurement','P3','|'.join(scope),26,'data-availability.md','Measure actual indexing and search/AI outcomes','High','External','Collect owner-provided console, analytics and verified crawler logs','Site owner','measurement access unavailable'],
 ['OBS-02','baseline','performance','P3',scope[0],1,'raw/performance/baseline-home.json: unused-css-rules and render-blocking-insight','Determine whether shared CSS affects real users','Medium','Medium','Use field data and repeat production lab runs before CSS splitting; local server is uncompressed','Site owner','recommendation; no established field regression']]
table('issues.csv',issues)
content=rows('content-audit.csv')
for r in content:
 url=r['url'];r['audience']='Developers learning or evaluating Kujo';r['currentness']='Reviewed 2026-10-28 against repository sources; no invented publication date'
 if '/examples/' in url and url.rstrip('/')!='https://kujolang.ai/examples':
  r.update(purpose='Copy, understand and verify one small program',intent='Task-based learning',original_evidence='Pinned source, sample SHA-256, command and explicit run/check scope',citation_worthiness='Specific first-party sample; actual citation not measured',gap='No observed content gap; search demand unavailable',action='Retain verification limits and link to full language documentation')
 elif '/performance/' in url:r.update(original_evidence='Existing dated JSON receipt: 10 local process runs; median 33.19 ms',citation_worthiness='Reproducible narrow workload; not a language comparison',action='Keep startup/workload limitations visible',gap='Broader benchmarks require a separately designed experiment')
 else:r.update(original_evidence='First-party installation, workflow or navigation details',citation_worthiness='Useful first-party guidance; actual citation not measured',action='Preserve factual voice and task focus',gap='Console data needed to establish demand or content overlap')
write('content-audit.csv',content)
(p/'data-availability.md').write_text(f'''# Data availability — 2026-10-28

Available: local source/build, full 281-page crawl, scoped 26-page production GET receipts, synthetic crawler probes, redirect chains, external links, four representative local Lighthouse runs per phase, Howl artifacts and GitHub Pages deployment receipts.

Search Console clicks, impressions, CTR, positions and index coverage: {NA}.
Bing Webmaster Tools indexing and AI Performance: {NA}.
Analytics conversions, organic sessions and AI referrals: {NA}.
Verified CDN/origin logs, actual crawler requests, full error-URL enumeration and backlinks: {NA}.
Field Core Web Vitals, including INP: {NA}.
Controlled AI answers/citations and exact country/device Google/Bing rankings: {NA}.

No access was requested to private accounts or granted by the audit tools. Synthetic user-agent requests are not proof of requests from verified provider IPs. A missing result in a short tool search is not proof a page is absent from an index.
''')
(p/'methodology.md').write_text('''# Methodology — 2026-10-28

Scope: the homepage, three guides, Examples index and 21 example pages (scope.json). Audience: English-speaking developers learning/evaluating Kujo. Intended actions: read, install, run a sample and consult the reference. No conversion figures are available.

Authority: repository changes and the existing main-branch GitHub Pages deployment were authorized. DNS/CDN controls, analytics accounts and training-crawler policies were not changed.

Delivery: content/pages and templates → build.kujo → output → responsive-image generation → GitHub Actions Pages artifact → production edge → browser. Source catalog pins samples to a runtime commit; guide generators preserve authored HTML. The generated site contains 281 canonical pages. Full-site context is under context/; primary datasets are scoped to 26 pages.

Baseline source commit: 9a28242f7838a3571f4f847a77757c1e1cd94cb4. Built with tmp/runtime/kujo before source edits. The full untouched output copy remains locally at tmp/seo-baseline-2026-10-28. Durable generated HTML/XML/text archive and a 2,252-file generated SHA-256 inventory, live HTML, headers, complete crawl tables and Lighthouse receipts are sealed by SHA-256 in baseline-seal.json. Reopen/hash verification is required; later crawls must not overwrite these receipts.

Reproduction: python3 scripts/seo_audit.py --output output --audit-dir seo-audit/2026-10-28/context/after --phase after; python3 seo-audit/2026-10-28/audit-scope.py after; python3 scripts/probe_site.py --audit-dir seo-audit/2026-10-28 --phase after --key-path /examples/request-hash/ --skip-external; python3 scripts/extract_lighthouse.py --audit-dir seo-audit/2026-10-28. Do not rerun baseline in this dated directory.

Local crawl robots_allowed is a generated-site check only; actual edge policy is recorded separately in crawler-access.csv. External 401/403/405/429 or transport failures are indeterminate, not broken links. Confirmed 404/410 counts are reported separately. No historical destination assumptions were made.

Lighthouse 13.0.1 uses the same local Python HTTP server, browser, mobile simulated throttling and one run per representative template per phase. This server lacks production compression/cache settings. Lab results are directional, noisy and not field CWV or INP. No controlled significance claim is made.

Content review covers purpose, audience, source attribution, limits, topic overlap, headings and server-rendered readability. The docs site is a related reference surface, not evidence of keyword cannibalization. Search observations are limited; competitive rank/share and AI citations require controlled measurement. No invented author, publication date, review, benchmark or product claim was added. Orwell editing principles were applied to revised captions; no word-count SEO rewrite was performed.

Schema verification checks parsing and alignment with visible breadcrumbs/sample text. It does not establish Google rich-result eligibility. WebPage remains the page entity, SoftwareSourceCode represents its visible sample, and the Examples index is CollectionPage. No special AI schema is claimed.

Internal SEO/AI readiness scores: not scored. Counts and evidence are used instead of a composite that would obscure missing platform data. Lighthouse category scores are lab tool outputs only.
''')
(p/'changes.md').write_text('''# Changes

- Added visible-hierarchy BreadcrumbList to 25 inner pages; marked Examples as CollectionPage.
- Added SoftwareSourceCode to 21 examples using exact public sample text and pinned source links.
- Fixed the shared Kujo logo accessible name. This shared template change also reaches older pages.
- Added responsive homepage hero candidates from the existing image pipeline. The first lab comparison exposed a duplicate hidden video poster download; the final revision defers that poster until video-open and sets preload=none.
- Replaced placeholder sources in 26 Howl entries; added a generated focused manifest and source freshness check. Generated the workflow YAML from the visible guide.
- Rendered all 26 cards through native Howl, saved show/caption receipts, checked 79 artifacts for deterministic output, visually reviewed all 26 social cards in contact-sheet.png, and regenerated the linked social JPEGs and default OG PNG.
- Added semantic regression checks and a dedicated Loop configuration without replacing prior state.

No routes, canonical targets, navigation destinations, training policies, performance claims or sample behavior changed. Howl displays source; the existing runtime gates separately verify samples.
''')
(p/'recommendations.md').write_text('''# Measurement plan

No scheduled automation was requested or created. Reuse scope.json, query themes and ai-search-benchmark.csv without changing wording between runs.

- 7 days (2026-11-04): inspect all 26 URLs in owner-provided Google/Bing indexing reports; inspect sitemap ingestion, selected canonicals and verified crawler logs. Repeat live routing/media probes and four production lab runs with the same device profile.
- 28 days (2026-11-25): compare the preceding 28 days with the prior 28 using the same country/device/property filters. Record clicks, impressions, CTR, position distributions, organic conversions and AI referrals, including denominators. Compare controlled AI answers for all 10 questions on each listed platform; save exact prompts, model/search mode, locale and cited URLs.
- 60 days (2026-12-27): repeat query/page and citation comparisons; review whether docs and examples compete for the same intent using actual impression data. Prefer complementary reference and executable-example roles.
- 90 days (2027-01-26): compare sustained trends, annotate releases and seasonality, and decide whether content or performance work has measured value. No causal claim from a single before/after reading.

Shared CSS splitting is an optional follow-up experiment if repeated production/field evidence supports it; the local uncompressed server exaggerates transfer costs. Keep training-crawler restrictions as an owner decision. Do not add AI-only markup, fabricated FAQ answers or unsupported claims.
''')
(p/'unresolved.md').write_text(f'''# Unresolved measurements

No known in-scope P0/P1 issue. Private console/analytics/log/field data and controlled AI answer benchmarks: {NA}. These limit outcome measurement, not the verified local fixes.

The edge disallows training crawlers GPTBot/ClaudeBot, and the synthetic ClaudeBot fetch is blocked. This is preserved policy, not a search-crawler outage. Search and user-fetch profiles are reported separately. Local robots.txt and edge-served policy differ; production receipts are authoritative for observed edge behavior.

The full-site context includes one pre-existing two-H1 page outside these 26 URLs; it is not presented as a new-page defect. No global editorial rewrite was authorized by this scoped request.

Optional performance work requires repeated production/field evidence before a larger CSS architecture change. No search, traffic, conversion or AI-citation improvement has been established.
''')
if after:
 a=json.loads((p/'after-summary.json').read_text());b=json.loads((p/'baseline-summary.json').read_text())
 (p/'before-after.md').write_text('# Before and after — 26 pages\n\n| Check | Before | After |\n|---|---:|---:|\n'+''.join(f'| {k} | {b[k]} | {a[k]} |\n' for k in ['pages','production_200','indexable','missing_titles','duplicate_titles','missing_descriptions','duplicate_descriptions','missing_canonicals','orphans','broken_internal_links'])+'\nBreadcrumbList coverage: 0 → 25. SoftwareSourceCode coverage: 0 → 21. CollectionPage coverage: 0 → 1. JSON-LD parse errors: 0 → 0. In-scope P0/P1: 0 → 0. Five baseline P2 root causes and one intermediate regression resolved; affected counts overlap. Page count unchanged.\n\nAll 26 have one H1, sitemap membership, canonical targets and language declarations. No pages exceed three clicks. No missing image alt attributes/dimensions or confirmed broken internal destinations. Empty alt text is intentional for decorative media. External statuses and redirect chains are in their CSVs; lab metrics are in performance.csv. Field data is unavailable. Scores are not assigned.\n')
print('Updated editorial audit artifacts')
if after and (p/'raw/after/deployment.json').exists():
 receipt=json.loads((p/'raw/after/deployment.json').read_text())
 perf=rows('performance.csv');pairs={}
 for r in perf:pairs.setdefault(r['template'],{})[r['phase']]=r
 with (p/'before-after.md').open('a') as f:
  f.write('\n## Representative local lab measurements\n\n| Template | Before LCP (ms) | After LCP (ms) | Before / after image bytes |\n|---|---:|---:|---:|\n')
  for name,v in pairs.items():f.write(f"| {name} | {float(v['baseline']['lcp_ms']):.0f} | {float(v['after']['lcp_ms']):.0f} | {v['baseline']['image_bytes']} / {v['after']['image_bytes']} |\n")
  f.write('\nOne run per template per phase. These values do not establish statistical significance or field improvement. Homepage CLS changed from 0 to 0.00049; other sampled templates remained 0. The deterministic improvement is removal of the hidden poster request: final home image transfers total 77,622 bytes versus 242,721 before. An intermediate 319,258-byte result exposed the duplicate download and was corrected before release.\n\nAll 38 unique scoped external destinations returned 200 in each phase. All 13 production routing probes passed, including canonical host/protocol, query preservation, feed and 404 behavior. The eight search/user-fetch crawler profiles passed; GPTBot is disallowed by robots policy and ClaudeBot is disallowed and returned 403. These preserved training policies are not search outages.\n')
 (p/'executive-summary.md').write_text(f'''# SEO and Howl audit — 2026-10-28

**PASS WITH RECOMMENDATIONS.** Audited all 26 new/refined pages, with a full 281-page crawl for linking context. Repository fixes are deployed and verified. No in-scope P0/P1 issue was found before or after.

The baseline already had unique titles/descriptions, working canonicals, sitemap membership, one H1 per scoped page and no broken internal links or orphans. The missing pieces were semantic page/sample descriptions, source-backed Howl entries, an accessible logo label and responsive homepage media.

Added breadcrumbs to 25 pages, exact-source schema to 21 examples and collection markup to the Examples index. Corrected the logo label and deferred the hidden video poster while adding responsive hero candidates. All 26 Howl entries now reference real examples; their SVG, HTML, Markdown, captions and gallery were generated with Howl 1.2.0. Two renders matched across all 79 artifacts. [Download the showcase archive](howl/showcase.zip).

All 26 live pages return 200 with their canonical URL and updated markup. All 26 social-image hashes match the generated files. All 38 unique external destinations returned 200. Thirteen redirect/error/feed probes passed; search and user-fetch crawler checks passed. Training-crawler restrictions were preserved. The default Python user agent received an image 403; the explicit audit agent used by the page crawl fetched matching images. This access-policy distinction is retained in raw receipts.

Verification includes 28 Node tests, the 21-example runtime checks, full build and 1,167 responsive assets, semantic/source checks, Howl validation and three local/live browser suites. The suites cover code copying, navigation, no-JavaScript content, accessibility and responsive layouts. Twenty-two distinct required gates have successful evidence across the documented Loop iterations; final closeout passed against 3,170 unchanged source/output hashes. Historical failures and their repairs remain recorded.

Deployment: [{receipt['run_id']}]({receipt['run_url']}) succeeded for `{receipt['deployed_commit']}`. Source commits: `cd89128` (SEO/media/accessibility) and `bbfb2b6` (Howl). See [changed files](changed-files.txt) and [iteration notes](../../.loop-engineering/seo-howl-pages/evidence/iteration-notes.md). The final evidence-only commit uses the repository's existing skip-CI convention; it does not change deployed site inputs.

In one comparable local mobile lab run, homepage LCP was 4,035 ms before and 3,157 ms after; image transfer was 242,721 versus 77,622 bytes. Other templates varied slightly. These are lab observations, not field CWV or a causal outcome study. [Before/after details](before-after.md) and [performance data](performance.csv) retain all values and limits.

Search-console, analytics, verified request logs, field CWV, controlled rankings and AI citation data: **NOT AVAILABLE — DATA ACCESS REQUIRED**. The limited public query observations cannot establish index coverage or rank. No ranking, traffic, conversion or citation gain is claimed. Internal SEO/AI scores are not assigned; verified counts are reported instead.

Next: use the same URL/query/question set for the dated [7-, 28-, 60- and 90-day measurement plan](recommendations.md). Private data access is a measurement limitation, not a blocker to the completed implementation. No new positioning, unsupported claims, training policy or external infrastructure settings were changed.
''')
