---
title: "VideoOps Production"
custom_url: "videoops-production"
description: "Initialize a real arbitrary production and emit a harness-neutral invocation for the VideoOps Producer."
featured_image: "/assets/images/ecosystem/workflows-evidence-routing-bench.webp"
social_image: "/assets/images/social/videoops-production.jpg"
section: "production capable with limitations"
order: "390"
install_command: "git clone --branch v0.6.0 --depth 1 https://github.com/kujolang/kujo-workflows.git && cd kujo-workflows && videoops-production/bin/run"
github_url: "https://github.com/kujolang/kujo-workflows/tree/v0.6.0/videoops-production"
launch_story: "A local-first workflow kit with explicit inputs, outputs, evidence, recovery, and approval boundaries."
scope_note: "Current readiness: production capable with limitations. Review the workflow README before live-provider or host-affecting use."
version: "0.6.0"
last_updated: "2026-09-06"
keywords: "VideoOps Production, Kujo workflow, videoops-production, local-first agent workflow"
seo_title: "VideoOps Production — Kujo Workflow"
seo_description: "Initialize a real arbitrary production and emit a harness-neutral invocation for the VideoOps Producer."
---

## Outcome

Initialize a real arbitrary production and emit a harness-neutral invocation for the VideoOps Producer.

## Inputs

- arbitrary production request file
- absolute target workspace
- VideoOps agent package

## Evidence and outputs

- preserved intake request
- producer request receipt
- project state
- RUN_VIDEOOPS.md

The workflow's evidence contract is: Original request checksum, producer request, initialized project state, and portable harness invocation.

## Approval boundaries

- Paid generation, authenticated capture, publication, and other external effects require separate operator approval.

## State and recovery

The initializer preserves source intake and refuses accidental replacement; the selected harness owns agent execution and resumes from file handoffs.

## Release boundary

Readiness is **production capable with limitations** in the 0.6.0 local technical preview. Hosted runners, broad live-provider coverage, and enterprise readiness are not implied.

## Source

- [Open the complete videoops-production workflow kit on GitHub](https://github.com/kujolang/kujo-workflows/tree/v0.6.0/videoops-production)
- [Browse the released workflow catalog](https://github.com/kujolang/kujo-workflows/blob/v0.6.0/docs/audit/workflow-catalog.json)
