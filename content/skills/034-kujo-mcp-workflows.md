---
title: "Kujo MCP"
custom_url: "kujo-mcp-workflows"
description: "Use this skill when generating, running, validating, deploying, packaging, or maintaining Kujo MCP servers and repo-specific MCP/Ability scaffolds: `mcp make`, `kujo run mcp.kujo --interpreter make`, `mcp-server.json`, MCP tool/resource registries, generated `.mcp/` outputs, `mcp.manifest.json`, repo profiles, MCP safety tiers, Ability projection/gateway/host packages, Watchdog lifecycle metadata, auth/host/request guardrails, endpoint tests, or MCP source/test changes."
excerpt: "Use this skill when generating, running, validating, deploying, packaging, or maintaining Kujo MCP servers and repo-specific MCP/Ability scaffolds."
featured_image: "/assets/images/ecosystem/skill-kujo-mcp-workflows.webp"
social_image: "/assets/images/social/kujo-mcp-workflows.jpg"
section: "Agent Skill"
order: "340"
install_command: "git clone --branch v0.7.0 --depth 1 https://github.com/kujolang/kujo-skills.git && mkdir -p ~/.codex/skills && cp -R kujo-skills/skills/kujo-mcp-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/v0.7.0/skills/kujo-mcp-workflows/SKILL.md"
launch_story: "One of 135 focused, repository-backed skills in the Kujo Skills 0.7.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.7.0"
last_updated: "2026-09-08"
keywords: "Kujo MCP, Kujo Agent Skill, kujo-mcp-workflows, repository-backed agent guidance"
seo_title: "Kujo MCP — Kujo Agent Skill"
seo_description: "Use this skill when generating, running, validating, deploying, packaging, or maintaining Kujo MCP servers and repo-specific MCP/Ability scaffolds: `mcp make`, `kujo run mcp.kujo --interpreter make`, `mcp-server.json`, MCP tool/resource registries, generated `.mcp/` outputs, `mcp.manifest.json`, repo profiles, MCP safety tiers, Ability projection/gateway/host packages, Watchdog lifecycle metadata, auth/host/request guardrails, endpoint tests, or MCP source/test changes."
---

## What it covers

Use this skill when generating, running, validating, deploying, packaging, or maintaining Kujo MCP servers and repo-specific MCP/Ability scaffolds: `mcp make`, `kujo run mcp.kujo --interpreter make`, `mcp-server.json`, MCP tool/resource registries, generated `.mcp/` outputs, `mcp.manifest.json`, repo profiles, MCP safety tiers, Ability projection/gateway/host packages, Watchdog lifecycle metadata, auth/host/request guardrails, endpoint tests, or MCP source/test changes.

Run the install command from a new working directory. If you already have the released checkout, copy the complete skill folder from it instead of cloning again.

## Released guidance

- Classify the request first: local demo server, generated repo server, framework/source change, Ability projection/gateway/host package work, Watchdog metadata integration, generated artifact review, or deployment hardening.
- Prefer the current reliable invocation for generation: `kujo run mcp.kujo --interpreter make <repo-path>`. The intended future `kujo mcp make <repo-path>` shape is not the dependable path yet.
- Treat generated `.mcp/` outputs as reviewable scaffolds, not magic truth. Inspect `repo-profile.json`, `mcp.manifest.json`, and `artifacts/safety-review.md` before recommending exposure.
- Keep MCP server capabilities least-privilege: read-only tools and allowlisted safe commands by default; review-required and blocked capabilities stay disabled unless explicitly justified.
- Ability projection is additive and opt-in. The canonical Ability contract owns identity, schemas, effects, idempotency, and receipt semantics; applications own principal/tenant resolution, authorization, approval consumption, handler execution, and durable audit storage.

## Release boundary

This page reflects the 0.7.0 technical preview on 2026-09-08. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-mcp-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/v0.7.0/skills/kujo-mcp-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/v0.7.0/SKILLS_INDEX.md)
