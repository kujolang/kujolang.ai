---
title: "Kujo CMS"
custom_url: "kujo-cms-workflows"
description: "Use this skill when running, validating, extending, or maintaining the Kujo CMS server-first showcase: `backend/runtime/main.kujo`, content models, delivery/discovery routes, auth/admin/session boundaries, WebMCP, Abilities/API connectors, extension packages, SEO/content/media workflows, contract tests, startup compatibility, webhook/background jobs, migration safety, backup/restore, release gates, or `cms` source/docs changes."
excerpt: "Use this skill when running, validating, extending, or maintaining the Kujo CMS server-first showcase."
featured_image: "/assets/images/ecosystem/skill-kujo-cms-workflows.webp"
social_image: "/assets/images/social/kujo-cms-workflows.jpg"
section: "Agent Skill"
order: "110"
install_command: "git clone --branch v0.7.0 --depth 1 https://github.com/kujolang/kujo-skills.git && mkdir -p ~/.codex/skills && cp -R kujo-skills/skills/kujo-cms-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/v0.7.0/skills/kujo-cms-workflows/SKILL.md"
launch_story: "One of 135 focused, repository-backed skills in the Kujo Skills 0.7.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.7.0"
last_updated: "2026-09-08"
keywords: "Kujo CMS, Kujo Agent Skill, kujo-cms-workflows, repository-backed agent guidance"
seo_title: "Kujo CMS — Kujo Agent Skill"
seo_description: "Use this skill when running, validating, extending, or maintaining the Kujo CMS server-first showcase: `backend/runtime/main.kujo`, content models, delivery/discovery routes, auth/admin/session boundaries, WebMCP, Abilities/API connectors, extension packages, SEO/content/media workflows, contract tests, startup compatibility, webhook/background jobs, migration safety, backup/restore, release gates, or `cms` source/docs changes."
---

## What it covers

Use this skill when running, validating, extending, or maintaining the Kujo CMS server-first showcase: `backend/runtime/main.kujo`, content models, delivery/discovery routes, auth/admin/session boundaries, WebMCP, Abilities/API connectors, extension packages, SEO/content/media workflows, contract tests, startup compatibility, webhook/background jobs, migration safety, backup/restore, release gates, or `cms` source/docs changes.

Run the install command from a new working directory. If you already have the released checkout, copy the complete skill folder from it instead of cloning again.

## Released guidance

- The canonical runtime entrypoint is `backend/runtime/main.kujo`; there is no standalone CLI wrapper.
- Public discovery routes, published-only anonymous reads, auth-gated write/admin routes, framework-neutral sessions, entry locks, revisions/rollback, webhook/background-job scripts, and operational scripts are part of the showcase surface.
- WebMCP is enabled by default through `/.well-known/kujo-webmcp.json`, `/assets/js/kujo-webmcp.js`, `/v1/webmcp/*`, and `/.well-known/kujo-site-index.json`. It exposes only same-origin read-only published content tools: `get_site_info`, `search_site`, `list_content`, and `get_content`.
- Portable theme/plugin package flows use bounded ZIP ingestion/upload, one canonical manifest, receipt-bound SHA-256 evidence, and managed storage. Package code is not executed during installation.
- CMS Abilities use strict `kujo.ability/v1` definitions, permission-scoped execution, request-bound one-time approvals for mutations, keyed idempotency, tenant-aware principals, and MCP-ready descriptors. Legacy `confirmed: true` is compatibility input only and grants no authority.

## CMS release capabilities

CMS 1.1.0 adds framework-neutral sessions and capabilities, granular SEO and social operations, verified extension ZIP ingestion, plugin abilities and connectors, atomic content and media workflows, official JavaScript and PHP clients, and built-in WebMCP.

## Release boundary

This page reflects the 0.7.0 technical preview on 2026-09-08. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-cms-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/v0.7.0/skills/kujo-cms-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/v0.7.0/SKILLS_INDEX.md)
