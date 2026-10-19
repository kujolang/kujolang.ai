# Measurement and SEO/GEO plan — 2026-10-19

## Observed baseline and authority

No analytics SDK or beacon was found in the reviewed shared layout, builder or site JavaScript. No new provider, cookies, tracking identifiers or paid services are introduced. Google Search Console, Bing Webmaster Tools, field Web Vitals, request logs, organic traffic and AI citation baselines are **NOT AVAILABLE — DATA ACCESS REQUIRED**.

Google's current AI-features guidance says normal SEO practices apply and that no special AI markup or machine-readable file is required for inclusion. Crawlable text, working internal links, metadata and visible-content-aligned structured data are supported practices. Markdown and llms.txt are convenience/discovery experiments, not guaranteed indexing or recommendation mechanisms. Sources reviewed: https://developers.google.com/search/docs/appearance/ai-features and https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a (Bing page had no substantive extract in this tool; no additional Bing-specific claim inferred).

## Events to configure when an existing approved collector is available

| Event | Trigger | Minimal fields |
|---|---|---|
| comparison_view | Page load under /compare/ | canonical path, page kind |
| documentation_click | Link to docs.kujolang.ai | source path, destination path |
| github_click | Source/repository CTA | source path, repository |
| install_open / install_copy | Existing quick-install actions | source path, action |
| related_content_click | Link to another guide/comparison | source path, target path |

Documented only; these events are not currently transmitted or claimed as measured. Use aggregate counts, omit query strings, user IDs, copied text and sensitive referrers. Respect the collector's consent and retention policy. Do not silently add a new analytics endpoint.

## Reporting after authorized publication

- Day 0: retain the launch commit and route inventory; confirm production HTTP/canonical/robots/sitemap and submit sitemap through the owner's existing search-console accounts.
- Day 7: check crawl/index coverage and broken destinations; do not treat early ranking movement as a content effect.
- Day 28: report impressions, clicks and landing-page engagement by route and intent. Compare an equivalent prior period with seasonality and launch-date caveats.
- Days 60 and 90: compare qualified documentation/GitHub/install engagement, query relevance and index coverage. Refresh facts only after reviewing new releases.
- Referrals: retain known search-engine hosts and identifiable assistant referrers as separate groups; unknown/direct traffic stays unknown/direct.
- AI visibility: use a fixed question set (what is Kujo; Kujo vs Bend; Kujo vs BAML; how to verify agent output; language for agent hosts). Record provider, date, exact prompt, observed answer and citation URL. A mention is not a citation; a citation is not proof of traffic or ranking impact. No such measurements were performed for this launch.

## Launch checklist

Implemented: static content; unique metadata; canonical routes; inherited robots policy; sitemap and llms indexing; visible breadcrumbs; appropriate WebPage/CollectionPage and breadcrumb schema; social cards; source links; responsive comparison tables; shared-source Markdown; editorial policy; source and content validation.

Verify locally using validation.md. Outstanding after source approval: owner-authorized merge/deployment, production checks, console data and an approved analytics integration if desired. These are publication/measurement prerequisites, not claims of improved rankings or citations.
