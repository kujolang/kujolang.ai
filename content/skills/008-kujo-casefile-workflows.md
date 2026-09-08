---
title: "Kujo Casefile"
custom_url: "kujo-casefile-workflows"
description: "Use this skill when capturing, reviewing, handing off, cleaning, or maintaining Casefile local failure evidence bundles: `casefile.kujo`, `casefile.toml`, `.casefile/`, `capture`, `show latest`, `list`, `doctor`, `clean`, `--from-log`, `--manual`, `--mirror-exit-code`, redaction, path safety, or Casefile CLI/tests/source changes."
excerpt: "Use this skill when capturing, reviewing, handing off, cleaning, or maintaining Casefile local failure evidence bundles."
featured_image: "/assets/images/ecosystem/skill-kujo-casefile-workflows.webp"
social_image: "/assets/images/social/kujo-casefile-workflows.jpg"
section: "Agent Skill"
order: "80"
install_command: "git clone --branch v0.7.0 --depth 1 https://github.com/kujolang/kujo-skills.git && mkdir -p ~/.codex/skills && cp -R kujo-skills/skills/kujo-casefile-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/v0.7.0/skills/kujo-casefile-workflows/SKILL.md"
launch_story: "One of 135 focused, repository-backed skills in the Kujo Skills 0.7.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.7.0"
last_updated: "2026-09-08"
keywords: "Kujo Casefile, Kujo Agent Skill, kujo-casefile-workflows, repository-backed agent guidance"
seo_title: "Kujo Casefile — Kujo Agent Skill"
seo_description: "Use this skill when capturing, reviewing, handing off, cleaning, or maintaining Casefile local failure evidence bundles: `casefile.kujo`, `casefile.toml`, `.casefile/`, `capture`, `show latest`, `list`, `doctor`, `clean`, `--from-log`, `--manual`, `--mirror-exit-code`, redaction, path safety, or Casefile CLI/tests/source changes."
---

## What it covers

Use this skill when capturing, reviewing, handing off, cleaning, or maintaining Casefile local failure evidence bundles: `casefile.kujo`, `casefile.toml`, `.casefile/`, `capture`, `show latest`, `list`, `doctor`, `clean`, `--from-log`, `--manual`, `--mirror-exit-code`, redaction, path safety, or Casefile CLI/tests/source changes.

Run the install command from a new working directory. If you already have the released checkout, copy the complete skill folder from it instead of cloning again.

## Released guidance

- Prefer interpreter mode in the Casefile repo: `kujo run --interpreter casefile.kujo -- <command>`.
- If `KUJO_BIN` is available, use `"$KUJO_BIN" run --interpreter casefile.kujo -- <command>`.
- Start new repos with `init`, `validate`, and often `doctor`.
- Use `capture --name <name> -- <argv...>` for failing commands; prefer argv after `--` over `--command` for complex commands.
- Use `capture --from-log <path> --name <name>` when rerunning is expensive or impossible.

## Release boundary

This page reflects the 0.7.0 technical preview on 2026-09-08. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-casefile-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/v0.7.0/skills/kujo-casefile-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/v0.7.0/SKILLS_INDEX.md)
