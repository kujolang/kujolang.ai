# Ability release audit

**PASS WITH RECOMMENDATIONS** — 2026-09-04.

194 canonical pages audited, 194 serving HTTP 200 after deployment. Four product content pages and the private-source template changed. One content-coverage root cause (P1) was resolved; P0 remained zero. Private-source links were corrected from verified access evidence.

| Metric | Before | After |
| --- | ---: | ---: |
| canonical_pages | 194 | 194 |
| indexable_pages | 194 | 194 |
| production_200_pages | 194 | 194 |
| sitemap_urls | 194 | 194 |
| missing_titles | 0 | 0 |
| duplicate_titles | 0 | 0 |
| missing_descriptions | 0 | 0 |
| duplicate_descriptions | 0 | 0 |
| h1_issues | 0 | 0 |
| missing_canonicals | 0 | 0 |
| canonical_mismatches | 0 | 0 |
| broken_internal_links | 0 | 0 |
| orphan_pages | 0 | 0 |
| pages_deeper_than_three_clicks | 0 | 0 |
| missing_alt | 0 | 0 |
| missing_dimensions | 0 | 0 |
| schema_parse_errors | 0 | 0 |
| schema_coverage_pages | 194 | 194 |
| Unique public external 404/410 destinations | 3 | 0 |
| P0 root causes | 0 | 0 |
| P1 content coverage root causes | 1 | 0 |

Internal SEO/AI scores: not computed. Lab evidence: performance.csv and raw Lighthouse JSON. Search visibility and AI citation outcomes: NOT AVAILABLE — DATA ACCESS REQUIRED. No outcome improvement claimed.

See issues.csv, changes.md, methodology.md, data-availability.md, and recommendations.md for reproducible evidence and 7/28/60/90-day measurements.

Performance outcome is inconclusive. Baseline Lighthouse performance was 100 (LCP 1.446s, TBT 16ms); two after runs were 52/45 (LCP 3.920s/5.582s, TBT 1623ms/3505ms). Both after runs explicitly warned that the test CPU was slower than expected; CPU benchmark indices were 400.5/932 versus baseline 1286. CSS, scripts, hero image and fonts have unchanged URLs and decoded sizes; HTML increased 185 bytes. These observations do not establish a release-caused regression or a performance pass. Rerun on an idle, calibrated runner before drawing a performance conclusion. Accessibility and SEO lab scores remained 100; CLS remained zero. The repeat Lighthouse final screenshot was blank, so it is not visual approval evidence; a separate live browser accessibility-tree review confirmed the complete page and updated links.
