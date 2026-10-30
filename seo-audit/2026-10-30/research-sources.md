# Primary guidance and observations — 2026-10-30

- [Google: AI features](https://developers.google.com/search/docs/appearance/ai-features) — official recommendation: ordinary crawlability, useful textual content, internal links and visible-content-aligned markup also apply to AI search. No special AI schema is required; eligibility does not guarantee inclusion.
- [Google: canonicals](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls) — official guidance: keep canonical signals consistent. We check markup, links and sitemap; only Search Console can establish Google's chosen canonical.
- [OpenAI crawler documentation](https://developers.openai.com/api/docs/bots) — official distinction: search indexing, user-triggered fetching and training have different agents. Synthetic user-agent probes do not establish verified provider-IP access or actual citations.
- [Bing Webmaster Guidelines](https://www.bing.com/webmasters/help/bing-webmaster-guidelines-30fba23a) — official recommendation: accessible, focused, accurate content supports grounding; SEO/GEO guarantees neither rankings nor citations.
- [Bing AI Performance](https://www.bing.com/webmasters/help/ai-performance-9f8e7d6c) — official measurement documentation: citation reporting is separate from traffic and rank. Owner exports are needed for a real visibility baseline.
- [Schema.org SoftwareSourceCode](https://schema.org/SoftwareSourceCode) — type definition for source code and repository references. Parsing/type use does not imply Google rich-result eligibility.
- [Cloudflare managed robots](https://developers.cloudflare.com/bots/additional-configurations/managed-robots-txt/) — official product documentation: managed robots directives may be added at the edge. The live Content-Signal extension is unknown to this Lighthouse version; the measured search profiles remain permitted and return200. Do not remove owner training policy to improve a tool score.

## Dated public search observations

Queries: `site:kujolang.ai Kujo programming language` and `"Kujo" "deterministic" programming language`. The tool's returned result set included docs.kujolang.ai/start-here/, docs.kujolang.ai/ and robertdevore.com/projects/kujo/. No controlled country/device ranking or index-coverage conclusion is possible from this small, provider-unspecified result set. The main site not appearing in the returned subset is not proof of deindexing.

## Comparable first-party content surfaces

- [BAML documentation](https://docs.boundaryml.com/home): direct links to guide, examples, reference and playground. Kujo already has the first three paths; an executable browser experience is an optional product experiment, not an SEO requirement.
- [DSPy documentation](https://dspy.ai/current/): task-oriented tutorials and explicit metrics/evaluation paths. Kujo's downloadable workflow applications are useful original evidence; connect future case studies to measured outcomes.
- [IBM PDL](https://ibm.github.io/prompt-declaration-language/): quick reference, tutorial and debugging guidance. Kujo's pinned examples and explicit runtime boundaries support a similar practical adoption path.

These are editorial comparisons, not observed rank competitors or proof of superior quality. No competitor performance/accuracy claims were imported. llms.txt remains an experimental convenience, not evidence of citations.
