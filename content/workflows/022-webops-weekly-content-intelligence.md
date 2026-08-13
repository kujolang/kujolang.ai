---
title: "Webops Weekly Content Intelligence"
custom_url: "webops-weekly-content-intelligence"
description: "Combine trends, query opportunity, content relationships, gaps, accuracy, and internal-link proposals."
featured_image: "/assets/images/ecosystem/workflow-webops-weekly-content-intelligence.webp"
social_image: "/assets/images/social/webops-weekly-content-intelligence.jpg"
section: "production capable with limitations"
order: "220"
install_command: "git clone https://github.com/kujolang/kujo-workflows.git && cd kujo-workflows && webops-weekly-content-intelligence/scripts/run.sh"
github_url: "https://github.com/kujolang/kujo-workflows/tree/main/webops-weekly-content-intelligence"
launch_story: "A local-first workflow kit with explicit inputs, outputs, evidence, recovery, and approval boundaries."
scope_note: "Current readiness: production capable with limitations. Review the workflow README before live-provider or host-affecting use."
version: "0.2.0"
last_updated: "2026-08-11"
keywords: "Webops Weekly Content Intelligence, Kujo workflow, webops-weekly-content-intelligence, local-first agent workflow"
seo_title: "Webops Weekly Content Intelligence — Kujo Workflow"
seo_description: "Combine trends, query opportunity, content relationships, gaps, accuracy, and internal-link proposals."
---

## Outcome

Combine trends, query opportunity, content relationships, gaps, accuracy, and internal-link proposals.

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

- Internal-link source changes require a separate ACT run.

## State and recovery

state.json records every step; rerun with --resume continues after completed steps.

## Release boundary

Readiness is **production capable with limitations** in the 0.2.0 local technical preview. Hosted runners, broad live-provider coverage, and enterprise readiness are not implied.

## Source

- [Open the complete webops-weekly-content-intelligence workflow kit on GitHub](https://github.com/kujolang/kujo-workflows/tree/main/webops-weekly-content-intelligence)
- [Browse the released workflow catalog](https://github.com/kujolang/kujo-workflows/blob/main/docs/audit/workflow-catalog.json)
