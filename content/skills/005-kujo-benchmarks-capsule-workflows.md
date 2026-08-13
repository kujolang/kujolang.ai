---
title: "Kujo Benchmarks Capsule"
custom_url: "kujo-benchmarks-capsule-workflows"
description: "Use this skill when running, validating, comparing, or maintaining the Capsule benchmark tool: `bin/capsule`, `make`, `inspect`, `validate`, `--stable`, `--dry-run`, `capsule.json`, `capsule.md`, `manifest.json`, fixture projects, benchmark evidence, or benchmarks-capsule source/test changes."
featured_image: "/assets/images/ecosystem/skill-kujo-benchmarks-capsule-workflows.webp"
social_image: "/assets/images/social/kujo-benchmarks-capsule-workflows.jpg"
section: "Agent Skill"
order: "50"
install_command: "mkdir -p ~/.codex/skills && cp -R skills/kujo-benchmarks-capsule-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-benchmarks-capsule-workflows/SKILL.md"
launch_story: "One of 83 focused, repository-backed skills in the Kujo Skills 0.2.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.2.0"
last_updated: "2026-08-11"
keywords: "Kujo Benchmarks Capsule, Kujo Agent Skill, kujo-benchmarks-capsule-workflows, repository-backed agent guidance"
seo_title: "Kujo Benchmarks Capsule — Kujo Agent Skill"
seo_description: "Use this skill when running, validating, comparing, or maintaining the Capsule benchmark tool: `bin/capsule`, `make`, `inspect`, `validate`, `--stable`, `--dry-run`, `capsule.json`, `capsule.md`, `manifest.json`, fixture projects, benchmark evidence, or benchmarks-capsule source/test changes."
---

## What it covers

Use this skill when running, validating, comparing, or maintaining the Capsule benchmark tool: `bin/capsule`, `make`, `inspect`, `validate`, `--stable`, `--dry-run`, `capsule.json`, `capsule.md`, `manifest.json`, fixture projects, benchmark evidence, or benchmarks-capsule source/test changes.

## Released guidance

- `bin/capsule` is a thin launcher; all logic lives in Kujo under `src/`.
- `make` writes `capsule.json`, `capsule.md`, and `manifest.json` unless `--format` or `--dry-run` changes output.
- `--stable` pins timestamp to `1970-01-01T00:00:00Z`, sorts output, uses POSIX-style relative paths, and should produce byte-identical repeated output.
- `validate` checks required shape, list types, file records, ignored reason vocabulary, and SHA-256 hex fields.
- Exit codes are `0` success, `1` validation/check failure, `2` usage error, and `3` unexpected runtime error.

## Release boundary

This page reflects the 0.2.0 technical preview on 2026-08-11. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-benchmarks-capsule-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-benchmarks-capsule-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/main/SKILLS_INDEX.md)
