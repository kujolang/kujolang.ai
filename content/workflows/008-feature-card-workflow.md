---
title: "Feature Card Workflow"
custom_url: "feature-card-workflow"
description: "Convert a developer task card into scoped implementation, verification, evidence and handoff."
featured_image: "/assets/images/ecosystem/workflow-feature-card-workflow.webp"
social_image: "/assets/images/social/feature-card-workflow.jpg"
section: "production capable with limitations"
order: "80"
install_command: "git clone https://github.com/kujolang/kujo-workflows.git && cd kujo-workflows && feature-card-workflow/muzzle-template/workflows/feature-card-full.sh"
github_url: "https://github.com/kujolang/kujo-workflows/tree/main/feature-card-workflow"
launch_story: "A local-first workflow kit with explicit inputs, outputs, evidence, recovery, and approval boundaries."
scope_note: "Current readiness: production capable with limitations. Review the workflow README before live-provider or host-affecting use."
version: "0.2.0"
last_updated: "2026-08-11"
keywords: "Feature Card Workflow, Kujo workflow, feature-card-workflow, local-first agent workflow"
seo_title: "Feature Card Workflow — Kujo Workflow"
seo_description: "Convert a developer task card into scoped implementation, verification, evidence and handoff."
---

## Outcome

Convert a developer task card into scoped implementation, verification, evidence and handoff.

## Inputs

- card ID
- task file
- target Git repository
- optional verification/browser configuration

## Evidence and outputs

- .kujo/feature-cards/<card-id>/status.tsv
- briefs
- proof
- reviewer-handoff.md

The workflow's evidence contract is: status.tsv, logs, tool reports, diff and handoff.

## Approval boundaries

- implementation command or Codex
- merge/deploy approval
- optional commit

## State and recovery

repo-local packet; stage results are durable but no resume command

## Release boundary

Readiness is **production capable with limitations** in the 0.2.0 local technical preview. Hosted runners, broad live-provider coverage, and enterprise readiness are not implied.

## Source

- [Open the complete feature-card-workflow workflow kit on GitHub](https://github.com/kujolang/kujo-workflows/tree/main/feature-card-workflow)
- [Browse the released workflow catalog](https://github.com/kujolang/kujo-workflows/blob/main/docs/audit/workflow-catalog.json)
