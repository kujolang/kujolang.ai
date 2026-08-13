---
title: "Kujo Loop Engineering"
custom_url: "kujo-loop-engineering-workflows"
description: "Use this skill when an agent should work through a bounded engineering task in an arbitrary repository with the Kujo loop-engineering harness: repo-local `.loop-engineering/` initialization, Markdown checklist classification, scoped local fixes only, deterministic eval gates, per-iteration evidence, structured external blockers, optional small commits/pushes, optional Strata handoff, and a fixed final summary contract."
excerpt: "Use this skill when an agent should work through a bounded engineering task in an arbitrary repository with the Kujo loop-engineering harness."
featured_image: "/assets/images/ecosystem/skill-kujo-loop-engineering-workflows.webp"
social_image: "/assets/images/social/kujo-loop-engineering-workflows.jpg"
section: "Agent Skill"
order: "270"
install_command: "mkdir -p ~/.codex/skills && cp -R skills/kujo-loop-engineering-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-loop-engineering-workflows/SKILL.md"
launch_story: "One of 83 focused, repository-backed skills in the Kujo Skills 0.2.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.2.0"
last_updated: "2026-08-11"
keywords: "Kujo Loop Engineering, Kujo Agent Skill, kujo-loop-engineering-workflows, repository-backed agent guidance"
seo_title: "Kujo Loop Engineering — Kujo Agent Skill"
seo_description: "Use this skill when an agent should work through a bounded engineering task in an arbitrary repository with the Kujo loop-engineering harness: repo-local `.loop-engineering/` initialization, Markdown checklist classification, scoped local fixes only, deterministic eval gates, per-iteration evidence, structured external blockers, optional small commits/pushes, optional Strata handoff, and a fixed final summary contract."
---

## What it covers

Use this skill when an agent should work through a bounded engineering task in an arbitrary repository with the Kujo loop-engineering harness: repo-local `.loop-engineering/` initialization, Markdown checklist classification, scoped local fixes only, deterministic eval gates, per-iteration evidence, structured external blockers, optional small commits/pushes, optional Strata handoff, and a fixed final summary contract.

## Released guidance

- Set `objective`.
- Set `checklist_file` when a Markdown checklist exists.
- Keep `allowed_actions` scoped to local repo work unless the user explicitly broadens scope.
- Keep deploy, destructive cleanup, production config changes, release actions, and contract changes blocked unless explicitly approved.
- Configure `eval_gates` with the repo's real install/test/lint/typecheck/build commands.

## Release boundary

This page reflects the 0.2.0 technical preview on 2026-08-11. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-loop-engineering-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-loop-engineering-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/main/SKILLS_INDEX.md)
