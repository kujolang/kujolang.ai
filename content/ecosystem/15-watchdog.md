---
title: "Watchdog"
custom_url: watchdog
description: "See what your AI apps use, what they cost, and where they fail."
featured_image: "/assets/images/ecosystem/watchdog-telemetry-alert.webp"
section: "Primitives"
tags: [Primitive, Observability]
order: 130
install_command: "kennel add watchdog"
github_url: "https://github.com/kujolang/watchdog"
launch_story: "Track model requests, tool calls, and agent steps in one local dashboard."
scope_note: "Your telemetry stays in a local SQLite database. Costs are estimates of direct API usage, not invoices."
keywords: "Watchdog, AI observability, token usage, API costs, local telemetry"
seo_title: "Watchdog — AI Usage and Cost Dashboard"
latest_release_url: "https://github.com/kujolang/watchdog/releases/latest"
last_updated: "2026-10-27"
---

## Know where your tokens go

Watchdog records model requests, tool calls, and agent steps. See request volume, token use, estimated costs, latency, and errors together. Filter by time, provider, project, or session, then open a request to inspect the details.

## See Watchdog in use

This demo shows 30 days of synthetic activity with more than 20 billion tokens. Busy stretches, quieter days, and occasional error spikes give the charts a realistic shape. Every total comes from the same sample records; no live account data appears here.

WATCHDOG_SCREENSHOT_GALLERY

## Connect your apps

Point an OpenAI-compatible client at Watchdog's `/proxy/v1` endpoint. Watchdog forwards requests to your provider and records their usage. Named upstream profiles let one server track several provider accounts.

Apps can also send telemetry directly through producer batches or supported OTLP traces. Connected Sources shows which apps and proxy profiles contribute data.

## Go from a spike to a request

Use the dashboard to spot a change in traffic or failures. Narrow the date range, filter the request list, and open a request or session to see what happened. Tool calls and agent steps add context to model activity.

Export records as JSONL or send supported telemetry through OTLP when you need it elsewhere. Runtime measurement references and RunLedger correlation help connect observations to recorded runs.

## Keep control of your data

Watchdog stores telemetry locally in SQLite and supports redaction, retention, and backups. Before exposing it beyond your machine, configure authentication, TLS, network access, and exporter credentials.

Estimated costs help compare usage; they are not provider bills. Recorded activity does not grant permission to retry an operation or prove that a business action succeeded.

Read the [setup guide](https://github.com/kujolang/watchdog#quick-start) to connect your first app, or check the [latest release](https://github.com/kujolang/watchdog/releases/latest) for changes.
