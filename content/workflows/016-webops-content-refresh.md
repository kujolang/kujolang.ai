---
title: "Webops Content Refresh"
custom_url: "webops-content-refresh"
description: "Turn decay and accuracy evidence into a Spec, approved update boundary, verification, and future measurement cue."
featured_image: "/assets/images/ecosystem/workflow-webops-content-refresh.webp"
social_image: "/assets/images/social/webops-content-refresh.jpg"
section: "production capable with limitations"
order: "160"
install_command: "git clone https://github.com/kujolang/kujo-workflows.git && cd kujo-workflows && webops-content-refresh/scripts/run.sh"
github_url: "https://github.com/kujolang/kujo-workflows/tree/main/webops-content-refresh"
launch_story: "A local-first workflow kit with explicit inputs, outputs, evidence, recovery, and approval boundaries."
scope_note: "Current readiness: production capable with limitations. Review the workflow README before live-provider or host-affecting use."
version: "0.2.0"
last_updated: "2026-08-12"
keywords: "Webops Content Refresh, Kujo workflow, webops-content-refresh, local-first agent workflow"
seo_title: "Webops Content Refresh — Kujo Workflow"
seo_description: "Turn decay and accuracy evidence into a Spec, approved update boundary, verification, and future measurement cue."
---

## Outcome

Turn decay and accuracy evidence into a Spec, approved update boundary, verification, and future measurement cue.

## Inputs

- WebOps site profile
- fixture or live mode
- optional previous findings and permission override

## Evidence and outputs

- state.json
- capabilities.json
- steps/*.json
- findings.json
- report.md
- run-receipt.json

The workflow's evidence contract is: versioned capability, step, finding, report, state, and run receipt artifacts.

## Approval boundaries

- Content mutation and submission pause for separate role-bounded ACT approval.

## State and recovery

state.json records every step; rerun with --resume continues after completed steps.

## Release boundary

Readiness is **production capable with limitations** in the 0.2.0 local technical preview. Hosted runners, broad live-provider coverage, and enterprise readiness are not implied.

## Source

- [Open the complete webops-content-refresh workflow kit on GitHub](https://github.com/kujolang/kujo-workflows/tree/main/webops-content-refresh)
- [Browse the released workflow catalog](https://github.com/kujolang/kujo-workflows/blob/main/docs/audit/workflow-catalog.json)
