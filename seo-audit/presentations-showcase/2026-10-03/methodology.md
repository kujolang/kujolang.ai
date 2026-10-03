# Methodology

Audit date: 2026-10-03

## Scope

Full local crawl and production baseline for kujolang.ai, with focused editorial, media, schema, and linking review for the new Presentations ecosystem page. Repository source, generated output, production responses, first-party product documentation, and current primary search/crawler guidance were kept as separate evidence layers.

## Evidence sequence

1. Checked out clean `origin/main` at `029066de787c8df1ec3fbbef58d554e66642bcfe`.
2. Built and validated the untouched 241-route site with Kujo 1.7.0.
3. Crawled every canonical page and probed each production equivalent.
4. Preserved the baseline output under the ignored `raw/baseline-build/` workspace before editing.
5. Added the source-backed page, generated hero, social card, catalog entry, documentation link, and contracts.
6. Rebuilt, regenerated responsive images, reran repository contracts, and crawled the same inventory fields.
7. Probed the live new route, documentation route, examples, release URL, robots policy, and OAI-SearchBot access separately.

## Current primary guidance consulted

See `research-sources.md`. The implementation follows documented requirements and recommendations for helpful content, crawlable links, descriptive metadata, canonicals, sitemaps, structured data, images, and crawler policy. No experimental protocol was treated as a ranking requirement.

## Build and crawl commands

`PATH=../kujo/target/release:$PATH kujo run ./build.kujo -- --site-url https://kujolang.ai`

`npm run images:responsive`

`bash scripts/verify-site-contract.sh output`

`bash scripts/validate-generated-output.sh output`

`python3 scripts/seo_audit.py --repo . --output output --audit-dir seo-audit/presentations-showcase/2026-10-03 --phase baseline|after --origin https://kujolang.ai`

## Interpretation limits

The after crawl is local generated-output evidence, not deployment evidence. Production, ranking, referral, field-performance, and AI-citation outcomes require deployment, elapsed time, and authenticated platform data. Schema.org validity does not imply a Google rich result.
