---
title: "Kujo Spec"
custom_url: "kujo-spec-workflows"
description: "Use this skill when creating, validating, exporting, reviewing, or maintaining Kujo Spec task contracts: `.spec.yml`, `.spec.yaml`, `.spec.toml`, `.spec.json`, `spec init`, `validate`, `render`, `export`, `export-agent-context`, `export-eval`, `ci`, `list`, `search`, `status`, `template`, `graph`, safe-write/template-source policy, Spec schema changes, or Spec CLI/tests/source changes."
excerpt: "Use this skill when creating, validating, exporting, reviewing, or maintaining Kujo Spec task contracts."
featured_image: "/assets/images/ecosystem/skill-kujo-spec-workflows.webp"
social_image: "/assets/images/social/kujo-spec-workflows.jpg"
section: "Agent Skill"
order: "490"
install_command: "mkdir -p ~/.codex/skills && cp -R skills/kujo-spec-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-spec-workflows/SKILL.md"
launch_story: "One of 83 focused, repository-backed skills in the Kujo Skills 0.2.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.2.0"
last_updated: "2026-08-11"
keywords: "Kujo Spec, Kujo Agent Skill, kujo-spec-workflows, repository-backed agent guidance"
seo_title: "Kujo Spec — Kujo Agent Skill"
seo_description: "Use this skill when creating, validating, exporting, reviewing, or maintaining Kujo Spec task contracts: `.spec.yml`, `.spec.yaml`, `.spec.toml`, `.spec.json`, `spec init`, `validate`, `render`, `export`, `export-agent-context`, `export-eval`, `ci`, `list`, `search`, `status`, `template`, `graph`, safe-write/template-source policy, Spec schema changes, or Spec CLI/tests/source changes."
---

## What it covers

Use this skill when creating, validating, exporting, reviewing, or maintaining Kujo Spec task contracts: `.spec.yml`, `.spec.yaml`, `.spec.toml`, `.spec.json`, `spec init`, `validate`, `render`, `export`, `export-agent-context`, `export-eval`, `ci`, `list`, `search`, `status`, `template`, `graph`, safe-write/template-source policy, Spec schema changes, or Spec CLI/tests/source changes.

## Released guidance

- "Users can switch between light and dark themes"
- "The selected theme persists after reload"
- Prefer `specs/` at project root for small projects.
- In monorepos, colocate specs with the bounded context: `services/api/specs/`,
- Spec discovery uses double extensions: `.spec.yml`, `.spec.yaml`,

## Release boundary

This page reflects the 0.2.0 technical preview on 2026-08-11. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-spec-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-spec-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/main/SKILLS_INDEX.md)
