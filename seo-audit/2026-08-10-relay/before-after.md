# Before and after

| Check | Before | After |
| --- | ---: | ---: |
| Canonical/indexable pages | 39 | 40 |
| Production pages returning 200 | 39 | 40 |
| Sitemap URLs | 39 | 40 |
| Schema-covered pages | 39 | 40 |
| Broken internal links | 0 | 0 |
| Orphan pages | 0 | 0 |
| Missing or duplicate titles | 0 | 0 |
| Missing or duplicate descriptions | 0 | 0 |
| Canonical mismatches | 0 | 0 |
| Schema parse errors | 0 | 0 |
| Images missing alt text or dimensions | 0 | 0 |

Relay is the single added canonical page. It is linked from the ecosystem collection, appears once in the sitemap and `llms.txt`, and exposes its canonical URL, unique metadata, Howl social image, `SoftwareSourceCode` JSON-LD, and GitHub repository URL.

The custom error document remains excluded from the sitemap. A synthetic nested missing route returns HTTP `404`, declares `noindex,follow`, omits a canonical link, and loads its stylesheet, JavaScript, icons, and brand image from root-absolute URLs.
