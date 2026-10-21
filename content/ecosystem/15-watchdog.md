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
scope_note: "Watchdog 1.2.2 hardens credentials, telemetry validation, OTLP retries and queue limits, reduces intake and client work, and refreshes pricing. Runtime observations do not authorize replay. Cost estimates are not invoices; auth, retention and deployment remain operator-owned."
keywords: "Watchdog, Kujo ecosystem, Primitive, Observability"
seo_title: "Watchdog — Kujo Ecosystem"
version: "1.2.2"
latest_release_url: "https://github.com/kujolang/watchdog/releases/tag/v1.2.2"
release_status: "Version identifies the published release. The Kennel command selects the latest stable registry package; see scope_note for release boundaries."
last_updated: "2026-10-21"
---

## What it does

An OpenAI-compatible proxy and dashboard for request, tool, step, audit, cost, latency, error, and redaction telemetry.

## Why it belongs in Kujo

Make AI application behavior observable without hiding the request path from the operator.

## Operating boundary

[Watchdog 1.2.2](https://github.com/kujolang/watchdog/releases/tag/v1.2.2) keeps gateway credentials out of provider requests, validates and redacts canonical metadata, fixes OTLP retries, and enforces queue limits. It reduces canonical intake work, JavaScript client cloning and backup memory use, and refreshes provider pricing.

It retains canonical v2 telemetry, JSONL/OTLP exports, runtime measurement references, RunLedger correlation and Connected Sources. Existing routes and schema versions remain compatible. Invalid telemetry returns errors; changed records with the same OTLP identity return 409.

Use Kujo 1.6.0 or newer. Runtime measurements do not authorize retries or prove business effects. Cost estimates are not invoices. Configure authentication, retention, exporter credentials and deployment controls for your environment; per-session rate limits do not establish a trusted caller identity.

## Learn more

The repository is the source of truth for current setup, commands, examples, security notes, compatibility, and verification evidence.
