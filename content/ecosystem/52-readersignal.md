---
title: "ReaderSignal"
custom_url: readersignal
description: "A local-first measurement ledger for privacy-bounded audience snapshots, feedback, comparisons, and evidence-linked learning."
featured_image: "/assets/images/ecosystem/readersignal-measurement-console.webp"
section: "Tooling"
tags: [Tool, Publishing]
order: 520
install_command: "git clone --branch v0.3.0 https://github.com/kujolang/readersignal.git"
github_url: "https://github.com/kujolang/readersignal"
launch_story: "Capture bounded audience evidence and compare compatible measurements without turning metrics into editorial authority."
scope_note: "ReaderSignal 0.3.0 requires POSIX Kujo 1.5.0 at d501c2c46c51718ee10c4434f6cf9750bbd81453 or a compatible newer build; 1.5.0 alone does not identify the preview filesystem APIs. Provider access, identity, consent, interpretation, and consequential decisions remain external responsibilities."
keywords: "ReaderSignal, Kujo ecosystem, audience measurement, reader feedback, privacy-bounded analytics, publishing intelligence"
seo_title: "ReaderSignal — Kujo Ecosystem"
version: "0.3.0"
latest_release_url: "https://github.com/kujolang/readersignal/releases/tag/v0.3.0"
release_status: "Version identifies the latest published GitHub Release. Unpinned clone commands select default-branch source; see scope_note for release boundaries."
last_updated: "2026-09-26"
---

## What it does

ReaderSignal captures immutable audience-measurement snapshots, structured feedback, compatible comparisons, and evidence-linked learning records. It gives analysts, editors, and agents a local contract for describing what was measured without requiring a hosted analytics service or model key.

## Released in 0.3.0

Journal-backed crash recovery, read-only recovery diagnostics, exact-evidence backup and restore, and ordered directory durability barriers strengthen local persistence. Directory pages, record reads, query output, and compaction inputs have explicit bounds. Existing 0.1.0 and 0.2.0 records remain readable under contract 1.0.0.

Stop older writers and run `readersignal init --state PATH` before using an existing state directory. Recovery and restore support read-only previews. Successful sync depends on the filesystem and hardware honoring sync; ReaderSignal does not claim hostile-root isolation or distributed coordination.

See the [0.3.0 release](https://github.com/kujolang/readersignal/releases/tag/v0.3.0) and [ReaderSignal documentation](https://docs.kujolang.ai/tools/readersignal/) for commands and upgrade boundaries.

## Comparable evidence

Measurements preserve their scope, method, provenance, and time boundary. Comparisons reject incompatible inputs rather than presenting false trends, while bounded queries and explicit records keep interpretation traceable to the underlying evidence.

## Why it belongs in Kujo

Audience signals should inform editorial work without silently controlling it. ReaderSignal provides a narrow learning loop for the Publishing House while keeping privacy, consent, judgment, and strategy visible.

## Operating boundary

The tool records measurements and feedback; it does not identify readers, infer consent, promise statistical validity, or authorize editorial and commercial decisions. External capabilities fail honestly when no adapter is configured.

## Learn more

The repository documents the snapshot, feedback, comparison, export, security, and deterministic validation contracts.
