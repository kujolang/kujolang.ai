---
title: "Kujo DocGen Public Docs Refresh"
custom_url: "kujo-docgen-public-docs-refresh"
description: "Use this skill when refreshing Kujo DocGen public docs, generated documentation, agent-readable JSON/gap outputs, coverage gates, README/reference alignment, or example smoke policy after readiness or docs-drift evidence. Use `kujo docgen` and validate before committing; do not publish or deploy without explicit supported authorization."
excerpt: "Use this skill when refreshing Kujo DocGen public docs, generated documentation, agent-readable JSON/gap outputs, coverage gates, README/reference alignment, or example smoke policy after readiness…"
featured_image: "/assets/images/ecosystem/skill-kujo-docgen-public-docs-refresh.webp"
social_image: "/assets/images/social/kujo-docgen-public-docs-refresh.jpg"
section: "Agent Skill"
order: "180"
install_command: "mkdir -p ~/.codex/skills && cp -R skills/kujo-docgen-public-docs-refresh ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-docgen-public-docs-refresh/SKILL.md"
launch_story: "One of 83 focused, repository-backed skills in the Kujo Skills 0.2.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.2.0"
last_updated: "2026-08-11"
keywords: "Kujo DocGen Public Docs Refresh, Kujo Agent Skill, kujo-docgen-public-docs-refresh, repository-backed agent guidance"
seo_title: "Kujo DocGen Public Docs Refresh — Kujo Agent Skill"
seo_description: "Use this skill when refreshing Kujo DocGen public docs, generated documentation, agent-readable JSON/gap outputs, coverage gates, README/reference alignment, or example smoke policy after readiness or docs-drift evidence. Use `kujo docgen` and validate before committing; do not publish or deploy without explicit supported authorization."
---

## What it covers

Use this skill when refreshing Kujo DocGen public docs, generated documentation, agent-readable JSON/gap outputs, coverage gates, README/reference alignment, or example smoke policy after readiness or docs-drift evidence. Use `kujo docgen` and validate before committing; do not publish or deploy without explicit supported authorization.

## Released guidance

- Use after readiness or docs-drift evidence shows generated/public docs, gap outputs, README/reference alignment, or examples are stale.
- Use `kujo docgen` and the `kujo-docgen-agent-readable` skill before choosing exact flags.
- Refresh generated docs, agent-readable JSON, gap outputs, coverage gates, and example smoke policy when the repo supports those outputs.
- Do not publish, deploy, upload, or release docs without explicit authorization and a supported workflow.
- `docs/DOCGEN.md`, `docs/CLI_MACHINE_READABLE_CONTRACTS.md`, README/reference docs, examples, DocGen tests, generated output directories, gap JSON/Markdown, AI task output.

## Release boundary

This page reflects the 0.2.0 technical preview on 2026-08-11. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-docgen-public-docs-refresh skill on GitHub](https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-docgen-public-docs-refresh/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/main/SKILLS_INDEX.md)
