---
title: "PressWire"
custom_url: presswire
description: "A local-first Kujo tool for approval-gated publication effects, receipts, corrections, and idempotent delivery."
featured_image: "/assets/images/ecosystem/presswire-publication-dispatch.webp"
section: "Tooling"
tags: [Tool, Publishing]
order: 510
install_command: "git clone https://github.com/kujolang/presswire.git"
github_url: "https://github.com/kujolang/presswire"
launch_story: "Preflight an exact approved package, perform a bounded publication effect, and retain an idempotent delivery receipt."
scope_note: "PressWire 0.1.0 performs only explicitly authorized publication effects; optional external destinations require configured adapters and valid approval scope."
keywords: "PressWire, Kujo ecosystem, approval-gated publishing, publication receipts, corrections, idempotent delivery"
seo_title: "PressWire — Kujo Ecosystem"
---

## What it does

PressWire is the Publishing House boundary for effects. It preflights an exact package and approval scope, performs bounded idempotent delivery, records receipts, and preserves corrections without conflating an attempted action with a successful external publication.

## Approval-gated delivery

Immutable records, append-only audit events, atomic writes, record locks, bounded inputs, structured errors, and exact checksum checks make repeated operations safe and inspectable. Local delivery is deterministic; external destinations are optional adapters.

## Why it belongs in Kujo

Most editorial tools should never publish. PressWire isolates that authority behind explicit approval and package verification so agents can prepare work without inheriting an ambient right to distribute it.

## Operating boundary

A receipt reports the effect PressWire could verify. It does not manufacture approval, widen its scope, guarantee third-party availability, or claim hosted multi-tenant coordination.

## Learn more

The repository documents the 0.1.0 preflight, publication, correction, receipt, export, security, and validation contracts.
