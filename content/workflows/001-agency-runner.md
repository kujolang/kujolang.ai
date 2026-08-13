---
title: "Agency Runner"
custom_url: "agency-runner"
description: "Turn an agency task and site profile into a resumable local proof packet."
featured_image: "/assets/images/ecosystem/workflow-agency-runner.webp"
social_image: "/assets/images/social/agency-runner.jpg"
section: "experimental"
order: "10"
install_command: "git clone https://github.com/kujolang/kujo-workflows.git && cd kujo-workflows && agency-runner/bin/agency-loop"
github_url: "https://github.com/kujolang/kujo-workflows/tree/main/agency-runner"
launch_story: "A local-first workflow kit with explicit inputs, outputs, evidence, recovery, and approval boundaries."
scope_note: "Current readiness: experimental. Review the workflow README before live-provider or host-affecting use."
version: "0.2.0"
last_updated: "2026-08-11"
keywords: "Agency Runner, Kujo workflow, agency-runner, local-first agent workflow"
seo_title: "Agency Runner — Kujo Workflow"
seo_description: "Turn an agency task and site profile into a resumable local proof packet."
---

## Outcome

Turn an agency task and site profile into a resumable local proof packet.

## Inputs

- site profile
- recipe
- task file or text

## Evidence and outputs

- run-state.json
- handoff
- proof artifacts
- logs

The workflow's evidence contract is: local run packet with redacted logs.

## Approval boundaries

- site credentials
- live-site mutation
- handoff acceptance

## State and recovery

run-state.json phase tracking; continue resumes pending phases

## Release boundary

Readiness is **experimental** in the 0.2.0 local technical preview. Hosted runners, broad live-provider coverage, and enterprise readiness are not implied.

## Source

- [Open the complete agency-runner workflow kit on GitHub](https://github.com/kujolang/kujo-workflows/tree/main/agency-runner)
- [Browse the released workflow catalog](https://github.com/kujolang/kujo-workflows/blob/main/docs/audit/workflow-catalog.json)
