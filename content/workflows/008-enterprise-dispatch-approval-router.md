---
title: "Enterprise Dispatch Approval Router"
custom_url: "enterprise-dispatch-approval-router"
description: "Run a resumable Dispatch workflow with an explicit approval boundary and diagnostics."
featured_image: "/assets/images/ecosystem/workflow-enterprise-dispatch-approval-router.webp"
social_image: "/assets/images/social/enterprise-dispatch-approval-router.jpg"
section: "production capable with limitations"
order: "80"
install_command: "git clone https://github.com/kujolang/kujo-workflows.git && cd kujo-workflows && enterprise-dispatch-approval-router/scripts/run-workflow.sh"
github_url: "https://github.com/kujolang/kujo-workflows/tree/main/enterprise-dispatch-approval-router"
launch_story: "A local-first workflow kit with explicit inputs, outputs, evidence, recovery, and approval boundaries."
scope_note: "Current readiness: production capable with limitations. Review the workflow README before live-provider or host-affecting use."
version: "0.3.0"
last_updated: "2026-08-22"
keywords: "Enterprise Dispatch Approval Router, Kujo workflow, enterprise-dispatch-approval-router, local-first agent workflow"
seo_title: "Enterprise Dispatch Approval Router — Kujo Workflow"
seo_description: "Run a resumable Dispatch workflow with an explicit approval boundary and diagnostics."
---

## Outcome

Run a resumable Dispatch workflow with an explicit approval boundary and diagnostics.

## Inputs

- offline fixture
- optional Leash callback URL

## Evidence and outputs

- state.json
- trace.md
- report.md
- diagnostics

The workflow's evidence contract is: Dispatch run artifacts and inspection JSON.

## Approval boundaries

- human intervention event and resume decision

## State and recovery

Dispatch persisted state; paused run resumes by run ID

## Release boundary

Readiness is **production capable with limitations** in the 0.3.0 local technical preview. Hosted runners, broad live-provider coverage, and enterprise readiness are not implied.

## Source

- [Open the complete enterprise-dispatch-approval-router workflow kit on GitHub](https://github.com/kujolang/kujo-workflows/tree/main/enterprise-dispatch-approval-router)
- [Browse the released workflow catalog](https://github.com/kujolang/kujo-workflows/blob/main/docs/audit/workflow-catalog.json)
