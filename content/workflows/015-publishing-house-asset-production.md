---
title: "Publishing House Asset Production"
custom_url: "publishing-house-asset-production"
description: "Plan and package supported accessible media assets with provenance."
featured_image: "/assets/images/ecosystem/workflow-publishing-house-asset-production.webp"
social_image: "/assets/images/social/publishing-house-asset-production.jpg"
section: "production capable with limitations"
order: "150"
install_command: "git clone https://github.com/kujolang/kujo-workflows.git && cd kujo-workflows && publishing-house-asset-production/bin/run"
github_url: "https://github.com/kujolang/kujo-workflows/tree/main/publishing-house-asset-production"
launch_story: "A local-first workflow kit with explicit inputs, outputs, evidence, recovery, and approval boundaries."
scope_note: "Current readiness: production capable with limitations. Review the workflow README before live-provider or host-affecting use."
version: "0.3.0"
last_updated: "2026-08-22"
keywords: "Publishing House Asset Production, Kujo workflow, publishing-house-asset-production, local-first agent workflow"
seo_title: "Publishing House Asset Production — Kujo Workflow"
seo_description: "Plan and package supported accessible media assets with provenance."
---

## Outcome

Plan and package supported accessible media assets with provenance.

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

- PROPOSE cannot manufacture evidence, review, approval, or publication authority

## State and recovery

Kujo-owned state.json with bounded retries, idempotent completed replay, and Dispatch canonical artifacts; approval workflow adds exact paused resume.

## Release boundary

Readiness is **production capable with limitations** in the 0.3.0 local technical preview. Hosted runners, broad live-provider coverage, and enterprise readiness are not implied.

## Source

- [Open the complete publishing-house-asset-production workflow kit on GitHub](https://github.com/kujolang/kujo-workflows/tree/main/publishing-house-asset-production)
- [Browse the released workflow catalog](https://github.com/kujolang/kujo-workflows/blob/main/docs/audit/workflow-catalog.json)
