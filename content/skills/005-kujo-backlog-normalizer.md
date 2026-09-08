---
title: "Kujo Backlog Normalizer"
custom_url: "kujo-backlog-normalizer"
description: "Use this skill when converting Kujo audit findings, drift reports, release blockers, DocGen gaps, Dependabot/security triage, or recurring automation output into fix-ready backlog tasks using Scout, PatchBrief, ChangeBucket, Spec, ShipCheck, DocGen evidence, and RunLedger context."
excerpt: "Use this skill when converting Kujo audit findings, drift reports, release blockers, DocGen gaps, Dependabot/security triage, or recurring automation output into fix-ready backlog tasks…"
featured_image: "/assets/images/ecosystem/skill-kujo-backlog-normalizer.webp"
social_image: "/assets/images/social/kujo-backlog-normalizer.jpg"
section: "Agent Skill"
order: "50"
install_command: "git clone --branch v0.7.0 --depth 1 https://github.com/kujolang/kujo-skills.git && mkdir -p ~/.codex/skills && cp -R kujo-skills/skills/kujo-backlog-normalizer ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/v0.7.0/skills/kujo-backlog-normalizer/SKILL.md"
launch_story: "One of 135 focused, repository-backed skills in the Kujo Skills 0.7.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.7.0"
last_updated: "tag v0.7.0 Tagger: Robert DeVore <deviodigital@gmail.com> Kujo Skills v0.7.0: reusable video styles 2026-09-08"
keywords: "Kujo Backlog Normalizer, Kujo Agent Skill, kujo-backlog-normalizer, repository-backed agent guidance"
seo_title: "Kujo Backlog Normalizer — Kujo Agent Skill"
seo_description: "Use this skill when converting Kujo audit findings, drift reports, release blockers, DocGen gaps, Dependabot/security triage, or recurring automation output into fix-ready backlog tasks using Scout, PatchBrief, ChangeBucket, Spec, ShipCheck, DocGen evidence, and RunLedger context."
---

## What it covers

Use this skill when converting Kujo audit findings, drift reports, release blockers, DocGen gaps, Dependabot/security triage, or recurring automation output into fix-ready backlog tasks using Scout, PatchBrief, ChangeBucket, Spec, ShipCheck, DocGen evidence, and RunLedger context.

Run the install command from a new working directory. If you already have the released checkout, copy the complete skill folder from it instead of cloning again.

## Released guidance

- Use after readiness audits, docs drift audits, release gates, DocGen gap output, security triage, or dogfood runs.
- Normalize findings into actionable tasks with repo, owner role, acceptance evidence, dependencies, and suggested validation.
- Avoid vague roadmap prose and duplicate backlog items.
- Audit reports, tool JSON/Markdown, Casefile bundles, RunLedger receipts, DocGen gaps, Dependabot/security triage summaries.
- Repo files: `README.md`, `AGENTS.md`, docs, tests, scripts, manifests, lockfiles, CI config.

## Release boundary

This page reflects the 0.7.0 technical preview on tag v0.7.0
Tagger: Robert DeVore <deviodigital@gmail.com>

Kujo Skills v0.7.0: reusable video styles
2026-09-08. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-backlog-normalizer skill on GitHub](https://github.com/kujolang/kujo-skills/blob/v0.7.0/skills/kujo-backlog-normalizer/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/v0.7.0/SKILLS_INDEX.md)
