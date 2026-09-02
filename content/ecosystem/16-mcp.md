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
version: "1.1.0"
last_updated: 2026-09-02
---

## What it does

Kujo MCP 1.1.0 is a framework and scaffold for MCP servers with tools, resources, path guards, authentication, limits, safety tiers, and multi-root workspaces. Version 1.1.0 also includes the local, unpublished Ability host preview for projecting reviewed Ability contracts into MCP tools.

## Why it belongs in Kujo

A guarded gateway for exposing useful capabilities to agents through explicit contracts.

## Operating boundary

Generated servers still require review of tool authority, data access, authentication, and deployment boundaries.

## Ability integration

MCP projects explicitly enabled Kujo Abilities into host-discoverable tools without becoming the semantic source of truth. Read effects are the default; write, delete, and external effects require explicit exposure policy. The executable gateway requires a server-resolved principal and delegates policy, approval, idempotency, handler execution, and receipts to the canonical Ability runtime.

The portable host package targets Codex, Cursor, VS Code, and generic STDIO MCP clients. Its packaged bridge and configuration have been validated in the repository. An installed VS Code 1.135 CLI accepted and persisted the server configuration in an isolated profile without storing a credential; authenticated end-to-end execution remains a live-gateway release gate, so this is configuration evidence rather than a completed editor certification.

The bridge connects to a local or HTTPS application gateway. The source-available [Kujo Ability Gateway](https://github.com/kujolang/ability-gateway) implements the controlled-beta Cloudflare Workers topology with OAuth 2.1, GitHub organization identity, tenant-scoped discovery, separate human approval, atomic idempotency, receipts, audit, quotas, and membership-driven revocation. It is not yet a live service. The public `mcp.kujolang.ai` catalog stays read-only and separate from privileged execution.

## 1.1.0 release boundary

The repository version is 1.1.0, but the Ability host artifact remains a local unpublished preview until the managed gateway is deployed and the authenticated VS Code flow, revocation, tenant isolation, approval replay, and free-tier CPU gates pass. No token should be copied into editor configuration.

[See the Ability contract and host architecture](/ecosystem/ability/).

## Learn more

The [MCP repository](https://github.com/kujolang/mcp) is the source of truth for setup, commands, examples, security notes, compatibility, and verification evidence. The [Ability Gateway repository](https://github.com/kujolang/ability-gateway) owns the managed control-plane implementation and deployment checklist.
