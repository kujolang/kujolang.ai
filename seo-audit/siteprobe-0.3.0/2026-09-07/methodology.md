# SiteProbe 0.3.0 website update — methodology

Scope: release-focused editorial correction on https://kujolang.ai, supported by a full
generated technical crawl and a complete sitemap production baseline. This is
not a new ranking, competitor, backlink or conversion audit. Preserve unchanged
URLs, templates, imagery, crawler training policy and unrelated content.

Audit date: 2026-09-07 America/Detroit. Research retrieved 2026-09-08T02:19:04.328190+00:00.
Source → Kujo SSG generated HTML → GitHub Pages → Cloudflare/public edge.
Baseline environment and exact commits are recorded in baseline-environment.json.
Local builds use the verified Kujo 1.3.1 CLI at 5dcbfcd; the website's
hosted workflow independently verifies its committed runtime pin. Documentation
uses its documented sibling SSG checkout. No build dependency is changed.

Compare baseline/after fields using the existing website scripts/seo_audit.py.
Crawl all generated canonical routes, metadata, headings, links, media attributes,
schema, sitemap, indexability and depth. Inspect changed pages for product truth,
source attribution, readable examples, visible/schema alignment and contextual
links. Probe live canonical pages, status/redirect variants, robots, sitemap,
llms.txt and representative crawler user agents. UA probes demonstrate responses
to those headers, not verified crawler-IP access or indexing outcomes.

No performance changes are intended: compare HTML/asset bytes and unchanged asset
hashes. Field CWV, rankings, analytics, logs, backlinks and controlled AI citations
are unavailable; do not infer them from a healthy build. llms.txt remains an
experimental discovery artifact, not a Google ranking requirement.

The older installed 1.2.3 baseline build was deliberately interrupted before completion; its logs are preserved and it is not counted as a passing build. The authoritative paired builds use identical hosted workflow pins for each website; see verification-receipt.json. The local marketing build is supplemental; the local docs errno-35 failure is not a pass.
