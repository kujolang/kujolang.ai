# Methodology

Audit date: 2026-09-04

## Scope

Focused remediation and verification of the open responsive-media finding from the complete 2026-09-04 Kujolang.ai SEO and AI-search audit. The primary affected route is `/ecosystem/`; the implementation applies consistently to every locally generated featured and listing WebP.

## Evidence sequence

The immutable baseline is imported from the complete audit's verified after-state, which matches the rendered site at baseline commit `378bb3b`. Its crawl datasets, output checksums, and ecosystem Lighthouse row are copied here with provenance. After implementation, the pinned Kujo runtime rebuilds the complete site, the responsive generator writes only to generated `output/`, contracts resolve every advertised candidate to a file, and the full crawl is repeated. A mobile-simulated Lighthouse run and real-browser Lens checks provide focused after evidence.

## Current primary guidance consulted

The same-day primary-source research from the complete audit is reused because no guidance window elapsed. Google recommends responsive images that give the browser width descriptors plus an accurate `sizes` expression; crawlability and valid markup do not establish indexing or ranking outcomes.

## Build and crawl commands

The pinned local Kujo release binary runs `kujo run ./build.kujo -- --site-url https://kujolang.ai`. `npm run images:responsive` creates deterministic 640 px, 960 px, and 1280 px WebP candidates. Verification uses `npm test`, `npm run images:verify`, `scripts/verify-site-contract.sh`, `scripts/validate-generated-output.sh`, `scripts/seo_audit.py`, `scripts/probe_site.py`, Lighthouse 13.4.1, and Lens desktop/mobile browser checks.

## Interpretation limits

The responsive candidates reduce browser-selected transfer only when viewport, layout width, and device pixel ratio select them. Lighthouse is single-run lab evidence, not field Core Web Vitals. Search Console, analytics, ranking, backlink, and controlled AI-citation data remain unavailable, so this audit makes no traffic, ranking, or citation claim.
