---
title: "Kujo PackWrite"
custom_url: "kujo-packwrite-workflows"
description: "Use this skill when generating, validating, reviewing, or maintaining PackWrite agent execution packs: `packwrite init`, `validate`, `prompt`, `config`, `doctor`, `packwrite.toml`, `MEGA_PROMPT.md`, generated `agent/` packs, model/provider setup, offline fake-response tests, or PackWrite CLI/source changes."
excerpt: "Use this skill when generating, validating, reviewing, or maintaining PackWrite agent execution packs."
featured_image: "/assets/images/ecosystem/skill-kujo-packwrite-workflows.webp"
social_image: "/assets/images/social/kujo-packwrite-workflows.jpg"
section: "Agent Skill"
order: "310"
install_command: "mkdir -p ~/.codex/skills && cp -R skills/kujo-packwrite-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-packwrite-workflows/SKILL.md"
launch_story: "One of 83 focused, repository-backed skills in the Kujo Skills 0.2.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.2.0"
last_updated: "2026-08-11"
keywords: "Kujo PackWrite, Kujo Agent Skill, kujo-packwrite-workflows, repository-backed agent guidance"
seo_title: "Kujo PackWrite — Kujo Agent Skill"
seo_description: "Use this skill when generating, validating, reviewing, or maintaining PackWrite agent execution packs: `packwrite init`, `validate`, `prompt`, `config`, `doctor`, `packwrite.toml`, `MEGA_PROMPT.md`, generated `agent/` packs, model/provider setup, offline fake-response tests, or PackWrite CLI/source changes."
---

## What it covers

Use this skill when generating, validating, reviewing, or maintaining PackWrite agent execution packs: `packwrite init`, `validate`, `prompt`, `config`, `doctor`, `packwrite.toml`, `MEGA_PROMPT.md`, generated `agent/` packs, model/provider setup, offline fake-response tests, or PackWrite CLI/source changes.

## Released guidance

- `MASTER.md` holds stable intent and assumptions.
- `TODO.md` tracks phase completion and links phase files.
- `HANDOFF.md`, `DECISIONS.md`, and `REVIEW_CHECKLIST.md` are mutable run state.
- `phases/*.md` hold scoped phase specs, acceptance criteria, and suggested checks.
- Optional files are controlled by `[pack]` config toggles and must stay aligned

## Release boundary

This page reflects the 0.2.0 technical preview on 2026-08-11. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-packwrite-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-packwrite-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/main/SKILLS_INDEX.md)
