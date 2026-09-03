---
title: "Casefile Incident Evidence Packet"
custom_url: "casefile-incident-evidence-packet"
description: "Capture a deterministic failure into a redacted incident evidence bundle."
featured_image: "/assets/images/ecosystem/workflow-casefile-incident-evidence-packet.webp"
social_image: "/assets/images/social/casefile-incident-evidence-packet.jpg"
section: "production capable with limitations"
order: "60"
install_command: "git clone https://github.com/kujolang/kujo-workflows.git && cd kujo-workflows && casefile-incident-evidence-packet/scripts/run-workflow.sh"
github_url: "https://github.com/kujolang/kujo-workflows/tree/main/casefile-incident-evidence-packet"
launch_story: "A local-first workflow kit with explicit inputs, outputs, evidence, recovery, and approval boundaries."
scope_note: "Current readiness: production capable with limitations. Review the workflow README before live-provider or host-affecting use."
version: "0.4.0"
last_updated: "2026-09-02"
keywords: "Casefile Incident Evidence Packet, Kujo workflow, casefile-incident-evidence-packet, local-first agent workflow"
seo_title: "Casefile Incident Evidence Packet — Kujo Workflow"
seo_description: "Capture a deterministic failure into a redacted incident evidence bundle."
---

## Outcome

Capture a deterministic failure into a redacted incident evidence bundle.

## Inputs

- failing command fixture

## Evidence and outputs

- case.md
- case.json
- handoff.md

The workflow's evidence contract is: CaseFile bundle and rendered views.

## Approval boundaries

- capture of environment and repository metadata

## State and recovery

single capture run; cleanup is local

## Release boundary

Readiness is **production capable with limitations** in the 0.4.0 local technical preview. Hosted runners, broad live-provider coverage, and enterprise readiness are not implied.

## Source

- [Open the complete casefile-incident-evidence-packet workflow kit on GitHub](https://github.com/kujolang/kujo-workflows/tree/main/casefile-incident-evidence-packet)
- [Browse the released workflow catalog](https://github.com/kujolang/kujo-workflows/blob/main/docs/audit/workflow-catalog.json)
