---
title: "Kujo Readiness Auditor"
custom_url: "kujo-readiness-auditor"
description: "Use this skill when auditing Kujo repositories for recurring readiness posture, release preparedness, production gaps, evidence quality, or weekly/monthly readiness reports across ShipCheck, Fence, Eval, Concord, ChangeBucket, RunLedger, and Casefile outputs."
excerpt: "Use this skill when auditing Kujo repositories for recurring readiness posture, release preparedness, production gaps, evidence quality, or weekly/monthly readiness reports across ShipCheck, Fence,…"
featured_image: "/assets/images/ecosystem/skill-kujo-readiness-auditor.webp"
social_image: "/assets/images/social/kujo-readiness-auditor.jpg"
section: "Agent Skill"
order: "340"
install_command: "mkdir -p ~/.codex/skills && cp -R skills/kujo-readiness-auditor ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-readiness-auditor/SKILL.md"
launch_story: "One of 83 focused, repository-backed skills in the Kujo Skills 0.2.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.2.0"
last_updated: "2026-08-11"
keywords: "Kujo Readiness Auditor, Kujo Agent Skill, kujo-readiness-auditor, repository-backed agent guidance"
seo_title: "Kujo Readiness Auditor — Kujo Agent Skill"
seo_description: "Use this skill when auditing Kujo repositories for recurring readiness posture, release preparedness, production gaps, evidence quality, or weekly/monthly readiness reports across ShipCheck, Fence, Eval, Concord, ChangeBucket, RunLedger, and Casefile outputs."
---

## What it covers

Use this skill when auditing Kujo repositories for recurring readiness posture, release preparedness, production gaps, evidence quality, or weekly/monthly readiness reports across ShipCheck, Fence, Eval, Concord, ChangeBucket, RunLedger, and Casefile outputs.

## Released guidance

- Use for weekly or monthly readiness audits of one or more Kujo repos.
- Focus on release blockers, drift, architecture boundaries, test/eval health, change footprint, evidence gaps, and next actions.
- Do not claim universal enterprise readiness unless the repo's own gates and live-environment evidence support it.
- Do not create broad roadmap docs; produce an audit report or focused backlog items.
- Repository: `README.md`, `AGENTS.md`, `docs/`, `tests/`, `scripts/`, `*.kujo`, manifests, lockfiles, CI config.

## Release boundary

This page reflects the 0.2.0 technical preview on 2026-08-11. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-readiness-auditor skill on GitHub](https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-readiness-auditor/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/main/SKILLS_INDEX.md)
