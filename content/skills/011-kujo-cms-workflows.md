---
title: "Kujo CMS"
custom_url: "kujo-cms-workflows"
description: "Use this skill when running, validating, extending, or maintaining the Kujo CMS server-first showcase: `backend/runtime/main.kujo`, content models, delivery routes, auth boundaries, contract tests, startup compatibility, webhook/background jobs, migration safety, backup/restore, release gates, or `cms` source/docs changes."
excerpt: "Use this skill when running, validating, extending, or maintaining the Kujo CMS server-first showcase."
featured_image: "/assets/images/ecosystem/skill-kujo-cms-workflows.webp"
social_image: "/assets/images/social/kujo-cms-workflows.jpg"
section: "Agent Skill"
order: "110"
install_command: "mkdir -p ~/.codex/skills && cp -R skills/kujo-cms-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-cms-workflows/SKILL.md"
launch_story: "One of 96 focused, repository-backed skills in the Kujo Skills 0.4.1 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.4.1"
last_updated: "2026-08-25"
keywords: "Kujo CMS, Kujo Agent Skill, kujo-cms-workflows, repository-backed agent guidance"
seo_title: "Kujo CMS — Kujo Agent Skill"
seo_description: "Use this skill when running, validating, extending, or maintaining the Kujo CMS server-first showcase: `backend/runtime/main.kujo`, content models, delivery routes, auth boundaries, contract tests, startup compatibility, webhook/background jobs, migration safety, backup/restore, release gates, or `cms` source/docs changes."
---

## What it covers

Use this skill when running, validating, extending, or maintaining the Kujo CMS server-first showcase: `backend/runtime/main.kujo`, content models, delivery routes, auth boundaries, contract tests, startup compatibility, webhook/background jobs, migration safety, backup/restore, release gates, or `cms` source/docs changes.

## Released guidance

- The canonical runtime entrypoint is `backend/runtime/main.kujo`; there is no standalone CLI wrapper.
- Public discovery routes, published-only anonymous reads, auth-gated write routes, entry locks, revisions/rollback, webhook/background-job scripts, and operational scripts are part of the showcase surface.
- The documented release gate covers contract, smoke, startup compatibility, integration, security, and optional performance checks; default branch protection remains the known governance item before claiming enterprise-complete posture.
- Webhook/background-job scripts may mutate local queues; inspect env and paths first.
- Default to loopback-local binds unless the user explicitly needs another host.

## Release boundary

This page reflects the 0.4.1 technical preview on 2026-08-25. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-cms-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-cms-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/main/SKILLS_INDEX.md)
