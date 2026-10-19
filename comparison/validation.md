# Launch validation — 2026-10-19

## Scope and reproducibility

Eight new static routes: the comparison hub, three direct comparisons, three distinct discovery pages and one consolidated workflow guide covering verification, evaluation, traceability, specifications and execution evidence. Existing Ethos, Spec and RunLedger pages provide contextual entry points. No production deployment was performed.

The immutable starting point is `db3f698cbb5eef73fe746bce3a8fee17e5250cfa`. The baseline crawl is under `seo-audit/2026-10-19-comparisons/baseline/`; its README records the full artifact archive hash. The implementation branch is `feat/comparison-discovery-20261019`.

## Checks

The full production build completed successfully in 2074.473751285 seconds. The build uses the official, checksum-verified Kujo 1.8.0 macOS x64 release, matching the repository CI pin. The independent artifact exercise uses Kujo 1.8.1 as explicitly required by its fixture. These are different purposes and are not comparative benchmark runs.

- Production build: `kujo run build.kujo -- --site-url https://kujolang.ai` passed with the checksum-verified 1.8.0 runtime.
- `npm run compare:verify`: eight routes and 342 internal links passed; public text and semantic table checks passed.
- `bash scripts/validate-generated-output.sh output`: all 256 HTML files passed.
- Mobile: all eight routes have 375-pixel page width in the 390-pixel iframe (scrollbar uses the remainder), without page overflow. The 700-pixel matrix scrolls within its 333-pixel region; ArrowRight moved scrollLeft to 40 while focused. Mobile menu opening and closing passed. Desktop hub review passed. See `research/mobile-checks.json`.
- `npm run images:responsive`: 1,167 variants generated; no skipped source sizes.
- `bash scripts/verify-site-contract.sh output`: passed, including 553 rendered responsive images and 255 social cards for 255 routes. The footer expectation was updated for the new Compare entry.
- Full after crawl: 255 canonical/indexable/sitemap pages; eight added, none removed. No broken internal links, orphan pages, metadata duplication, canonical mismatches, missing image accessibility fields, missing responsive candidates or schema syntax errors. The single pre-existing Muzzle H1 issue is unchanged. See `seo-audit/2026-10-19-comparisons/after/after-summary.json` and `route-delta.json`.
- `npm test`: 14 passed, including negative catalog-validation cases and byte-for-byte checks of 21 generated projections.
- `npm run compare:check`: seven records and all 21 projections valid.
- `node --check assets/js/site.js`: passed.
- `bash -n scripts/dev.sh scripts/verify-site-contract.sh`: passed.
- `npm audit --omit=dev`: zero vulnerabilities reported.
- Public source receipts: all 24 unique catalog URLs returned HTTP 200 during review; see `research/source-checks.json`.
- Artifact exercise: expected value accepted; wrong value and malformed/missing/wrong-type controls rejected. One repetition, no timing or cross-language superiority conclusion. See `research/artifact-exercise.json`.

## SEO, accessibility and evidence integrity

Static content supplies distinct titles/descriptions, canonical URLs, crawlable links, sitemap entries, existing robots policy, social images, visible breadcrumbs and matching BreadcrumbList JSON-LD. The hub uses CollectionPage; comparison articles retain the existing site schema convention. No FAQ rich-result promise or fabricated aggregate ratings were added. Markdown and HTML are generated from one catalog; llms.txt uses the SSG collection index. Machine-readable exports are conveniences, not indexing guarantees.

The matrices use captions, row/column headers, textual statuses and focusable horizontal scrolling. Existing SiteKit navigation and typography are retained. Mobile checks use a 390-pixel iframe viewport and desktop checks use the in-app browser. This is a targeted visual/keyboard/semantic review, not a screen-reader certification or field performance measurement.

## Limits and publication prerequisites

- Zero's official domain identifies the requested preview language, but a canonical source repository and numbered release could not be verified. The page explicitly limits claims to official documentation and labels that evidence accordingly.
- Bend/BAML implementation and test source were inspected at pinned commits; their complete runtimes/test suites were not executed. No fair cross-language benchmark was established or claimed.
- Production Python probes returned 403 while the homepage loaded in the browser. Automated production crawl access remains indeterminate; local validation does not establish search-engine indexing.
- Search Console, Bing Webmaster Tools, controlled Google/Bing rankings, keyword-volume exports, analytics and observed AI citations were unavailable. See `measurement.md` for a privacy-conscious reporting plan.
- The baseline contains an existing second H1 on `/ecosystem/muzzle/`; this comparison change does not alter it.
- Publish only after explicit approval. After publication, confirm live responses/canonicals, submit or inspect the sitemap in existing webmaster accounts, establish actual landing/referral/conversion baselines, and recheck volatile competitor versions before treating the research date as current.

## Next content decisions

`research/opportunities.csv` is the ordered roadmap. Python/TypeScript migration evidence comes before additional generic language pages. Rust/Mojo require a comparable workload and environment. MoonBit/Unison need deeper implementation review. Refresh Zero provenance when the project supplies it; do not guess a repository.

## Change inventory and commands

Research and evidence: `4f89d7d`. Implementation and automated checks: `d8048f2`. The final validation commit adds this report and the after-crawl artifacts. Use `git diff --name-status db3f698c..HEAD` for the complete created/modified file inventory.

See `README.md` in this directory for generation, build and preview commands. Use a supported Kujo release matching the repository workflow; the unrelated older executable on this machine's default PATH is not the tested runtime.
