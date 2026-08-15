---
title: "WebOps Quarterly Content Portfolio"
custom_url: "webops-quarterly-content-portfolio"
description: "Classify the content portfolio from graph, search, analytics, decay, pruning, and information-architecture evidence."
featured_image: "/assets/images/ecosystem/workflow-webops-quarterly-content-portfolio.webp"
social_image: "/assets/images/social/webops-quarterly-content-portfolio.jpg"
section: "production capable with limitations"
order: "200"
install_command: "git clone https://github.com/kujolang/kujo-workflows.git && cd kujo-workflows && webops-quarterly-content-portfolio/scripts/run.sh"
github_url: "https://github.com/kujolang/kujo-workflows/tree/main/webops-quarterly-content-portfolio"
launch_story: "A local-first workflow kit with explicit inputs, outputs, evidence, recovery, and approval boundaries."
scope_note: "Current readiness: production capable with limitations. Review the workflow README before live-provider or host-affecting use."
version: "0.2.0"
last_updated: "2026-08-12"
keywords: "WebOps Quarterly Content Portfolio, Kujo workflow, webops-quarterly-content-portfolio, local-first agent workflow"
seo_title: "WebOps Quarterly Content Portfolio — Kujo Workflow"
seo_description: "Classify the content portfolio from graph, search, analytics, decay, pruning, and information-architecture evidence."
---

## Outcome

Classify the content portfolio from graph, search, analytics, decay, pruning, and information-architecture evidence.

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

- Merge, redirect, retire, or URL changes require separate ACT and migration approval.

## State and recovery

state.json records every step; rerun with --resume continues after completed steps.

## Release boundary

Readiness is **production capable with limitations** in the 0.2.0 local technical preview. Hosted runners, broad live-provider coverage, and enterprise readiness are not implied.

## Source

- [Open the complete webops-quarterly-content-portfolio workflow kit on GitHub](https://github.com/kujolang/kujo-workflows/tree/main/webops-quarterly-content-portfolio)
- [Browse the released workflow catalog](https://github.com/kujolang/kujo-workflows/blob/main/docs/audit/workflow-catalog.json)
