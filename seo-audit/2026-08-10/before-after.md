# Before and after

Audit date: 2026-08-10

Immediate technical evidence only; search outcomes require post-deployment data
and elapsed time.

| Metric | Baseline | After | Evidence |
| --- | ---: | ---: | --- |
| Canonical/indexable pages | 38 | 38 | `baseline-summary.json`, `after-summary.json` |
| Production canonical pages returning 200 | 38 | 38 | Baseline/after live page probes |
| Missing titles/descriptions | 0 / 0 | 0 / 0 | Crawl datasets |
| Duplicate titles/descriptions | 0 / 2 pages | 0 / 0 | Crawl datasets |
| Missing canonicals / canonical mismatches | 0 / 0 | 0 / 0 | Crawl datasets |
| H1 issues | 0 | 0 | Crawl datasets |
| Broken internal links | 0 | 0 | Link graph |
| Confirmed external 404/410 links | 2 | 2 unresolved | Live anonymous probes |
| Orphans / depth greater than 3 | 0 / 0 | 0 / 0 | Link graph |
| Missing alt attributes | 0 | 0 | Image audit |
| Missing intrinsic dimensions | 71 | 0 | Image audit |
| JSON-LD parse errors | 0 | 0 | Schema audit |
| Page-purpose schema coverage | 1/38 | 38/38 | Baseline/after schema inventory |
| Duplicate nested output aliases | 38 flat aliases | 0 flat aliases | Output manifests |
| Home Lighthouse performance | 71 | 86 | Comparable one-run lab receipts |
| Ecosystem Lighthouse performance | 55 | 70 | Comparable one-run lab receipts |
| Detail Lighthouse performance | 76 | 87 | Comparable one-run lab receipts |
| Home / ecosystem / detail LCP | 3,730 / 7,903 / 3,610 ms | 3,757 / 6,382 / 3,682 ms | Comparable one-run lab receipts |
| P0 issues | 0 | 0 | `issues.csv` |
| P1 root causes | 2 | 1 | `issues.csv` |
| Internal SEO health heuristic | 71/100 | 86/100 | Weighted rubric below |
| Internal AI-search readiness heuristic | 65/100 | 74/100 | Weighted rubric below |

## Internal heuristic scoring

SEO weights: crawlability/indexability 20; metadata 15; architecture 15;
content 15; structured data 10; performance 10; media 5; authority/trust 5;
AI readiness 5. After scores were 20, 15, 15, 8, 10, 6, 5, 3, and 4.

AI-search weights: search crawler access 15; indexability 10; entity clarity 10;
source attribution 10; original/citable information 15; semantic data 10;
internal topic relationships 10; freshness 5; technical/media 5; measured AI
visibility 10. After scores were 15, 10, 9, 7, 8, 10, 10, 0, 5, and 0.
Missing measured visibility earns zero. These are trend heuristics only.
