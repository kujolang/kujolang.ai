# Methodology

Audit date: 2026-08-14

## Scope

All 165 canonical routes were crawled, with focused manual and browser review of `/ecosystem/`, `/ecosystem/tooling/`, and `/ecosystem/{assetworks,bluepencil,dossier,galleypack,presswire,readersignal,storydesk,versionseal}/`. The audit also covered desktop/mobile dropdown markup and behavior, titles, descriptions, canonicals, Open Graph/Twitter metadata, Howl assets, JSON-LD, internal/external links, images, `robots.txt`, `sitemap.xml`, RSS, `llms.txt`, redirects, crawler access, and representative lab performance.

## Evidence sequence

Before source changes, the generated output and live production response state were preserved in `baseline.csv`, `baseline-summary.json`, and `raw/baseline-output.tar.gz` with a SHA-256 receipt. The rebuilt artifact was crawled into `after.csv`; production was re-probed after deployment. Raw Lighthouse JSON preserves representative template runs.

## Current primary guidance consulted

Current first-party Google Search Central, Bing Webmaster, OpenAI, Anthropic, Perplexity, and Schema.org guidance is recorded in `research-sources.md`. `llms.txt` is treated as experimental discovery assistance, not a ranking or citation guarantee.

## Build and crawl commands

```text
python3 scripts/seo_audit.py --repo . --output output --audit-dir seo-audit/2026-08-14 --phase baseline --origin https://kujolang.ai --probe-production
python3 scripts/probe_site.py --audit-dir seo-audit/2026-08-14 --origin https://kujolang.ai --phase baseline
kujo run ./build.kujo -- --site-url https://kujolang.ai
bash scripts/verify-site-contract.sh output
bash scripts/validate-generated-output.sh output
python3 scripts/seo_audit.py --repo . --output output --audit-dir seo-audit/2026-08-14 --phase after --origin https://kujolang.ai --probe-production
npx --no-install lighthouse <representative-url> --only-categories=performance,accessibility,seo,best-practices --output=json
```

## Interpretation limits

Lighthouse is a throttled lab diagnostic, not field Core Web Vitals. Baseline and after runs used the same production URLs and tool version, but lab variability still applies. Search visibility, rankings, traffic, engagement, and AI citations were not inferred without provider evidence.
