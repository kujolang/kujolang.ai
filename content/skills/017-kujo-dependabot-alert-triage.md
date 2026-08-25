---
title: "Kujo Dependabot Alert Triage"
custom_url: "kujo-dependabot-alert-triage"
description: "Use this skill when triaging GitHub Dependabot or security alerts across Kujo repos, summarizing affected repositories/packages/severity/status/patched versions/PR state/next actions, creating fix-ready tasks, or maintaining a Strata running list. Do not dismiss alerts or mutate GitHub security state without explicit authorization."
excerpt: "Use this skill when triaging GitHub Dependabot or security alerts across Kujo repos, summarizing affected repositories/packages/severity/status/patched versions/PR state/next actions, creating fix-ready tasks, or maintaining…"
featured_image: "/assets/images/ecosystem/skill-kujo-dependabot-alert-triage.webp"
social_image: "/assets/images/social/kujo-dependabot-alert-triage.jpg"
section: "Agent Skill"
order: "170"
install_command: "mkdir -p ~/.codex/skills && cp -R skills/kujo-dependabot-alert-triage ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-dependabot-alert-triage/SKILL.md"
launch_story: "One of 96 focused, repository-backed skills in the Kujo Skills 0.4.1 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.4.1"
last_updated: "2026-08-25"
keywords: "Kujo Dependabot Alert Triage, Kujo Agent Skill, kujo-dependabot-alert-triage, repository-backed agent guidance"
seo_title: "Kujo Dependabot Alert Triage — Kujo Agent Skill"
seo_description: "Use this skill when triaging GitHub Dependabot or security alerts across Kujo repos, summarizing affected repositories/packages/severity/status/patched versions/PR state/next actions, creating fix-ready tasks, or maintaining a Strata running list. Do not dismiss alerts or mutate GitHub security state without explicit authorization."
---

## What it covers

Use this skill when triaging GitHub Dependabot or security alerts across Kujo repos, summarizing affected repositories/packages/severity/status/patched versions/PR state/next actions, creating fix-ready tasks, or maintaining a Strata running list. Do not dismiss alerts or mutate GitHub security state without explicit authorization.

## Released guidance

- Use for recurring weekly/monthly Dependabot or GitHub security alert triage across in-scope Kujo repos.
- Summarize affected repo, package, ecosystem, manifest/lockfile, severity, alert status, patched version, existing PR state, and next action.
- Create fix-ready tasks or Spec/backlog entries when authorized.
- Maintain a compact Strata running list after triage.
- GitHub Dependabot/security alert surfaces, Dependabot PRs, security advisory metadata exposed by supported tools, manifests, lockfiles, audit reports, CI checks, and repository tests.

## Release boundary

This page reflects the 0.4.1 technical preview on 2026-08-25. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-dependabot-alert-triage skill on GitHub](https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-dependabot-alert-triage/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/main/SKILLS_INDEX.md)
