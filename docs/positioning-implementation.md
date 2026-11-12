# Positioning implementation — November 12, 2026

Approved implementation of the November 12 positioning and claims audit. Baseline: `590b6b1ea9bf48af13eecbc243a6176ab53921b4`. The original audit and immutable live/generated evidence are retained outside the repository in the Codex chat artifact directory, `kujo-positioning-audit` (chat `01a1d01a-7822-7db3-97bc-ade5cf960da9`).

## Implemented scope

- R01–R05: qualify provider portability, strict cassette replay, Eval/Lens environmental dependencies, workflow local-preview badges, Watchdog exports and the Muzzle heading.
- R06–R10: language-and-toolchain homepage, existing-project entry, Clarity/Context/Control, a real failed/passing Hermes example, integration and accountability guides, and static provider links with progressive enhancement.
- R11–R14: task-oriented priority titles, evidence links, installation distinctions, fixture-first agent entry, historical comparison limits and nearby maturity/authority boundaries.
- R15–R16: link the existing checkout case study and distinguish package/source evidence from live-provider certification. No unperformed live tests or new case-study results are claimed.

The implementation preserves separate runtime/package/plugin versions, host-owned authorization, cooperative agent cancellation, strict versus fallthrough cassettes, unsigned receipt limits, local telemetry exports, configured Docker/Podman boundaries and the published alpha/beta recovery limits. BB remains a theme; Source remains an experimental Node application.

## Source ownership and checks

Edit guide content in `content/pages`, then run `npm run guides:generate`. Edit provider records in `assets/data/providers.json`, then run `npm run providers:generate`; CI checks the generated directory. Workflow readiness display is mirrored in `scripts/sync-ecosystem-catalogs.mjs`. Comparison wording belongs in the comparison generator. Social cards and their manifests include both new routes.

Required checks: Node tests; provider and guide freshness; pinned example and workflow freshness/execution; Kujo build; responsive images; site contract and generated HTML; language, social, comparison and SEO validators; JavaScript syntax; production dependency audit; diff whitespace. Use the official Kujo 1.9.0 artifact via `KUJO_BIN` for execution tests. Browser checks cover the existing language experience and `scripts/test-positioning-browser.cjs` (provider search/modal, no-JS and failed-fetch links, responsive guides).

## Measurement and later evidence

R17 requires post-publication observations, not invented baseline numbers. At 7 days check indexing/canonicals and new-route crawlability. At 28 days compare Search Console impressions, clicks and query-to-page mapping against a recorded pre-publication period. At 60 days inspect language/install, existing-project and integration entry paths using available consented analytics. At 90 days decide whether separate evaluation or orchestration pages are justified by distinct queries and evidence. Account access and a publication date are prerequisites; no schedule or automation is created here.

Additional paid-provider certifications and release-specific case studies remain future research. Preserve test versions, environment, assertions, failed/passed artifacts and limitations when adding them. This website change does not certify new product behavior or authorize production deployment.

## Verification result

Verified against the official Kujo 1.9.0 macOS x64 release: 28 Node tests, 50 pinned examples, and 28 workflow tests across 13 applications passed. The final build has 327 shareable routes; all have unique titles/descriptions/canonicals, one H1 and parseable JSON-LD. Both new guides have breadcrumb schema. Site contract, 328-file HTML validation (including 404), 327 social cards, 70-page SEO/source alignment, comparison links, generator freshness and JavaScript syntax checks passed. Production dependency audit reported zero vulnerabilities.

Language browser tests passed at desktop/tablet/mobile sizes. Additional browser tests passed with provider JavaScript enabled, disabled and a failed registry fetch; search, modal dismissal, all 25 static package links and responsive guides remain usable. Mobile guide screenshots were inspected. Responsive images were generated once; final content rebuilds reused 1,179 derivatives only after verifying each original image’s SHA-256 was unchanged. Detailed execution logs and screenshots are in the session’s local `/tmp/kujo-positioning-checks` evidence directory; the committed test scripts reproduce the checks.

## Production cache correction

The first production verification found that the unversioned provider script could remain cached after the new static directory deployed, replacing its cards with the previous JavaScript rendering. The builder now fingerprints the provider script URL, as it already does for the main site script and stylesheet. The positioning validator checks that the rendered URL matches the current script content hash; browser tests cover the resulting enhancement.
