---
title: "Publishing House Evidence Dossier"
custom_url: "publishing-house-evidence-dossier"
description: "Create independently reviewed claim, source, evidence, rights, and packet records."
featured_image: "/assets/images/ecosystem/workflow-publishing-house-evidence-dossier.webp"
social_image: "/assets/images/social/publishing-house-evidence-dossier.jpg"
section: "production capable with limitations"
order: "200"
install_command: "git clone https://github.com/kujolang/kujo-workflows.git && cd kujo-workflows && publishing-house-evidence-dossier/bin/run"
github_url: "https://github.com/kujolang/kujo-workflows/tree/main/publishing-house-evidence-dossier"
launch_story: "A local-first workflow kit with explicit inputs, outputs, evidence, recovery, and approval boundaries."
scope_note: "Current readiness: production capable with limitations. Review the workflow README before live-provider or host-affecting use."
version: "0.4.0"
last_updated: "2026-09-02"
keywords: "Publishing House Evidence Dossier, Kujo workflow, publishing-house-evidence-dossier, local-first agent workflow"
seo_title: "Publishing House Evidence Dossier — Kujo Workflow"
seo_description: "Create independently reviewed claim, source, evidence, rights, and packet records."
---

## Outcome

Create independently reviewed claim, source, evidence, rights, and packet records.

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

Readiness is **production capable with limitations** in the 0.4.0 local technical preview. Hosted runners, broad live-provider coverage, and enterprise readiness are not implied.

## Source

- [Open the complete publishing-house-evidence-dossier workflow kit on GitHub](https://github.com/kujolang/kujo-workflows/tree/main/publishing-house-evidence-dossier)
- [Browse the released workflow catalog](https://github.com/kujolang/kujo-workflows/blob/main/docs/audit/workflow-catalog.json)
