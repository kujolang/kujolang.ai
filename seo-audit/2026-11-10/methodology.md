# Scoped Kujo Hermes launch audit — November 10, 2026

Scope: new tool pages, relevant internal discovery links, social previews, read-only MCP discovery and Kennel suitability. This is not a repeat full-site content strategy audit. Existing full-site audits remain immutable. Current repositories were fast-forwarded before source-baseline.json was sealed. Generated baseline HTML is archived per site. Local builds used the available Kujo 1.9.0 source-built runtime; deployment CI pins official 1.9.0. An initial shell-default 1.5.0 build was stopped and not used as evidence.

The baseline marketing crawl precedes its responsive-image generation step: missing variants there are incomplete pipeline artifacts, not new production defects or claimed SEO gains. Source snapshots, live HTTP receipts and generated HTML are separate evidence. The after crawl includes the completed build pipeline.

Review: titles, descriptions, H1, canonicals, crawlable incoming links, sitemap, JSON-LD parsing, image dimensions, source-grounded installation and limitations. No changes to crawler training policy, DNS, redirects or structured product claims. MCP is a protocol catalog, not an HTML landing page; it inherits reviewed metadata from the marketing source. Kennel does not distribute this Python host plugin.

No traffic, ranking, citation or Core Web Vitals improvement is claimed. Follow comparable search-console, referral and citation measurements at 7, 28, 60 and 90 days. No speculative readiness score is assigned.

Final validation repeated with checksum-verified official Kujo 1.9.0. The development runtime passed site builds but failed native MCP tests due to missing interpreter features; passing official-runtime tests are the final evidence.

Reproduce scoped production checks with `python3 seo-audit/2026-11-10/verify-live.py`. Reproduce inventory with `python3 scripts/seo_audit.py --repo . --output output --audit-dir NEW_DIRECTORY --phase after --origin https://kujolang.ai`; preserve this baseline directory.
