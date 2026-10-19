# Comparison decision guides

All four non-direct comparison pages now share the hub's SiteKit visual system while retaining distinct subject matter:

- AI-native languages: three meanings of the label, six candidate approaches, adoption trials and claim-to-evidence examples.
- Languages for agents: host/tool/target boundaries, six integration requirements, failure/recovery probes and an illustrative duplicate-effect scenario.
- Verification tools: six assurance layers, their limits, adversarial controls and the JSON artifact truth table.
- Workflow verification: an auditable acceptance contract, four practical steps, downloadable producer/verifier, command panel and receipt-field interpretation.

Catalog `guide` data owns all added content. Source-backed tool scopes carry references; proposed trials and illustrative outcomes are labeled rather than represented as measured results. Existing full notes, FAQs, review dates and source identities remain available. No comparative runtime benchmark or agent success rate was added.

`render-comparison-guide.mjs` generates HTML and Markdown, and validates required evidence and table shapes. Generated frontmatter selects `post-comparison-guide.html` through the existing SSG mechanism. This replaces the old prose layout for the four remaining routes without adding client JavaScript. SiteKit cards, semantic tables, native disclosures and the hub's responsive grid vocabulary provide the structure.

Checks: 22 Node tests; generated-output parity; two tables and nine section anchors per guide; focused SSG route/metadata/link checks and HTML validation; desktop/mobile browser review, including keyboard table/disclosure behavior; full site deployment CI and live route checks. Focused builds resolve unchanged link destinations against the previous full build; deployment CI validates a fresh complete build.
