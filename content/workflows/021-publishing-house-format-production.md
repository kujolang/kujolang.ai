---
title: "Publishing House Format Production"
custom_url: "publishing-house-format-production"
description: "Produce reviewable newsletter, social, case-study, and video/audio packages from approved lineage."
featured_image: "/assets/images/ecosystem/workflow-publishing-house-format-production.webp"
social_image: "/assets/images/social/publishing-house-format-production.jpg"
section: "production capable with limitations"
order: "210"
install_command: "git clone https://github.com/kujolang/kujo-workflows.git && cd kujo-workflows && publishing-house-format-production/bin/run"
github_url: "https://github.com/kujolang/kujo-workflows/tree/main/publishing-house-format-production"
launch_story: "A local-first workflow kit with explicit inputs, outputs, evidence, recovery, and approval boundaries."
scope_note: "Current readiness: production capable with limitations. Review the workflow README before live-provider or host-affecting use."
version: "0.4.0"
last_updated: "2026-09-02"
keywords: "Publishing House Format Production, Kujo workflow, publishing-house-format-production, local-first agent workflow"
seo_title: "Publishing House Format Production — Kujo Workflow"
seo_description: "Produce reviewable newsletter, social, case-study, and video/audio packages from approved lineage."
---

## Outcome

Produce reviewable newsletter, social, case-study, and video/audio packages from approved lineage.

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

- Format production creates proposals and packages only; it cannot publish, infer consent, or expand claims beyond approved evidence.

## State and recovery

Kujo-owned state.json with bounded retries, idempotent completed replay, and Dispatch canonical artifacts; approval workflow adds exact paused resume.

## Release boundary

Readiness is **production capable with limitations** in the 0.4.0 local technical preview. Hosted runners, broad live-provider coverage, and enterprise readiness are not implied.

## Source

- [Open the complete publishing-house-format-production workflow kit on GitHub](https://github.com/kujolang/kujo-workflows/tree/main/publishing-house-format-production)
- [Browse the released workflow catalog](https://github.com/kujolang/kujo-workflows/blob/main/docs/audit/workflow-catalog.json)
