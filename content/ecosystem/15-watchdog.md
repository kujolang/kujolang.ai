---
title: "Watchdog"
custom_url: watchdog
description: "An OpenAI-compatible proxy and dashboard for request, tool, step, audit, cost, latency, error, and redaction telemetry."
featured_image: "/assets/images/ecosystem/watchdog-telemetry-alert.webp"
section: "Primitives"
tags: [Primitive, Observability]
order: 130
install_command: "kennel add watchdog"
github_url: "https://github.com/kujolang/watchdog"
launch_story: "Make AI application behavior observable without hiding the request path from the operator."
scope_note: "Watchdog 1.2.0 adds verified Kujo 1.6 runtime measurement references and RunLedger correlation to its existing telemetry and Connected Sources panel. Direct-provider cost estimates are not invoices; auth, retention, exporter credentials, and deployment remain operator-owned."
keywords: "Watchdog, Kujo ecosystem, Primitive, Observability"
seo_title: "Watchdog — Kujo Ecosystem"
version: "1.2.0"
latest_release_url: "https://github.com/kujolang/watchdog/releases/tag/v1.2.0"
release_status: "Version identifies the published release. The Kennel command selects the latest stable registry package; see scope_note for release boundaries."
last_updated: "2026-09-29"
---

## What it does

An OpenAI-compatible proxy and dashboard for request, tool, step, audit, cost, latency, error, and redaction telemetry.

## Why it belongs in Kujo

Make AI application behavior observable without hiding the request path from the operator.

## Operating boundary

[Watchdog 1.2.0](https://github.com/kujolang/watchdog/releases/tag/v1.2.0) adds bounded, verified Kujo 1.6 runtime measurements and exact artifact references to execution observations, with RunLedger correlation through HTTP intake and restart. It retains canonical v2 telemetry, lossless JSONL/OTLP projections, and an authenticated Connected Sources panel for exact evidence-backed inbound producer inventory and safe named proxy-profile management. Named profile changes apply to new requests without restarting Watchdog, while disabled and deleted profiles fail closed before upstream egress. Direct-provider cost estimates are not invoices; auth, retention, exporter credentials, and deployment remain operator-owned.

Runtime measurements stay content-light and observational: they do not authorize retries, prove business effects, or change billing truth. Use Kujo 1.6.0 for this release.

## Learn more

The repository is the source of truth for current setup, commands, examples, security notes, compatibility, and verification evidence.
