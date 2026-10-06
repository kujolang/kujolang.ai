---
title: "Kujo CMD"
custom_url: kujo-cmd
description: "A local-first bridge that installs Kujo Abilities, Agent Skills, scoped agents, approvals, receipts, and browser QA in Command Code."
featured_image: "/assets/images/ecosystem/mcp-tool-connectors.webp"
section: "Tooling"
tags: [Tool, Agents, MCP]
order: 190
install_command: "npx github:kujolang/kujo-cmd#v0.2.0 setup"
github_url: "https://github.com/kujolang/kujo-cmd"
launch_story: "Bring Kujo's reviewed tools into Command Code through one local MCP server without replacing either system's permission boundary."
scope_note: "Kujo CMD installs and projects local Kujo capabilities; it does not choose models, proxy provider traffic, or turn Command Code identity metadata into verified identity. Mutating and external effects still require Kujo approval and the host's separate permission check."
keywords: "Kujo CMD, Command Code integration, Kujo MCP tools, local agent tools, Command Code agents"
seo_title: "Kujo CMD 0.2.0 — Kujo Tools for Command Code"
seo_description: "Install 38 Kujo Abilities, seven scoped agents, approvals, receipts, correlation, and optional Lens browser QA in Command Code."
version: "0.2.0"
latest_release_url: "https://github.com/kujolang/kujo-cmd/releases/tag/v0.2.0"
release_status: "The GitHub release is published. npm publication is temporarily pending restored registry authorization, so the install command runs the same tagged package directly from GitHub."
last_updated: "2026-10-06"
---

## What it does

Kujo CMD connects Command Code to 25 pinned Kujo source projects through one
local STDIO MCP server. Release 0.2.0 exposes 38 portable Abilities, links the
canonical Agent Skills, projects seven task-scoped agents with explicit MCP
allowlists, and retains Kujo policy decisions and receipts around every call.

The GitHub release is live. npm publication is temporarily pending restoration
of the package's trusted-publisher or `NPM_TOKEN` authorization. The install
command above runs the tagged 0.2.0 package directly from GitHub in the interim.

Four profiles keep the visible surface manageable: Essentials exposes 5
read-mostly tools, Review exposes 18, Ship exposes 29, and Full exposes all 38.
Changing profiles is local and immediate after restarting Command Code.

## Integrated workflows

The catalog covers repository inspection, context packs, change review,
architecture checks, task contracts, evaluations, release readiness, durable
run evidence, drift detection, failure capture, privacy operations, decision
review, browser QA, showcase rendering, local retrieval, workflow execution,
and package management.

Lens flow validation works without a browser. Real-page checks use an explicit
`kujo-cmd browser install` step that installs Lens's pinned Chromium runtime.
Setup does not hide that networked dependency.

## Trust and evidence

Read-only Abilities run under local policy. Write, delete, or external effects
stop and return an input-bound, expiring, one-use Kujo approval request.
Command Code's own tool permission remains a separate outer check. Every call
returns structured MCP content and a durable local receipt.

The projected mod can correlate sessions, subagents, and Kujo tool calls with
loopback Watchdog using metadata only. It can optionally record RunLedger
start/finish events and applies a one-shot Jidoka continuation after a failed
Kujo tool call. Automatic RunLedger recording is off by default.

## Operating boundary

Kujo CMD does not choose or proxy the model. Caller-supplied session, run,
agent, and model identifiers aid correlation but are not verified Command Code
identity. The release is verified against Command Code 1.75.1.

## Learn more

- [Install and use Kujo CMD](https://docs.kujolang.ai/tools/kujo-cmd/)
- [Kujo CMD 0.2.0 release](https://github.com/kujolang/kujo-cmd/releases/tag/v0.2.0)
- [Kujo CMD repository](https://github.com/kujolang/kujo-cmd)
