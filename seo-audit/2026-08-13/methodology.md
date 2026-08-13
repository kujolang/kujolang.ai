# Methodology

Audit date: 2026-08-13

## Scope and evidence sequence

The audit preserved the pre-change generated output and production response state as `baseline.csv`, then crawled the rebuilt static artifact into `after.csv`. Route discovery combined generated HTML and sitemap evidence. Checks covered local/production status, indexability, canonicals, titles, descriptions, headings, internal links, depth, orphans, images, JSON-LD, and sitemap inclusion.

## Current primary guidance consulted

Current first-party Google Search Central, Bing Webmaster Tools, OpenAI crawler, and Schema.org guidance is recorded in `research-sources.md`. Technical readiness is not treated as a ranking or AI-citation guarantee.

## Commands

```text
python3 scripts/seo_audit.py --repo . --output output --audit-dir seo-audit/2026-08-13 --phase baseline --origin https://kujolang.ai --probe-production
kujo run ./build.kujo -- --site-url https://kujolang.ai
python3 scripts/seo_audit.py --repo . --output output --audit-dir seo-audit/2026-08-13 --phase after --origin https://kujolang.ai
bash scripts/verify-site-contract.sh output
```

## Limits

No authenticated search, analytics, log, ranking, CrUX, or AI-answer datasets were available. Browser screenshots and geometry checks are implementation QA, not field performance evidence.
