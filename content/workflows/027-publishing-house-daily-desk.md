---
title: "Publishing House Daily Desk"
custom_url: "publishing-house-daily-desk"
description: "Validate a daily editorial packet, inspect StoryDesk state, and route each item to the narrowest actionable Publishing House workflow."
featured_image: "/assets/images/ecosystem/workflow-publishing-house-daily-desk.webp"
social_image: "/assets/images/social/publishing-house-daily-desk.jpg"
section: "production capable with limitations"
order: "270"
install_command: "git clone --branch v0.3.0 --depth 1 https://github.com/kujolang/kujo-workflows.git && cd kujo-workflows && bash scripts/install-publishing-house.sh --prefix $PWD/.local/publishing-house && KUJO_REPOS=$PWD/.local/publishing-house/repos KUJO_BIN=$PWD/.local/publishing-house/bin/kujo bash $PWD/.local/publishing-house/kujo-workflows/publishing-house-daily-desk/bin/run --request fixtures/request.fixture.json --json"
github_url: "https://github.com/kujolang/kujo-workflows/tree/main/publishing-house-daily-desk"
launch_story: "Turn a portable daily packet into auditable child-run requests without drafting, approving, or publishing content."
scope_note: "Installable today for deterministic local routing. Live use requires operator-supplied profiles and compatible StoryDesk, Dispatch, and Agents SDK installations."
version: "0.3.0"
last_updated: "2026-08-14"
keywords: "Publishing House Daily Desk, editorial routing workflow, StoryDesk, Dispatch, Kujo workflow"
seo_title: "Publishing House Daily Desk — Kujo Workflow"
seo_description: "Run a local, resumable editorial desk that validates daily packets and routes work through the Publishing House lifecycle."
---

## Outcome

Validate a normalized daily editorial packet, classify StoryDesk items, and emit explicit child-run requests, deferrals, blockers, and a routing receipt.

## Inputs

- normalized daily packet or StoryDesk packet reference
- portable House, Brand, and Audience profiles
- permission mode, capabilities, and execute-or-plan-only policy

## Evidence and outputs

- validated packet and dependency graph
- routing decisions and child workflow requests
- Dispatch state, trace, report, and resumable run state
- agent receipts, run summary, and completion or blocker receipt

## Approval boundaries

Daily Desk defaults to **PROPOSE**. It may route work, but it cannot manufacture a commission, evidence decision, review verdict, approval, or publication receipt.

## State and recovery

Runs are deterministic and idempotent in fixture mode. Bounded retries and stable record references support inspection and resume after interruption.

## Release boundary

The workflow contract is 0.1.0 and ships in Kujo Workflows 0.3.0. The offline fixture is supported; live adapters and operator capacity policy remain deployment-specific.

## Source

- [Open the Daily Desk workflow kit on GitHub](https://github.com/kujolang/kujo-workflows/tree/main/publishing-house-daily-desk)
- [Read the Publishing House workflow overview](https://github.com/kujolang/kujo-workflows/blob/main/docs/publishing-house/README.md)
