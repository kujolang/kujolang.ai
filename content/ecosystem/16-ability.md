---
title: "Ability"
custom_url: ability
description: "Portable, versioned operation contracts with typed schemas, declared effects, retry semantics, policy gates, approvals, idempotency, and canonical receipts."
featured_image: "/assets/images/ecosystem/ability-portable-operation-contracts.webp"
section: "Primitives"
tags: [Primitive, Contracts]
order: 65
install_command: "git clone https://github.com/kujolang/ability.git"
github_url: "https://github.com/kujolang/ability"
launch_story: "Define an operation once, then project the same meaning into applications, agents, and MCP hosts without moving authority into the contract."
scope_note: "Ability is a contract and runtime package, not a hosted gateway, global catalog, identity provider, permission system, or workflow engine."
keywords: "Kujo Ability, operation contracts, MCP tools, agent tools, typed schemas, policy gates, execution receipts"
seo_title: "Kujo Ability — Portable Operation Contracts"
version: "1.0.1"
last_updated: 2026-09-01
---

## What it does

Kujo Ability 1.0.1 gives an operation a stable identity, version, input and output schemas, declared effects, and retry semantics. Its runtime validates the exact definition and binding, evaluates application policy, enforces approval and idempotency requirements, invokes the application-owned handler, validates the result, and returns a canonical receipt.

The portable definition says what an operation means. The application still owns credentials, identity, authorization, storage, network access, handlers, and deployment policy.

## Why it belongs in Kujo

AI tools often expose the same operation through several surfaces: an application API, an agent runtime, a command line, or an MCP server. Ability keeps those projections anchored to one contract instead of letting every integration invent different inputs, effects, and safety claims.

## What ships in 1.0.1

- The stable `kujo.ability/v1` definition contract and JSON Schema
- Supporting binding, exposure, invocation, policy-decision, approval, and receipt contracts
- Deterministic definition digests and exact-version registry resolution
- A fail-closed execution pipeline for policy, approval, idempotency, audit, handler execution, output validation, and receipts
- Conformance guidance for products and adapters
- A documentation example used as a fixture, not a production operation catalog

Ability recognizes read, write, delete, and external effects. Idempotency can be intrinsic, keyed, or explicitly unavailable.

## Where it works today

Kujo CMS defines six production-domain Abilities for site inspection, content listing, SEO auditing, SEO entry updates, bulk SEO updates, and AI-integration inspection. CMS binds those definitions to its own handlers, permissions, tenant identity, request-bound approvals, idempotency records, and audit trail.

Kujo Agents SDK can project a canonical Ability into its native Tool registry for either local handlers or server-owned gateway execution. Kujo MCP can project explicitly enabled Abilities into MCP tools and includes a portable STDIO host package for Codex, Cursor, VS Code, and generic MCP clients.

These hosts do not receive different Ability semantics. Host packages provide installation, discovery, prompts, and approval UX while the application gateway remains the authority.

## Local, hosted, and customer-hosted use

For local use, an MCP host can start the Kujo Ability STDIO bridge and connect it to a loopback CMS or another compatible application gateway. For a managed or customer-hosted deployment, the same bridge can connect over HTTPS through OAuth authorization.

The source-available [Kujo Ability Gateway](https://github.com/kujolang/ability-gateway) now runs the controlled-beta remote topology at [ability.kujolang.ai](https://ability.kujolang.ai): OAuth 2.1 with PKCE and audience binding, GitHub organization identity, tenant-scoped discovery, durable approval and receipt state, atomic idempotency, quotas, retention, and signed membership-removal revocation. A VS Code 1.136 editor smoke certificate covers authenticated discovery and `gateway_echo`. Access remains controlled while refresh/revocation drills, representative Free-plan CPU measurements, and public-release approvals are completed.

The public `mcp.kujolang.ai` endpoint remains a read-only ecosystem catalog. It should not hold customer credentials or become the privileged Ability execution plane.

## CMS and SSG

CMS is the current reference producer because it has authenticated users, durable state, approvals, and domain handlers. SSG can use Ability for build inspection, validation, and publishing operations, but static browser-facing WebMCP should remain read-only. Any build, file-write, network, or deploy Ability belongs behind a trusted local or authenticated server execution boundary.

## Operating boundary

An Ability definition never grants permission. Production deployments must authenticate the principal before discovery, authorize every invocation server-side, keep secrets out of definitions and receipts, bind one-time approvals to the exact invocation, scope idempotency by tenant and operation, enforce hard timeouts and cancellation at the handler boundary, and retain redacted audit evidence.

## Release

Ability 1.0.1 is the current release. Install it through Kennel from the reviewed [`v1.0.1` release](https://github.com/kujolang/ability/releases/tag/v1.0.1), and keep the generated lockfile in source control.

## Learn more

The [Ability repository](https://github.com/kujolang/ability) is the source of truth for the contract, runtime, compatibility policy, production-readiness guidance, tests, and release notes. The [Kujo MCP repository](https://github.com/kujolang/mcp) contains the executable projection and portable agent-host package. The [Ability Gateway repository](https://github.com/kujolang/ability-gateway) owns the managed controlled-beta service implementation.
