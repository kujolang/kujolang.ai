# Comparison hub redesign — 2026-10-19

The initial hub introduced the topic but did not provide enough comparative depth at a glance. This revision makes the hub a working overview: four adoption profiles, a six-dimension matrix with 24 cells, three expandable architecture briefs, a five-stage workflow and a concrete positive/negative artifact check.

## Component review and implementation

Reviewed the vendored SiteKit component manifest, distribution guidance and the site's actual card, table, feature-grid, accordion and stats styles. The new page uses `sk-card`, `sk-table`, `sk-feature-grid`, `sk-accordion` and `sk-button`; a compact section index and a contrasting orientation panel establish hierarchy. No UI framework or new browser JavaScript was added. Native disclosures keep summaries visible and expose source evidence on demand.

Hub profiles and matrix summaries live in `comparison/catalog.json` under `hub`. Matrix facts reference stable dimension labels, not array positions; reordering a comparison cannot silently change its meaning. The generator validates those references and produces the hub HTML and Markdown overview. Architecture, coexistence and limitations reuse the existing direct-comparison sections. The redesign adds decision context and access to existing research, not new benchmark or competitor-runtime claims.

## Local verification

- 16 Node tests passed, including rejected stale fact references, incomplete matrix rows and exact generation drift across 23 projections.
- Kujo 1.8.0 focused build passed in 90.29580231099999 seconds, using the seven comparison records and unchanged shared builder/layout.
- Generated HTML validation passed for the focused output. Canonicals, sitemap entries, JSON-LD, one H1, section anchors and public Markdown checked for all eight comparison routes.
- 37 unique internal destinations checked. Unchanged ecosystem/marketing destinations resolved against the previously validated full build; exact fallback list is in `research/hub-redesign-validation.json`.
- Desktop table fits its container. Mobile page width equals the 375px content viewport; the 1040px table scrolls within a 333px region, with row labels kept visible. Keyboard table scrolling and native disclosure activation passed.
- Section anchors clear the fixed navigation. Matrix cells expose evidence and source scope; technical disclosures expose four subsections each.

The full repository build and site contract run in the Pages deployment workflow. Local checks above are deliberately described as focused, not a fresh full-site build. Deployment and live verification receipts belong to the release handoff.
