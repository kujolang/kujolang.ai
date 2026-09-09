---
title: "Agents SDK"
custom_url: agents-sdk
description: "Agent runners, tools, approvals, handoffs, tracing, sessions, memory, retrieval, artifact stores, budgets, and offline fixtures."
featured_image: "/assets/images/ecosystem/agents-sdk-human-handoff.webp"
section: "Primitives"
tags: [Primitive, Agents]
order: 100
install_command: "git clone https://github.com/kujolang/agents-sdk.git"
github_url: "https://github.com/kujolang/agents-sdk"
launch_story: "Composable local-first runtime primitives for building inspectable agents."
scope_note: "The 1.0.0 release provides library-first agent primitives. Newer default-branch work adds bounded lifecycle observations, retrieval preferences, and real MCP tool examples; these are not retroactively in the release archive."
keywords: "Agents SDK, Kujo ecosystem, Primitive, Agents"
seo_title: "Agents SDK — Kujo Ecosystem"
version: "1.0.0"
latest_release_url: "https://github.com/kujolang/agents-sdk/releases/tag/v1.0.0"
release_status: "published GitHub Release; see scope_note for newer source work"
last_updated: "2026-09-09"
---

## What it does

Agent runners, tools, approvals, handoffs, tracing, sessions, memory, retrieval, artifact stores, budgets, and offline fixtures.

## Why it belongs in Kujo

Composable local-first runtime primitives for building inspectable agents.

## Operating boundary

The 1.0.0 release provides library-first agent primitives. Newer default-branch work adds bounded lifecycle observations, retrieval preferences, and real MCP tool examples; these are not retroactively in the release archive.

## Ability integration

Agents SDK projects a validated `kujo.ability/v1` definition into its native Tool registry. A tool can call a local application-owned handler or delegate execution to an authenticated gateway while preserving the Ability ID, version, definition digest, schemas, effects, and canonical receipt. The SDK supplies agent runtime behavior; the application still owns identity, policy, approvals, idempotency, credentials, and durable audit storage.

[Learn how Kujo Ability keeps one operation contract consistent across agent and MCP surfaces](/ecosystem/ability/).

## Learn more

The repository is the source of truth for current setup, commands, examples, security notes, compatibility, and verification evidence.
