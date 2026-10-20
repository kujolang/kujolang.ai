# Bend review release verification — 2026-10-20

Evidence commit: `34259f2`. Deployed comparison commit: `4411f49fc374d046a53ba6067bc3b16697f30c6a`.

Production build and deployment succeeded: https://github.com/kujolang/kujolang.ai/actions/runs/39449575810.

All 8 live comparison pages and 48 URLs passed, including the new Bend boundary table and exact Markdown projections. Local checks passed 26 Node tests, four Python tests, evidence hashes, 23 generated projections, 445 internal links, 255 social cards, 553 responsive images and 256 HTML documents. The local render covered the comparison pages over an existing site graph; production performed a fresh full build.

Runtime evidence: 76 macOS and 83 Linux command observations plus 12 independent-kernel controls. The final commit also passed the Linux workflow at https://github.com/kujolang/kujolang.ai/actions/runs/39449435258. Counts include builds and controls. Scope and untested boundaries are recorded in README.md. No new upstream defect was established and no issue was posted. SignalBox: no captures warranted.
