---
title: "Workcell Execution Gate"
custom_url: "workcell-execution-gate"
description: "Validate, inspect, and attempt bounded Workcell Docker execution with explicit completion evidence."
featured_image: "/assets/images/ecosystem/workflow-workcell-execution-gate.webp"
social_image: "/assets/images/social/workcell-execution-gate.jpg"
section: "production capable with limitations"
order: "260"
install_command: "git clone https://github.com/kujolang/kujo-workflows.git && cd kujo-workflows && workcell-execution-gate/scripts/run.sh"
github_url: "https://github.com/kujolang/kujo-workflows/tree/main/workcell-execution-gate"
launch_story: "A local-first workflow kit with explicit inputs, outputs, evidence, recovery, and approval boundaries."
scope_note: "Current readiness: production capable with limitations. Review the workflow README before live-provider or host-affecting use."
version: "0.2.0"
last_updated: "2026-08-12"
keywords: "Workcell Execution Gate, Kujo workflow, workcell-execution-gate, local-first agent workflow"
seo_title: "Workcell Execution Gate — Kujo Workflow"
seo_description: "Validate, inspect, and attempt bounded Workcell Docker execution with explicit completion evidence."
---

## Outcome

Validate, inspect, and attempt bounded Workcell Docker execution with explicit completion evidence.

## Inputs

- clean Git fixture
- Workcell hello definition
- KUJO_BIN

## Evidence and outputs

- validate.json
- inspect.json
- run-result.json
- work-package.json
- completion-receipt.json

The workflow's evidence contract is: Workcell validate/inspect/run output mapped to contracts/workcell/*.v1.schema.json.

## Approval boundaries

- Docker daemon and image are trusted local infrastructure; network is none; declared artifacts only

## State and recovery

Workcell owns bounded lifecycle, cleanup, and receipt; this workflow does not claim reassignment or multi-worker scheduling.

## Release boundary

Readiness is **production capable with limitations** in the 0.2.0 local technical preview. Hosted runners, broad live-provider coverage, and enterprise readiness are not implied.

## Source

- [Open the complete workcell-execution-gate workflow kit on GitHub](https://github.com/kujolang/kujo-workflows/tree/main/workcell-execution-gate)
- [Browse the released workflow catalog](https://github.com/kujolang/kujo-workflows/blob/main/docs/audit/workflow-catalog.json)
