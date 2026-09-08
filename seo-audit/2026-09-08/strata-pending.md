# Pending Strata consolidation

Target: Agent Notes. Read-side exact/concept searches returned no matching note. A supported notes create call failed with Could not reach Strata API at http://127.0.0.1:3939 on 2026-09-08. Nothing saved or retrieval-verified.

Save command: `npm run strata -- notes create --file <this-bundle> --project "Agent Notes" --json` from /Users/robertdevore/2026/strata. After a successful write, retrieve the returned exact ID and search the concepts below.

# Memory · lesson · Kujo catalog sync must peel annotated release tags

- Status: active
- Authority: source and repeatable verification
- Confidence: High
- Scope: kujolang/kujolang.ai, scripts/sync-ecosystem-catalogs.mjs
- Date: 2026-09-08
- Local Strata Session ID: kujo-video-sites-20260908
- Evidence: commit b23a132a6528391a4b146d518a510ccbd755376b; seo-audit/2026-09-08

When synchronizing a version-pinned skills catalog, read the release date from `${skillsRef}^{commit}`. `git show -s --format=%cs v0.7.0` includes annotated-tag text, which polluted generated date fields. The peeled commit returns the date alone. `KUJO_SKILLS_REF=v0.7.0 node scripts/sync-ecosystem-catalogs.mjs --skills-only` now reproduces the committed 135-page catalog without a diff. Curated supplemental guidance belongs in catalog-overrides/skills so future syncs retain it.

Retrieval cues: Kujo website annotated tag date catalog generation; skills-only sync v0.7.0.

# Session handoff · Kujo video skills on both public sites · 2026-09-08

- Scope: kujolang/kujolang.ai and kujolang/docs.kujolang.ai; main branches.
- Local Strata Session ID: kujo-video-sites-20260908.
- User intent: publish the new video skills and audit both sites to SEO/AI-search standards.
- Evidence/current state: each repository’s seo-audit/2026-09-08/after-provenance.json, final-verification.json, executive-summary.md and Git history are authoritative.
- Docs source f44a76b and deployment 1489d31 publish the ten-style guide, prompts, narrator defaults/overrides, and responsive tables.
- Website source b3d7304 updates the catalog to all 135 skills, preserves curated guidance, and corrects shared-image sizing and text-decoration performance. Final workflow 34279154149 deployed successfully; both sites pass full canonical live verification (233 website pages and 101 docs pages).
- Measurement limits: authenticated search/analytics/logs, field CWV and controlled AI-citation benchmarks unavailable. No ranking improvement claimed.
- Next starting point: final-verification.json in each audit, then the dated measurement plan; no SignalBox capture warranted for completed fixes.
- Retrieval cues: public Kujo skills catalog video styles docs HyperFrames ElevenLabs v0.7.0 SEO audit September 2026.
