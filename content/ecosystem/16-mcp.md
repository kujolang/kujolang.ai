---
title: "MCP"
custom_url: mcp
description: "A framework and scaffold for MCP servers with tools, resources, path guards, authentication, limits, safety tiers, and multi-root workspaces."
featured_image: "/assets/images/ecosystem/mcp-tool-connectors.webp"
section: "Primitives"
tags: [Primitive, Gateway]
order: 70
install_command: "git clone https://github.com/kujolang/mcp.git"
github_url: "https://github.com/kujolang/mcp"
launch_story: "A guarded gateway for exposing useful capabilities to agents through explicit contracts."
scope_note: "Generated servers still require review of tool authority, data access, authentication, and deployment boundaries."
keywords: "MCP, Kujo ecosystem, Primitive, Gateway"
seo_title: "MCP — Kujo Ecosystem"
last_updated: 2026-09-04
---

## What it does

Kujo MCP is a released framework and scaffold for MCP servers with tools, resources, path guards, authentication, limits, safety tiers, and multi-root workspaces. It also includes the portable Ability host package for projecting reviewed Ability contracts into MCP tools.

## Why it belongs in Kujo

A guarded gateway for exposing useful capabilities to agents through explicit contracts.

## Operating boundary

Generated servers still require review of tool authority, data access, authentication, and deployment boundaries.

## Ability integration

MCP projects explicitly enabled Kujo Abilities into host-discoverable tools without becoming the semantic source of truth. Read effects are the default; write, delete, and external effects require explicit exposure policy. The executable gateway requires a server-resolved principal and delegates policy, approval, idempotency, handler execution, and receipts to the canonical Ability runtime.

The portable host package targets Codex, Cursor, VS Code, and generic STDIO MCP clients. Its packaged bridge and configuration have been validated in the repository. VS Code completed the native localhost callback and PKCE exchange, restored its refreshable session after restart, discovered both managed tools, and invoked `gateway_echo` through the editor tool API without storing a bearer token in editor configuration. This is a managed read-only smoke certificate, not mutating or enterprise certification.

The bridge connects to a local or HTTPS application gateway. The Kujo Ability Gateway runs the controlled-beta Cloudflare Workers topology at [ability.kujolang.ai](https://ability.kujolang.ai) with OAuth authorization, GitHub organization identity, tenant-scoped discovery, separate human approval, atomic idempotency, receipts, audit, quotas, and membership-driven revocation. The public `mcp.kujolang.ai` catalog stays read-only and separate from privileged execution.

## Release boundary

The portable host artifact is reproducible, includes executable npm launchers plus SBOM and provenance metadata, and has completed repository package, Codex install, VS Code configuration, generic bridge, and managed VS Code read-only checks. The npm package remains unavailable until registry authentication is supplied; refresh/revocation, tenant isolation, approval replay, mutation, recovery, marketplace, signing, and enterprise certification remain separate gates. No token should be copied into editor configuration.

[See the Ability contract and host architecture](/ecosystem/ability/).

## Learn more

The [MCP repository](https://github.com/kujolang/mcp) is the source of truth for setup, commands, examples, security notes, compatibility, and verification evidence. The Ability Gateway repository owns the managed control-plane implementation and deployment checklist.

The Ability Gateway repository is private; public source access is not available.
