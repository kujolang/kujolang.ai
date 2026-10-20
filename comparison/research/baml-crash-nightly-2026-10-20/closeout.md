# Release verification

Evidence commit: `3b4080c`. Deployed comparison commit: `fa30c50ef4a5b6e0b41b27916f13cdbc0cfc702d`.

[Production build and deployment](https://github.com/kujolang/kujolang.ai/actions/runs/39430825911) succeeded. Live verification on 2026-10-20 checked all eight comparison pages and 48 URLs with zero errors or retries. Local checks passed: 26 Node tests, four Python tests, evidence checks, generated projections, comparison links, social cards, responsive images and the full site contract. See the adjacent JSON receipts for scope and counts.

The upstream BAML crash remains unresolved in the tested nightly. No external report was submitted. Blocked security analysis was omitted; no security-impact claim is made.
