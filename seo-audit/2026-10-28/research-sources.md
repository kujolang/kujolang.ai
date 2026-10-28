# Current primary guidance

Retrieved 2026-10-28. Exact URLs are evidence pointers; search snippets were not treated as stronger than opened documentation.

| Source | Conclusion | Classification |
|---|---|---|
| https://developers.google.com/search/docs/appearance/ai-features | Crawlable, indexable, useful content remains central; no special AI schema or text file is required. Inclusion is not guaranteed. | Official guidance |
| https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls | Consistent canonical signals help consolidate duplicate URLs. | Official recommendation |
| https://developers.google.com/search/docs/appearance/structured-data/sd-policies | Structured data must represent visible content; valid markup does not guarantee rich results. | Official requirement for rich-result eligibility |
| https://developers.openai.com/api/docs/bots | OAI-SearchBot is a search crawler; GPTBot is a training crawler. Their controls are independent. | Official crawler documentation |
| https://docs.perplexity.ai/docs/resources/perplexity-crawlers | Search crawler access and user-triggered fetching are distinct. Probe user agents are only synthetic access tests, not verified provider-IP crawl evidence. | Official documentation / test limitation |
| https://schema.org/SoftwareSourceCode | Appropriate vocabulary for visible code samples, language and repository links. It is not itself a Google rich-result promise. | Schema vocabulary |
| https://blogs.bing.com/search/2026/6/New-AI-Visibility-Insights-in-Bing-Webmaster-Tools-Intents-Topics-Citation-Share-Compare/ | First-party citation reporting supports time comparisons; citation share is observational, not traffic share or a quality score. No property measurements were available. | Official product documentation, opened 2026-10-28 |
| https://www.bing.com/webmasters/help/ai-performance-9f8e7d6c | First-party search result describes citation reporting; opened page requires JavaScript. Actual property data is unavailable. | Documented feature; account-data limitation |
| https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a | Opened help shell requires JavaScript; no detailed requirement inferred from the inaccessible body. | Retrieval limitation |

Existing llms.txt is treated as an experimental discovery aid, not a ranking requirement. Training-crawler policy is preserved.
