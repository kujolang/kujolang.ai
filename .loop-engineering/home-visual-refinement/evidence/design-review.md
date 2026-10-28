# Homepage visual refinement

## Request and scope

User correction: homepage is too text-heavy, lacks visual separation; use Compare pages as the design reference, show the shared footer, and avoid release labels such as v1.9.

## Design decisions

- Shortened hero copy and replaced repeated prose grids with distinct editorial sections.
- Reused Compare's monochrome contrast, numbered kickers, bordered panels, split headings and compact link rails.
- Added a dark runtime section, a dedicated terminal panel, compact ecosystem links and a spacious final call to action.
- Kept the interactive six-example explorer and its complete no-JavaScript fallback. Detailed provenance remains on example pages; homepage sample metadata and installation command are release-neutral.
- Removed the obsolete global rule that hid the shared footer when `.home-hero` exists; no duplicate footer markup.
- Preserved source samples, internal release pins, comparison pages and all routes.

## Workflow and evidence

Native Loop Engineering runner uses this directory's `loop.yml`; the original `.loop-engineering/loop.yml` and its historical run are unchanged. Implementation is performed by the agent; native eval gates record actual command outcomes. Automatic commits remain disabled because the runner may commit on failure. Reviewed commits and pushes happen only after passing checks.

Desktop visual inspection: clear separation between hero, code, use cases, runtime, install, ecosystem, evidence and final CTA. The shared footer is visible. Final browser screenshots and accessibility reports are in `final/evidence/browser/`; successful gate receipts are in `final/iterations/001/`. The initial attempt is retained in `iterations/001/`.

Browser regression checks now explicitly require the homepage footer and prohibit the removed version label, in addition to existing clipboard, selection, no-JS, responsive, navigation and accessibility checks. Evidence output can be directed to a new directory to preserve past runs.

## Responsive iteration

The initial mobile visual preview exposed horizontal overflow (497px document at 390px viewport): collapsing the three-line installation heading joined it into one unbreakable word. Removed that mobile override and set the installation grid children to `min-width: 0`. A source-CSS preview then measured exactly 390px at a 390px viewport. This preview is diagnostic only; final acceptance requires a fresh native build and browser gate, without route interception.

## Final local verification

All 15 required gates passed on the fresh build: generated examples, 21 runtime sample checks, 26 Node tests, build, 1,167 responsive images, site contract, generated output, language routes, social cards, comparisons, JavaScript and shell syntax, dependency audit, browser suite and diff checks. Browser checks cover desktop/tablet/mobile, footer visibility, no homepage version label, keyboard selection, exact clipboard contents, filtering, navigation, no-JavaScript fallback and six page types with zero Axe WCAG A/AA violations. Final mobile rendering measures 390px document width at a 390px viewport.

The native final iteration verdict is success with zero required failures and zero external blockers. Its initial summary remained partial only because the checklist still listed the verification and publication steps; their final disposition is recorded in the phase SUMMARY after publication. The first attempt failed on the mobile overflow and outdated homepage contract; final verification supersedes it.

## Publication

Application commit 445adaa0c02bb02791cc97d71813ba03d05d9e36 was pushed after all required local gates passed. The existing authorized GitHub Pages workflow completed successfully in run 40609501440. All 28 public routes and the full production browser/accessibility suite passed. `production.json` and `production-browser/` preserve the release evidence.
