---
title: "Kujo Skill Auditor"
custom_url: "kujo-skill-auditor"
description: "Use this skill when reviewing, refreshing, or auditing the Kujo skills pack so each `skills/*/SKILL.md` file matches current Kujo tool behavior, commands, docs, tests, safety boundaries, and repo reality. Use for weekly skill maintenance, stale skill checks, trigger/index updates, or when Kujo tools changed and their agent skills may need synchronization."
excerpt: "Use this skill when reviewing, refreshing, or auditing the Kujo skills pack so each `skills/*/SKILL.md` file matches current Kujo tool behavior, commands, docs, tests,…"
featured_image: "/assets/images/ecosystem/skill-kujo-skill-auditor.webp"
social_image: "/assets/images/social/kujo-skill-auditor.jpg"
section: "Agent Skill"
order: "560"
install_command: "mkdir -p ~/.codex/skills && cp -R skills/kujo-skill-auditor ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-skill-auditor/SKILL.md"
launch_story: "One of 96 focused, repository-backed skills in the Kujo Skills 0.4.1 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.4.1"
last_updated: "2026-08-25"
keywords: "Kujo Skill Auditor, Kujo Agent Skill, kujo-skill-auditor, repository-backed agent guidance"
seo_title: "Kujo Skill Auditor — Kujo Agent Skill"
seo_description: "Use this skill when reviewing, refreshing, or auditing the Kujo skills pack so each `skills/*/SKILL.md` file matches current Kujo tool behavior, commands, docs, tests, safety boundaries, and repo reality. Use for weekly skill maintenance, stale skill checks, trigger/index updates, or when Kujo tools changed and their agent skills may need synchronization."
---

## What it covers

Use this skill when reviewing, refreshing, or auditing the Kujo skills pack so each `skills/*/SKILL.md` file matches current Kujo tool behavior, commands, docs, tests, safety boundaries, and repo reality. Use for weekly skill maintenance, stale skill checks, trigger/index updates, or when Kujo tools changed and their agent skills may need synchronization.

## Released guidance

- Verify behavior from repo artifacts before editing: `README.md`, `AGENTS.md`, docs, command inventories, manifests, entrypoint `.kujo` files, tests, scripts, and recent commits.
- Keep skills short, imperative, and repo-backed. Preserve the existing Kujo skill style.
- Update only claims that are stale, incomplete, misleading, or missing important safety/test/CLI contract details.
- Do not invent commands, flags, artifacts, tests, release status, or safety guarantees.
- Do not hand-edit generated output in target tool repos unless that tool's docs say it is source-owned.

## Release boundary

This page reflects the 0.4.1 technical preview on 2026-08-25. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-skill-auditor skill on GitHub](https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-skill-auditor/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/main/SKILLS_INDEX.md)
