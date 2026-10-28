# Methodology — 2026-10-28

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
