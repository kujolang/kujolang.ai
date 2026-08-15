---
title: "Publishing House Primary Piece Production"
custom_url: "publishing-house-primary-piece"
description: "Create the authoritative editorial artifact from an Editorial Brief and evidence-ready Dossier packet, then package its exact bytes in GalleyPack."
featured_image: "/assets/images/ecosystem/workflow-publishing-house-primary-piece.webp"
social_image: "/assets/images/social/publishing-house-primary-piece.jpg"
section: "production capable with limitations"
order: "300"
install_command: "git clone --branch v0.3.0 --depth 1 https://github.com/kujolang/kujo-workflows.git && cd kujo-workflows && bash scripts/install-publishing-house.sh --prefix $PWD/.local/publishing-house && KUJO_REPOS=$PWD/.local/publishing-house/repos KUJO_BIN=$PWD/.local/publishing-house/bin/kujo bash $PWD/.local/publishing-house/kujo-workflows/publishing-house-primary-piece/bin/run --request fixtures/request.fixture.json --json"
github_url: "https://github.com/kujolang/kujo-workflows/tree/main/publishing-house-primary-piece"
launch_story: "Draft a claim-mapped primary artifact through one reusable engine with five portable format profiles and bounded developmental revision."
scope_note: "Installable today with deterministic fixture agents. Live model execution is optional, explicit, and remains a proposal rather than evidence or authority."
version: "0.3.0"
last_updated: "2026-08-14"
keywords: "Publishing House Primary Piece, editorial production workflow, GalleyPack, Dossier, Kujo workflow"
seo_title: "Publishing House Primary Piece Production — Kujo Workflow"
seo_description: "Produce a claim-mapped article or campaign artifact, revise it within bounds, and freeze exact lineage and checksums in GalleyPack."
---

## Outcome

Produce an authoritative Markdown or campaign artifact, map claims to Dossier evidence, perform bounded developmental revision, and add exact bytes to GalleyPack.

## Inputs

- Editorial Brief and evidence-ready Dossier decision
- one of five format profiles
- permission mode and declared local capabilities

## Evidence and outputs

- primary artifact, metadata, CTA, and optional code or diagram brief
- GalleyPack artifact record, lineage, claim references, and checksum
- Asset Production and Editorial Review child-run requests
- Dispatch evidence, agent receipts, and production receipt

## Approval boundaries

New or unsupported claims return to Dossier before continuing. Drafting never creates evidence, human approval, or publication authority.

## State and recovery

Bounded revisions create traceable versions. Repeated fixture execution is deterministic and preserves exact artifact checksums.

## Release boundary

The workflow contract is 0.1.0 and ships in Kujo Workflows 0.3.0. Live generation requires an explicit Agents SDK and AI SDK provider configuration.

## Source

- [Open the Primary Piece workflow kit on GitHub](https://github.com/kujolang/kujo-workflows/tree/main/publishing-house-primary-piece)
- [Read the Publishing House workflow overview](https://github.com/kujolang/kujo-workflows/blob/main/docs/publishing-house/README.md)
