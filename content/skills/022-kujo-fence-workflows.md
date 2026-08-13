---
title: "Kujo Fence Workflows"
custom_url: "kujo-fence-workflows"
description: "Use this skill when setting up, running, interpreting, integrating, or maintaining Fence architecture-boundary checks for Kujo ecosystem repositories: `fence.kujo`, `fence.toml`, `fence-baseline.json`, `init`, `validate`, `check`, `explain`, `graph`, `baseline create`, `--changed-only`, `--baseline`, JSON/Markdown/SARIF reports, CI gates, zone rules, import-boundary violations, or Fence CLI/source/test changes."
featured_image: "/assets/images/ecosystem/skill-kujo-fence-workflows.webp"
social_image: "/assets/images/social/kujo-fence-workflows.jpg"
section: "Agent Skill"
order: "220"
install_command: "mkdir -p ~/.codex/skills && cp -R skills/kujo-fence-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-fence-workflows/SKILL.md"
launch_story: "One of 83 focused, repository-backed skills in the Kujo Skills 0.2.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.2.0"
last_updated: "2026-08-11"
keywords: "Kujo Fence Workflows, Kujo Agent Skill, kujo-fence-workflows, repository-backed agent guidance"
seo_title: "Kujo Fence Workflows — Kujo Agent Skill"
seo_description: "Use this skill when setting up, running, interpreting, integrating, or maintaining Fence architecture-boundary checks for Kujo ecosystem repositories: `fence.kujo`, `fence.toml`, `fence-baseline.json`, `init`, `validate`, `check`, `explain`, `graph`, `baseline create`, `--changed-only`, `--baseline`, JSON/Markdown/SARIF reports, CI gates, zone rules, import-boundary violations, or Fence CLI/source/test changes."
---

## What it covers

Use this skill when setting up, running, interpreting, integrating, or maintaining Fence architecture-boundary checks for Kujo ecosystem repositories: `fence.kujo`, `fence.toml`, `fence-baseline.json`, `init`, `validate`, `check`, `explain`, `graph`, `baseline create`, `--changed-only`, `--baseline`, JSON/Markdown/SARIF reports, CI gates, zone rules, import-boundary violations, or Fence CLI/source/test changes.

## Released guidance

- Default to the local Fence repo unless the user points elsewhere: `/Users/robertdevore/2026/Kujolang/kujo-repos/fence`.
- Use `KUJO_BIN` when available; otherwise try `kujo` on `PATH`.
- Run Fence from inside the target repository being checked. Module imports resolve relative to `fence.kujo`, but source scanning uses the current working directory.
- Start new repos with `init`, edit `fence.toml`, then run `validate` and `check`.
- Before implementation work in a fenced repo, run `graph` and `check` to learn the allowed dependency direction and current violations.

## Release boundary

This page reflects the 0.2.0 technical preview on 2026-08-11. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-fence-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-fence-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/main/SKILLS_INDEX.md)
