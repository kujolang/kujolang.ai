# Methodology

Audit date: 2026-09-04

## Scope

Release-publication audit of all 194 generated canonical pages, with focused
content review of `/ecosystem/searchbridge/` and global verification of
metadata, canonicals, sitemap membership, robots policy, structured data,
internal links, media attributes, redirects, external destinations, and
search/AI crawler access. The earlier immutable `seo-audit/2026-09-04/`
remains the full-site performance and search-observation baseline.

## Evidence sequence

1. Built and crawled commit `a1b32cdc4c0f2365f252f2e5ee294e16f5080946`
   before editing and stored its output hash and live receipts.
2. Updated only factual SearchBridge release copy and site version surfaces.
3. Rebuilt and ran the same 194-page crawl after publication.
4. Probed production independently through Cloudflare and GitHub Pages.

## Current primary guidance consulted

See `research-sources.md`. Requirements, recommendations, best practices, and
measurement limitations are kept separate; no ranking or citation outcome is
inferred from technical validity.

## Build and crawl commands

```bash
kujo run ./build.kujo -- --site-url https://kujolang.ai
bash scripts/verify-site-contract.sh output
bash scripts/validate-generated-output.sh output
node --check assets/js/site.js
npm test
npm audit --omit=dev
python3 scripts/seo_audit.py --repo . --output output \
  --audit-dir seo-audit/2026-09-04-searchbridge-v1.0/2026-09-04 \
  --phase baseline --origin https://kujolang.ai --probe-production
python3 scripts/probe_site.py \
  --audit-dir seo-audit/2026-09-04-searchbridge-v1.0/2026-09-04 \
  --origin https://kujolang.ai --phase baseline \
  --key-path /ecosystem/searchbridge/ --feed-path /feed/index.xml
```

The baseline probe mistakenly requested `/feed.xml`; the immutable receipt is
preserved, but that 404 is a probe-configuration error because the documented
feed is `/feed/index.xml`. The after probe uses the correct route. The crawl and
probe commands were otherwise repeated with `--phase after` after deploy.

## Interpretation limits

The crawl is deterministic technical evidence, not proof of indexing, ranking,
traffic, or AI citation. External 401/403/405/429 responses are treated as
indeterminate. The audit adds no new product claim beyond the tagged
SearchBridge release record and its sanitized live-contract evidence.
