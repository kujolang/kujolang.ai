---
title: "Kujo ChangeBucket"
custom_url: "kujo-changebucket-workflows"
description: "Use this skill when measuring or enforcing code-change footprint with ChangeBucket: `changebucket`, `changebucket check`, `--json`, `--markdown`, `--output`, `--base`, `--head`, `--repo`, budget flags, risk/blast-radius reports, file-category counts, generated markdown reports, or ChangeBucket CLI/tests/source changes."
excerpt: "Use this skill when measuring or enforcing code-change footprint with ChangeBucket."
featured_image: "/assets/images/ecosystem/skill-kujo-changebucket-workflows.webp"
social_image: "/assets/images/social/kujo-changebucket-workflows.jpg"
section: "Agent Skill"
order: "90"
install_command: "git clone --branch v0.7.0 --depth 1 https://github.com/kujolang/kujo-skills.git && mkdir -p ~/.codex/skills && cp -R kujo-skills/skills/kujo-changebucket-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/v0.7.0/skills/kujo-changebucket-workflows/SKILL.md"
launch_story: "One of 135 focused, repository-backed skills in the Kujo Skills 0.7.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.7.0"
last_updated: "tag v0.7.0 Tagger: Robert DeVore <deviodigital@gmail.com> Kujo Skills v0.7.0: reusable video styles 2026-09-08"
keywords: "Kujo ChangeBucket, Kujo Agent Skill, kujo-changebucket-workflows, repository-backed agent guidance"
seo_title: "Kujo ChangeBucket — Kujo Agent Skill"
seo_description: "Use this skill when measuring or enforcing code-change footprint with ChangeBucket: `changebucket`, `changebucket check`, `--json`, `--markdown`, `--output`, `--base`, `--head`, `--repo`, budget flags, risk/blast-radius reports, file-category counts, generated markdown reports, or ChangeBucket CLI/tests/source changes."
---

## What it covers

Use this skill when measuring or enforcing code-change footprint with ChangeBucket: `changebucket`, `changebucket check`, `--json`, `--markdown`, `--output`, `--base`, `--head`, `--repo`, budget flags, risk/blast-radius reports, file-category counts, generated markdown reports, or ChangeBucket CLI/tests/source changes.

Run the install command from a new working directory. If you already have the released checkout, copy the complete skill folder from it instead of cloning again.

## Released guidance

- `changebucket [options]` prints a text, JSON, or markdown footprint report and exits `0` on successful analysis.
- `changebucket check [budget options]` exits `1` when the budget is exceeded.
- `--json` prints exactly one JSON object to stdout.
- `--output <file>` writes a markdown report and prints `Wrote report to <file>`.
- Non-git targets print `error: not a git repository: <path>` and exit `1`.

## Release boundary

This page reflects the 0.7.0 technical preview on tag v0.7.0
Tagger: Robert DeVore <deviodigital@gmail.com>

Kujo Skills v0.7.0: reusable video styles
2026-09-08. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-changebucket-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/v0.7.0/skills/kujo-changebucket-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/v0.7.0/SKILLS_INDEX.md)
