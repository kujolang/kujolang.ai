# Verification closeout

Deployed commit: `1a27227dc0862fd148fa9991c48e6fd3827c0e88`. [Fresh full build and deployment](https://github.com/kujolang/kujolang.ai/actions/runs/39352818454) passed. Live verification at 2026-10-20T01:29:17.143162+00:00: 8 comparison pages, 48 URLs, zero errors; Markdown matches committed projections.

Local checks: 25 Node tests, 4 Python tests, 23 projection files, 436 internal links, 255 social routes and 256 HTML files. A focused local comparison build was overlaid onto the immutable full-site graph for graph checks; production CI independently performed the fresh full build. The new seven-row table was inspected at desktop width and a 375px mobile viewport: no page overflow, Departure Mono headings, scrollable table, 128px anchor offset under the fixed header.

The portable runner was executed separately. All 32 names, exits and stdout results matched the original probe receipts, including the arithmetic SIGSEGV. This corroborates recorded behavior; it does not resolve the upstream defect. Original sandboxed and unsandboxed controls remain intact.

The upstream crash is the sole new unresolved human-review finding. No external issue was filed. Cloud providers, other bridge/platform/release combinations, native root cause and exploitability were not established. No comparative performance claim was made.
