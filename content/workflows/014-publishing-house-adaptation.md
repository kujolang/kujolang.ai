---
title: "Publishing House Adaptation"
custom_url: "publishing-house-adaptation"
description: "Create a versioned cross-format adaptation plan without expanding approved claim boundaries."
featured_image: "/assets/images/ecosystem/workflow-publishing-house-adaptation.webp"
social_image: "/assets/images/social/publishing-house-adaptation.jpg"
section: "production capable with limitations"
order: "140"
install_command: "git clone https://github.com/kujolang/kujo-workflows.git && cd kujo-workflows && publishing-house-adaptation/bin/run"
github_url: "https://github.com/kujolang/kujo-workflows/tree/main/publishing-house-adaptation"
launch_story: "A local-first workflow kit with explicit inputs, outputs, evidence, recovery, and approval boundaries."
scope_note: "Current readiness: production capable with limitations. Review the workflow README before live-provider or host-affecting use."
version: "0.4.0"
last_updated: "2026-09-02"
keywords: "Publishing House Adaptation, Kujo workflow, publishing-house-adaptation, local-first agent workflow"
seo_title: "Publishing House Adaptation — Kujo Workflow"
seo_description: "Create a versioned cross-format adaptation plan without expanding approved claim boundaries."
---

## Outcome

Create a versioned cross-format adaptation plan without expanding approved claim boundaries.

## Inputs

- publishing-house.workflow-run-request/v1
- portable House, Brand, and Audience profiles
- declared local capabilities

## Evidence and outputs

- capability-receipt.json
- agent-contracts/*.md
- agent-receipts/*.json
- Dispatch state/trace/report artifacts
- run-summary.json
- completion-receipt.json or blocker.json

The workflow's evidence contract is: deterministic offline fixture records and docs/evidence/publishing-house-fixture-proof.json.

## Approval boundaries

- Adaptation remains PROPOSE-only; new or strengthened claims return to Dossier and every derivative retains source lineage.

## State and recovery

Kujo-owned state.json with bounded retries, idempotent completed replay, and Dispatch canonical artifacts; approval workflow adds exact paused resume.

## Release boundary

Readiness is **production capable with limitations** in the 0.4.0 local technical preview. Hosted runners, broad live-provider coverage, and enterprise readiness are not implied.

## Source

- [Open the complete publishing-house-adaptation workflow kit on GitHub](https://github.com/kujolang/kujo-workflows/tree/main/publishing-house-adaptation)
- [Browse the released workflow catalog](https://github.com/kujolang/kujo-workflows/blob/main/docs/audit/workflow-catalog.json)
