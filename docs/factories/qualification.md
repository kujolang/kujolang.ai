# Factories integration qualification

Verified on 2026-11-13 in the local `kujolang.ai` checkout using Node 26.12.1, Kujo 1.9.0 and Chrome. The source baseline was clean `main` at `5fad198eadcb5fcff0b185c952ca8748d7bb5ba1`; work is on `feat/factories-ecosystem`. No live factory generation, paid provider calls or production deployment formed part of these checks.

## Build and regression results

All commands below passed. Kujo was invoked through `/Users/robertdevore/2026/Kujolang/kujo-repos/kujo/target/release/kujo` because the older executable on the user-local path was 1.5.0.

| Command | Observed result |
| --- | --- |
| `kujo run ./build.kujo -- --site-url https://kujolang.ai` | Kujo 1.9.0 build completed; 73 pages versus 72 in the separately built baseline. |
| `npm test` | 34 passed, 0 failed; 1 built-output test intentionally gated until the production build. |
| `npm run factories:verify` | 7 passed, including the previously gated output checks. |
| `npm run images:responsive` | 1,230 variants generated at 640, 960 and 1,280 pixels; 0 skipped. |
| `npm run images:verify` | Responsive contract passed for 573 rendered images. |
| `bash scripts/verify-site-contract.sh output` | Passed: 4 ecosystem section catalogs, existing ecosystem routes, 135 skills, 44 released workflow kits plus Publishing House Operator, navigation, metadata and SiteKit 1.2.0 integrity. |
| `bash scripts/validate-generated-output.sh output` | 339 HTML files checked; validation passed. |
| `npm run social:cards` and `npm run social:verify` | Howl cards generated; 333 cards cover 333 shareable routes, with the branded homepage fallback for 404. |
| `npm run examples:check`, `npm run workflows:check`, `npm run providers:check`, `npm run guides:check` | All generated sources match their canonical inputs. |
| `npm run examples:verify` | 50 pinned examples passed, along with explicit AI capability and nested-route traversal gates. |
| `npm run workflows:verify` | 28 tests passed. |
| `npm audit --omit=dev` | 0 vulnerabilities reported. |

The factory regression test runs catalog synchronization against temporary, real Git fixture catalogs. It confirms that every existing ecosystem Markdown page, all five factory pages, the category page and their social cards survive synchronization unchanged. Built checks confirm unique canonicals, related-product routes, release boundaries, images, demonstrations, metadata, sitemap inclusion and one discovery record per new route.

## Browser and visual checks

Final browser run: **19:18:37–19:19:03 UTC, 2026-11-13; passed**. The exact command was:

```sh
PLAYWRIGHT_MODULE=/Users/robertdevore/2026/Kujolang/kujo-repos/site-kit/node_modules/playwright \
AXE_SCRIPT=/Users/robertdevore/2026/Kujolang/kujo-repos/site-kit/node_modules/axe-core/axe.min.js \
CHROME_BIN='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' \
node scripts/test-factories-browser.cjs
```

The site was served at `http://127.0.0.1:4178`. Coverage included all six new routes at 1440×1000 and 390×1000:

- 12 page/viewport cases and 12 Axe WCAG A/AA audits; **0 violations** and **0 console errors**.
- 20 local links returned successful responses. In-page anchors resolve, images decode, and the pages have one main landmark and one H1 without viewport overflow.
- All five native MP4 players decoded metadata and advanced muted playback; their local download URLs returned successful HEAD responses. Controls, posters, `preload="none"` and absence of autoplay were checked.
- Mobile menu opening, Escape dismissal and the Factories navigation link passed. All six pages retain content, links and native players with JavaScript disabled.
- Homepage, ecosystem index and the three existing ecosystem category routes passed desktop/mobile regression checks.
- All six routes occur exactly once in the discovery index. A separate live local `search_site` query returned the five factory products; see [discovery verification](discovery-verification.json).

All 12 final hero screenshots were visually inspected: headings and calls to action are readable, the monochrome artwork fits the desktop/mobile crop, code panels stay within the viewport, and breadcrumbs clear the fixed navigation. The header-clearance regression initially exposed a 14-pixel overlap: the header occupied 112 pixels while the breadcrumb started at 98 pixels. Increasing the factory breadcrumb padding to `calc(var(--site-header-block) + 3rem)` fixed it; the final browser run passed the bounding-box assertion on both viewport sizes.

The site uses its existing static `kujo-light` theme. A separate dark theme was not introduced or claimed. Reduced-motion browser contexts were used for stable visual inspection.

Evidence: [browser receipt](../../.loop-engineering/evidence/factories-browser/receipt.json), the adjacent full-page and hero screenshots, and the 12 `axe-*.json` reports. Native video playback here is a technical check, **not full listening review, creative approval or approval of an example campaign**.

## Source, artwork and media evidence

- [Capability matrix](capability-matrix.md) and [machine-readable matrix](capability-matrix.json): exact upstream commits, release references, contracts, agents, setup, limitations and evidence links.
- [Dependency map](dependency-map.md): direct execution, pinned source and contract relationships kept separate from optional or proposed work.
- [Research verification](research-verification.json): isolated Product Launch v0.1.0 contract tests passed 12 Python and 11 Node tests without provider calls; this does not repeat the upstream Ubuntu installation benchmark.
- [Hero prompts and validation](../../assets/prompts/factory-heroes.json) and [Factory Floor provenance](media-provenance.json): generated artwork is distinct from authentic interface evidence.
- [Video mirrors](video-mirrors.json): all five local MP4 mirrors match the SHA-256 of their downloaded public source. Product Launch uses the approved v0.1.0 coordinator demo, not the example campaign clip.
- [Public link verification](public-link-verification.json): public repository, evidence and media link checks.
- [Integration inventory](integration-inventory.md): exact canonical URLs, website surfaces, canonical content ownership and preserved routes.

## CI and deployment boundary

The implementation branch's [CI run 43489311196](https://github.com/kujolang/kujolang.ai/actions/runs/43489311196) passed at commit `25571ce`. The subsequent breadcrumb change at `b0e65ea` passed [CI run 43490632497](https://github.com/kujolang/kujolang.ai/actions/runs/43490632497), with the deploy job skipped. The final local browser and output checks above include the breadcrumb fix.

This qualification does not establish production deployment. The feature branch and PR retain the repository's main-branch-only Pages deployment boundary. No unresolved local build, navigation, image, playback, accessibility or link failure remained after the final checks.
