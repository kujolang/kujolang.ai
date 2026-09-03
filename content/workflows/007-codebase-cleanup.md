---
title: "Codebase Cleanup"
custom_url: "codebase-cleanup"
description: "Reduce unnecessary repository code and complexity through evidence-classified analysis, reviewer-approved mechanical cleanup, verification rollback, and structured reporting."
featured_image: "/assets/images/ecosystem/workflow-codebase-cleanup.webp"
social_image: "/assets/images/social/codebase-cleanup.jpg"
section: "production capable with limitations"
order: "70"
install_command: "git clone https://github.com/kujolang/kujo-workflows.git && cd kujo-workflows && codebase-cleanup/scripts/run-workflow.sh"
github_url: "https://github.com/kujolang/kujo-workflows/tree/main/codebase-cleanup"
launch_story: "A local-first workflow kit with explicit inputs, outputs, evidence, recovery, and approval boundaries."
scope_note: "Current readiness: production capable with limitations. Review the workflow README before live-provider or host-affecting use."
version: "0.4.0"
last_updated: "2026-09-02"
keywords: "Codebase Cleanup, Kujo workflow, codebase-cleanup, local-first agent workflow"
seo_title: "Codebase Cleanup — Kujo Workflow"
seo_description: "Reduce unnecessary repository code and complexity through evidence-classified analysis, reviewer-approved mechanical cleanup, verification rollback, and structured reporting."
---

## Outcome

Reduce unnecessary repository code and complexity through evidence-classified analysis, reviewer-approved mechanical cleanup, verification rollback, and structured reporting.

## Inputs

- target Git repository
- optional scope and cleanup category controls
- repository-owned verification commands
- optional reviewer-approved cleanup plan

## Evidence and outputs

- .cleanup-runs/<timestamp>/REPORT.md
- .cleanup-runs/<timestamp>/report.json
- .cleanup-runs/<timestamp>/cleanup-plan.json
- optional companion-tool evidence logs

The workflow's evidence contract is: classified findings, preserved complexity, stable IDs, before/after metrics, command exit/output hashes, integration dispositions, and Markdown/JSON reports.

## Approval boundaries

- analysis is read-only; mutation requires explicit stable finding IDs from a matching repository fingerprint
- only PROVEN supported operations auto-apply; public API, compatibility, dependency, architecture, and uncertain candidates require human judgment
- new verification failures roll back the complete cleanup batch

## State and recovery

timestamped analysis/apply packets; exact-content guards reject stale candidates; verification regressions restore all files changed by the batch

## Release boundary

Readiness is **production capable with limitations** in the 0.4.0 local technical preview. Hosted runners, broad live-provider coverage, and enterprise readiness are not implied.

## Source

- [Open the complete codebase-cleanup workflow kit on GitHub](https://github.com/kujolang/kujo-workflows/tree/main/codebase-cleanup)
- [Browse the released workflow catalog](https://github.com/kujolang/kujo-workflows/blob/main/docs/audit/workflow-catalog.json)
