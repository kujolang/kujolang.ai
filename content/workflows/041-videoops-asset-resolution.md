---
title: "VideoOps Asset Resolution"
custom_url: "videoops-asset-resolution"
description: "Resolve every asset requirement with rights-aware status and provenance."
featured_image: "/assets/images/ecosystem/workflows-evidence-routing-bench.webp"
social_image: "/assets/images/social/videoops-asset-resolution.jpg"
section: "production capable with limitations"
order: "410"
install_command: "git clone --branch v0.6.0 --depth 1 https://github.com/kujolang/kujo-workflows.git && cd kujo-workflows && videoops-asset-resolution/bin/run"
github_url: "https://github.com/kujolang/kujo-workflows/tree/v0.6.0/videoops-asset-resolution"
launch_story: "A local-first workflow kit with explicit inputs, outputs, evidence, recovery, and approval boundaries."
scope_note: "Current readiness: production capable with limitations. Review the workflow README before live-provider or host-affecting use."
version: "0.6.0"
last_updated: "2026-09-06"
keywords: "VideoOps Asset Resolution, Kujo workflow, videoops-asset-resolution, local-first agent workflow"
seo_title: "VideoOps Asset Resolution — Kujo Workflow"
seo_description: "Resolve every asset requirement with rights-aware status and provenance."
---

## Outcome

Resolve every asset requirement with rights-aware status and provenance.

## Inputs

- validated VideoOps workspace
- explicit fixture mode
- explicit run id

## Evidence and outputs

- asset manifest
- license record
- source log
- handoff

The workflow's evidence contract is: VideoOps stage receipt, handoff, deterministic gate evidence, and RunLedger fixture receipt.

## Approval boundaries

- Live providers, paid generation, accounts, cloud rendering, and publication require separate operator approval.

## State and recovery

Stage receipts and explicit artifact handoffs support bounded restart; the fixture driver is not a production master orchestrator.

## Release boundary

Readiness is **production capable with limitations** in the 0.6.0 local technical preview. Hosted runners, broad live-provider coverage, and enterprise readiness are not implied.

## Source

- [Open the complete videoops-asset-resolution workflow kit on GitHub](https://github.com/kujolang/kujo-workflows/tree/v0.6.0/videoops-asset-resolution)
- [Browse the released workflow catalog](https://github.com/kujolang/kujo-workflows/blob/v0.6.0/docs/audit/workflow-catalog.json)
