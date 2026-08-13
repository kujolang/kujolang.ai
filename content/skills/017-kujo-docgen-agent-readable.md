---
title: "Kujo DocGen And DocsGen"
custom_url: "kujo-docgen-agent-readable"
description: "Use this skill when working on Kujo DocGen/DocsGen (`kujo docgen`), generated documentation, docs-as-contract surfaces, agent-readable JSON/gap outputs, documentation coverage gates, public-only docs gates, link validation, adapter extraction, README/reference alignment, or example smoke policy."
excerpt: "Use this skill when working on Kujo DocGen/DocsGen (`kujo docgen`), generated documentation, docs-as-contract surfaces, agent-readable JSON/gap outputs, documentation coverage gates, public-only docs gates, link…"
featured_image: "/assets/images/ecosystem/skill-kujo-docgen-agent-readable.webp"
social_image: "/assets/images/social/kujo-docgen-agent-readable.jpg"
section: "Agent Skill"
order: "170"
install_command: "mkdir -p ~/.codex/skills && cp -R skills/kujo-docgen-agent-readable ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-docgen-agent-readable/SKILL.md"
launch_story: "One of 83 focused, repository-backed skills in the Kujo Skills 0.2.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.2.0"
last_updated: "2026-08-11"
keywords: "Kujo DocGen And DocsGen, Kujo Agent Skill, kujo-docgen-agent-readable, repository-backed agent guidance"
seo_title: "Kujo DocGen And DocsGen — Kujo Agent Skill"
seo_description: "Use this skill when working on Kujo DocGen/DocsGen (`kujo docgen`), generated documentation, docs-as-contract surfaces, agent-readable JSON/gap outputs, documentation coverage gates, public-only docs gates, link validation, adapter extraction, README/reference alignment, or example smoke policy."
---

## What it covers

Use this skill when working on Kujo DocGen/DocsGen (`kujo docgen`), generated documentation, docs-as-contract surfaces, agent-readable JSON/gap outputs, documentation coverage gates, public-only docs gates, link validation, adapter extraction, README/reference alignment, or example smoke policy.

## Released guidance

- `kujo-cli-contracts` for `--json` payload compatibility, stdout/stderr, exit codes, and breaking-change review.
- `kujo-docgen-public-docs-refresh` for regenerating committed/public docs after drift evidence.
- `kujo-language-implementation` for broader Rust compiler/runtime changes outside `src/docgen`.
- CLI wiring and flags: `src/main.rs`.
- core orchestration, output writing, gates, cache, and typed CLI JSON builder: `src/docgen/core.rs`.

## Release boundary

This page reflects the 0.2.0 technical preview on 2026-08-11. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-docgen-agent-readable skill on GitHub](https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-docgen-agent-readable/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/main/SKILLS_INDEX.md)
