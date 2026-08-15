---
title: "Publishing House Commissioning"
custom_url: "publishing-house-commissioning"
description: "Turn an approved idea, campaign need, or follow-up recommendation into a specific Editorial Brief and bounded assignments."
featured_image: "/assets/images/ecosystem/workflow-publishing-house-commissioning.webp"
social_image: "/assets/images/social/publishing-house-commissioning.jpg"
section: "production capable with limitations"
order: "280"
install_command: "git clone --branch v0.3.0 --depth 1 https://github.com/kujolang/kujo-workflows.git && cd kujo-workflows && bash scripts/install-publishing-house.sh --prefix $PWD/.local/publishing-house && KUJO_REPOS=$PWD/.local/publishing-house/repos KUJO_BIN=$PWD/.local/publishing-house/bin/kujo bash $PWD/.local/publishing-house/kujo-workflows/publishing-house-commissioning/bin/run --request fixtures/request.fixture.json --json"
github_url: "https://github.com/kujolang/kujo-workflows/tree/main/publishing-house-commissioning"
launch_story: "Create a defensible commission with a thesis, reader promise, artifact bundle, evidence burden, owners, and kill conditions."
scope_note: "Installable today for deterministic local commissioning. Live use requires operator-supplied strategy profiles and compatible StoryDesk and Dossier installations."
version: "0.3.0"
last_updated: "2026-08-14"
keywords: "Publishing House Commissioning, Editorial Brief workflow, StoryDesk, Dossier, Kujo workflow"
seo_title: "Publishing House Commissioning — Kujo Workflow"
seo_description: "Create a precise Editorial Brief, assignments, claim inventory, and evidence work order with a local Kujo workflow."
---

## Outcome

Create a StoryDesk Editorial Brief with exact strategy, reader promise, format, CTA, evidence burden, assignment boundaries, dependencies, and approval owner.

## Inputs

- approved idea, campaign need, calendar entry, or follow-up recommendation
- House, Brand, and Audience profiles
- permission mode and declared local capabilities

## Evidence and outputs

- StoryDesk Editorial Brief and assignments
- dependencies, initial claim inventory, and evidence work order
- Evidence Dossier child-run request
- Dispatch evidence, agent receipts, and commissioning receipt

## Approval boundaries

Commissioning defaults to **PROPOSE**. It records a commission but does not declare evidence ready, approve an artifact, or publish.

## State and recovery

Stable assignment and record references make reruns idempotent. Invalid profiles, generic angles, or infeasible evidence produce bounded blockers.

## Release boundary

The workflow contract is 0.1.0 and ships in Kujo Workflows 0.3.0. Fixture commissioning works offline; live editorial strategy and adapters are operator-owned.

## Source

- [Open the Commissioning workflow kit on GitHub](https://github.com/kujolang/kujo-workflows/tree/main/publishing-house-commissioning)
- [Read the Publishing House workflow overview](https://github.com/kujolang/kujo-workflows/blob/main/docs/publishing-house/README.md)
