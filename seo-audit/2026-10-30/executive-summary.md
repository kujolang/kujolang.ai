# Kujo SEO and AI-search audit

**PASS WITH RECOMMENDATIONS — 30 October 2026.** Technical discovery is healthy. The audit found two concrete page defects and one content gap, with no observed P0 or P1 problem. This was a report-only audit: **323 pages audited; zero website pages changed or deployed**.

## What passed

- **323/323 canonical pages returned HTTP 200** and match the 323-entry sitemap. All live canonicals matched their URLs.
- No missing or duplicate titles/descriptions, missing canonicals, broken internal links, orphan pages, or pages more than three clicks from the homepage in the generated link graph.
- Structured data parses on every page. All 63 examples retain source-backed content; parsing does not establish rich-result eligibility.
- **1,206 image occurrences** have alt attributes and intrinsic dimensions; no missing responsive candidates were found. Decorative empty alt is not treated as an error.
- Googlebot, Bingbot, OAI-SearchBot, ChatGPT-User, Claude-SearchBot, Claude-User, PerplexityBot and Perplexity-User passed all sampled robots/home/key-page/sitemap requests. These are synthetic agent tests, not verified provider-IP logs.
- All 13 host/path/feed/error probes behaved as expected. HTTPwww uses two permanent hops; this is optional polish.

## Prioritized findings

| Priority | Finding | Recommended next action |
|---|---|---|
| P2 | [Muzzle](https://kujolang.ai/ecosystem/muzzle/) renders a shell comment as an H1 inside its code block, creating two H1s and altering the displayed command. | Repair fenced-code rendering and add a regression check. Evidence: [code-heading-findings.json](code-heading-findings.json). |
| P2 | [Dispatch](https://kujolang.ai/ecosystem/dispatch/) links to a missing v1.4.0 release/upgrade evidence file. Both GitHub HTML and raw endpoints return 404; the tag's directory listing lacks the file. | Locate the correct version-specific evidence before replacing the link. |
| P2 | [Writing](https://kujolang.ai/writing/) remains a coming-soon page linked in primary navigation. | Publish substantive material or choose a suitable navigation/indexing treatment. This is a usefulness gap, not a proven search penalty. |
| P3 | Actual search and AI citation outcomes are unmeasured. | Obtain owner exports and run the fixed benchmark plan. |

Of **468 unique external destinations**, **466 returned200**, **one returned 404**, and **one npm page returned403**. The npm version exists in the registry (HTTP 200), so the website 403 is an access limitation, not a confirmed broken package. See [external-links.csv](external-links.csv).

## Production performance

Four Lighthouse 13.0.1 mobile simulated runs scored **98–100 performance**, **100 accessibility**, **100 best practices**, and **92 SEO**. The SEO deduction in all four reports is the same unknown `Content-Signal` directive inserted by Cloudflare. Sampled search crawlers are allowed; the warning does not demonstrate an indexing failure. Preserve the existing training policy.

| Template | Lab LCP | Lab CLS | Document response time |
|---|---:|---:|---:|
| application | 1.8 s | 0.00000 | 172 ms |
| ecosystem | 1.18 s | 0.00000 | 224 ms |
| examples | 1.8 s | 0.00021 | 183 ms |
| home | 2.11 s | 0.00049 | 263 ms |

These are one-run lab observations, not field Core Web Vitals, INP, or a speed guarantee. Minor cache/image/legacy-JS opportunities are optional experiments given the measured performance. Raw receipts are preserved in [audit-receipts.tar.gz](audit-receipts.tar.gz).

## AI-search readiness and content

The strongest citation candidates are the 63 executable/source-linked examples, dated comparisons, explicit failure boundaries, and reproducible performance receipt. The site explains what checks prove and what they do not. Keep these distinctions when adding content. The documentation site is a complementary reference surface; cannibalization is not established without query data.

Comparable BAML, DSPy and PDL documentation emphasizes examples, task-based tutorials, references and debugging/evaluation paths. Kujo's application downloads are useful original evidence. A next editorial investment should be a measured field report showing a real problem, inputs, failures, results and limitations—not additional generic keyword pages. See [research sources](research-sources.md).

`llms.txt` is available but remains an experimental convenience. Search eligibility, crawler access and valid markup do not prove that an AI system cites the site. Google documents that no special AI markup is required for its search features.

## Visibility and limitations

Search Console/Bing indexing, impressions, clicks, CTR, positions, organic conversions, verified bot logs, backlinks, field CWV/INP, and controlled AI-answer citations: **NOT AVAILABLE — DATA ACCESS REQUIRED**. Public tool searches returned related Kujo docs and creator pages, but do not establish main-site index coverage or rankings. No ranking, traffic or AI-citation improvement is claimed.

Internal SEO/AI-readiness scores: **not assigned**, before or after; a composite would obscure unavailable outcome evidence. P0/P1 counts remain **0/0 before and after**. Site inputs and output are unchanged; findings remain open. Report source commit: `ffad82c72423131674733c3f6a02620b08d2d28a`.

## Next measurements

Use the same URL inventory and benchmark questions on **6 November (7 days), 27 November (28 days), 29 December (60 days), and 28 January 2027 (90 days)**. Compare like-for-like country/device filters and date windows. See [recommendations](recommendations.md), [issues](issues.csv), [data availability](data-availability.md), and [methodology](methodology.md).
