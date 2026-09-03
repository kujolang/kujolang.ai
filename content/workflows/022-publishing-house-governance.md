---
title: "Publishing House Governance"
custom_url: "publishing-house-governance"
description: "Set a bounded house mandate, portfolio decision, operating priorities, and accountable handoffs."
featured_image: "/assets/images/ecosystem/workflow-publishing-house-governance.webp"
social_image: "/assets/images/social/publishing-house-governance.jpg"
section: "production capable with limitations"
order: "220"
install_command: "git clone https://github.com/kujolang/kujo-workflows.git && cd kujo-workflows && publishing-house-governance/bin/run"
github_url: "https://github.com/kujolang/kujo-workflows/tree/main/publishing-house-governance"
launch_story: "A local-first workflow kit with explicit inputs, outputs, evidence, recovery, and approval boundaries."
scope_note: "Current readiness: production capable with limitations. Review the workflow README before live-provider or host-affecting use."
version: "0.4.0"
last_updated: "2026-09-02"
keywords: "Publishing House Governance, Kujo workflow, publishing-house-governance, local-first agent workflow"
seo_title: "Publishing House Governance — Kujo Workflow"
seo_description: "Set a bounded house mandate, portfolio decision, operating priorities, and accountable handoffs."
---

## Outcome

Set a bounded house mandate, portfolio decision, operating priorities, and accountable handoffs.

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

- Governance may commission, defer, revise, or decline work under PROPOSE; it cannot approve or publish artifacts.

## State and recovery

Kujo-owned state.json with bounded retries, idempotent completed replay, and Dispatch canonical artifacts; approval workflow adds exact paused resume.

## Release boundary

Readiness is **production capable with limitations** in the 0.4.0 local technical preview. Hosted runners, broad live-provider coverage, and enterprise readiness are not implied.

## Source

- [Open the complete publishing-house-governance workflow kit on GitHub](https://github.com/kujolang/kujo-workflows/tree/main/publishing-house-governance)
- [Browse the released workflow catalog](https://github.com/kujolang/kujo-workflows/blob/main/docs/audit/workflow-catalog.json)
