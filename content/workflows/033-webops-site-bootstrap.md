---
title: "WebOps Site Bootstrap"
custom_url: "webops-site-bootstrap"
description: "Establish a credential-free initial website, repository, content-graph, browser, and reporting baseline."
featured_image: "/assets/images/ecosystem/workflow-webops-site-bootstrap.webp"
social_image: "/assets/images/social/webops-site-bootstrap.jpg"
section: "production capable with limitations"
order: "330"
install_command: "git clone https://github.com/kujolang/kujo-workflows.git && cd kujo-workflows && webops-site-bootstrap/scripts/run.sh"
github_url: "https://github.com/kujolang/kujo-workflows/tree/main/webops-site-bootstrap"
launch_story: "A local-first workflow kit with explicit inputs, outputs, evidence, recovery, and approval boundaries."
scope_note: "Current readiness: production capable with limitations. Review the workflow README before live-provider or host-affecting use."
version: "0.3.0"
last_updated: "2026-08-22"
keywords: "WebOps Site Bootstrap, Kujo workflow, webops-site-bootstrap, local-first agent workflow"
seo_title: "WebOps Site Bootstrap — Kujo Workflow"
seo_description: "Establish a credential-free initial website, repository, content-graph, browser, and reporting baseline."
---

## Outcome

Establish a credential-free initial website, repository, content-graph, browser, and reporting baseline.

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

- Repository access is read-only; authenticated browser state is optional and external.

## State and recovery

state.json records every step; rerun with --resume continues after completed steps.

## Release boundary

Readiness is **production capable with limitations** in the 0.3.0 local technical preview. Hosted runners, broad live-provider coverage, and enterprise readiness are not implied.

## Source

- [Open the complete webops-site-bootstrap workflow kit on GitHub](https://github.com/kujolang/kujo-workflows/tree/main/webops-site-bootstrap)
- [Browse the released workflow catalog](https://github.com/kujolang/kujo-workflows/blob/main/docs/audit/workflow-catalog.json)
