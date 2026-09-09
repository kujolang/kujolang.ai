---
title: "VideoOps Quality Review"
custom_url: "videoops-quality-review"
description: "Run deterministic and independent structured review with bounded revision routing."
featured_image: "/assets/images/ecosystem/workflows-evidence-routing-bench.webp"
social_image: "/assets/images/social/videoops-quality-review.jpg"
section: "production capable with limitations"
order: "440"
install_command: "git clone --branch v0.6.0 --depth 1 https://github.com/kujolang/kujo-workflows.git && cd kujo-workflows && videoops-quality-review/bin/run"
github_url: "https://github.com/kujolang/kujo-workflows/tree/v0.6.0/videoops-quality-review"
launch_story: "A local-first workflow kit with explicit inputs, outputs, evidence, recovery, and approval boundaries."
scope_note: "Current readiness: production capable with limitations. Review the workflow README before live-provider or host-affecting use."
version: "0.6.0"
last_updated: "2026-09-06"
keywords: "VideoOps Quality Review, Kujo workflow, videoops-quality-review, local-first agent workflow"
seo_title: "VideoOps Quality Review — Kujo Workflow"
seo_description: "Run deterministic and independent structured review with bounded revision routing."
---

## Outcome

Run deterministic and independent structured review with bounded revision routing.

## Inputs

- validated VideoOps workspace
- explicit fixture mode
- explicit run id

## Evidence and outputs

- critique
- approval
- conditional fix list
- handoff

The workflow's evidence contract is: VideoOps stage receipt, handoff, deterministic gate evidence, and RunLedger fixture receipt.

## Approval boundaries

- Live providers, paid generation, accounts, cloud rendering, and publication require separate operator approval.

## State and recovery

Stage receipts and explicit artifact handoffs support bounded restart; the fixture driver is not a production master orchestrator.

## Release boundary

Readiness is **production capable with limitations** in the 0.6.0 local technical preview. Hosted runners, broad live-provider coverage, and enterprise readiness are not implied.

## Source

- [Open the complete videoops-quality-review workflow kit on GitHub](https://github.com/kujolang/kujo-workflows/tree/v0.6.0/videoops-quality-review)
- [Browse the released workflow catalog](https://github.com/kujolang/kujo-workflows/blob/v0.6.0/docs/audit/workflow-catalog.json)
