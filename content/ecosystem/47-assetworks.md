---
title: "AssetWorks"
custom_url: assetworks
description: "A local-first media production ledger for asset planning, immutable provenance, accessibility artifacts, and checksum-backed validation."
featured_image: "/assets/images/ecosystem/assetworks-media-provenance.webp"
section: "Tooling"
tags: [Tool, Publishing]
order: 470
install_command: "git clone https://github.com/kujolang/assetworks.git"
github_url: "https://github.com/kujolang/assetworks"
launch_story: "Plan publication assets, preserve their lineage, and validate accessible production deliverables against exact checksums."
scope_note: "AssetWorks 0.1.0 is a local-first evidence system; hosted identity, distributed coordination, and external media services require operator-provided adapters."
keywords: "AssetWorks, Kujo ecosystem, publishing assets, media provenance, accessibility artifacts, checksum validation"
seo_title: "AssetWorks — Kujo Ecosystem"
---

## What it does

AssetWorks gives publishing teams a durable place to plan media assets, record immutable provenance, attach accessibility artifacts, and detect file drift with exact checksums. Its structured JSON contracts support editorial operators, agents, and CI without requiring a hosted service, database, or model key.

## Production evidence

Records and audit events are immutable, writes are atomic and lock-protected, and inputs, files, and queries are bounded. Validation rejects traversal, symlinks, secret-shaped fields, incompatible schemas, duplicate identifiers, unsafe overwrites, and checksum drift.

## Why it belongs in Kujo

AssetWorks turns visual production from a mutable folder of deliverables into inspectable evidence. It gives the Publishing House team a clear boundary between planning, provenance, accessibility work, and the external systems that ultimately create or distribute media.

## Operating boundary

Core workflows are local and deterministic. Optional integrations must be configured explicitly, and a stored record does not claim hosted identity, distributed coordination, or authority outside the recorded asset scope.

## Learn more

The repository documents the 0.1.0 commands, public schemas, deterministic fixtures, security model, and complete validation gate.
