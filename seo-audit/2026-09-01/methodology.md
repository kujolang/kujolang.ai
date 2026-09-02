# Methodology

Audit window: 2026-09-01 through 2026-09-02 (America/Detroit). Baseline commit: `d479ba9f99ac258d4e03b8fe02e6cf88247487b9` (the current production source after synchronizing concurrent upstream provider work). Production origin: `https://kujolang.ai`.

## Scope

The inventory covers every production-sitemap canonical. No writing content was changed. Implementation scope is the Ability page, reciprocal ecosystem links, collection count, hero and social image, metadata, sitemap, `llms.txt`, and generated WebMCP catalog entry.

## Evidence sequence

The immutable before state is the 190-URL production sitemap and downloaded canonical HTML under `raw/production-before/`, plus live redirect, crawler, DNS, TLS, header, and external-link receipts under `raw/live/`. The edited repository is built and crawled with the same origin. Production is probed again after deployment is visible.

## Current primary guidance consulted

First-party Google Search Central and Bing Webmaster guidance listed in `research-sources.md` informed canonical, sitemap, crawlability, image, and post-launch checks.

## Build and crawl commands

The site is built with Kujo, verified with `scripts/verify-site-contract.sh` and `scripts/validate-generated-output.sh`, crawled with `scripts/seo_audit.py`, and live-probed with `scripts/probe_site.py`. Howl renders the social set and `scripts/verify-social-cards.mjs` validates image and page metadata.

## Interpretation limits

Search-console, analytics, CDN, revenue, conversion, and backlink-platform evidence was unavailable and is not inferred from crawl data.
