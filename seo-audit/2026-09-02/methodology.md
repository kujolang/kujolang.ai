# Methodology

Audit date: 2026-09-02

## Scope

Full-site technical, on-page, schema, crawler, image, and internal-link audit of
`https://kujolang.ai/`, with focused content and rendered-mobile review of the
Publishing House Operator page. The docs site received a source-backed content
sync and its own build validation, but is not represented as part of this site's
192-URL inventory.

## Evidence sequence

1. Record the starting Git revision and preserve all 192 public canonical pages.
2. Run a real Chromium mobile Lens check on the changed workflow route.
3. Audit the preserved baseline for metadata, schema, links, images, indexability,
   sitemap membership, crawler access, and redirects.
4. Inspect repository source, Kujo SSG output contracts, Howl manifest coverage,
   and the Publishing House implementation that supports readiness claims.
5. Apply the smallest source-level CSS and content corrections.
6. Build from source, repeat the crawl and Lens check, validate every Howl card,
   and run repository and WebOps gates.
7. Deploy through the existing GitHub Pages contracts and verify the public edge.

## Current primary guidance consulted

Only first-party Google, Bing, and OpenAI documentation listed in
`research-sources.md` was used for current crawler, structured-data, mobile, AI
search, image, sitemap, and robots conclusions.

## Build and crawl commands

```bash
KUJO_BIN=/absolute/path/to/kujo bash ../ssg/scripts/build-parallel.sh 8 8 --site-url https://kujolang.ai
python3 scripts/seo_audit.py --repo . --output output --audit-dir seo-audit/2026-09-02 --phase after --origin https://kujolang.ai --probe-production
python3 scripts/probe_site.py --audit-dir seo-audit/2026-09-02 --origin https://kujolang.ai --phase after --skip-external
npm test
npm run social:cards
npm run social:verify
```

Lens used a 390px mobile Chromium viewport before and after. WebOps post-publish,
weekly site health, and finding-to-fix workflows were run in their deterministic,
non-mutating mode to exercise their evidence and authority boundaries.

## Interpretation limits

Technical readiness is not a ranking, indexation, traffic, AI citation, or
conversion guarantee. A local build is not a publication effect. Fixture WebOps
receipts prove deterministic workflow behavior, not authenticated provider
access. Search and audience outcomes require the unavailable longitudinal data
listed in `data-availability.md`.
