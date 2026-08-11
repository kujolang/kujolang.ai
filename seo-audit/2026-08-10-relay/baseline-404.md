# Relay and nested 404 baseline

Captured at `2026-08-11T03:40:02Z` before implementation.

- `https://kujolang.ai/ecosystem/relay/` returned HTTP `404`.
- `https://kujolang.ai/ecosystem/not-a-real-tool/` returned HTTP `404`.
- The served custom error document referenced relative assets such as `assets/css/sitekit.css`, `assets/js/site.js`, `favicon.ico`, and `assets/images/kujo-logomark.svg`. At a nested missing URL those resolve below the nonexistent route and fail to load.
- The error document canonicalized to `https://kujolang.ai/` and did not declare a robots directive.
- The production sitemap did not contain Relay or the synthetic missing route.

The machine-readable site baseline is preserved in `baseline.csv` and `baseline-summary.json` in this directory.
