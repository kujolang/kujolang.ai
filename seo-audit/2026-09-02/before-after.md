# Before and after

Audit date: 2026-09-02

Immediate technical evidence only; search outcomes require post-deployment data and elapsed time.

| Measure | Before | After | Evidence |
| --- | --- | --- | --- |
| Publishing House mobile document width | 1,059px in a 390px viewport | 390px in a 390px viewport | Lens `dom-summary.json` |
| Severe horizontal overflow | 1 error | 0 errors | Lens reports |
| Automated accessibility errors on changed route | 0 in baseline run without contained code scrolling | 0 after scrollable code blocks became keyboard-focusable | Lens axe-core output |
| Canonical/indexable pages | 192 / 192 | 192 / 192 | `baseline-summary.json`, `after-summary.json` |
| Broken internal links in generated site | Baseline production download not suitable for local target resolution | 0 | `after-summary.json` |
| Missing/duplicate titles and descriptions | 0 / 0 | 0 / 0 | crawl datasets |
| Canonical mismatches | 0 | 0 | crawl datasets |
| Schema parse errors | 0 | 0 | schema audit |
| Images missing alt text or intrinsic dimensions | 0 / 0 | 0 / 0 | image audit |
| Howl social-card coverage | 192 declared cards | 192 generated cards for 192 shareable routes | Howl validation and site contract |
| Operator readiness label | Fixture-operational disclaimer | Production-capable live control-plane contract with explicit deployment gates | source and rendered page |
