---
title: "Loop Engineering"
custom_url: "loop-engineering"
description: "Run a bounded Goal to Context to Act to Evaluate to Record to Stop loop in any repository."
featured_image: "/assets/images/ecosystem/workflow-loop-engineering.webp"
social_image: "/assets/images/social/loop-engineering.jpg"
section: "production ready"
order: "100"
install_command: "git clone https://github.com/kujolang/kujo-workflows.git && cd kujo-workflows && loop-engineering/scripts/run-workflow.sh"
github_url: "https://github.com/kujolang/kujo-workflows/tree/main/loop-engineering"
launch_story: "A local-first workflow kit with explicit inputs, outputs, evidence, recovery, and approval boundaries."
scope_note: "Current readiness: production ready. Review the workflow README before live-provider or host-affecting use."
version: "0.2.0"
last_updated: "2026-08-12"
keywords: "Loop Engineering, Kujo workflow, loop-engineering, local-first agent workflow"
seo_title: "Loop Engineering — Kujo Workflow"
seo_description: "Run a bounded Goal to Context to Act to Evaluate to Record to Stop loop in any repository."
---

## Outcome

Run a bounded Goal to Context to Act to Evaluate to Record to Stop loop in any repository.

## Inputs

- repo-local loop.yml or Markdown checklist

## Evidence and outputs

- .loop-engineering/SUMMARY.md
- ledger.tsv
- iterations
- blockers.md

The workflow's evidence contract is: context, action, diff, eval log, verdict per iteration.

## Approval boundaries

- commit/push opt-in
- deploy and destructive actions blocked by default

## State and recovery

iteration evidence and structured external blockers

## Release boundary

Readiness is **production ready** in the 0.2.0 local technical preview. Hosted runners, broad live-provider coverage, and enterprise readiness are not implied.

## Source

- [Open the complete loop-engineering workflow kit on GitHub](https://github.com/kujolang/kujo-workflows/tree/main/loop-engineering)
- [Browse the released workflow catalog](https://github.com/kujolang/kujo-workflows/blob/main/docs/audit/workflow-catalog.json)
