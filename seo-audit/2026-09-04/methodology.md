# Methodology

Audit date: 2026-09-04

## Scope

Full repository and production audit of `https://kujolang.ai`: all 193 canonical pages, rendered metadata and JSON-LD, robots and sitemap behavior, internal and external link graphs, images, redirect variants, ten crawler identities, representative search observations, and four Lighthouse templates.

## Evidence sequence

The untouched `output/` was copied to `raw/baseline-output/` and fingerprinted before source changes. `scripts/seo_audit.py` crawled every canonical output page and probed production. `scripts/probe_site.py` independently exercised redirects, crawlers, and external destinations. Lighthouse 13.4.1 collected one mobile-simulated lab run for home, catalog, PackWrite, and Ability templates. The same build, crawl, validation, and lab sequence was repeated after remediation.

## Build and crawl commands

The pinned Kujo release binary ran `kujo run ./build.kujo -- --site-url https://kujolang.ai`. Verification used `scripts/verify-site-contract.sh`, `scripts/validate-generated-output.sh`, `npm run social:verify`, `scripts/seo_audit.py`, and `scripts/probe_site.py`. Raw receipts and normalized datasets live beneath this directory.

## Interpretation limits

Production probes establish behavior at audit time, not index coverage. Search observations are anonymous snapshots, not stable rank measurements. Lighthouse is lab evidence, not field Core Web Vitals. GitHub 404s were classified as access-blocked only after authenticated metadata proved the targets exist privately. No result is treated as traffic, ranking, backlink, or AI-citation improvement.
