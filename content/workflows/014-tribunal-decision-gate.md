---
title: "Tribunal Decision Gate"
custom_url: "tribunal-decision-gate"
description: "Run an advisory Tribunal mock review and emit a verified, versioned decision receipt."
featured_image: "/assets/images/ecosystem/workflow-tribunal-decision-gate.webp"
social_image: "/assets/images/social/tribunal-decision-gate.jpg"
section: "production capable with limitations"
order: "140"
install_command: "git clone https://github.com/kujolang/kujo-workflows.git && cd kujo-workflows && tribunal-decision-gate/scripts/run.sh"
github_url: "https://github.com/kujolang/kujo-workflows/tree/main/tribunal-decision-gate"
launch_story: "A local-first workflow kit with explicit inputs, outputs, evidence, recovery, and approval boundaries."
scope_note: "Current readiness: production capable with limitations. Review the workflow README before live-provider or host-affecting use."
version: "0.2.0"
last_updated: "2026-08-11"
keywords: "Tribunal Decision Gate, Kujo workflow, tribunal-decision-gate, local-first agent workflow"
seo_title: "Tribunal Decision Gate — Kujo Workflow"
seo_description: "Run an advisory Tribunal mock review and emit a verified, versioned decision receipt."
---

## Outcome

Run an advisory Tribunal mock review and emit a verified, versioned decision receipt.

## Inputs

- Tribunal product-decision fixture
- KUJO_BIN

## Evidence and outputs

- review.txt
- verify.json
- export.json
- decision-receipt.json

The workflow's evidence contract is: verified Tribunal artifact export mapped to contracts/tribunal/decision-receipt.v1.schema.json.

## Approval boundaries

- mock receipt is advisory and unsigned; binding production approval requires trust-policy verification

## State and recovery

Tribunal persists a run; workflow is rerunnable by idempotency key but does not resume a stopped hearing.

## Release boundary

Readiness is **production capable with limitations** in the 0.2.0 local technical preview. Hosted runners, broad live-provider coverage, and enterprise readiness are not implied.

## Source

- [Open the complete tribunal-decision-gate workflow kit on GitHub](https://github.com/kujolang/kujo-workflows/tree/main/tribunal-decision-gate)
- [Browse the released workflow catalog](https://github.com/kujolang/kujo-workflows/blob/main/docs/audit/workflow-catalog.json)
