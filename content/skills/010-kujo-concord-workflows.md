---
title: "Kujo Concord Workflows"
custom_url: "kujo-concord-workflows"
description: "Use this skill when scanning, reporting, triaging, or maintaining Concord artifact-drift checks for Kujo ecosystem repositories: `concord scan`, `check`, `report`, `tasks`, `--format json`, `--output`, CLI/docs drift, Spec/Eval alignment, manifest/docs alignment, version consistency, example validity, source-of-truth findings, `.dogfood/concord/` outputs, or Concord CLI/source/test changes."
featured_image: "/assets/images/ecosystem/skill-kujo-concord-workflows.webp"
social_image: "/assets/images/social/kujo-concord-workflows.jpg"
section: "Agent Skill"
order: "100"
install_command: "mkdir -p ~/.codex/skills && cp -R skills/kujo-concord-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-concord-workflows/SKILL.md"
launch_story: "One of 83 focused, repository-backed skills in the Kujo Skills 0.2.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.2.0"
last_updated: "2026-08-11"
keywords: "Kujo Concord Workflows, Kujo Agent Skill, kujo-concord-workflows, repository-backed agent guidance"
seo_title: "Kujo Concord Workflows — Kujo Agent Skill"
seo_description: "Use this skill when scanning, reporting, triaging, or maintaining Concord artifact-drift checks for Kujo ecosystem repositories: `concord scan`, `check`, `report`, `tasks`, `--format json`, `--output`, CLI/docs drift, Spec/Eval alignment, manifest/docs alignment, version consistency, example validity, source-of-truth findings, `.dogfood/concord/` outputs, or Concord CLI/source/test changes."
---

## What it covers

Use this skill when scanning, reporting, triaging, or maintaining Concord artifact-drift checks for Kujo ecosystem repositories: `concord scan`, `check`, `report`, `tasks`, `--format json`, `--output`, CLI/docs drift, Spec/Eval alignment, manifest/docs alignment, version consistency, example validity, source-of-truth findings, `.dogfood/concord/` outputs, or Concord CLI/source/test changes.

## Released guidance

- Run `scan` for a full artifact drift report before changing docs, specs, evals, manifests, examples, or CLI contracts.
- Prefer `--format json` when another tool or follow-up script needs stable fields. The JSON report includes `findings` with `id`, `severity`, `confidence`, `category`, `title`, and `summary`.
- Use `--output <path>` for durable reports. Keep generated dogfood artifacts under `.dogfood/concord/` when working inside the Concord repo.
- Use `tasks` after a scan when the user wants actionable fix cards rather than the full report.
- Summarize findings by severity, category, likely source artifact, likely target artifact, and whether human review is required.

## Release boundary

This page reflects the 0.2.0 technical preview on 2026-08-11. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-concord-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-concord-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/main/SKILLS_INDEX.md)
