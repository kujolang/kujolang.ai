# Prompt: evidence-led review of Kujo comparison pages

Act as an independent technical researcher and skeptical editor. Audit every substantive page under https://kujolang.ai/compare/ against current primary evidence as of the day you run this review. Your goal is a fair, reproducible comparison that a maintainer of any covered project would consider accurate. Do not assume Kujo wins.

Scope:
- /compare/
- /compare/kujo-vs-bend/
- /compare/kujo-vs-baml/
- /compare/kujo-vs-zero/
- /compare/ai-native-programming-languages/
- /compare/programming-languages-for-ai-agents/
- /compare/ai-code-verification-tools/
- /compare/verify-agent-workflows/
- Their Markdown alternatives, FAQs, tables, examples, source lists, metadata, JSON-LD and Howl social cards.
Discover any additional populated comparison pages in the repository and include them. Exclude empty planned routes.

Work in the kujolang/kujolang.ai repository. Read applicable AGENTS.md, comparison/README.md, comparison/catalog.json, the editorial policy, existing research and the latest seo-audit/comparison-quality artifacts before editing. Preserve unrelated work. The catalog is the factual source of truth; use its generators instead of hand-editing generated projections. Read and apply the Orwell writing skill for prose, audit-seo-ai-search for discovery/technical checks, and kujo-howl-workflows for affected social cards. Do not use these skills as substitutes for factual research.

1. Establish identities and current versions
Browse official project websites, repositories, release feeds, package registries linked by those projects, changelogs and versioned documentation. Verify canonical ownership and project identity first, especially Bend and Vercel Zerolang at zerolang.ai. Do not conflate historical Bend/HVM with the current Bend project, or conflate Vercel Zerolang with another project named Zero.
For Kujo, Bend, BAML, Zero, and any other language or tool making substantive appearances, record: official site/repository, latest stable release and release date, latest preview/nightly separately, reviewed commit/tag, documentation version, installed/tested version, retrieval timestamp and source URLs. A nightly is not the latest stable release. A moving branch is not a release. Unknown versions remain unknown. Never trust this prompt's or the site's previous version numbers without checking again.

2. Build a claim ledger
Extract every material factual claim, including table cells, limitations, negative claims, recommendations based on capabilities, FAQs and code comments. Record exact quote, page/section, source field, claim type, product/version, primary evidence URL with commit/line or section where practical, evidence date, verdict, confidence, reproduction result and proposed correction.
Use verdicts: verified; partly supported; outdated; contradicted; not verified; not applicable. Absence of documentation does not establish lack of support. Distinguish product assertions, source inspection and independently executed evidence. Resolve conflicts explicitly rather than choosing the source that favors Kujo.

3. Investigate technical depth
Review design goals, target users, syntax and programming model, type system, compilation/runtime architecture, concurrency/parallelism, memory/resource semantics, effects and I/O, formal proof/checking boundaries, testing, LLM/agent integration, host bridges, packages, deployment, observability, reproducibility, sandbox/security boundaries, maturity and limitations. Separate core-language capabilities from first-party tools, third-party integrations and roadmap items. Check actual implementations and tests behind high-impact claims. For each language explain appropriate use cases, where a competitor is stronger, and when tools can coexist.
Do not equate passing tests, schema validation or a workflow receipt with a formal proof. State precisely what a proof/check establishes and what lies outside its trusted boundary. Do not imply deterministic model outputs, sandboxing or performance advantages without evidence.

4. Reproduce examples safely
Use pinned releases in isolated temporary directories; do not modify unrelated repositories. Record commands, OS/architecture, dependencies, hashes, outputs, exit statuses and limitations. Run positive and meaningful negative cases. For Kujo's published producer/checker example, verify exact integer handling and rejection of incorrect integers, strings, booleans, floating-point values, missing data and malformed input. For competitor examples, distinguish inspected from executed. No fabricated benchmarks: if performance is claimed, require a comparable reproducible methodology, raw results and explicit limits. Do not run untrusted code with secrets or broad permissions.

5. Review fairness and usefulness
Read each page as a developer choosing tools. Check whether the answer, grids, tables, examples and recommendations agree; whether material caveats are adjacent to claims; whether descriptions are specific and readable; and whether category pages serve distinct intents. Preserve useful technical depth while replacing slogans and fragments with clear explanations. Retain Departure Mono for prominent headings and keep Compare out of the header unless separately authorized. Do not add filler, automatic winner badges, guessed support statuses, invented expertise or keyword stuffing.

6. Produce evidence, then correct supported errors
Save a dated research report, claim ledger, release/version matrix, reproducibility receipts and severity-ranked correction list. Include a per-page verdict with exact unresolved claims and what evidence would settle them. Implement narrow, evidence-supported factual corrections in the catalog and related source files; do not silently change positioning or manufacture missing evidence. Explicitly disclose unresolved uncertainty. Update review dates only for claims actually reviewed, and preserve publication history.
Regenerate HTML/Markdown projections and affected Howl assets. Run the repository's generation checks, tests, full pinned build, comparison validation, metadata/canonical/sitemap/schema/link checks, mobile layout checks and card inspections. Verify source-to-rendered parity. Commit supported fixes in meaningful commits and push according to repository instructions; do not deploy unless the session explicitly authorizes deployment. If deployed, independently verify all live pages and assets.

Deliver:
- Concise overall verdict and per-page status.
- Claim ledger and version matrix with primary citations and retrieval dates.
- Corrected claims with before/after wording and evidence.
- Reproduction receipts, test outcomes and precise limitations.
- Unresolved questions ranked by user impact, with the next evidence needed.
- Maintenance plan: release-watch sources, claims likely to drift, review triggers and a repeatable re-audit checklist. Do not create recurring jobs without authorization.

Never claim rankings, traffic, indexing, AI citations or measured performance improved without actual data. Treat crawler access as access, not proof of indexing or citation. End with verified changes and remaining blockers, not a generic assurance that everything is current.
