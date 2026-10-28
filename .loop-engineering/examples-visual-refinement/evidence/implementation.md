# Examples visual refinement

## Scope and user steering

Match the updated homepage across the Examples index and all 21 individual pages. Add in-block top-right copy icons on these pages and the homepage. Use conventional readable code fonts instead of Departure Mono and beautify code presentation.

## Implementation

The existing example generator owns the index, detail layouts and homepage explorer. The index uses a split introduction, dark collection panel, filter toolbar, numbered categories, bordered cards and a contrasting integration section. Detail pages use one title, a source panel alongside a runbook, a separate expected-output panel, expandable provenance and previous/next navigation.

Copy buttons are accessible 44px SVG icons inside source, command and expected-output blocks. Space above the code prevents overlap. Live status feedback is positioned inside the block. Native no-JavaScript content/downloads remain available.

Code blocks use the system monospace stack with ligatures disabled, standard indentation tab stops and comfortable line height. Escaped token highlighting distinguishes comments, strings, keywords, numbers and literals without changing source whitespace or copied bytes. Catalog hashes, downloadable samples, runtime commands and verification boundaries remain intact.

## Iteration

The first evaluation was interrupted after the user added the code-font/beautification requirement; its build predates that steering. The next complete build visually matched the intended desktop/mobile layouts, and a diagnostic suite passed all 21 individual examples, exact source/output clipboard checks and their accessibility audits. An index audit found two low-contrast dark-panel labels (2.72:1). Their foreground was changed to #ccc before the acceptance rebuild.

Final native gate receipts and browser screenshots identify the accepted build; earlier attempts are historical evidence, not acceptance claims. Original repository Loop configuration and previous task runs remain untouched.

## Accepted verification

The fresh `acceptance/` native run passed all 16 required gates with zero failures or external blockers. This includes all 21 verified samples, 26 Node tests, a full build, 1,167 responsive image variants, site contracts, generated output, language routes, social cards, comparisons, syntax, audit and both browser suites.

The dedicated browser suite covers all 21 detail pages at desktop/mobile widths, the index at desktop/tablet/mobile widths, conventional code fonts, top-right copy-icon geometry, exact source and output clipboard contents, verification disclosures, filtering and no-JavaScript content. Every individual example passed WCAG A/AA checks. The shared suite also verifies the index and homepage accessibility. Final screenshots and Axe receipts are under `acceptance/evidence/`.

Catalog and downloadable sources are unchanged. `acceptance/evidence/verified-build-sha256.json` binds the reviewed source and built pages. Publication uses the existing main-branch GitHub Pages workflow after this acceptance; final deployment and live-check results are recorded in Strata session `local:kujo-examples-visual-20261027` to avoid altering the accepted application.
