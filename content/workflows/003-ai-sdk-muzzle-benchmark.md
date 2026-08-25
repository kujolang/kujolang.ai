---
title: "AI SDK Muzzle Benchmark"
custom_url: "ai-sdk-muzzle-benchmark"
description: "Compare raw and Muzzle-mediated AI SDK runs with token and transcript evidence."
featured_image: "/assets/images/ecosystem/workflow-ai-sdk-muzzle-benchmark.webp"
social_image: "/assets/images/social/ai-sdk-muzzle-benchmark.jpg"
section: "production capable with limitations"
order: "30"
install_command: "git clone https://github.com/kujolang/kujo-workflows.git && cd kujo-workflows && ai-sdk-muzzle-benchmark/scripts/run-benchmark.sh"
github_url: "https://github.com/kujolang/kujo-workflows/tree/main/ai-sdk-muzzle-benchmark"
launch_story: "A local-first workflow kit with explicit inputs, outputs, evidence, recovery, and approval boundaries."
scope_note: "Current readiness: production capable with limitations. Review the workflow README before live-provider or host-affecting use."
version: "0.3.0"
last_updated: "2026-08-22"
keywords: "AI SDK Muzzle Benchmark, Kujo workflow, ai-sdk-muzzle-benchmark, local-first agent workflow"
seo_title: "AI SDK Muzzle Benchmark — Kujo Workflow"
seo_description: "Compare raw and Muzzle-mediated AI SDK runs with token and transcript evidence."
---

## Outcome

Compare raw and Muzzle-mediated AI SDK runs with token and transcript evidence.

## Inputs

- provider/model or fixture mode
- prompt template
- trial count

## Evidence and outputs

- ack.json
- compare.md
- summary.md
- RunLedger records

The workflow's evidence contract is: raw/muzzle logs, metrics, token metadata.

## Approval boundaries

- live provider credentials and spend

## State and recovery

per-run directories; suite aggregation is not resumable

## Release boundary

Readiness is **production capable with limitations** in the 0.3.0 local technical preview. Hosted runners, broad live-provider coverage, and enterprise readiness are not implied.

## Source

- [Open the complete ai-sdk-muzzle-benchmark workflow kit on GitHub](https://github.com/kujolang/kujo-workflows/tree/main/ai-sdk-muzzle-benchmark)
- [Browse the released workflow catalog](https://github.com/kujolang/kujo-workflows/blob/main/docs/audit/workflow-catalog.json)
