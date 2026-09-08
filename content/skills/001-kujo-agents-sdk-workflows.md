---
title: "Agents SDK"
custom_url: "kujo-agents-sdk-workflows"
description: "Use this skill when working on Kujo Agents SDK runtime primitives, examples, offline fixtures, agent runners, tools, portable Ability projection/gateway tools, approvals, handoffs, tracing, Watchdog telemetry, artifact/session/memory stores, retrieval providers, integration adapters, MCP 2026 helpers, budget limits, no-network harnesses, or `agents-sdk` source/test changes."
excerpt: "Use this skill when working on Kujo Agents SDK runtime primitives, examples, offline fixtures, agent runners, tools, portable Ability projection/gateway tools, approvals, handoffs, tracing,…"
featured_image: "/assets/images/ecosystem/skill-kujo-agents-sdk-workflows.webp"
social_image: "/assets/images/social/kujo-agents-sdk-workflows.jpg"
section: "Agent Skill"
order: "10"
install_command: "git clone --branch v0.7.0 --depth 1 https://github.com/kujolang/kujo-skills.git && mkdir -p ~/.codex/skills && cp -R kujo-skills/skills/kujo-agents-sdk-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/v0.7.0/skills/kujo-agents-sdk-workflows/SKILL.md"
launch_story: "One of 135 focused, repository-backed skills in the Kujo Skills 0.7.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.7.0"
last_updated: "2026-09-08"
keywords: "Agents SDK, Kujo Agent Skill, kujo-agents-sdk-workflows, repository-backed agent guidance"
seo_title: "Agents SDK — Kujo Agent Skill"
seo_description: "Use this skill when working on Kujo Agents SDK runtime primitives, examples, offline fixtures, agent runners, tools, portable Ability projection/gateway tools, approvals, handoffs, tracing, Watchdog telemetry, artifact/session/memory stores, retrieval providers, integration adapters, MCP 2026 helpers, budget limits, no-network harnesses, or `agents-sdk` source/test changes."
---

## What it covers

Use this skill when working on Kujo Agents SDK runtime primitives, examples, offline fixtures, agent runners, tools, portable Ability projection/gateway tools, approvals, handoffs, tracing, Watchdog telemetry, artifact/session/memory stores, retrieval providers, integration adapters, MCP 2026 helpers, budget limits, no-network harnesses, or `agents-sdk` source/test changes.

Run the install command from a new working directory. If you already have the released checkout, copy the complete skill folder from it instead of cloning again.

## Released guidance

- `examples/*_agent.kujo` are canonical runnable examples; `examples/examples_smoke_runner.kujo` is the offline aggregate smoke path.
- Offline fixture behavior and no-network boundaries are part of the public contract.
- Integration adapters live behind `src/agents/integrations/adapters.kujo`; MCP `2026-07-28` support is limited to stateless JSON-RPC request helpers, required per-request `_meta`, Streamable HTTP routing headers, tool-list cache metadata, input-required result normalization, unsupported-version errors, and lossless tool schema/display metadata mapping into registry contracts.
- Portable Ability projection lives in `src/agents/abilities/contract.kujo`. The SDK validates canonical `kujo.ability/v1` definitions from the commit-pinned Ability package, maps exposed abilities into Tool contracts, and preserves canonical identity/digest metadata without owning application bindings, permissions, approvals, or handler policy.
- Server-owned Ability execution uses `register_ability_gateway_tool` with a narrow transport callback. The gateway remains responsible for authentication and principal/tenant resolution; returned canonical receipts are validated and kept as tool execution evidence.

## Release boundary

This page reflects the 0.7.0 technical preview on 2026-09-08. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-agents-sdk-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/v0.7.0/skills/kujo-agents-sdk-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/v0.7.0/SKILLS_INDEX.md)
