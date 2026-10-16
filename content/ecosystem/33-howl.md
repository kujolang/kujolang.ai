---
title: "Howl"
custom_url: howl
description: "Deterministic Markdown, HTML, SVG, gallery, card, and caption assets generated from trusted Kujo examples and manifests."
featured_image: "/assets/images/ecosystem/howl-showcase-renderer.webp"
section: "Tooling"
tags: [Tool, Assets]
order: 300
install_command: "kennel tool install howl"
github_url: "https://github.com/kujolang/howl"
launch_story: "Turn verified examples into reusable launch and proof assets."
scope_note: "Howl renders source material; claims remain limited by the examples and evidence supplied to it."
keywords: "Howl, Kujo ecosystem, Tool, Assets"
seo_title: "Howl — Kujo Ecosystem"
version: "1.2.0"
latest_release_url: "https://github.com/kujolang/howl/releases/tag/v1.2.0"
release_status: "Version identifies the published release. The Kennel command selects the latest stable registry package; see scope_note for release boundaries."
last_updated: "2026-10-16"
---

## What it does

Deterministic Markdown, HTML, SVG, gallery, card, and caption assets generated from trusted Kujo examples and manifests.

## Why it belongs in Kujo

Turn verified examples into reusable launch and proof assets.

## Operating boundary

Howl renders source material; claims remain limited by the examples and evidence supplied to it.

## Howl 1.2.0

The 1.2.0 release adds atomic output replacement, contained input paths, early
rejection of non-regular manifests, and preflight checks that preserve examples
when forced initialization has an invalid destination. Identical renders keep
their mtimes. Metadata commands and SVG layouts skip unused content, and long
text wrapping stops after overflow is established.

Select an option-shaped card ID with `howl show -- --format`. Howl requires
Kujo 1.3.1 or newer; global installation uses Kennel 1.1.0 or newer with its
supported runtime. Use `kennel add howl@1.2.0` for a project dependency.

Writes are atomic per file, not a transaction across a gallery. Roots and their
ancestors must be trusted. Howl renders example text; it does not execute it,
validate its claims, or post to social platforms.

See the [Howl 1.2.0 release](https://github.com/kujolang/howl/releases/tag/v1.2.0)
and [Howl documentation](https://docs.kujolang.ai/tools/howl/).

## Learn more

The repository is the source of truth for current setup, commands, examples, security notes, compatibility, and verification evidence.
