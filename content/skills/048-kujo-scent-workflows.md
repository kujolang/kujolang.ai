---
title: "Kujo Scent"
custom_url: "kujo-scent-workflows"
description: "Use this skill when creating, previewing, reviewing, or maintaining Scent context packs for agent handoff: `scent pack`, `--dry-run`, `--json`, `--budget`, `--target`, `--include`, `--exclude`, `--changed`, `--staged`, `--unstaged`, `.scent/` or generated pack artifacts, `context.md`, `context.json`, `manifest.json`, `files.json`, `redactions.json`, and Scent CLI/source/test changes."
excerpt: "Use this skill when creating, previewing, reviewing, or maintaining Scent context packs for agent handoff."
featured_image: "/assets/images/ecosystem/skill-kujo-scent-workflows.webp"
social_image: "/assets/images/social/kujo-scent-workflows.jpg"
section: "Agent Skill"
order: "480"
install_command: "mkdir -p ~/.codex/skills && cp -R skills/kujo-scent-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-scent-workflows/SKILL.md"
launch_story: "One of 96 focused, repository-backed skills in the Kujo Skills 0.4.1 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.4.1"
last_updated: "2026-08-25"
keywords: "Kujo Scent, Kujo Agent Skill, kujo-scent-workflows, repository-backed agent guidance"
seo_title: "Kujo Scent — Kujo Agent Skill"
seo_description: "Use this skill when creating, previewing, reviewing, or maintaining Scent context packs for agent handoff: `scent pack`, `--dry-run`, `--json`, `--budget`, `--target`, `--include`, `--exclude`, `--changed`, `--staged`, `--unstaged`, `.scent/` or generated pack artifacts, `context.md`, `context.json`, `manifest.json`, `files.json`, `redactions.json`, and Scent CLI/source/test changes."
---

## What it covers

Use this skill when creating, previewing, reviewing, or maintaining Scent context packs for agent handoff: `scent pack`, `--dry-run`, `--json`, `--budget`, `--target`, `--include`, `--exclude`, `--changed`, `--staged`, `--unstaged`, `.scent/` or generated pack artifacts, `context.md`, `context.json`, `manifest.json`, `files.json`, `redactions.json`, and Scent CLI/source/test changes.

## Released guidance

- Run Scent from inside the repository being packed; it discovers the repo root from the current working directory.
- Start with `pack --dry-run --json` to estimate size, included files, and warnings before writing artifacts.
- Prefer an explicit `--task` that names the work the downstream agent should do, not a vague repo summary.
- Use `--changed`, `--staged`, or `--unstaged` when the handoff should focus on current working-tree changes.
- Use repeated `--include <path>` for important task areas and `--exclude <path>` for irrelevant generated, vendor, build, cache, or bulk data.

## Release boundary

This page reflects the 0.4.1 technical preview on 2026-08-25. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-scent-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-scent-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/main/SKILLS_INDEX.md)
