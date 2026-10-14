# Before and after — Source release discovery

| Check | Before | After |
| --- | --- | --- |
| Source ecosystem URL | HTTP 404 | HTTP 200 |
| Docs status | Private repository instructions | Public v0.1.0 setup and explicit limits |
| Website HTML routes, including recovery page | 246 | 247; no removals |
| Docs HTML routes | 107 | 107; no removals |
| MCP catalog items | 234; no Source entry | 235; exact Source lookup verified |
| Invalid JSON-LD | 0 | 0 |
| Broken generated internal destinations | 0 | 0 |
| Missing titles | 0 | 0 |
| Missing canonicals | One noindex recovery page | Same recovery page only |
| Howl social cards | 245 | 246; every shareable route covered |
| Source hero | None | 1916×821 WebP, 48,154 bytes, pure 0/255 channels |
| Source social image | None | 1200×630 JPEG, 188,551 bytes |

The final generated artifact is from successful run 38597461622 at content commit 4e7110308b9815c254a2fd4bfbc872af0749641b. The public original image bytes match the reviewed files. Browser checks passed at 1440px and 390px with all images loaded and no document overflow. HTTP/www/slash variants reach the canonical page in one redirect; the canonical and query variant return 200 directly.

These are technical publication results. No search ranking, traffic, AI citation or runtime performance gain is claimed. Baseline build timing 1090.803s was measured locally; final CI build 368.948s ran on a different machine and is not a valid before/after performance comparison.
