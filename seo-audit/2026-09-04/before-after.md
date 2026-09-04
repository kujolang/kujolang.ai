# Before and after

Audit date: 2026-09-04

Immediate technical evidence only; search outcomes require elapsed time and first-party platform data.

| Metric | Baseline | After | Interpretation |
| --- | ---: | ---: | --- |
| Canonical/indexable pages | 193 | 194 | One concurrent Paperclip release added one valid page |
| Production 200 pages | 193 | 194 | Every canonical after page verified live |
| Sitemap URLs | 193 | 194 | Exact canonical inventory |
| Missing/duplicate titles | 0 / 0 | 0 / 0 | Passed |
| Missing/duplicate descriptions | 0 / 0 | 0 / 0 | Passed |
| Missing canonicals / mismatches | 0 / 0 | 0 / 0 | Passed |
| H1 issues | 0 | 0 | Passed |
| Broken internal links | 0 | 0 | Passed |
| Orphans / depth >3 | 0 / 0 | 0 / 0 | Passed |
| Images / missing alt / missing dimensions | 823 / 0 / 0 | 828 / 0 / 0 | Attributes passed; transfer size remains a recommendation |
| Schema parse errors / covered pages | 0 / 193 | 0 / 194 | Full parse coverage |
| Redirect issues | 0 | 0 | Canonical variants passed |
| Crawler access issues | 0 | 0 | Search/user-fetch allowed; training bots intentionally disallowed |
| P0 root causes | 0 | 0 | None |
| P1 root causes | 2 | 1 | Hero scripting fixed; private-repository CTA decision remains |
| SEO health heuristic | 84/100 | 89/100 | Performance evidence improved |
| AI readiness heuristic | 82/100 | 83/100 | Technical readiness improved; measured AI visibility remains 0/10 |

## Representative Lighthouse lab results

| Template | Baseline LCP | After LCP | Baseline TBT | After TBT |
| --- | ---: | ---: | ---: | ---: |
| Home | 3.71 s | 3.76 s | 1.09 s | 0.24 s |
| Ecosystem catalog | 12.36 s | 8.94 s | 2.93 s | 0.83 s |
| PackWrite | 12.59 s | 3.61 s | 1.56 s | 0.21 s |
| Ability | 10.90 s | 2.73 s | 8.91 s | 0.15 s |

These are single mobile-simulated lab runs. They demonstrate the scripting fix but do not substitute for field CWV or establish search impact.
