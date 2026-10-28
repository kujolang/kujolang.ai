# SEO and Howl audit — 2026-10-28

**PASS WITH RECOMMENDATIONS.** Audited all 26 new/refined pages, with a full 281-page crawl for linking context. Repository fixes are deployed and verified. No in-scope P0/P1 issue was found before or after.

The baseline already had unique titles/descriptions, working canonicals, sitemap membership, one H1 per scoped page and no broken internal links or orphans. The missing pieces were semantic page/sample descriptions, source-backed Howl entries, an accessible logo label and responsive homepage media.

Added breadcrumbs to 25 pages, exact-source schema to 21 examples and collection markup to the Examples index. Corrected the logo label and deferred the hidden video poster while adding responsive hero candidates. All 26 Howl entries now reference real examples; their SVG, HTML, Markdown, captions and gallery were generated with Howl 1.2.0. Two renders matched across all 79 artifacts. [Download the showcase archive](howl/showcase.zip).

All 26 live pages return 200 with their canonical URL and updated markup. All 26 social-image hashes match the generated files. All 38 unique external destinations returned 200. Thirteen redirect/error/feed probes passed; search and user-fetch crawler checks passed. Training-crawler restrictions were preserved. The default Python user agent received an image 403; the explicit audit agent used by the page crawl fetched matching images. This access-policy distinction is retained in raw receipts.

Verification includes 28 Node tests, the 21-example runtime checks, full build and 1,167 responsive assets, semantic/source checks, Howl validation and three local/live browser suites. The suites cover code copying, navigation, no-JavaScript content, accessibility and responsive layouts. Twenty-two distinct required gates have successful evidence across the documented Loop iterations; final closeout passed against 3,170 unchanged source/output hashes. Historical failures and their repairs remain recorded.

Deployment: [40679981222](https://github.com/kujolang/kujolang.ai/actions/runs/40679981222) succeeded for `bbfb2b623e4af118fa9fe8da0aeeb09c3644e5e0`. Source commits: `cd89128` (SEO/media/accessibility) and `bbfb2b6` (Howl). See [changed files](changed-files.txt) and [iteration notes](../../.loop-engineering/seo-howl-pages/evidence/iteration-notes.md). The final evidence-only commit uses the repository's existing skip-CI convention; it does not change deployed site inputs.

In one comparable local mobile lab run, homepage LCP was 4,035 ms before and 3,157 ms after; image transfer was 242,721 versus 77,622 bytes. Other templates varied slightly. These are lab observations, not field CWV or a causal outcome study. [Before/after details](before-after.md) and [performance data](performance.csv) retain all values and limits.

Search-console, analytics, verified request logs, field CWV, controlled rankings and AI citation data: **NOT AVAILABLE — DATA ACCESS REQUIRED**. The limited public query observations cannot establish index coverage or rank. No ranking, traffic, conversion or citation gain is claimed. Internal SEO/AI scores are not assigned; verified counts are reported instead.

Next: use the same URL/query/question set for the dated [7-, 28-, 60- and 90-day measurement plan](recommendations.md). Private data access is a measurement limitation, not a blocker to the completed implementation. No new positioning, unsupported claims, training policy or external infrastructure settings were changed.
