---
title: "Kujo Muzzle"
custom_url: "kujo-muzzle-workflows"
description: "Use this skill when setting up, running, or reviewing Muzzle quiet workflows for AI-assisted development: `muzzle init`, `.muzzle/workflows/`, `.muzzle/manifests/`, `muzzle run`, `--json`, `--verbose`, `--dry-run`, workflow logs/reports, loop mode, or Muzzle safety and output-contract changes."
featured_image: "/assets/images/ecosystem/skill-kujo-muzzle-workflows.webp"
social_image: "/assets/images/social/kujo-muzzle-workflows.jpg"
section: "Agent Skill"
order: "300"
install_command: "mkdir -p ~/.codex/skills && cp -R skills/kujo-muzzle-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-muzzle-workflows/SKILL.md"
launch_story: "One of 83 focused, repository-backed skills in the Kujo Skills 0.2.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.2.0"
last_updated: "2026-08-11"
keywords: "Kujo Muzzle, Kujo Agent Skill, kujo-muzzle-workflows, repository-backed agent guidance"
seo_title: "Kujo Muzzle — Kujo Agent Skill"
seo_description: "Use this skill when setting up, running, or reviewing Muzzle quiet workflows for AI-assisted development: `muzzle init`, `.muzzle/workflows/`, `.muzzle/manifests/`, `muzzle run`, `--json`, `--verbose`, `--dry-run`, workflow logs/reports, loop mode, or Muzzle safety and output-contract changes."
---

## What it covers

Use this skill when setting up, running, or reviewing Muzzle quiet workflows for AI-assisted development: `muzzle init`, `.muzzle/workflows/`, `.muzzle/manifests/`, `muzzle run`, `--json`, `--verbose`, `--dry-run`, workflow logs/reports, loop mode, or Muzzle safety and output-contract changes.

## Released guidance

- Check setup with `muzzle --help`, `muzzle version`, and `muzzle list`.
- Prefer `muzzle run <workflow>` for known noisy build, test, deploy, scan, or release tasks.
- Use `muzzle run <workflow> --json` when a downstream step should parse status, exit code, duration, `log_path`, or `report_path`.
- Use `muzzle run <workflow> --dry-run` before new, destructive, networked, deploy, publish, or production-like workflows.
- Use `--verbose` only when live full output is needed; otherwise read logs after failure.

## Release boundary

This page reflects the 0.2.0 technical preview on 2026-08-11. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-muzzle-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-muzzle-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/main/SKILLS_INDEX.md)
