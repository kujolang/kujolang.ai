---
title: "Kujo Enterprise Automation"
custom_url: "kujo-enterprise-automation"
description: "Use this skill when designing Kujo automation for CI, policy gates, operational workflows, enterprise-safe scripting, audit logs, machine-readable reports, or capability-minimal production runs."
featured_image: "/assets/images/ecosystem/skill-kujo-enterprise-automation.webp"
social_image: "/assets/images/social/kujo-enterprise-automation.jpg"
section: "Agent Skill"
order: "200"
install_command: "mkdir -p ~/.codex/skills && cp -R skills/kujo-enterprise-automation ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-enterprise-automation/SKILL.md"
launch_story: "One of 83 focused, repository-backed skills in the Kujo Skills 0.2.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.2.0"
last_updated: "2026-08-11"
keywords: "Kujo Enterprise Automation, Kujo Agent Skill, kujo-enterprise-automation, repository-backed agent guidance"
seo_title: "Kujo Enterprise Automation — Kujo Agent Skill"
seo_description: "Use this skill when designing Kujo automation for CI, policy gates, operational workflows, enterprise-safe scripting, audit logs, machine-readable reports, or capability-minimal production runs."
---

## What it covers

Use this skill when designing Kujo automation for CI, policy gates, operational workflows, enterprise-safe scripting, audit logs, machine-readable reports, or capability-minimal production runs.

## Released guidance

- Use VM default: `kujo run workflow.kujo -- args`.
- Reserve stdout for machine-readable JSON when the workflow is consumed by automation.
- Treat non-zero exit codes as authoritative failure signals.
- Keep policy inputs explicit and validated at startup.
- Prefer `kujo package-install --frozen` to verify manifests/lockfiles without rewriting them.

## Release boundary

This page reflects the 0.2.0 technical preview on 2026-08-11. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-enterprise-automation skill on GitHub](https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-enterprise-automation/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/main/SKILLS_INDEX.md)
