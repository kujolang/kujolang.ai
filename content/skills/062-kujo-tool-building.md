---
title: "Kujo Tool Building"
custom_url: "kujo-tool-building"
description: "Use this skill when building practical Kujo CLI tools, quality gates, policy checkers, repo scanners, JSON-reporting scripts, or local automation that needs deterministic arguments, output, and exit behavior."
excerpt: "Use this skill when building practical Kujo CLI tools, quality gates, policy checkers, repo scanners, JSON-reporting scripts, or local automation that needs deterministic arguments,…"
featured_image: "/assets/images/ecosystem/skill-kujo-tool-building.webp"
social_image: "/assets/images/social/kujo-tool-building.jpg"
section: "Agent Skill"
order: "620"
install_command: "mkdir -p ~/.codex/skills && cp -R skills/kujo-tool-building ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-tool-building/SKILL.md"
launch_story: "One of 96 focused, repository-backed skills in the Kujo Skills 0.4.1 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.4.1"
last_updated: "2026-08-25"
keywords: "Kujo Tool Building, Kujo Agent Skill, kujo-tool-building, repository-backed agent guidance"
seo_title: "Kujo Tool Building — Kujo Agent Skill"
seo_description: "Use this skill when building practical Kujo CLI tools, quality gates, policy checkers, repo scanners, JSON-reporting scripts, or local automation that needs deterministic arguments, output, and exit behavior."
---

## What it covers

Use this skill when building practical Kujo CLI tools, quality gates, policy checkers, repo scanners, JSON-reporting scripts, or local automation that needs deterministic arguments, output, and exit behavior.

## Released guidance

- `0`: success.
- `1`: policy/gate failure.
- `2`: usage error.
- `4`: runtime/semantic failure.
- For JSON tools, emit one machine-readable payload on stdout and keep human text off stdout.

## Release boundary

This page reflects the 0.4.1 technical preview on 2026-08-25. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-tool-building skill on GitHub](https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-tool-building/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/main/SKILLS_INDEX.md)
