# Recommendations and measurement plan

Audit date: 2026-09-04

## Immediate after deployment

- Confirm GitHub Pages serves both responsive candidates with `200`, the expected WebP content type, and long-lived caching.
- Re-run the `/ecosystem/` mobile lab measurement against production after CDN propagation.

## 7-day checks

- Review field CWV and image transfer by viewport if first-party measurement becomes available.
- Check Search Console page indexing and enhancement reports; do not infer index changes from deployment alone.

## 28-, 60-, and 90-day comparisons

- Compare field LCP, image bytes, organic landings, and branded/non-branded queries against the dated baseline when those sources are connected.
- Repeat anonymous search and AI-answer observations under the same documented methodology; treat them as observations, not stable rankings.

## Editorial decisions

- Decide whether the Ability Gateway, Leash, and Ward repositories should be public or whether their public source/install calls to action should be revised.
