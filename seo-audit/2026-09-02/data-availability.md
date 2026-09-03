# Data availability

Audit date: 2026-09-02

| Source | Available | Scope / limitation |
| --- | --- | --- |
| Repository source and generated output | Yes | Source was audited at the recorded Git revision; a clean production build supplies the after crawl. |
| Production canonical crawl | Yes | All 192 sitemap canonicals were downloaded before edits under `raw/production-before/`. |
| Lens rendered-browser evidence | Yes | Mobile baseline and after evidence cover the changed Publishing House Operator route; screenshots supplement assertions. |
| robots.txt, sitemap, canonical HTML, schema, metadata, and links | Yes | Measured from production baseline and generated after output. |
| Howl manifest and generated social images | Yes | All declared cards, source routes, dimensions, and generated files are validated after the build. |
| DNS, TLS, HTTP variants, and crawler user agents | Yes | Public probes include desktop, mobile, Google, Bing, OpenAI, and common AI crawler identities. |
| Google Search Console and Bing Webmaster Tools | No | No authenticated console export was available; index coverage and query data are not inferred. |
| Analytics, conversion, RUM, and CDN telemetry | No | No authenticated measurement export was available; traffic and conversion impact are not claimed. |
| Backlink index and rank tracker | No | No paid third-party dataset was used. |
| Authenticated AI answer surfaces | No | AI citations and answer inclusion cannot be established by a technical crawl alone. |
