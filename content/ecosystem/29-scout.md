---
title: "Scout"
custom_url: scout
description: "Local repository intelligence with bounded scanning, route and dependency discovery, security exports, agent context packs, and deterministic CI contracts."
featured_image: "/assets/images/ecosystem/scout-codebase-map.webp"
section: "Primitives"
tags: [Primitive, Intelligence]
order: 50
install_command: "git clone --depth 1 --branch v1.1.0 https://github.com/kujolang/scout.git"
github_url: "https://github.com/kujolang/scout"
launch_story: "Shorten codebase orientation without turning discovery into an opaque hosted index."
scope_note: "Scout accelerates onboarding; project-specific architecture and security judgment still matter."
keywords: "Scout, Kujo ecosystem, Tool, Intelligence"
seo_title: "Scout — Kujo Ecosystem"
version: "1.1.0"
latest_release_url: "https://github.com/kujolang/scout/releases/tag/v1.1.0"
release_status: "Version and pinned clone command identify the latest published GitHub Release; see scope_note for the product boundary."
last_updated: "2026-09-26"
---

## What it does

Scout 1.1.0 turns a local repository into a reviewable context pack: file trees,
language metrics, dependency and route discovery, security signals, `llms.txt`,
agent guidance, checklists, JSON intelligence, manifests, and optional SARIF/JSONL
and Kennel-compatible artifacts.

## What changed in 1.1.0

- Rooted, bounded source and metadata reads plus fail-closed aggregate resource ceilings.
- Stable `SCOUT-LIMIT-*` identifiers for CI consumers and strict partial-scan handling.
- Deterministic performance gates and exact-match corpus metrics across 18 route and
  10 dependency-manifest families.
- Native Windows route, security-export, and artifact contract verification.

Scout 1.1.0 requires Kujo 1.5.0 or newer.

## Why it belongs in Kujo

Shorten codebase orientation without turning discovery into an opaque hosted index.

## Operating boundary

Scout accelerates onboarding; project-specific architecture and security judgment still matter.

## Learn more

The repository is the source of truth for current setup, commands, examples, security notes, compatibility, and verification evidence.
