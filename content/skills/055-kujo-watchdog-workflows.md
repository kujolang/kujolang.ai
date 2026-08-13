---
title: "Kujo Watchdog"
custom_url: "kujo-watchdog-workflows"
description: "Use this skill when running, configuring, testing, integrating, or maintaining Watchdog local AI telemetry/proxy workflows: `dashboard_server.kujo`, `/proxy/v1`, `/api/requests`, `/api/proxy-config`, SQLite telemetry, auth modes, redaction, rate limits, dashboard assets, benchmark scripts, AI Chat integration, or `watchdog` source/docs changes."
featured_image: "/assets/images/ecosystem/skill-kujo-watchdog-workflows.webp"
social_image: "/assets/images/social/kujo-watchdog-workflows.jpg"
section: "Agent Skill"
order: "550"
install_command: "mkdir -p ~/.codex/skills && cp -R skills/kujo-watchdog-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-watchdog-workflows/SKILL.md"
launch_story: "One of 83 focused, repository-backed skills in the Kujo Skills 0.2.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.2.0"
last_updated: "2026-08-11"
keywords: "Kujo Watchdog, Kujo Agent Skill, kujo-watchdog-workflows, repository-backed agent guidance"
seo_title: "Kujo Watchdog — Kujo Agent Skill"
seo_description: "Use this skill when running, configuring, testing, integrating, or maintaining Watchdog local AI telemetry/proxy workflows: `dashboard_server.kujo`, `/proxy/v1`, `/api/requests`, `/api/proxy-config`, SQLite telemetry, auth modes, redaction, rate limits, dashboard assets, benchmark scripts, AI Chat integration, or `watchdog` source/docs changes."
---

## What it covers

Use this skill when running, configuring, testing, integrating, or maintaining Watchdog local AI telemetry/proxy workflows: `dashboard_server.kujo`, `/proxy/v1`, `/api/requests`, `/api/proxy-config`, SQLite telemetry, auth modes, redaction, rate limits, dashboard assets, benchmark scripts, AI Chat integration, or `watchdog` source/docs changes.

## Released guidance

- Root `dashboard_server.kujo`, `dashboard.html`, `watchdog.kujo`, and `watchdog_shared.kujo` are compatibility mirrors of `src/` surfaces.
- Proxy smoke may intentionally produce upstream `401` without an API key while still recording telemetry.
- Named upstream profiles live in `watchdog_proxy_config.json` and are selected with `X-Watchdog-Upstream-Profile`; unknown profile names fail before upstream egress.
- Keep `WDG_API_AUTH_TOKEN`, `WDG_PROXY_AUTHZ_TOKEN`, and upstream provider keys as separate credentials. Production profile startup requires token-protected API and proxy posture.
- `WDG_RATE_LIMIT_MODE=basic` uses SQLite-backed buckets for both `/api/*` and `/proxy/*`; redaction defaults to basic before persistence/export.

## Release boundary

This page reflects the 0.2.0 technical preview on 2026-08-11. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-watchdog-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-watchdog-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/main/SKILLS_INDEX.md)
