---
title: "Kujo CRUD API"
custom_url: "kujo-crud-api-workflows"
description: "Use this skill when running, testing, extending, or maintaining the CRUD API showcase: `main.kujo`, SQLite item/project APIs, Next.js playground, auth strategies, smoke tests, frontend lint/build, DR/performance drills, API contracts, release checklist, or `crud-api` source/docs changes."
featured_image: "/assets/images/ecosystem/skill-kujo-crud-api-workflows.webp"
social_image: "/assets/images/social/kujo-crud-api-workflows.jpg"
section: "Agent Skill"
order: "140"
install_command: "mkdir -p ~/.codex/skills && cp -R skills/kujo-crud-api-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-crud-api-workflows/SKILL.md"
launch_story: "One of 83 focused, repository-backed skills in the Kujo Skills 0.2.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.2.0"
last_updated: "2026-08-11"
keywords: "Kujo CRUD API, Kujo Agent Skill, kujo-crud-api-workflows, repository-backed agent guidance"
seo_title: "Kujo CRUD API — Kujo Agent Skill"
seo_description: "Use this skill when running, testing, extending, or maintaining the CRUD API showcase: `main.kujo`, SQLite item/project APIs, Next.js playground, auth strategies, smoke tests, frontend lint/build, DR/performance drills, API contracts, release checklist, or `crud-api` source/docs changes."
---

## What it covers

Use this skill when running, testing, extending, or maintaining the CRUD API showcase: `main.kujo`, SQLite item/project APIs, Next.js playground, auth strategies, smoke tests, frontend lint/build, DR/performance drills, API contracts, release checklist, or `crud-api` source/docs changes.

## Released guidance

- Backend starts from `main.kujo`; frontend playground lives under `frontend/`.
- API write auth, request validation, and concurrency behavior are contract surfaces.
- Generated DB files, frontend build output, and smoke artifacts should stay out of commits unless explicitly requested.
- Default server binds to `127.0.0.1`; preserve reviewed local showcase defaults.
- Do not mix CMS behavior into this smaller CRUD API surface.

## Release boundary

This page reflects the 0.2.0 technical preview on 2026-08-11. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-crud-api-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-crud-api-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/main/SKILLS_INDEX.md)
