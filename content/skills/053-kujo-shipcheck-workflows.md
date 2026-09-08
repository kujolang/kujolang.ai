---
title: "Kujo ShipCheck"
custom_url: "kujo-shipcheck-workflows"
description: "Use this skill when running, reviewing, integrating, or maintaining ShipCheck release-readiness workflows for Kujo ecosystem repositories: `shipcheck.kujo`, `scan`, `checklist`, `gate`, `release-note`, `--format json`, CI release gates, markdown/json reports, release check catalogs, gate exit semantics, or ShipCheck CLI/source/test changes."
excerpt: "Use this skill when running, reviewing, integrating, or maintaining ShipCheck release-readiness workflows for Kujo ecosystem repositories."
featured_image: "/assets/images/ecosystem/skill-kujo-shipcheck-workflows.webp"
social_image: "/assets/images/social/kujo-shipcheck-workflows.jpg"
section: "Agent Skill"
order: "530"
install_command: "git clone --branch v0.7.0 --depth 1 https://github.com/kujolang/kujo-skills.git && mkdir -p ~/.codex/skills && cp -R kujo-skills/skills/kujo-shipcheck-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/v0.7.0/skills/kujo-shipcheck-workflows/SKILL.md"
launch_story: "One of 135 focused, repository-backed skills in the Kujo Skills 0.7.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.7.0"
last_updated: "2026-09-08"
keywords: "Kujo ShipCheck, Kujo Agent Skill, kujo-shipcheck-workflows, repository-backed agent guidance"
seo_title: "Kujo ShipCheck — Kujo Agent Skill"
seo_description: "Use this skill when running, reviewing, integrating, or maintaining ShipCheck release-readiness workflows for Kujo ecosystem repositories: `shipcheck.kujo`, `scan`, `checklist`, `gate`, `release-note`, `--format json`, CI release gates, markdown/json reports, release check catalogs, gate exit semantics, or ShipCheck CLI/source/test changes."
---

## What it covers

Use this skill when running, reviewing, integrating, or maintaining ShipCheck release-readiness workflows for Kujo ecosystem repositories: `shipcheck.kujo`, `scan`, `checklist`, `gate`, `release-note`, `--format json`, CI release gates, markdown/json reports, release check catalogs, gate exit semantics, or ShipCheck CLI/source/test changes.

Run the install command from a new working directory. If you already have the released checkout, copy the complete skill folder from it instead of cloning again.

## Released guidance

- Run `scan` first to surface repository health, code quality, documentation, and release metadata findings.
- Use `--format json` when a CI step, policy script, or follow-up analysis needs stable fields.
- `scan --format json` and `gate --format json` conform to `schemas/shipcheck-report.schema.json` for the current `1.x` line; consumers should rely on exit status plus `summary.gate_passed` and ignore unknown future fields.
- Run `checklist` when the user wants actionable release tasks in human-readable form.
- Run `gate` as the enforcement step after fixes. Do not use `scan` as a blocking gate.

## Release boundary

This page reflects the 0.7.0 technical preview on 2026-09-08. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-shipcheck-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/v0.7.0/skills/kujo-shipcheck-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/v0.7.0/SKILLS_INDEX.md)
