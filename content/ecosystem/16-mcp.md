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
---

## What it does

A framework and scaffold for MCP servers with tools, resources, path guards, authentication, limits, safety tiers, and multi-root workspaces.

## Why it belongs in Kujo

A guarded gateway for exposing useful capabilities to agents through explicit contracts.

## Operating boundary

Generated servers still require review of tool authority, data access, authentication, and deployment boundaries.

## Ability integration

MCP projects explicitly enabled Kujo Abilities into host-discoverable tools without becoming the semantic source of truth. Read effects are the default; write, delete, and external effects require explicit exposure policy. The executable gateway requires a server-resolved principal and delegates policy, approval, idempotency, handler execution, and receipts to the canonical Ability runtime.

The portable host package supports Codex, Cursor, VS Code, and generic STDIO MCP clients. It connects to a local or HTTPS application gateway; the public `mcp.kujolang.ai` catalog stays read-only and separate from privileged execution.

[See the Ability contract and host architecture](/ecosystem/ability/).

## Learn more

The repository is the source of truth for current setup, commands, examples, security notes, compatibility, and verification evidence.
