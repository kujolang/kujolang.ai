---
title: "Publishing House Asset Production"
custom_url: "publishing-house-asset-production"
description: "Plan, validate, and package supported media assets with rights, provenance, variants, captions, transcripts, alt text, and checksums."
featured_image: "/assets/images/ecosystem/workflow-publishing-house-asset-production.webp"
social_image: "/assets/images/social/publishing-house-asset-production.jpg"
section: "production capable with limitations"
order: "310"
install_command: "git clone --branch v0.3.0 --depth 1 https://github.com/kujolang/kujo-workflows.git && cd kujo-workflows && bash scripts/install-publishing-house.sh --prefix $PWD/.local/publishing-house && KUJO_REPOS=$PWD/.local/publishing-house/repos KUJO_BIN=$PWD/.local/publishing-house/bin/kujo bash $PWD/.local/publishing-house/kujo-workflows/publishing-house-asset-production/bin/run --request fixtures/request.fixture.json --json"
github_url: "https://github.com/kujolang/kujo-workflows/tree/main/publishing-house-asset-production"
launch_story: "Preserve source media, execute only supported transformations, and attach an accessibility-aware AssetWorks manifest to GalleyPack."
scope_note: "Installable today for local fixture assets and validation. Unsupported transformations return bounded blockers; this workflow does not publish assets."
version: "0.3.0"
last_updated: "2026-08-14"
keywords: "Publishing House Asset Production, AssetWorks, media manifest, accessibility workflow, Kujo workflow"
seo_title: "Publishing House Asset Production — Kujo Workflow"
seo_description: "Create or validate media variants, accessibility records, provenance, and an AssetWorks manifest for an exact GalleyPack package."
---

## Outcome

Plan and execute supported local media operations, validate accessibility and provenance, and attach exact files plus an AssetWorks Media Manifest to GalleyPack.

## Inputs

- asset brief and source artifact
- source media and rights, consent, privacy, and disclosure references
- declared local transformation capabilities

## Evidence and outputs

- AssetWorks plan, jobs, variants, and accessibility records
- captions, transcripts, alt text, provenance, and disclosures
- Media Manifest with exact file checksums
- GalleyPack attachments, Dispatch evidence, agent receipts, and asset receipt

## Approval boundaries

Only supported operations run. Source files remain preserved, unsupported requirements block cleanly, and the workflow never publishes assets.

## State and recovery

Stable job IDs, idempotency keys, and checksums make safe retry and resume possible without accidental overwrite.

## Release boundary

The workflow contract is 0.1.0 and ships in Kujo Workflows 0.3.0. Optional media adapters must be configured explicitly; Dither, Howl, website creation, and publication are excluded.

## Source

- [Open the Asset Production workflow kit on GitHub](https://github.com/kujolang/kujo-workflows/tree/main/publishing-house-asset-production)
- [Read the Publishing House workflow overview](https://github.com/kujolang/kujo-workflows/blob/main/docs/publishing-house/README.md)
