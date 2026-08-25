---
title: "Kujo Docs Drift Auditor"
custom_url: "kujo-docs-drift-auditor"
description: "Use this skill when auditing Kujo documentation drift, README/reference mismatches, generated-doc staleness, CLI/docs drift, example validity, or recurring docs health using Concord, Scout, PatchBrief, Lens, DocGen, and Muzzle evidence."
excerpt: "Use this skill when auditing Kujo documentation drift, README/reference mismatches, generated-doc staleness, CLI/docs drift, example validity, or recurring docs health using Concord, Scout, PatchBrief,…"
featured_image: "/assets/images/ecosystem/skill-kujo-docs-drift-auditor.webp"
social_image: "/assets/images/social/kujo-docs-drift-auditor.jpg"
section: "Agent Skill"
order: "210"
install_command: "mkdir -p ~/.codex/skills && cp -R skills/kujo-docs-drift-auditor ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-docs-drift-auditor/SKILL.md"
launch_story: "One of 96 focused, repository-backed skills in the Kujo Skills 0.4.1 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.4.1"
last_updated: "2026-08-25"
keywords: "Kujo Docs Drift Auditor, Kujo Agent Skill, kujo-docs-drift-auditor, repository-backed agent guidance"
seo_title: "Kujo Docs Drift Auditor — Kujo Agent Skill"
seo_description: "Use this skill when auditing Kujo documentation drift, README/reference mismatches, generated-doc staleness, CLI/docs drift, example validity, or recurring docs health using Concord, Scout, PatchBrief, Lens, DocGen, and Muzzle evidence."
---

## What it covers

Use this skill when auditing Kujo documentation drift, README/reference mismatches, generated-doc staleness, CLI/docs drift, example validity, or recurring docs health using Concord, Scout, PatchBrief, Lens, DocGen, and Muzzle evidence.

## Released guidance

- Use for weekly/monthly docs drift checks across Kujo repos or for a focused repo after source changes.
- Compare docs against current code, CLI help, tests, examples, generated artifacts, and machine-readable contracts.
- Use Lens only when UI docs or screenshots require browser proof.
- Avoid broad process docs; report drift and precise fixes.
- Source: `README.md`, `AGENTS.md`, docs, examples, tests, scripts, `*.kujo`, `src/`, CLI help output, generated docs.

## Release boundary

This page reflects the 0.4.1 technical preview on 2026-08-25. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-docs-drift-auditor skill on GitHub](https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-docs-drift-auditor/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/main/SKILLS_INDEX.md)
