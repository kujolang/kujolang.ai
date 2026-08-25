---
title: "Publishing House Approval Publication"
custom_url: "publishing-house-approval-publication"
description: "Pause for checksum-bound VersionSeal approval and perform only bounded PressWire effects."
featured_image: "/assets/images/ecosystem/workflow-publishing-house-approval-publication.webp"
social_image: "/assets/images/social/publishing-house-approval-publication.jpg"
section: "production capable with limitations"
order: "140"
install_command: "git clone https://github.com/kujolang/kujo-workflows.git && cd kujo-workflows && publishing-house-approval-publication/bin/run"
github_url: "https://github.com/kujolang/kujo-workflows/tree/main/publishing-house-approval-publication"
launch_story: "A local-first workflow kit with explicit inputs, outputs, evidence, recovery, and approval boundaries."
scope_note: "Current readiness: production capable with limitations. Review the workflow README before live-provider or host-affecting use."
version: "0.3.0"
last_updated: "2026-08-22"
keywords: "Publishing House Approval Publication, Kujo workflow, publishing-house-approval-publication, local-first agent workflow"
seo_title: "Publishing House Approval Publication — Kujo Workflow"
seo_description: "Pause for checksum-bound VersionSeal approval and perform only bounded PressWire effects."
---

## Outcome

Pause for checksum-bound VersionSeal approval and perform only bounded PressWire effects.

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

- VersionSeal exact checksum approval is required before an ACT-scoped PressWire operation; fixture approval is labeled and local only

## State and recovery

Kujo-owned state.json with bounded retries, idempotent completed replay, and Dispatch canonical artifacts; approval workflow adds exact paused resume.

## Release boundary

Readiness is **production capable with limitations** in the 0.3.0 local technical preview. Hosted runners, broad live-provider coverage, and enterprise readiness are not implied.

## Source

- [Open the complete publishing-house-approval-publication workflow kit on GitHub](https://github.com/kujolang/kujo-workflows/tree/main/publishing-house-approval-publication)
- [Browse the released workflow catalog](https://github.com/kujolang/kujo-workflows/blob/main/docs/audit/workflow-catalog.json)
