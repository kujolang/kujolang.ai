---
title: "Webops Weekly Site Health"
custom_url: "webops-weekly-site-health"
description: "Compare weekly crawl and rendered site health, links, performance, accessibility, schema, and metadata."
featured_image: "/assets/images/ecosystem/workflow-webops-weekly-site-health.webp"
social_image: "/assets/images/social/webops-weekly-site-health.jpg"
section: "production capable with limitations"
order: "240"
install_command: "git clone https://github.com/kujolang/kujo-workflows.git && cd kujo-workflows && webops-weekly-site-health/scripts/run.sh"
github_url: "https://github.com/kujolang/kujo-workflows/tree/main/webops-weekly-site-health"
launch_story: "A local-first workflow kit with explicit inputs, outputs, evidence, recovery, and approval boundaries."
scope_note: "Current readiness: production capable with limitations. Review the workflow README before live-provider or host-affecting use."
version: "0.2.0"
last_updated: "2026-08-11"
keywords: "Webops Weekly Site Health, Kujo workflow, webops-weekly-site-health, local-first agent workflow"
seo_title: "Webops Weekly Site Health — Kujo Workflow"
seo_description: "Compare weekly crawl and rendered site health, links, performance, accessibility, schema, and metadata."
---

## Outcome

Compare weekly crawl and rendered site health, links, performance, accessibility, schema, and metadata.

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

- No site mutation; optional provider credentials enable performance modules only.

## State and recovery

state.json records every step; rerun with --resume continues after completed steps.

## Release boundary

Readiness is **production capable with limitations** in the 0.2.0 local technical preview. Hosted runners, broad live-provider coverage, and enterprise readiness are not implied.

## Source

- [Open the complete webops-weekly-site-health workflow kit on GitHub](https://github.com/kujolang/kujo-workflows/tree/main/webops-weekly-site-health)
- [Browse the released workflow catalog](https://github.com/kujolang/kujo-workflows/blob/main/docs/audit/workflow-catalog.json)
