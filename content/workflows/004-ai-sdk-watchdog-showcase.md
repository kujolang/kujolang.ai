---
title: "AI SDK Watchdog Showcase"
custom_url: "ai-sdk-watchdog-showcase"
description: "Route AI SDK chat traffic through Watchdog and export telemetry."
featured_image: "/assets/images/ecosystem/workflow-ai-sdk-watchdog-showcase.webp"
social_image: "/assets/images/social/ai-sdk-watchdog-showcase.jpg"
section: "production capable with limitations"
order: "40"
install_command: "git clone https://github.com/kujolang/kujo-workflows.git && cd kujo-workflows && ai-sdk-watchdog-showcase/scripts/run-showcase.sh"
github_url: "https://github.com/kujolang/kujo-workflows/tree/main/ai-sdk-watchdog-showcase"
launch_story: "A local-first workflow kit with explicit inputs, outputs, evidence, recovery, and approval boundaries."
scope_note: "Current readiness: production capable with limitations. Review the workflow README before live-provider or host-affecting use."
version: "0.3.0"
last_updated: "2026-08-22"
keywords: "AI SDK Watchdog Showcase, Kujo workflow, ai-sdk-watchdog-showcase, local-first agent workflow"
seo_title: "AI SDK Watchdog Showcase — Kujo Workflow"
seo_description: "Route AI SDK chat traffic through Watchdog and export telemetry."
---

## Outcome

Route AI SDK chat traffic through Watchdog and export telemetry.

## Inputs

- fixture or live provider configuration

## Evidence and outputs

- responses
- Watchdog telemetry exports
- summary.md

The workflow's evidence contract is: request, usage, error and agent-step exports.

## Approval boundaries

- live provider key and spend

## State and recovery

local process cleanup trap; no resume protocol

## Release boundary

Readiness is **production capable with limitations** in the 0.3.0 local technical preview. Hosted runners, broad live-provider coverage, and enterprise readiness are not implied.

## Source

- [Open the complete ai-sdk-watchdog-showcase workflow kit on GitHub](https://github.com/kujolang/kujo-workflows/tree/main/ai-sdk-watchdog-showcase)
- [Browse the released workflow catalog](https://github.com/kujolang/kujo-workflows/blob/main/docs/audit/workflow-catalog.json)
