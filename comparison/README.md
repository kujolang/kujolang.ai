# Comparison and discovery system

The site remains a Kujo SSG site using vendored SiteKit. `comparison/catalog.json` is the editable source for seven substantive pages and the comparison hub. `scripts/render-comparisons.mjs` validates it and generates `content/compare/*.md`, the public Markdown equivalents under `public/compare/text/`, and escaped semantic HTML partials under `templates/compare-content/`. The builder reads those generated partials for the compare collection because its Markdown renderer deliberately escapes raw HTML. Markdown remains the readable indexing projection; partials provide semantic tables without changing global Markdown behavior. The SSG's existing collection handling owns `/compare/` and nested routes, sitemap entries and llms.txt indexing. `templates/compare.html` supplies the item frame; `templates/page-compare.html` is the curated hub.

## Add or revise a comparison

1. Establish canonical project identity and pin source evidence. Add references with real review date, evidence level and version. Mark unresolved identity explicitly.
2. Add a `direct` record with technology identity, dimensions referencing centralized Kujo facts, honest limitations, recommendations, FAQ and related slugs. Recommendations are editorial prose; matrix facts carry status and layer.
3. Include competitor strengths, when to choose each tool, coexistence limits and benchmark methodology or an explicit no-benchmark explanation.
4. Run `npm run compare:generate`. Never hand-edit generated content or public text.
5. Add a matching Howl social card and generate its JPEG using the existing social-card workflow. Source image URLs belong in metadata, not copied HTML.
6. Run `npm test`, the production SSG build, responsive images and both site contracts. Run `npm run compare:verify` against generated output; review desktop and mobile rendering and source-link receipts.
7. Update the research and validation records only for checks actually performed. Commit source and generated Markdown together. Generated `output/` remains ignored.

```sh
npm ci
npm run compare:generate
npm test
kujo run ./build.kujo -- --site-url https://kujolang.ai
npm run images:responsive
bash scripts/verify-site-contract.sh output
bash scripts/validate-generated-output.sh output
npm run compare:verify
npm run social:verify
```

Preview: `kujo serve output --host 127.0.0.1 --port 4178`. Full convenience build/preview remains `bash scripts/dev.sh 4178`.

## Validation and integrity

The data validator rejects missing sources, unknown fact references, unsupported statuses, invalid slugs/dates, duplicate routes, missing mandatory direct-comparison sections and broken related references. Node tests exercise rejection paths and byte-for-byte generation drift. The output verifier checks routes, metadata, sitemap, JSON-LD, internal links and text consistency. HTTP source checks are review receipts, not a guarantee of future link availability.

The public Markdown and HTML share catalog facts. HTML uses an accessible horizontally scrollable table on narrow screens, explicit textual evidence statuses and normal source links. No comparison JavaScript or tracking dependency is required. Page content remains readable with JavaScript disabled. Shared native site interactions continue to work.

## Research and measurement

See `research/implementation-inventory.md`, `research/ecosystem-inventory.json`, `research/research-report.md`, `research/opportunities.csv`, `research/source-checks.json`, `measurement.md` and `validation.md`. The public editorial policy is `public/compare/editorial-policy.md`. The artifact exercise is public, runnable and deliberately not a cross-language benchmark.

Pushing main triggers GitHub Pages. The user authorized comparison releases and live verification in this session; preserve the required checks before publishing.

## Hub overview

`catalog.hub` owns the four profiles and six comparison dimensions. Each supported matrix cell references an existing catalog fact by `kujo:factName` or `page-slug:dimensionLabel`; the generator rejects stale references. Empty references mean not assessed, never unsupported. `render-comparison-hub.mjs` produces the hub template and public `overview.md`. Technical briefs reuse the direct comparisons; update their sections at the source. SiteKit card, table, feature-grid and native accordion primitives provide the layout without new client JavaScript.

Direct comparison pages also use catalog `deepDive` records for architecture lenses, decision scenarios and proposed evaluation plans. See [direct-redesign.md](direct-redesign.md). Their generated frontmatter selects the field-guide template; do not edit generated HTML or Markdown directly.

Discovery and workflow guides use catalog `guide` data for cited decision lenses and matrices, evaluation steps, worked examples and interpretation pitfalls. `render-comparison-guide.mjs` projects them into the shared field-guide template and public Markdown. See [guide-redesign.md](guide-redesign.md).
