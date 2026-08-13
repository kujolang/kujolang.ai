---
title: "Kujo MCP"
custom_url: "kujo-mcp-workflows"
description: "Use this skill when generating, running, validating, deploying, or maintaining Kujo MCP servers and repo-specific MCP scaffolds: `mcp make`, `kujo run mcp.kujo --interpreter make`, `mcp-server.json`, MCP tool/resource registries, generated `.mcp/` outputs, `mcp.manifest.json`, repo profiles, MCP safety tiers, auth/host/request guardrails, endpoint tests, or MCP source/test changes."
excerpt: "Use this skill when generating, running, validating, deploying, or maintaining Kujo MCP servers and repo-specific MCP scaffolds."
featured_image: "/assets/images/ecosystem/skill-kujo-mcp-workflows.webp"
social_image: "/assets/images/social/kujo-mcp-workflows.jpg"
section: "Agent Skill"
order: "290"
install_command: "mkdir -p ~/.codex/skills && cp -R skills/kujo-mcp-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-mcp-workflows/SKILL.md"
launch_story: "One of 83 focused, repository-backed skills in the Kujo Skills 0.2.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.2.0"
last_updated: "2026-08-11"
keywords: "Kujo MCP, Kujo Agent Skill, kujo-mcp-workflows, repository-backed agent guidance"
seo_title: "Kujo MCP — Kujo Agent Skill"
seo_description: "Use this skill when generating, running, validating, deploying, or maintaining Kujo MCP servers and repo-specific MCP scaffolds: `mcp make`, `kujo run mcp.kujo --interpreter make`, `mcp-server.json`, MCP tool/resource registries, generated `.mcp/` outputs, `mcp.manifest.json`, repo profiles, MCP safety tiers, auth/host/request guardrails, endpoint tests, or MCP source/test changes."
---

## What it covers

Use this skill when generating, running, validating, deploying, or maintaining Kujo MCP servers and repo-specific MCP scaffolds: `mcp make`, `kujo run mcp.kujo --interpreter make`, `mcp-server.json`, MCP tool/resource registries, generated `.mcp/` outputs, `mcp.manifest.json`, repo profiles, MCP safety tiers, auth/host/request guardrails, endpoint tests, or MCP source/test changes.

## Released guidance

- Classify the request first: local demo server, generated repo server, framework/source change, generated artifact review, or deployment hardening.
- Prefer the current reliable invocation for generation: `kujo run mcp.kujo --interpreter make <repo-path>`. The intended future `kujo mcp make <repo-path>` shape is not the dependable path yet.
- Treat generated `.mcp/` outputs as reviewable scaffolds, not magic truth. Inspect `repo-profile.json`, `mcp.manifest.json`, and `artifacts/safety-review.md` before recommending exposure.
- Keep MCP server capabilities least-privilege: read-only tools and allowlisted safe commands by default; review-required and blocked capabilities stay disabled unless explicitly justified.
- Run focused tests after narrow edits and `bash tests/run_all_tests.sh` after security, config, endpoint, generation, or registry changes.

## Release boundary

This page reflects the 0.2.0 technical preview on 2026-08-11. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-mcp-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-mcp-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/main/SKILLS_INDEX.md)
