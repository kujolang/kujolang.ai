---
title: "Kujo CMS"
custom_url: "kujo-cms-workflows"
description: "Use this skill to run, validate, extend, or maintain Kujo CMS, including content, identity, SEO, extension packages, abilities, connectors, WebMCP, operations, and release gates."
excerpt: "Repository-backed guidance for running and maintaining the current Kujo CMS contracts and release gates."
featured_image: "/assets/images/ecosystem/skill-kujo-cms-workflows.webp"
social_image: "/assets/images/social/kujo-cms-workflows.jpg"
section: "Agent Skill"
order: "110"
install_command: "mkdir -p ~/.codex/skills && cp -R skills/kujo-cms-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-cms-workflows/SKILL.md"
launch_story: "One of 96 focused, repository-backed skills in the Kujo Skills 0.4.1 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.4.1"
last_updated: "2026-08-30"
keywords: "Kujo CMS, Kujo Agent Skill, kujo-cms-workflows, abilities API, WebMCP, extension packages, repository-backed agent guidance"
seo_title: "Kujo CMS — Kujo Agent Skill"
seo_description: "Use the Kujo CMS workflow skill for content, identity, SEO, themes, plugins, abilities, connectors, WebMCP, operations, tests, and release gates."
---

## What it covers

Use this skill when running, validating, extending, or maintaining Kujo CMS. It routes work through the canonical `backend/runtime/main.kujo` entrypoint and keeps content, identity, SEO, theme and plugin packages, abilities, connectors, WebMCP, operational scripts, documentation, and release evidence aligned.

## Released guidance

- The canonical runtime entrypoint is `backend/runtime/main.kujo`; there is no standalone CLI wrapper.
- Public discovery routes, published-only anonymous reads, auth-gated write routes, entry locks, revisions/rollback, webhook/background-job scripts, and operational scripts are part of the showcase surface.
- CMS 1.1.0 adds framework-neutral sessions and capabilities, granular SEO and social operations, verified extension ZIP ingestion, plugin abilities and connectors, atomic content and media workflows, official JavaScript and PHP clients, and built-in WebMCP.
- Administration, API, terminal, and agent consumers must use the same core permission and audit contracts rather than duplicating business rules in a frontend adapter.
- The documented release gate covers contract, smoke, startup compatibility, integration, security, and optional performance checks; default branch protection remains the known governance item before claiming enterprise-complete posture.
- Webhook/background-job scripts may mutate local queues; inspect env and paths first.
- Default to loopback-local binds unless the user explicitly needs another host.

## Release boundary

This page reflects the 0.4.1 technical preview guidance reviewed against CMS 1.1.0 on 2026-08-30. The skill provides repository-backed guidance; the agent host remains responsible for permissions, approval, and enforcement.

## Source

- [Read the complete kujo-cms-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-cms-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/main/SKILLS_INDEX.md)
