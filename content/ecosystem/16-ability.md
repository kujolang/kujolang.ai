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
last_updated: 2026-09-04
---

## What it does

Kujo Ability gives an operation a stable identity, version, input and output schemas, declared effects, and retry semantics. Its runtime validates the exact definition and binding, evaluates application policy, enforces approval and idempotency requirements, invokes the application-owned handler, validates the result, and returns a canonical receipt.

The portable definition says what an operation means. The application still owns credentials, identity, authorization, storage, network access, handlers, and deployment policy.

## Why it belongs in Kujo

AI tools often expose the same operation through several surfaces: an application API, an agent runtime, a command line, or an MCP server. Ability keeps those projections anchored to one contract instead of letting every integration invent different inputs, effects, and safety claims.

## What it includes

- The stable Ability definition contract and JSON Schema
- Supporting binding, exposure, invocation, policy-decision, approval, and receipt contracts
- Deterministic definition digests and exact-version registry resolution
- A fail-closed execution pipeline for policy, approval, idempotency, audit, handler execution, output validation, and receipts
- Local TypeScript and Python SDK previews for shared definition digests, receipt checks, and effect review
- Offline verification of signed packs, checksums, publisher trust, revocation, compatibility, and tenant visibility
- A fixture development kit for definition checks, reference docs, approval simulation, keyed replay, and receipt inspection
- Conformance guidance for products and adapters
- A documentation example used as a fixture, not a production operation catalog

Ability recognizes read, write, delete, and external effects. Idempotency can be intrinsic, keyed, or explicitly unavailable.

## Where it works today

Kujo CMS defines six production-domain Abilities for site inspection, content listing, SEO auditing, SEO entry updates, bulk SEO updates, and AI-integration inspection. CMS binds those definitions to its own handlers, permissions, tenant identity, request-bound approvals, idempotency records, and audit trail.

Kujo Agents SDK can project a canonical Ability into its native Tool registry for either local handlers or server-owned gateway execution. Kujo MCP can project explicitly enabled Abilities into MCP tools and includes a portable STDIO host package for Codex, Cursor, VS Code, and generic MCP clients.

These hosts do not receive different Ability semantics. Host packages provide installation, discovery, prompts, and approval UX while the application gateway remains the authority.

## Local, hosted, and customer-hosted use

For local use, an MCP host can start the Kujo Ability STDIO bridge and connect it to a loopback CMS or another compatible application gateway. For a managed or customer-hosted deployment, the same bridge can connect over HTTPS through OAuth authorization.

The Kujo Ability Gateway runs a controlled beta at [ability.kujolang.ai](https://ability.kujolang.ai). It supplies authenticated discovery and an application execution boundary. Access remains controlled; the gateway repository is private.

The public `mcp.kujolang.ai` endpoint remains a read-only ecosystem catalog. It should not hold customer credentials or become the privileged Ability execution plane.

## CMS and SSG

CMS is the current reference producer because it has authenticated users, durable state, approvals, and domain handlers. SSG publishes inspect, validate, and approval-gated build definitions. Static browser-facing WebMCP remains read-only. Any build, file-write, network, or deploy Ability belongs behind a trusted local or authenticated server execution boundary.

## Operating boundary

An Ability definition never grants permission. Production deployments must authenticate the principal before discovery, authorize every invocation server-side, keep secrets out of definitions and receipts, bind one-time approvals to the exact invocation, scope idempotency by tenant and operation, enforce hard timeouts and cancellation at the handler boundary, and retain redacted audit evidence.

## Try an operation locally

Use the fixture development kit to validate a definition, generate its reference docs, and test approval and retry behavior before connecting an application. The local server uses bounded fixture outputs and requires authentication. Production execution belongs in the canonical runtime or an application gateway.

The TypeScript and Python helpers are local previews. The offline pack verifier checks package trust; it does not operate a registry or grant permission to run an operation.

[Read the Ability guide](https://docs.kujolang.ai/tools/ability/) for installation, digest compatibility, and development-kit commands. Choose a reviewed [release](https://github.com/kujolang/ability/releases/latest) and keep the generated Kennel lockfile in source control.

## Learn more

The [Ability repository](https://github.com/kujolang/ability) is the source of truth for the contract, runtime, compatibility policy, production-readiness guidance, tests, and release notes. The [Kujo MCP repository](https://github.com/kujolang/mcp) contains the executable projection and portable agent-host package. The separately operated Ability Gateway owns the controlled beta service.
