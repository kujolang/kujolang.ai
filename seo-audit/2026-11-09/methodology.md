# Methodology

Scope: add Website Cloner to the marketing site, homepage, ecosystem/showcase listings and public read-only MCP catalog. Audit the generated site for regressions and verify the new route, metadata, video, images and incoming links. This is a scoped launch audit, not a new ranking study.

The clean checkout was behind the current website. It was fast-forwarded to 05064fd before applying this addition. Immutable source hashes are in source-baseline.json; historical full-site evidence remains in ../2026-10-30/. Command-line production requests received 403 while the normal browser rendered the site; those are recorded separately, not labeled as universal site failures.

Build with the CI-pinned Kujo 1.9.0, generate responsive images, run site contracts and Node tests, crawl generated HTML with scripts/seo_audit.py, and inspect desktop/mobile in the browser. Public metadata and media checks follow deployment. Passing markup checks does not establish rich-result eligibility or search visibility.

Follow-up standard curl probes returned HTTP 200 for the existing homepage, ecosystem, showcase, sitemap and llms.txt; the not-yet-published new route returned 404. See baseline-curl.json. Python urllib received 403; no access policy was changed.
