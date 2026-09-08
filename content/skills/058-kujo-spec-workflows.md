---
title: "Kujo Spec"
custom_url: "kujo-spec-workflows"
description: "Use this skill when creating, validating, exporting, reviewing, or maintaining Kujo Spec task contracts: `.spec.yml`, `.spec.yaml`, `.spec.toml`, `.spec.json`, `spec init`, `validate`, `render`, `export`, `export-agent-context`, `export-eval`, `ci`, `list`, `search`, `status`, `template`, `graph`, safe-write/template-source policy, Spec schema changes, or Spec CLI/tests/source changes."
excerpt: "Use this skill when creating, validating, exporting, reviewing, or maintaining Kujo Spec task contracts."
featured_image: "/assets/images/ecosystem/skill-kujo-spec-workflows.webp"
social_image: "/assets/images/social/kujo-spec-workflows.jpg"
section: "Agent Skill"
order: "580"
install_command: "git clone --branch v0.7.0 --depth 1 https://github.com/kujolang/kujo-skills.git && mkdir -p ~/.codex/skills && cp -R kujo-skills/skills/kujo-spec-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/v0.7.0/skills/kujo-spec-workflows/SKILL.md"
launch_story: "One of 135 focused, repository-backed skills in the Kujo Skills 0.7.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.7.0"
last_updated: "tag v0.7.0 Tagger: Robert DeVore <deviodigital@gmail.com> Kujo Skills v0.7.0: reusable video styles 2026-09-08"
keywords: "Kujo Spec, Kujo Agent Skill, kujo-spec-workflows, repository-backed agent guidance"
seo_title: "Kujo Spec — Kujo Agent Skill"
seo_description: "Use this skill when creating, validating, exporting, reviewing, or maintaining Kujo Spec task contracts: `.spec.yml`, `.spec.yaml`, `.spec.toml`, `.spec.json`, `spec init`, `validate`, `render`, `export`, `export-agent-context`, `export-eval`, `ci`, `list`, `search`, `status`, `template`, `graph`, safe-write/template-source policy, Spec schema changes, or Spec CLI/tests/source changes."
---

## What it covers

Use this skill when creating, validating, exporting, reviewing, or maintaining Kujo Spec task contracts: `.spec.yml`, `.spec.yaml`, `.spec.toml`, `.spec.json`, `spec init`, `validate`, `render`, `export`, `export-agent-context`, `export-eval`, `ci`, `list`, `search`, `status`, `template`, `graph`, safe-write/template-source policy, Spec schema changes, or Spec CLI/tests/source changes.

Run the install command from a new working directory. If you already have the released checkout, copy the complete skill folder from it instead of cloning again.

## Released guidance

- "Users can switch between light and dark themes"
- "The selected theme persists after reload"
- Prefer `specs/` at project root for small projects.
- In monorepos, colocate specs with the bounded context: `services/api/specs/`,
- Spec discovery uses double extensions: `.spec.yml`, `.spec.yaml`,

## Release boundary

This page reflects the 0.7.0 technical preview on tag v0.7.0
Tagger: Robert DeVore <deviodigital@gmail.com>

Kujo Skills v0.7.0: reusable video styles
2026-09-08. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-spec-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/v0.7.0/skills/kujo-spec-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/v0.7.0/SKILLS_INDEX.md)
