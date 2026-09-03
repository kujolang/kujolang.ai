---
title: "Agency Verified Fix Loop"
custom_url: "agency-verified-fix-loop"
description: "Demonstrate a deterministic browser-visible fix with staged evidence and handoff."
featured_image: "/assets/images/ecosystem/workflow-agency-verified-fix-loop.webp"
social_image: "/assets/images/social/agency-verified-fix-loop.jpg"
section: "production capable with limitations"
order: "30"
install_command: "git clone https://github.com/kujolang/kujo-workflows.git && cd kujo-workflows && agency-verified-fix-loop/scripts/run-loop.sh"
github_url: "https://github.com/kujolang/kujo-workflows/tree/main/agency-verified-fix-loop"
launch_story: "A local-first workflow kit with explicit inputs, outputs, evidence, recovery, and approval boundaries."
scope_note: "Current readiness: production capable with limitations. Review the workflow README before live-provider or host-affecting use."
version: "0.4.0"
last_updated: "2026-09-02"
keywords: "Agency Verified Fix Loop, Kujo workflow, agency-verified-fix-loop, local-first agent workflow"
seo_title: "Agency Verified Fix Loop — Kujo Workflow"
seo_description: "Demonstrate a deterministic browser-visible fix with staged evidence and handoff."
---

## Outcome

Demonstrate a deterministic browser-visible fix with staged evidence and handoff.

## Inputs

- fixture repository
- optional PORT, STRICT, KEEP_WORK

## Evidence and outputs

- .runs/<timestamp>/summary.md
- Lens walkthrough
- handoff
- tool briefs

The workflow's evidence contract is: stage table, logs, proof artifacts, receipts.

## Approval boundaries

- live provider PackWrite
- non-fixture site access

## State and recovery

timestamped run and disposable work tree; cleanup trap

## Release boundary

Readiness is **production capable with limitations** in the 0.4.0 local technical preview. Hosted runners, broad live-provider coverage, and enterprise readiness are not implied.

## Source

- [Open the complete agency-verified-fix-loop workflow kit on GitHub](https://github.com/kujolang/kujo-workflows/tree/main/agency-verified-fix-loop)
- [Browse the released workflow catalog](https://github.com/kujolang/kujo-workflows/blob/main/docs/audit/workflow-catalog.json)
