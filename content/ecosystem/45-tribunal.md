---
title: "Tribunal"
custom_url: tribunal
description: "A local-first decision review engine that turns consequential proposals into adversarial hearings and durable, execution-ready decision evidence."
featured_image: "/assets/images/ecosystem/tribunal-adversarial-hearing.webp"
section: "Showcase"
tags: [Showcase, Decisions]
order: 450
install_command: "git clone https://github.com/kujolang/tribunal.git"
github_url: "https://github.com/kujolang/tribunal"
launch_story: "Replace a disposable model answer with independent testimony, cross-examination, a fatal-flaw pass, an explicit ruling, and a sealed decision packet."
scope_note: "Tribunal 1.0 is stable for local or operator-controlled decision evidence; shared, regulated, or hosted deployments require environment-specific identity, custody, storage, network, and independent security certification."
keywords: "Tribunal, Kujo ecosystem, decision review, adversarial hearing, sealed evidence"
seo_title: "Tribunal — Kujo Ecosystem"
---

## What it does

Tribunal 1.0 runs a consequential proposal through a structured nine-stage hearing: docket opening, scope validation, context construction, blind specialist testimony, cross-examination, an Executioner fatal-flaw pass, a Judge ruling, a decision packet, and durable persistence. Focused, two-model, and five-seat panels support different review depths, while deterministic mock mode remains offline and credential-free.

## Durable decision evidence

Every completed or stopped run produces human-readable and machine-readable evidence, including prompts, testimony, cross-examination, the ruling, a receipt, an event log, and a byte-accurate SHA-256 artifact manifest. Runs are replayable, optionally RSA-signed, portable as verified bundles, and designed for idempotent handoff to RunLedger or CaseFile.

## Why it belongs in Kujo

Tribunal is a complete Kujo-native application that combines orchestration, schemas, cryptography, process isolation, filesystem safety, testing, and release evidence. The hearing remains inspectable from source through ruling instead of hiding consequential judgment inside a single provider response.

## Operating boundary

The v1 contract covers documented local CLI, library API, configuration, evidence, inspection, and bundle behavior on verified platforms. It does not provide a public hosted service or automatically certify managed identity, signing custody, remote storage, tenancy, regulated deployment, live-provider behavior, backup, recovery, or organizational approval.

## Learn more

The repository contains installation and rollback guidance, panel and seat contracts, example decision galleries, enterprise controls, threat modeling, platform receipts, library APIs, schema definitions, operations recipes, compatibility guarantees, and release verification evidence.
