---
title: "Agents SDK"
custom_url: agents-sdk
description: "Agent runners, tools, approvals, handoffs, tracing, sessions, memory, retrieval, artifact stores, budgets, and offline fixtures."
featured_image: "/assets/images/ecosystem/agents-sdk-human-handoff.webp"
section: "Primitives"
tags: [Primitive, Agents]
order: 100
install_command: "kennel add agents-sdk@1.1.3"
github_url: "https://github.com/kujolang/agents-sdk"
launch_story: "Build local agents with explicit tools, approvals, state, and run evidence."
scope_note: "Version 1.1.3 hardens approvals, state recovery, storage, retries, and token accounting while preserving public contracts. Use Kujo 1.6.0+ and Kennel 1.1.0+. Controlled Ability handoffs remain experimental; the host owns provider permissions and cost governance."
keywords: "Agents SDK, Kujo ecosystem, Primitive, Agents"
seo_title: "Agents SDK — Kujo Ecosystem"
version: "1.1.3"
latest_release_url: "https://github.com/kujolang/agents-sdk/releases/tag/v1.1.3"
release_status: "Version identifies the published release. The Kennel command selects the latest stable registry package; see scope_note for release boundaries."
last_updated: "2026-10-13"
---

## What it does

Agent runners, tools, approvals, handoffs, tracing, sessions, memory, retrieval, artifact stores, budgets, and offline fixtures.

## Why it belongs in Kujo

Build local agents with explicit tools, approvals, state, and run evidence.

## Operating boundary

Version 1.1.3 hardens approvals, state recovery, storage, retries, and token accounting while preserving public contracts. Use Kujo 1.6.0+ and Kennel 1.1.0+. Controlled Ability handoffs remain experimental; the host owns provider permissions and cost governance.

## Version 1.1.3

This patch preserves source text in retrieval and tool artifacts, prevents automatic
storage IDs from replacing records, and counts reported tokens from failed model
attempts. Memory, artifact, and trace queries materialize only the requested page.
Retries no longer consume another call frame per attempt.

```bash
kennel add agents-sdk@1.1.3
kennel install
```

The pinned Ability 1.0.1 dependency requires Git and GitHub access. Offline examples
need no provider credentials. Verification covers 277 contract cases, 42 fixtures,
and the context regression gates. See the [release notes](https://github.com/kujolang/agents-sdk/releases/tag/v1.1.3)
and [setup guide](https://docs.kujolang.ai/tools/agents-sdk/).

Token budgets include reported usage from every attempt. Timeouts and cancellation
remain cooperative; callbacks enforce per-attempt limits. Cent-denominated cost
telemetry is not automatically converted to the generic cost-budget unit, so
monetary limits belong in the host/provider layer.

## Ability integration

Agents SDK projects a validated `kujo.ability/v1` definition into its native Tool registry. A tool can call a local application-owned handler or delegate execution to an authenticated gateway while preserving the Ability ID, version, definition digest, schemas, effects, and canonical receipt. The SDK supplies agent runtime behavior; the application still owns identity, policy, approvals, idempotency, credentials, and durable audit storage.

[Learn how Kujo Ability keeps one operation contract consistent across agent and MCP surfaces](/ecosystem/ability/).

## Learn more

The repository is the source of truth for current setup, commands, examples, security notes, compatibility, and verification evidence.
