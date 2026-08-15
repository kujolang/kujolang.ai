---
title: "Publishing House Post-Publication Learning"
custom_url: "publishing-house-post-publication"
description: "Turn a verified publication receipt, measurements, and audience feedback into bounded editorial learning and follow-up recommendations."
featured_image: "/assets/images/ecosystem/workflow-publishing-house-post-publication.webp"
social_image: "/assets/images/social/publishing-house-post-publication.jpg"
section: "production capable with limitations"
order: "340"
install_command: "git clone --branch v0.3.0 --depth 1 https://github.com/kujolang/kujo-workflows.git && cd kujo-workflows && bash scripts/install-publishing-house.sh --prefix $PWD/.local/publishing-house && KUJO_REPOS=$PWD/.local/publishing-house/repos KUJO_BIN=$PWD/.local/publishing-house/bin/kujo bash $PWD/.local/publishing-house/kujo-workflows/publishing-house-post-publication/bin/run --request fixtures/request.fixture.json --json"
github_url: "https://github.com/kujolang/kujo-workflows/tree/main/publishing-house-post-publication"
launch_story: "Preserve measurement and attribution limits, compare only compatible windows, and return a reviewable recommendation to StoryDesk."
scope_note: "Installable today with deterministic metrics and feedback fixtures. Live measurement providers are optional and missing data remains explicitly missing."
version: "0.3.0"
last_updated: "2026-08-14"
keywords: "Publishing House Post-Publication Learning, ReaderSignal, editorial analytics workflow, StoryDesk, Kujo workflow"
seo_title: "Publishing House Post-Publication Learning — Kujo Workflow"
seo_description: "Verify a PressWire receipt, record measured audience signals, and return bounded editorial learning to StoryDesk."
---

## Outcome

Produce quantified and qualitative ReaderSignal learning, preserve privacy and attribution limits, and return a follow-up recommendation to StoryDesk without commissioning it automatically.

## Inputs

- verified PressWire Publication Receipt
- measurement definitions, compatible windows, and privacy policy
- deterministic metrics, manual snapshots, feedback, or explicit provider adapters

## Evidence and outputs

- ReaderSignal measurements, feedback, comparisons, and learning records
- follow-up, clarification, proof, refresh, correction, adaptation, or no-action recommendation
- StoryDesk idea or follow-up recommendation reference
- Dispatch evidence, agent receipts, report, and completion receipt

## Approval boundaries

Missing metrics remain missing and estimates remain labeled. Correlation is not promoted to causation, and recommendations confer neither commissioning nor publication authority.

## State and recovery

Stable publication and measurement references support idempotent replay. Any follow-up begins a new run with a new run ID and explicit operator policy.

## Release boundary

The workflow contract is 0.1.0 and ships in Kujo Workflows 0.3.0. Fixture learning is offline; live metrics require operator-configured ReaderSignal providers.

## Source

- [Open the Post-Publication Learning workflow kit on GitHub](https://github.com/kujolang/kujo-workflows/tree/main/publishing-house-post-publication)
- [Read the Publishing House workflow overview](https://github.com/kujolang/kujo-workflows/blob/main/docs/publishing-house/README.md)
