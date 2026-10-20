# Release verification — 2026-10-20

Evidence commit: `1ea8b96`. Deployed comparison commit: `75ccc21d4f062495439a5cab4f9701681c979654`.

Production build and deployment succeeded: https://github.com/kujolang/kujolang.ai/actions/runs/39444056732.

All eight live comparison pages and 48 URLs passed, with zero errors or retries. Checks included the new Zerolang table, citations, navigation label, metadata, and exact Markdown projection. Local verification passed 26 Node tests, four Python tests, evidence checks, 23 generated projections, 444 internal links, social/responsive-image contracts and 256 HTML documents. The local render covered the comparison pages over an existing full-site graph; production performed a fresh full build.

No new upstream defect was established, so no issue was filed. Remaining runtime scope is documented in README.md. SignalBox: no captures warranted.
