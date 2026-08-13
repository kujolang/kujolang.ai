---
title: "Webops AI Visibility Benchmark"
custom_url: "webops-ai-visibility-benchmark"
description: "Run a fixed longitudinal query suite across explicitly available AI/search surfaces without fabricated availability."
featured_image: "/assets/images/ecosystem/workflow-webops-ai-visibility-benchmark.webp"
social_image: "/assets/images/social/webops-ai-visibility-benchmark.jpg"
section: "experimental"
order: "150"
install_command: "git clone https://github.com/kujolang/kujo-workflows.git && cd kujo-workflows && webops-ai-visibility-benchmark/scripts/run.sh"
github_url: "https://github.com/kujolang/kujo-workflows/tree/main/webops-ai-visibility-benchmark"
launch_story: "A local-first workflow kit with explicit inputs, outputs, evidence, recovery, and approval boundaries."
scope_note: "Current readiness: experimental. Review the workflow README before live-provider or host-affecting use."
version: "0.2.0"
last_updated: "2026-08-12"
keywords: "Webops AI Visibility Benchmark, Kujo workflow, webops-ai-visibility-benchmark, local-first agent workflow"
seo_title: "Webops AI Visibility Benchmark — Kujo Workflow"
seo_description: "Run a fixed longitudinal query suite across explicitly available AI/search surfaces without fabricated availability."
---

## Outcome

Run a fixed longitudinal query suite across explicitly available AI/search surfaces without fabricated availability.

## Inputs

- WebOps site profile
- fixture or live mode
- optional previous findings and permission override

## Evidence and outputs

- state.json
- capabilities.json
- steps/*.json
- findings.json
- report.md
- run-receipt.json

The workflow's evidence contract is: versioned capability, step, finding, report, state, and run receipt artifacts.

## Approval boundaries

- Live provider cost and terms; unavailable surfaces are skipped.

## State and recovery

state.json records every step; rerun with --resume continues after completed steps.

## Release boundary

Readiness is **experimental** in the 0.2.0 local technical preview. Hosted runners, broad live-provider coverage, and enterprise readiness are not implied.

## Source

- [Open the complete webops-ai-visibility-benchmark workflow kit on GitHub](https://github.com/kujolang/kujo-workflows/tree/main/webops-ai-visibility-benchmark)
- [Browse the released workflow catalog](https://github.com/kujolang/kujo-workflows/blob/main/docs/audit/workflow-catalog.json)
