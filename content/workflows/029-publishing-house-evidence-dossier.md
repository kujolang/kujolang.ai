---
title: "Publishing House Evidence Dossier"
custom_url: "publishing-house-evidence-dossier"
description: "Build and independently review the claims, sources, evidence, quotations, rights, consent, conflicts, and freshness packet for an assignment."
featured_image: "/assets/images/ecosystem/workflow-publishing-house-evidence-dossier.webp"
social_image: "/assets/images/social/publishing-house-evidence-dossier.jpg"
section: "production capable with limitations"
order: "290"
install_command: "git clone --branch v0.3.0 --depth 1 https://github.com/kujolang/kujo-workflows.git && cd kujo-workflows && bash scripts/install-publishing-house.sh --prefix $PWD/.local/publishing-house && KUJO_REPOS=$PWD/.local/publishing-house/repos KUJO_BIN=$PWD/.local/publishing-house/bin/kujo bash $PWD/.local/publishing-house/kujo-workflows/publishing-house-evidence-dossier/bin/run --request fixtures/request.fixture.json --json"
github_url: "https://github.com/kujolang/kujo-workflows/tree/main/publishing-house-evidence-dossier"
launch_story: "Convert every material claim into a resolvable Dossier record and fail closed when evidence is unsupported, stale, or incompatible."
scope_note: "Installable today with captured local fixture evidence. Live retrieval providers are optional, explicit adapters and are never silently substituted."
version: "0.3.0"
last_updated: "2026-08-14"
keywords: "Publishing House Evidence Dossier, claims workflow, Dossier, editorial evidence, Kujo workflow"
seo_title: "Publishing House Evidence Dossier — Kujo Workflow"
seo_description: "Build a checksum-bound editorial evidence packet with claim classification, source locations, rights, consent, and freshness review."
---

## Outcome

Return an evidence-ready, partial, conflicted, blocked, or rejected decision with exact Dossier record references for every material claim.

## Inputs

- StoryDesk Editorial Brief and claim inventory
- captured local sources and evidence
- rights, consent, privacy, disclosure, and freshness requirements

## Evidence and outputs

- Dossier claim, source, evidence, quotation, conflict, and rights references
- independent Standards & Evidence review
- StoryDesk handoff and Primary Piece child-run request
- Dispatch evidence, agent receipts, and evidence decision receipt

## Approval boundaries

The workflow classifies evidence honestly. A URL or agent assertion is not promoted to verified evidence, and unsupported material claims block or narrow the assignment.

## State and recovery

Checksums and retrieval timestamps bind captured evidence. Resume preserves conflicts and prior classifications instead of flattening or overwriting them.

## Release boundary

The workflow contract is 0.1.0 and ships in Kujo Workflows 0.3.0. The bundled proof is offline; live retrieval depends on explicitly configured providers.

## Source

- [Open the Evidence Dossier workflow kit on GitHub](https://github.com/kujolang/kujo-workflows/tree/main/publishing-house-evidence-dossier)
- [Read the Publishing House workflow overview](https://github.com/kujolang/kujo-workflows/blob/main/docs/publishing-house/README.md)
