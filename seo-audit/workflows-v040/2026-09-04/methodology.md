# Methodology

Audit date: 2026-09-04

## Scope

Full repository and production audit of `https://kujolang.ai`, with focused
editorial review and browser proof for the `kujo-workflows 0.4.0` catalog,
Owned Agent Project, and Publishing House Operator surfaces. The crawl covers
all 194 canonical URLs; the focused review checks visible release facts,
metadata, schema, source links, Howl social images, accessibility, and mobile
layout.

## Evidence sequence

1. Preserve the deployed GitHub Pages artifact from run `33878265415` before editing.
2. Fingerprint that 195-file HTML/404 artifact and crawl its 194 canonical pages against production.
3. Probe redirects, robots policy, ten crawler identities, sitemap, feed, and external destinations.
4. Run Lens against the workflow collection and operator at desktop and 390px mobile sizes.
5. Review the rendered facts against `kujo-workflows v0.4.0` source and release evidence.
6. Correct verified source defects, rebuild in clean GitHub Actions, repeat the crawl and browser checks, and verify production independently.

## Current primary guidance consulted

Only the dated first-party sources in `research-sources.md` support crawler,
canonical, sitemap, structured-data, and AI-search conclusions. `llms.txt`
remains an experimental discovery aid, not a ranking requirement.

## Build and crawl commands

```bash
kujo run ./build.kujo -- --site-url https://kujolang.ai
bash scripts/verify-site-contract.sh output
bash scripts/validate-generated-output.sh output
python3 scripts/seo_audit.py --repo . --output output --audit-dir seo-audit/workflows-v040/2026-09-04 --phase after --origin https://kujolang.ai --probe-production
python3 scripts/probe_site.py --audit-dir seo-audit/workflows-v040/2026-09-04 --origin https://kujolang.ai --phase after
npm test
npm run social:verify
```

The after build runs from a clean GitHub Actions checkout because the full local
SSG takes substantially longer under simultaneous local repository builds. The
deployed Actions artifact is downloaded, fingerprinted, and independently
crawled; this is clean-machine build evidence rather than an inferred result.

## Interpretation limits

Technical readiness does not prove ranking, indexation, traffic, conversion, or
AI citation. Anonymous search results are dated observations. Lens timing is
lab evidence and not field Core Web Vitals. Third-party 401/403/405/429 results
remain indeterminate; confirmed 404s are reported without guessing the intended
replacement.
