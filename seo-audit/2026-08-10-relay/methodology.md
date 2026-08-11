# Methodology

This is a scoped additive audit for the Relay launch and custom nested 404 behavior. The existing comprehensive `seo-audit/2026-08-10/` baseline remains immutable.

1. Crawl the committed pre-change output and probe canonical production pages with `scripts/seo_audit.py`.
2. Record the live Relay and synthetic nested-missing-route HTTP status and metadata before changes.
3. Add Relay through the same collection source, canonical route, internal listing, social-card, structured-data, sitemap, and `llms.txt` pipeline as existing ecosystem projects.
4. Make the custom error document root-safe and non-indexable without changing the origin's real HTTP 404 status for missing routes.
5. Rebuild from source, rerun the audit and repository contracts, deploy, and verify the production route, sitemap, metadata, assets, and missing-route response.
