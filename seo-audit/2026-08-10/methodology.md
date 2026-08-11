# Methodology

Audit date: 2026-08-10

## Scope

Repository source, generated static output, GitHub Pages production delivery,
canonical/indexable routes, aliases, metadata, content, internal/external
links, JSON-LD, images, representative lab performance, search observations,
and search/AI crawler access were in scope. DNS/CDN changes, search-console
configuration, repository visibility changes, training-crawler policy, and
editorial publication were not changed without owner input.

Canonical origin: `https://kujolang.ai`

Locale: English (`en` / `en_US`)

Audience: developers and teams building AI-native, local-first, agentic
software. Primary conversions are ecosystem/source exploration, installation,
documentation visits, and contact/community engagement.

## Evidence sequence

1. Confirmed a clean `main` worktree and read repository/build/deployment files.
2. Built the untouched site with the documented Kujo toolchain.
3. Copied the untouched `output/` to
   `seo-audit/2026-08-10/raw/baseline-generated/` before editing source.
4. Crawled 38 canonical pages discovered from generated route files and the
   sitemap; hashed the full baseline output.
5. Probed production routes, host/protocol variants, crawler user agents, and
   unique external destinations; retained raw JSON receipts.
6. Ran Lighthouse 13.0.1 against three representative local templates using
   its mobile simulated-throttling defaults.
7. Implemented source/template/generator fixes, rebuilt, ran repository
   contracts, recrawled the same inventory, and repeated Lighthouse.
8. Compared stable fields in `baseline.csv`, `after.csv`, both summary JSON
   files, `performance.csv`, and the output hash manifests.

## Current primary guidance consulted

Guidance was retrieved on 2026-08-10 and is listed with classification and
interpretation in `research-sources.md`. Search/AI behavior changes; later audits
must re-check those sources.

## Build and crawl commands

```bash
kujo run ./build.kujo -- --site-url https://kujolang.ai
bash scripts/verify-site-contract.sh output
bash scripts/validate-generated-output.sh output
node --check output/assets/js/site.js
npm audit --omit=dev
python3 scripts/seo_audit.py --repo . --output output \
  --audit-dir seo-audit/2026-08-10 --phase after \
  --origin https://kujolang.ai
python3 scripts/probe_site.py --audit-dir seo-audit/2026-08-10 \
  --origin https://kujolang.ai --phase after
python3 scripts/extract_lighthouse.py --audit-dir seo-audit/2026-08-10
```

## Interpretation limits

- Character lengths, internal scores, and Lighthouse category scores are review
  signals, not ranking factors or platform health scores.
- A single lab run is not field Core Web Vitals and does not establish a stable
  performance distribution.
- The web-search connector does not expose a guaranteed engine, complete result
  set, locale, or exact rank; observations are recorded only as returned/not
  returned in the sampled results.
- A 401/403/405/429 external response is indeterminate. The two reported broken
  GitHub links were repeatable anonymous 404 responses and are still subject to
  owner confirmation because private repositories also appear as 404.
- `llms.txt` remains an experimental discovery aid. No consulted search or AI
  provider documents it as an indexing or ranking requirement.
