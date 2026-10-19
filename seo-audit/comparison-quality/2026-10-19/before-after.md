# Before and after

| Check | Before | After |
|---|---:|---:|
| Canonical comparison pages | 8 | 8 |
| Technically indexable pages | 8 | 8 |
| Missing/duplicate title or description | 0 | 0 |
| Canonical mismatch / missing sitemap entry | 0 | 0 |
| H1 issues / orphans / depth greater than 3 | 0 | 0 |
| Broken internal links | 0 | 0 |
| Confirmed broken cited destinations | 0 of 28 | 0 of 28 after deploy |
| Missing alt / intrinsic dimensions | 0 | 0 |
| JSON-LD parse errors | 0 | 0 |
| Pages with appropriate schema | 8 | 8 |
| Truncated social-card titles | 5 | 0 |
| Truncated social-card descriptions | 7 | 0 |
| Generic hub search title | 1 | 0 |
| P0 / P1 root causes in scoped pages | 0 / 0 | 0 / 0 |
| Internal numeric SEO / AI readiness score | Not assigned | Not assigned |

Baseline robots results were false negatives caused by the audit client's generic fetch; corrected live parsing establishes Allow: / for all eight routes. No server robots change occurred. Ten crawler profiles were probed on the hub; eight search/user-fetch profiles were also probed across all eight pages. ClaudeBot training requests returned 403 while its robots fetch returned 200. This is not evidence of search-bot blocking, and training policy was not altered. HTTP www takes two hops to canonical HTTPS; HTTPS www and slash normalization take one. Missing-route probes return genuine 404s. No production host failures were observed.

No measured search or AI visibility improvement is claimed.
