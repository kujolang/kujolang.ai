---
title: "Kujo Watchdog"
custom_url: "kujo-watchdog-workflows"
description: "Use this skill when running, configuring, testing, integrating, or maintaining Watchdog local AI telemetry/proxy workflows: `dashboard_server.kujo`, `/proxy/v1`, `/api/requests`, `/api/proxy-config`, `/api/sources`, `/telemetry/v2/batches`, OTLP ingestion/export, SQLite telemetry, auth modes, redaction, rate limits, connected sources, dashboard assets, benchmark scripts, AI Chat/Agents SDK integration, or `watchdog` source/docs changes."
excerpt: "Use this skill when running, configuring, testing, integrating, or maintaining Watchdog local AI telemetry/proxy workflows."
featured_image: "/assets/images/ecosystem/skill-kujo-watchdog-workflows.webp"
social_image: "/assets/images/social/kujo-watchdog-workflows.jpg"
section: "Agent Skill"
order: "680"
install_command: "git clone --branch v0.7.0 --depth 1 https://github.com/kujolang/kujo-skills.git && mkdir -p ~/.codex/skills && cp -R kujo-skills/skills/kujo-watchdog-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/v0.7.0/skills/kujo-watchdog-workflows/SKILL.md"
launch_story: "One of 135 focused, repository-backed skills in the Kujo Skills 0.7.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.7.0"
last_updated: "tag v0.7.0 Tagger: Robert DeVore <deviodigital@gmail.com> Kujo Skills v0.7.0: reusable video styles 2026-09-08"
keywords: "Kujo Watchdog, Kujo Agent Skill, kujo-watchdog-workflows, repository-backed agent guidance"
seo_title: "Kujo Watchdog — Kujo Agent Skill"
seo_description: "Use this skill when running, configuring, testing, integrating, or maintaining Watchdog local AI telemetry/proxy workflows: `dashboard_server.kujo`, `/proxy/v1`, `/api/requests`, `/api/proxy-config`, `/api/sources`, `/telemetry/v2/batches`, OTLP ingestion/export, SQLite telemetry, auth modes, redaction, rate limits, connected sources, dashboard assets, benchmark scripts, AI Chat/Agents SDK integration, or `watchdog` source/docs changes."
---

## What it covers

Use this skill when running, configuring, testing, integrating, or maintaining Watchdog local AI telemetry/proxy workflows: `dashboard_server.kujo`, `/proxy/v1`, `/api/requests`, `/api/proxy-config`, `/api/sources`, `/telemetry/v2/batches`, OTLP ingestion/export, SQLite telemetry, auth modes, redaction, rate limits, connected sources, dashboard assets, benchmark scripts, AI Chat/Agents SDK integration, or `watchdog` source/docs changes.

Run the install command from a new working directory. If you already have the released checkout, copy the complete skill folder from it instead of cloning again.

## Released guidance

- Root `dashboard_server.kujo`, `dashboard.html`, `watchdog.kujo`, and `watchdog_shared.kujo` are compatibility mirrors of `src/` surfaces.
- Proxy smoke may intentionally produce upstream `401` without an API key while still recording telemetry.
- Named upstream profiles live in `watchdog_proxy_config.json` and are selected with `X-Watchdog-Upstream-Profile`; unknown profile names fail before upstream egress.
- A single Watchdog server can proxy several provider accounts through named upstream profiles, including AI Chat's shared OpenRouter and Ollama lanes; per-request profile metadata is preserved for filtering and telemetry.
- Connected Sources live in private `watchdog_sources.json` metadata plus accepted telemetry evidence. `/api/sources` reports observed/registered native producers, guarded OTLP producers, and proxy profiles without contacting external providers.

## Release boundary

This page reflects the 0.7.0 technical preview on tag v0.7.0
Tagger: Robert DeVore <deviodigital@gmail.com>

Kujo Skills v0.7.0: reusable video styles
2026-09-08. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-watchdog-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/v0.7.0/skills/kujo-watchdog-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/v0.7.0/SKILLS_INDEX.md)
