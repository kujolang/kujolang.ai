---
title: "Kujo Lens"
custom_url: "kujo-lens-workflows"
description: "Use this skill when setting up, running, interpreting, or maintaining Lens deterministic browser and visual QA workflows: `lens check`, `lens inspect`, `lens flow`, `.lens.toml`, `.lens/runs/`, `lens-report.json`, Agent Repair Briefs, screenshots, accessibility checks, link checks, visual baselines, CI action wiring, RunLedger/Howl output, or Lens source/test changes."
excerpt: "Use this skill when setting up, running, interpreting, or maintaining Lens deterministic browser and visual QA workflows."
featured_image: "/assets/images/ecosystem/skill-kujo-lens-workflows.webp"
social_image: "/assets/images/social/kujo-lens-workflows.jpg"
section: "Agent Skill"
order: "260"
install_command: "mkdir -p ~/.codex/skills && cp -R skills/kujo-lens-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-lens-workflows/SKILL.md"
launch_story: "One of 83 focused, repository-backed skills in the Kujo Skills 0.2.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.2.0"
last_updated: "2026-08-11"
keywords: "Kujo Lens, Kujo Agent Skill, kujo-lens-workflows, repository-backed agent guidance"
seo_title: "Kujo Lens — Kujo Agent Skill"
seo_description: "Use this skill when setting up, running, interpreting, or maintaining Lens deterministic browser and visual QA workflows: `lens check`, `lens inspect`, `lens flow`, `.lens.toml`, `.lens/runs/`, `lens-report.json`, Agent Repair Briefs, screenshots, accessibility checks, link checks, visual baselines, CI action wiring, RunLedger/Howl output, or Lens source/test changes."
---

## What it covers

Use this skill when setting up, running, interpreting, or maintaining Lens deterministic browser and visual QA workflows: `lens check`, `lens inspect`, `lens flow`, `.lens.toml`, `.lens/runs/`, `lens-report.json`, Agent Repair Briefs, screenshots, accessibility checks, link checks, visual baselines, CI action wiring, RunLedger/Howl output, or Lens source/test changes.

## Released guidance

- Prefer Lens after meaningful frontend changes when a local URL is available.
- Start with `lens --help` and `lens --version` if the install is uncertain.
- Ensure the app server is running before Lens; Lens verifies rendered behavior, not server startup.
- Run a basic check first, then add optional depth only when the task calls for it.
- Branch on Lens exit codes: `0` pass, `1` findings at or above `--fail-on`, `2` invalid input, `3` browser/provider failure, `4` artifact-write failure.

## Release boundary

This page reflects the 0.2.0 technical preview on 2026-08-11. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-lens-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-lens-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/main/SKILLS_INDEX.md)
