---
title: "Webops Weekly Search Intelligence"
custom_url: "webops-weekly-search-intelligence"
description: "Compare measured search evidence, keyword opportunities, and decay signals with capability-level degradation."
featured_image: "/assets/images/ecosystem/workflow-webops-weekly-search-intelligence.webp"
social_image: "/assets/images/social/webops-weekly-search-intelligence.jpg"
section: "production capable with limitations"
order: "230"
install_command: "git clone https://github.com/kujolang/kujo-workflows.git && cd kujo-workflows && webops-weekly-search-intelligence/scripts/run.sh"
github_url: "https://github.com/kujolang/kujo-workflows/tree/main/webops-weekly-search-intelligence"
launch_story: "A local-first workflow kit with explicit inputs, outputs, evidence, recovery, and approval boundaries."
scope_note: "Current readiness: production capable with limitations. Review the workflow README before live-provider or host-affecting use."
version: "0.2.0"
last_updated: "2026-08-11"
keywords: "Webops Weekly Search Intelligence, Kujo workflow, webops-weekly-search-intelligence, local-first agent workflow"
seo_title: "Webops Weekly Search Intelligence — Kujo Workflow"
seo_description: "Compare measured search evidence, keyword opportunities, and decay signals with capability-level degradation."
---

## Outcome

Compare measured search evidence, keyword opportunities, and decay signals with capability-level degradation.

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

- Provider cost and property access; fixture mode is credential-free.

## State and recovery

state.json records every step; rerun with --resume continues after completed steps.

## Release boundary

Readiness is **production capable with limitations** in the 0.2.0 local technical preview. Hosted runners, broad live-provider coverage, and enterprise readiness are not implied.

## Source

- [Open the complete webops-weekly-search-intelligence workflow kit on GitHub](https://github.com/kujolang/kujo-workflows/tree/main/webops-weekly-search-intelligence)
- [Browse the released workflow catalog](https://github.com/kujolang/kujo-workflows/blob/main/docs/audit/workflow-catalog.json)
