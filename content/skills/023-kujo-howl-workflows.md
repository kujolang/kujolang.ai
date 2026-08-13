---
title: "Kujo Howl"
custom_url: "kujo-howl-workflows"
description: "Use this skill when creating, validating, rendering, reviewing, or maintaining Howl showcase artifacts for Kujo examples: `howl init`, `howl validate`, `howl list`, `howl show`, `howl caption`, `howl render`, `howl.json`, `examples/*.kujo`, `dist/howl/`, deterministic SVG/Markdown/HTML cards, static galleries, social captions, or Howl CLI/source/test changes."
featured_image: "/assets/images/ecosystem/skill-kujo-howl-workflows.webp"
social_image: "/assets/images/social/kujo-howl-workflows.jpg"
section: "Agent Skill"
order: "230"
install_command: "mkdir -p ~/.codex/skills && cp -R skills/kujo-howl-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-howl-workflows/SKILL.md"
launch_story: "One of 83 focused, repository-backed skills in the Kujo Skills 0.2.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.2.0"
last_updated: "2026-08-11"
keywords: "Kujo Howl, Kujo Agent Skill, kujo-howl-workflows, repository-backed agent guidance"
seo_title: "Kujo Howl — Kujo Agent Skill"
seo_description: "Use this skill when creating, validating, rendering, reviewing, or maintaining Howl showcase artifacts for Kujo examples: `howl init`, `howl validate`, `howl list`, `howl show`, `howl caption`, `howl render`, `howl.json`, `examples/*.kujo`, `dist/howl/`, deterministic SVG/Markdown/HTML cards, static galleries, social captions, or Howl CLI/source/test changes."
---

## What it covers

Use this skill when creating, validating, rendering, reviewing, or maintaining Howl showcase artifacts for Kujo examples: `howl init`, `howl validate`, `howl list`, `howl show`, `howl caption`, `howl render`, `howl.json`, `examples/*.kujo`, `dist/howl/`, deterministic SVG/Markdown/HTML cards, static galleries, social captions, or Howl CLI/source/test changes.

## Released guidance

- Check setup with `howl help` or `KUJO=/path/to/kujo/target/release/kujo ./bin/howl help`.
- Prefer `howl validate` before rendering, committing artifacts, or editing showcase metadata.
- Use `howl list` to discover card ids, then `howl show <id>` to inspect the manifest metadata and code preview.
- Use `howl caption <id>` for deterministic share copy, and `howl caption <id> --platform x` for the X.com-bounded variant.
- Use `howl render` to regenerate `dist/howl/`, or `howl render --out <dir> --format svg|html|markdown` for targeted output.

## Release boundary

This page reflects the 0.2.0 technical preview on 2026-08-11. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-howl-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-howl-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/main/SKILLS_INDEX.md)
