# Before and after — 26 pages

| Check | Before | After |
|---|---:|---:|
| pages | 26 | 26 |
| production_200 | 26 | 26 |
| indexable | 26 | 26 |
| missing_titles | 0 | 0 |
| duplicate_titles | 0 | 0 |
| missing_descriptions | 0 | 0 |
| duplicate_descriptions | 0 | 0 |
| missing_canonicals | 0 | 0 |
| orphans | 0 | 0 |
| broken_internal_links | 0 | 0 |

BreadcrumbList coverage: 0 → 25. SoftwareSourceCode coverage: 0 → 21. CollectionPage coverage: 0 → 1. JSON-LD parse errors: 0 → 0. In-scope P0/P1: 0 → 0. Five baseline P2 root causes and one intermediate regression resolved; affected counts overlap. Page count unchanged.

All 26 have one H1, sitemap membership, canonical targets and language declarations. No pages exceed three clicks. No missing image alt attributes/dimensions or confirmed broken internal destinations. Empty alt text is intentional for decorative media. External statuses and redirect chains are in their CSVs; lab metrics are in performance.csv. Field data is unavailable. Scores are not assigned.

## Representative local lab measurements

| Template | Before LCP (ms) | After LCP (ms) | Before / after image bytes |
|---|---:|---:|---:|
| example | 2779 | 2705 | 1085 / 1085 |
| guide | 2628 | 2790 | 1085 / 1085 |
| home | 4035 | 3157 | 242721 / 77622 |
| index | 2705 | 2790 | 1085 / 1085 |

One run per template per phase. These values do not establish statistical significance or field improvement. Homepage CLS changed from 0 to 0.00049; other sampled templates remained 0. The deterministic improvement is removal of the hidden poster request: final home image transfers total 77,622 bytes versus 242,721 before. An intermediate 319,258-byte result exposed the duplicate download and was corrected before release.

All 38 unique scoped external destinations returned 200 in each phase. All 13 production routing probes passed, including canonical host/protocol, query preservation, feed and 404 behavior. The eight search/user-fetch crawler profiles passed; GPTBot is disallowed by robots policy and ClaudeBot is disallowed and returned 403. These preserved training policies are not search outages.
