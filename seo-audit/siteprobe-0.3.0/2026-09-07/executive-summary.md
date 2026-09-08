# SiteProbe 0.3.0 website release verification

Status: **PASS WITH RECOMMENDATIONS**. Release content and technical deployment are verified; search performance and AI citations require platform access.

## Scope and provenance

- Repository: `kujolang/kujolang.ai`, branch `main`.
- Starting SHA: `078d3ae77861fef489445dfec0b446e341cbc019`.
- Published content SHA: `28e6f0980814ffe89a9023a7c325ec00d696dad5`. Subsequent audit-only commits do not change rendered content.
- Baseline workflow: https://github.com/kujolang/kujolang.ai/actions/runs/34180933653.
- Verified update workflow: https://github.com/kujolang/kujolang.ai/actions/runs/34181638601.
- Deployment: https://github.com/kujolang/kujolang.ai/actions/runs/34181638601 — PASS; GitHub Pages artifact from source 28e6f0980814ffe89a9023a7c325ec00d696dad5.
- Live release page: https://kujolang.ai/ecosystem/siteprobe/.
- Audit workspace: `seo-audit/siteprobe-0.3.0/2026-09-07/` (September 7 local date; UTC timestamps are September 8).
- Product source: [SiteProbe v0.3.0](https://github.com/kujolang/siteprobe/releases/tag/v0.3.0), commit `71a2071b60174cf755084e167ccc392710a104b8`.

## Findings and changes

| ID | Priority | Evidence | Action | Status |
| --- | --- | --- | --- | --- |
| SP-WEB-01 | P1 | Baseline release page omitted current native 0.3.0 qualification; marketing still said 0.1 | Replace stale release facts using the versioned product README, release and audit | Fixed |
| SP-WEB-02 | P1 | Baseline installation guidance omitted the required runtime and source-only package boundary | Document KUJO_REVISION, KUJO_BIN, source packages, verification and platform launchers; link installation guide | Fixed |
| SP-WEB-03 | P2 | Docs had local verification commands but no hosted complete-build gate | Add pinned-runtime/SSG verification and retained deployable artifact; keep existing manual gh-pages publication | Fixed in docs repository |

Changed content is narrowly scoped to the SiteProbe page, its generated discovery entries and CHANGELOG. Docs README describes its new verification workflow. Existing website version/TOML metadata continues to describe the website's own release, not SiteProbe's version; no unrelated website release/tag was created. No templates, images, CSS, JavaScript, URLs, crawler policy, DNS or CDN settings changed.

## Before and after

| Measurement | Baseline | After |
| --- | ---: | ---: |
| Canonical/indexable pages | 194 | 194 |
| Sitemap URLs | 194 | 194 |
| Broken internal links | 0 | 0 |
| Missing/duplicate titles | 0/0 | 0/0 |
| Missing/duplicate descriptions | 0/0 | 0/0 |
| Missing/mismatched canonicals | 0/0 | 0/0 |
| H1 issues / schema parse errors | 0/0 | 0/0 |
| Missing alt / dimensions | 0/0 | 0/0 |
| SiteProbe HTML bytes | 19137 | 20664 |

All 194 canonical routes are preserved and return HTTP 200 after deployment. All 1034 static files under assets retain their baseline SHA-256 (the generated docs search index is checked separately). HTML grew to include accurate installation and release evidence; this is not a performance optimization. Generated-output summaries do not request production (`production_200_pages: 0` means unmeasured there); separate full live receipts record actual successful requests.

## Verification receipt

- Hosted baseline and update: pinned `cargo build --release --locked`, `npm ci`, `npm test` (3 tests), `kujo run ./build.kujo -- --site-url https://kujolang.ai`, `npm run images:responsive`, `bash scripts/verify-site-contract.sh output`, `bash scripts/validate-generated-output.sh output`, `node --check output/assets/js/site.js`: PASS.
- Supplemental local baseline with verified 1.3.1 runtime: full SSG build, responsive images, both validators: PASS. `node --check assets/js/site.js`: PASS. `npm audit --omit=dev --json`: PASS, zero reported vulnerabilities.
- Both phases: `python3 scripts/seo_audit.py --repo . --output seo-audit/siteprobe-0.3.0/2026-09-07/raw/<phase>-output --audit-dir seo-audit/siteprobe-0.3.0/2026-09-07 --phase <phase> --origin https://kujolang.ai`: PASS.
- `python3 /tmp/siteprobe_compare.py kujolang.ai-work`: PASS; unchanged asset hashes, preserved routes, release facts.
- `python3 /tmp/siteprobe_after_live.py kujolang.ai-work` and `python3 /tmp/siteprobe_website_probe.py kujolang.ai-work after`: PASS; 194 HTTP 200 canonical routes and 21 edge probes.
- `python3 /tmp/siteprobe_links.py`: PASS, seven reference links HTTP 200.
- `git diff --check`: PASS. Exact comparison/extraction/probe helpers and CI logs retained under audit raw/.

The complete hosted baseline artifacts were preserved and hash-manifested. The marketing content was edited after its successful local full baseline was preserved, and its already-running hosted baseline subsequently passed at the original source SHA. Docs content was edited only after its full hosted baseline artifact was downloaded, preserved and reopened. Baseline datasets are copied under `raw/baseline-datasets/` before the after crawl. Source, build, HTTP and artifact hashes distinguish local output from production.

Local environment limitations are recorded, not counted as successful checks: the installed Kujo 1.2.3 attempt was stopped; a modern docs build hit host process exhaustion (errno 35). The modern local marketing build and both validators passed. Paired authoritative builds use the same committed hosted pins for each website, with all complete hosted checks passing. No check was disabled and no timeout increased.

Live edge probes cover canonical routes, slash/HTTPS redirects with query preservation, robots/sitemap/llms, deliberate 404s and representative search/training/user-fetcher user agents. These verify HTTP responses to supplied headers, not verified crawler IPs, indexing, rankings or citations. The existing managed robots training restriction is preserved. All seven distinct release/reference links returned HTTP 200.

## Search and AI-search limitations

`NOT AVAILABLE — DATA ACCESS REQUIRED`: Search Console/Bing index coverage and queries; analytics/conversions/referrals; verified CDN crawler logs; CrUX/RUM; authorized rank/backlink data; controlled AI-platform citation measurements. No health score, ranking, citation, traffic, conversion or Core Web Vitals uplift is claimed. No new Lighthouse run was made for this content-only change; asset hash and HTML-byte comparisons are the measured resource evidence.

Research: [Google AI features](https://developers.google.com/search/docs/appearance/ai-features), [Google generated-content guidance](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content), [OpenAI crawler purposes](https://developers.openai.com/api/docs/bots), [Schema.org SoftwareApplication](https://schema.org/SoftwareApplication), retrieved September 8 UTC. Standard crawlable, accurate, sourced content supports discovery; llms.txt is treated as experimental, and valid JSON-LD does not prove rich-result eligibility.

At 7 days recheck live/indexability and URL inspection if access exists. At 28/60/90 days compare matched page/query cohorts and the same documented AI questions, recording deployment and algorithm changes as confounders. Unrelated pages received a full technical crawl, not a new editorial/keyword/competitor audit. No unresolved technical blocker or required cross-repository implementation remains.
