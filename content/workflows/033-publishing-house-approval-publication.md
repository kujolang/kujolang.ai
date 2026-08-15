---
title: "Publishing House Approval and Publication"
custom_url: "publishing-house-approval-publication"
description: "Freeze an exact package, pause for human approval, bind VersionSeal authority to its checksum, and publish only through PressWire."
featured_image: "/assets/images/ecosystem/workflow-publishing-house-approval-publication.webp"
social_image: "/assets/images/social/publishing-house-approval-publication.jpg"
section: "production capable with limitations"
order: "330"
install_command: "git clone --branch v0.3.0 --depth 1 https://github.com/kujolang/kujo-workflows.git && cd kujo-workflows && bash scripts/install-publishing-house.sh --prefix $PWD/.local/publishing-house && KUJO_REPOS=$PWD/.local/publishing-house/repos KUJO_BIN=$PWD/.local/publishing-house/bin/kujo bash $PWD/.local/publishing-house/kujo-workflows/publishing-house-approval-publication/bin/run --request fixtures/request.fixture.json --json"
github_url: "https://github.com/kujolang/kujo-workflows/tree/main/publishing-house-approval-publication"
launch_story: "Fail closed across the exact human approval boundary, invalidate changed bytes, and require a PressWire receipt for publication success."
scope_note: "Installable today for dry-run and bounded local fixture publication. Live ACT requires a real human VersionSeal record and an operator-configured PressWire adapter."
version: "0.3.0"
last_updated: "2026-08-14"
keywords: "Publishing House Approval Publication, VersionSeal, PressWire, human approval workflow, Kujo workflow"
seo_title: "Publishing House Approval and Publication — Kujo Workflow"
seo_description: "Pause for exact checksum-bound human approval, verify permissions and destination, and publish only through PressWire."
---

## Outcome

Freeze the reviewed package, pause for a real human VersionSeal decision, verify exact authority on resume, and create a PressWire Publication Receipt when authorized.

## Inputs

- reviewed GalleyPack package, Dossier and AssetWorks references
- destination, action constraints, permission mode, and idempotency key
- VersionSeal approval record supplied only after the pause

## Evidence and outputs

- frozen package and checksum validation
- VersionSeal approval request, pause, resume, and exact decision reference
- PressWire preflight and dry-run or publication receipt
- StoryDesk update, Dispatch evidence, agent receipts, and completion or blocker receipt

## Approval boundaries

Only the Publishing Operations Director may reach **ACT**. Changed bytes, destination, action, expiry, revocation, missing adapter, or fixture external-effect attempts fail closed. Only PressWire publishes.

## State and recovery

The Dispatch run pauses and resumes exactly. Repeated resumes and duplicate idempotency keys are safe; request changes route back to the exact editorial owner.

## Release boundary

The workflow contract is 0.1.0 and ships in Kujo Workflows 0.3.0. Fixture approval is explicitly labeled and can only produce a bounded local effect; live publication requires operator-owned authority and adapters.

## Source

- [Open the Approval and Publication workflow kit on GitHub](https://github.com/kujolang/kujo-workflows/tree/main/publishing-house-approval-publication)
- [Read the Publishing House workflow overview](https://github.com/kujolang/kujo-workflows/blob/main/docs/publishing-house/README.md)
