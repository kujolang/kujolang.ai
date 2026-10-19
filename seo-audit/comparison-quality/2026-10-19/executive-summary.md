# Comparison SEO and Howl audit

Audit date: 2026-10-19. Status: PASS WITH RECOMMENDATIONS.

All eight comparison pages passed the scoped technical crawl: one H1 each, unique metadata, matching canonicals, sitemap inclusion, no orphan pages, no broken internal links, and valid JSON-LD. The complete 255-page graph supplies context. Every comparison is within two clicks of the homepage. Eight live routes and 28 unique cited destinations returned 200. No P0/P1 issue was found.

The audit corrected truncated text on social cards, the hub's generic search title and two audit-tooling errors. All eight 1200×630 Howl cards now show full titles and descriptions in Departure Mono. Desktop and 375px mobile checks passed with no page overflow. The full page copy, sources and review dates are unchanged.

| Page | Visible words (heuristic) | Click depth | Technical result |
|---|---:|---:|---|
| /compare/ai-code-verification-tools/ | 1732 | 2 | Pass |
| /compare/ai-native-programming-languages/ | 1818 | 2 | Pass |
| /compare/ | 2477 | 1 | Pass |
| /compare/kujo-vs-baml/ | 1641 | 2 | Pass |
| /compare/kujo-vs-bend/ | 1630 | 2 | Pass |
| /compare/kujo-vs-zero/ | 1591 | 2 | Pass |
| /compare/programming-languages-for-ai-agents/ | 1736 | 2 | Pass |
| /compare/verify-agent-workflows/ | 1899 | 2 | Pass |

Evidence: baseline/after CSVs and summaries; metadata, links, schema, media, performance and crawler datasets; howl-verification.json; browser/mobile receipts; baseline-provenance.json; deployment-verification.json when finalized. Checks include 22 Node tests, four robots regression tests, comparison generation validation, full-site HTML/site contracts, Howl rendering and direct production requests. P0/P1 before→after: 0/0→0/0. Numeric SEO/AI scores are not assigned.

The baseline is the verified immutable Pages artifact from source 8551554 plus a fresh focused pinned build and live receipts. The after graph combines the unchanged full-site context with fresh focused output; the production CI run validates the complete final site independently. See methodology.md for this distinction.

Rankings, indexing outcomes, traffic, conversions, AI citations and field/lab performance: NOT AVAILABLE — DATA ACCESS REQUIRED. The report makes no visibility-lift claims. The 7/28/60/90-day plan defines how to measure outcomes once platform data is available.

Use comparison/fact-review-prompt.md for the requested independent deep factual/version review. It requires a claim ledger, release matrix, source/implementation evidence, reproducible examples, fair competitor treatment and explicit unresolved claims.

Deployment verified: [run 39328814874](https://github.com/kujolang/kujolang.ai/actions/runs/39328814874), source 3fea59754be8520804d03ae5efd67a0234b78412. Full build and deploy passed. Post-deployment verification checked 48 unique URLs, all eight social-image hashes and all 28 cited destinations without failures. Additional commits contain audit tooling and documentation only; they do not change the deployed website.
