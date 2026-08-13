---
title: "Kujo Tribunal"
custom_url: "kujo-tribunal-workflows"
description: "Use this skill when running, reviewing, integrating, or maintaining Tribunal local decision-evidence workflows: `tribunal review`, `resume`, `compare`, `re-review`, `kill`, `validate`, `audit`, `verify`, bundle/store/provenance commands, signed evidence, trust policies, run artifacts, schemas, release gates, or Tribunal source/docs changes."
excerpt: "Use this skill when running, reviewing, integrating, or maintaining Tribunal local decision-evidence workflows."
featured_image: "/assets/images/ecosystem/skill-kujo-tribunal-workflows.webp"
social_image: "/assets/images/social/kujo-tribunal-workflows.jpg"
section: "Agent Skill"
order: "540"
install_command: "mkdir -p ~/.codex/skills && cp -R skills/kujo-tribunal-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-tribunal-workflows/SKILL.md"
launch_story: "One of 83 focused, repository-backed skills in the Kujo Skills 0.2.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.2.0"
last_updated: "2026-08-11"
keywords: "Kujo Tribunal, Kujo Agent Skill, kujo-tribunal-workflows, repository-backed agent guidance"
seo_title: "Kujo Tribunal — Kujo Agent Skill"
seo_description: "Use this skill when running, reviewing, integrating, or maintaining Tribunal local decision-evidence workflows: `tribunal review`, `resume`, `compare`, `re-review`, `kill`, `validate`, `audit`, `verify`, bundle/store/provenance commands, signed evidence, trust policies, run artifacts, schemas, release gates, or Tribunal source/docs changes."
---

## What it covers

Use this skill when running, reviewing, integrating, or maintaining Tribunal local decision-evidence workflows: `tribunal review`, `resume`, `compare`, `re-review`, `kill`, `validate`, `audit`, `verify`, bundle/store/provenance commands, signed evidence, trust policies, run artifacts, schemas, release gates, or Tribunal source/docs changes.

## Released guidance

- Mock mode is deterministic, offline, credential-free, and the default.
- Live provider calls go through the adjacent Kujo AI SDK; Tribunal owns hearing orchestration and evidence, not provider transport.
- Completed hearings write run artifacts under `tribunal-runs/<run-id>/` by default, including record, receipt, manifest, event log, prompts, testimony, ruling, decision packet, and optional signature.
- Exit codes are stable: `0` success, `1` runtime failure, `2` usage/configuration error, and `3` integrity failure.
- Normal production verification uses `tribunal audit <run-id> --trust-policy <path> --target audit --require-signature --json`.

## Release boundary

This page reflects the 0.2.0 technical preview on 2026-08-11. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-tribunal-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-tribunal-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/main/SKILLS_INDEX.md)
