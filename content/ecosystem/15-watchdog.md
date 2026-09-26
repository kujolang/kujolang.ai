---
title: "Watchdog"
custom_url: watchdog
description: "An OpenAI-compatible proxy and dashboard for request, tool, step, audit, cost, latency, error, and redaction telemetry."
featured_image: "/assets/images/ecosystem/watchdog-telemetry-alert.webp"
section: "Primitives"
tags: [Primitive, Observability]
order: 130
install_command: "git clone https://github.com/kujolang/watchdog.git"
github_url: "https://github.com/kujolang/watchdog"
launch_story: "Make AI application behavior observable without hiding the request path from the operator."
scope_note: "Watchdog 1.1.0 adds canonical v2 telemetry, lossless JSONL/OTLP projections, and the evidence-backed Connected Sources panel. Direct-provider cost estimates are not invoices; auth, retention, exporter credentials, and deployment remain operator-owned."
keywords: "Watchdog, Kujo ecosystem, Primitive, Observability"
seo_title: "Watchdog — Kujo Ecosystem"
version: "1.1.0"
latest_release_url: "https://github.com/kujolang/watchdog/releases/tag/v1.1.0"
release_status: "Version identifies the latest published GitHub Release. Unpinned clone commands select default-branch source; see scope_note for release boundaries."
last_updated: "2026-09-26"
---

## What it does

An OpenAI-compatible proxy and dashboard for request, tool, step, audit, cost, latency, error, and redaction telemetry.

## Why it belongs in Kujo

Make AI application behavior observable without hiding the request path from the operator.

## Operating boundary

[Watchdog 1.1.0](https://github.com/kujolang/watchdog/releases/tag/v1.1.0) adds canonical v2 telemetry, lossless JSONL/OTLP projections, and an authenticated Connected Sources panel for exact evidence-backed inbound producer inventory and safe named proxy-profile management. Named profile changes apply to new requests without restarting Watchdog, while disabled and deleted profiles fail closed before upstream egress. Direct-provider cost estimates are not invoices; auth, retention, exporter credentials, and deployment remain operator-owned.

## Learn more

The repository is the source of truth for current setup, commands, examples, security notes, compatibility, and verification evidence.
