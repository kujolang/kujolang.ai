---
title: "WebOps Finding To Fix"
custom_url: "webops-finding-to-fix"
description: "Move one stable WebOps finding through Spec, proposal, approval, implementation boundary, Eval, Lens, SiteProbe, and receipt evidence."
featured_image: "/assets/images/ecosystem/workflow-webops-finding-to-fix.webp"
social_image: "/assets/images/social/webops-finding-to-fix.jpg"
section: "production capable with limitations"
order: "300"
install_command: "git clone https://github.com/kujolang/kujo-workflows.git && cd kujo-workflows && webops-finding-to-fix/scripts/run.sh"
github_url: "https://github.com/kujolang/kujo-workflows/tree/main/webops-finding-to-fix"
launch_story: "A local-first workflow kit with explicit inputs, outputs, evidence, recovery, and approval boundaries."
scope_note: "Current readiness: production capable with limitations. Review the workflow README before live-provider or host-affecting use."
version: "0.4.0"
last_updated: "2026-09-02"
keywords: "WebOps Finding To Fix, Kujo workflow, webops-finding-to-fix, local-first agent workflow"
seo_title: "WebOps Finding To Fix — Kujo Workflow"
seo_description: "Move one stable WebOps finding through Spec, proposal, approval, implementation boundary, Eval, Lens, SiteProbe, and receipt evidence."
---

## Outcome

Move one stable WebOps finding through Spec, proposal, approval, implementation boundary, Eval, Lens, SiteProbe, and receipt evidence.

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

- Implementation and any production mutation require explicit role-bounded ACT; fixture mode produces proposal and proof plan.

## State and recovery

state.json records every step; rerun with --resume continues after completed steps.

## Release boundary

Readiness is **production capable with limitations** in the 0.4.0 local technical preview. Hosted runners, broad live-provider coverage, and enterprise readiness are not implied.

## Source

- [Open the complete webops-finding-to-fix workflow kit on GitHub](https://github.com/kujolang/kujo-workflows/tree/main/webops-finding-to-fix)
- [Browse the released workflow catalog](https://github.com/kujolang/kujo-workflows/blob/main/docs/audit/workflow-catalog.json)
