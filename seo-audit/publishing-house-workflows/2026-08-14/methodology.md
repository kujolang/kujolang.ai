# Methodology

Audit date: 2026-08-14

## Scope

The audit covers the Workflows catalog and the eight new Publishing House detail routes, plus sitewide crawl effects from expanding the canonical route set from 165 to 173. It verifies source metadata, canonicals, indexability, sitemap and `llms.txt` discovery, internal links, JSON-LD, image metadata, Howl social cards, and generated-output integrity.

## Evidence sequence

The immutable pre-change artifact at `seo-audit/2026-08-14/raw/baseline-output.tar.gz` and its SHA-256 receipt are the before source. That archive was crawled into this packet before the rebuilt artifact was crawled. The live catalog was also observed at 26 workflows and kujo-workflows 0.2.0 before deployment. After deployment, production responses are re-probed for all eight routes and the catalog.

## Current primary guidance consulted

Current first-party Google Search Central and Bing Webmaster guidance is recorded in `research-sources.md`. Search guidance informs discoverability and metadata checks; it does not justify claims about rankings, traffic, or AI citations.

## Build and crawl commands

```text
python3 scripts/seo_audit.py --repo . --output <immutable-baseline-output> --audit-dir seo-audit/publishing-house-workflows/2026-08-14 --phase baseline --origin https://kujolang.ai --probe-production
kujo run ./build.kujo -- --site-url https://kujolang.ai
bash scripts/verify-site-contract.sh output
bash scripts/validate-generated-output.sh output
npm run social:verify
python3 scripts/seo_audit.py --repo . --output output --audit-dir seo-audit/publishing-house-workflows/2026-08-14 --phase after --origin https://kujolang.ai --probe-production
```

## Interpretation limits

Repository and HTTP evidence can prove route availability, technical crawlability, metadata, and artifact integrity. Google Search Console, Bing Webmaster Tools, analytics, field Core Web Vitals, rankings, and authenticated AI citation measurements were not available and are not inferred.
