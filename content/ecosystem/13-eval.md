---
title: "Eval"
custom_url: eval
description: "Check agent outputs, commands, HTTP, JSON and workflow artifacts with declared assertions and CI-friendly verdicts."
featured_image: "/assets/images/ecosystem/eval-quality-gates.webp"
section: "Primitives"
tags: [Primitive, Verification]
order: 40
install_command: "kennel add eval"
github_url: "https://github.com/kujolang/eval"
launch_story: "An independent acceptance layer that makes success criteria executable."
scope_note: "Eval verifies declared checks; it is only as complete as the suite and policies a project defines."
keywords: "Eval, Kujo ecosystem, Primitive, Verification"
seo_title: "Eval — Test Agent Outputs and Workflow Artifacts | Kujo"
version: "1.1.0"
latest_release_url: "https://github.com/kujolang/eval/releases/tag/v1.1.0"
release_status: "Version identifies the published release. The Kennel command selects the latest stable registry package; see scope_note for release boundaries."
last_updated: "2026-10-14"
---

## What it does

Declared checks for files, commands, HTTP, JSON, snapshots, policy, and workflow artifacts with CI-friendly verdicts. Results depend on the inputs, environment and assertions.

## Why it belongs in Kujo

An independent acceptance layer that makes success criteria executable.

## Operating boundary

Eval verifies declared checks; it is only as complete as the suite and policies a project defines.

## Learn more

The repository is the source of truth for current setup, commands, examples, security notes, compatibility, and verification evidence.

## October 14 release update

Portable results and JSON-shape, threshold, snapshot and CLI repairs improve deterministic evaluation; Watchdog correlation preserves observed evidence.

## Inspect the evidence

Review the [published release](https://github.com/kujolang/eval/releases/tag/v1.1.0), [source and test instructions](https://github.com/kujolang/eval), and [agent accountability boundaries](/agent-accountability/). Run the documented checks in your own environment; release labels do not certify every provider, host or workload.
