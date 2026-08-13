---
title: "Relay Lifecycle Handoff"
custom_url: "relay-lifecycle-handoff"
description: "Exercise Relay pause/resume, integrity-checked export, and a local persisted handoff receipt."
featured_image: "/assets/images/ecosystem/workflow-relay-lifecycle-handoff.webp"
social_image: "/assets/images/social/relay-lifecycle-handoff.jpg"
section: "production capable with limitations"
order: "130"
install_command: "git clone https://github.com/kujolang/kujo-workflows.git && cd kujo-workflows && relay-lifecycle-handoff/scripts/run.sh"
github_url: "https://github.com/kujolang/kujo-workflows/tree/main/relay-lifecycle-handoff"
launch_story: "A local-first workflow kit with explicit inputs, outputs, evidence, recovery, and approval boundaries."
scope_note: "Current readiness: production capable with limitations. Review the workflow README before live-provider or host-affecting use."
version: "0.2.0"
last_updated: "2026-08-12"
keywords: "Relay Lifecycle Handoff, Kujo workflow, relay-lifecycle-handoff, local-first agent workflow"
seo_title: "Relay Lifecycle Handoff — Kujo Workflow"
seo_description: "Exercise Relay pause/resume, integrity-checked export, and a local persisted handoff receipt."
---

## Outcome

Exercise Relay pause/resume, integrity-checked export, and a local persisted handoff receipt.

## Inputs

- clean Git fixture
- Relay worktree mission fixture
- KUJO_BIN

## Evidence and outputs

- paused.json
- resumed.json
- export.json
- message-envelope.json
- delivery-receipt.json
- cleanup.json

The workflow's evidence contract is: Relay pause/resume/export/cleanup output mapped to contracts/relay/*.v1.schema.json.

## Approval boundaries

- mission approval is fixture-scoped
- external delivery is not implied by local receipt

## State and recovery

Relay persists a paused run, resumes by run ID, verifies event/receipt integrity, and cleans the isolated worktree.

## Release boundary

Readiness is **production capable with limitations** in the 0.2.0 local technical preview. Hosted runners, broad live-provider coverage, and enterprise readiness are not implied.

## Source

- [Open the complete relay-lifecycle-handoff workflow kit on GitHub](https://github.com/kujolang/kujo-workflows/tree/main/relay-lifecycle-handoff)
- [Browse the released workflow catalog](https://github.com/kujolang/kujo-workflows/blob/main/docs/audit/workflow-catalog.json)
