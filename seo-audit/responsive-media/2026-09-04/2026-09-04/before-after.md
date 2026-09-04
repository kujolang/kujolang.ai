# Before and after

Audit date: 2026-09-04

Immediate technical evidence only; search outcomes require elapsed time and first-party platform data.

| Metric | Baseline | After | Interpretation |
| --- | ---: | ---: | --- |
| Canonical/indexable pages | 194 | 194 | Complete inventory preserved |
| Production 200 pages | 194 | 194 | Every canonical page verified live |
| Missing/duplicate titles | 0 / 0 | 0 / 0 | Passed |
| Missing/duplicate descriptions | 0 / 0 | 0 / 0 | Passed |
| Missing canonicals / mismatches | 0 / 0 | 0 / 0 | Passed |
| Broken internal links | 0 | 0 | Passed |
| Orphans / depth >3 | 0 / 0 | 0 / 0 | Passed |
| Images / missing alt / missing dimensions | 828 / 0 / 0 | 828 / 0 / 0 | Existing accessibility and layout safeguards preserved |
| Responsive rendered images / missing candidates | 0 / n/a | 439 / 0 | Generator and rendered contract verified |
| Schema parse errors / covered pages | 0 / 194 | 0 / 194 | Full parse coverage preserved |
| Redirect issues | 0 | 0 | Canonical variants passed |
| Crawler access issues | 0 | 0 | Search/user-fetch allowed; training policy unchanged |
| Confirmed external 404/410 links | 6 | 6 | Separate owner decision remains |
| `/ecosystem/` image transfer | 3,475,511 B | 834,556 B | Down 76.0% in comparable lab runs |
| `/ecosystem/` LCP | 8.94 s | 5.42 s | Down 39.4% in one comparable lab run |
| P0 / P1 root causes | 0 / 1 | 0 / 1 | Private-repository journey remains |
| SEO health heuristic | 89/100 | 90/100 | Media readiness improved |
| AI readiness heuristic | 83/100 | 83/100 | No AI visibility claim |

The Lighthouse comparison uses one mobile-simulated run per phase on local static output with Lighthouse 13.4.1. It is lab evidence, not field Core Web Vitals.

Immediate technical evidence only; search outcomes require post-deployment data and elapsed time.
