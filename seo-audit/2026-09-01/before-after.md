# Before and after

Audit started: 2026-09-01. Deployment verification: 2026-09-02.

Immediate technical evidence only; search outcomes require post-deployment data and elapsed time.

| Metric | Production baseline | After launch | Change |
| --- | ---: | ---: | ---: |
| Canonical pages | 190 | 191 | +1 intentional |
| Production HTTP 200 pages | 190 | 191 | +1 |
| Indexable pages | 190 | 191 | +1 |
| Sitemap URLs | 190 | 191 | +1 |
| Missing or duplicate titles | 0 | 0 | 0 |
| Missing or duplicate descriptions | 0 | 0 | 0 |
| H1 issues | 0 | 0 | 0 |
| Missing or mismatched canonicals | 0 | 0 | 0 |
| Orphan pages | 0 | 0 | 0 |
| Pages deeper than three clicks | 0 | 0 | 0 |
| Missing image alt text | 0 | 0 | 0 |
| Missing intrinsic image dimensions | 0 | 0 | 0 |
| JSON-LD parse errors | 0 | 0 | 0 |
| Pages with schema coverage | 190 | 191 | +1 |
| Confirmed public external 404/410 destinations | Not measured | 2 | Current evidence |

The baseline download intentionally retained canonical HTML rather than a full
asset mirror, so its raw local link-status count is not used as a production
broken-link claim. Live production page status, canonical membership, and the
complete rendered after crawl are the comparable launch evidence.

The canonical-set diff is exact: `/ecosystem/ability/` was added and no route was
removed. Search rankings, traffic, conversions, and AI-answer visibility require
future platform evidence and are not included in this technical delta.

The two external 404s are the pre-existing Leash and Ward GitHub destinations.
Local authenticated git access confirms both repositories exist, but the public
URLs are not usable by an unauthenticated site visitor. They are reported as P2
owner decisions and are unrelated to the Ability release.
