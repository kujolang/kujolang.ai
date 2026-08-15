---
title: "Publishing House Editorial Review and Revision"
custom_url: "publishing-house-editorial-review"
description: "Review an exact GalleyPack version against evidence, brand, format, accessibility, and the eight-dimension Publishing House quality standard."
featured_image: "/assets/images/ecosystem/workflow-publishing-house-editorial-review.webp"
social_image: "/assets/images/social/publishing-house-editorial-review.jpg"
section: "production capable with limitations"
order: "320"
install_command: "git clone --branch v0.3.0 --depth 1 https://github.com/kujolang/kujo-workflows.git && cd kujo-workflows && bash scripts/install-publishing-house.sh --prefix $PWD/.local/publishing-house && KUJO_REPOS=$PWD/.local/publishing-house/repos KUJO_BIN=$PWD/.local/publishing-house/bin/kujo bash $PWD/.local/publishing-house/kujo-workflows/publishing-house-editorial-review/bin/run --request fixtures/request.fixture.json --json"
github_url: "https://github.com/kujolang/kujo-workflows/tree/main/publishing-house-editorial-review"
launch_story: "Preserve independent BluePencil findings and disagreements, route precise changes, and require a new GalleyPack version after edits."
scope_note: "Installable today with a deterministic bounded revision proof. Semantic live review requires explicitly configured agents and does not confer publication approval."
version: "0.3.0"
last_updated: "2026-08-14"
keywords: "Publishing House Editorial Review, BluePencil, GalleyPack revision workflow, editorial quality, Kujo workflow"
seo_title: "Publishing House Editorial Review — Kujo Workflow"
seo_description: "Run independent editorial reviews against exact package checksums, preserve disagreements, and route a bounded revision loop."
---

## Outcome

Return pass, pass with queries, revise, blocked, reject, or unverified for one exact GalleyPack version, followed by an Editor-in-Chief recommendation.

## Inputs

- exact GalleyPack package and checksum
- Editorial Brief, Dossier references, Brand Profile, and format requirements
- required reviewer matrix and revision limit

## Evidence and outputs

- BluePencil review requests, findings, disagreements, and verdicts
- deterministic structure, claim-reference, format, and accessibility results
- revised GalleyPack versions and attached prior review records
- approval child-run request, Dispatch evidence, agent receipts, and review receipt

## Approval boundaries

Blocker precedence is preserved; scores are not averaged over blocking failures. BluePencil verdicts and agent recommendations are not human publication approval.

## State and recovery

Revisions are bounded and each edit requires a new package version. Resume re-runs only necessary reviews while preserving the complete prior record.

## Release boundary

The workflow contract is 0.1.0 and ships in Kujo Workflows 0.3.0. Fixture review is deterministic; live editorial judgment depends on configured agents and human policy.

## Source

- [Open the Editorial Review workflow kit on GitHub](https://github.com/kujolang/kujo-workflows/tree/main/publishing-house-editorial-review)
- [Read the Publishing House workflow overview](https://github.com/kujolang/kujo-workflows/blob/main/docs/publishing-house/README.md)
