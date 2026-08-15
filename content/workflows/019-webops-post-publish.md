---
title: "WebOps Post Publish"
custom_url: "webops-post-publish"
description: "Verify newly published content, relationships, rendered quality, optional submission, distribution assets, and receipts."
featured_image: "/assets/images/ecosystem/workflow-webops-post-publish.webp"
social_image: "/assets/images/social/webops-post-publish.jpg"
section: "production capable with limitations"
order: "190"
install_command: "git clone https://github.com/kujolang/kujo-workflows.git && cd kujo-workflows && webops-post-publish/scripts/run.sh"
github_url: "https://github.com/kujolang/kujo-workflows/tree/main/webops-post-publish"
launch_story: "A local-first workflow kit with explicit inputs, outputs, evidence, recovery, and approval boundaries."
scope_note: "Current readiness: production capable with limitations. Review the workflow README before live-provider or host-affecting use."
version: "0.2.0"
last_updated: "2026-08-12"
keywords: "WebOps Post Publish, Kujo workflow, webops-post-publish, local-first agent workflow"
seo_title: "WebOps Post Publish — Kujo Workflow"
seo_description: "Verify newly published content, relationships, rendered quality, optional submission, distribution assets, and receipts."
---

## Outcome

Verify newly published content, relationships, rendered quality, optional submission, distribution assets, and receipts.

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

- Search submission and distribution publishing require explicit ACT; fixture mode creates receipts/assets only.

## State and recovery

state.json records every step; rerun with --resume continues after completed steps.

## Release boundary

Readiness is **production capable with limitations** in the 0.2.0 local technical preview. Hosted runners, broad live-provider coverage, and enterprise readiness are not implied.

## Source

- [Open the complete webops-post-publish workflow kit on GitHub](https://github.com/kujolang/kujo-workflows/tree/main/webops-post-publish)
- [Browse the released workflow catalog](https://github.com/kujolang/kujo-workflows/blob/main/docs/audit/workflow-catalog.json)
