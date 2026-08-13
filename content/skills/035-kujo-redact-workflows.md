---
title: "Kujo Redact Workflows"
custom_url: "kujo-redact-workflows"
description: "Use this skill when scanning, sanitizing, verifying, packing, or maintaining Redact local deterministic anonymization workflows: `redact.kujo`, `scan`, `sanitize`, `verify`, `pack`, policy YAML files, `.redact/runs/` audit artifacts, leakage checks, unsafe originals, AI-stub boundaries, or Redact CLI/source/test changes."
featured_image: "/assets/images/ecosystem/skill-kujo-redact-workflows.webp"
social_image: "/assets/images/social/kujo-redact-workflows.jpg"
section: "Agent Skill"
order: "350"
install_command: "mkdir -p ~/.codex/skills && cp -R skills/kujo-redact-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-redact-workflows/SKILL.md"
launch_story: "One of 83 focused, repository-backed skills in the Kujo Skills 0.2.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.2.0"
last_updated: "2026-08-11"
keywords: "Kujo Redact Workflows, Kujo Agent Skill, kujo-redact-workflows, repository-backed agent guidance"
seo_title: "Kujo Redact Workflows — Kujo Agent Skill"
seo_description: "Use this skill when scanning, sanitizing, verifying, packing, or maintaining Redact local deterministic anonymization workflows: `redact.kujo`, `scan`, `sanitize`, `verify`, `pack`, policy YAML files, `.redact/runs/` audit artifacts, leakage checks, unsafe originals, AI-stub boundaries, or Redact CLI/source/test changes."
---

## What it covers

Use this skill when scanning, sanitizing, verifying, packing, or maintaining Redact local deterministic anonymization workflows: `redact.kujo`, `scan`, `sanitize`, `verify`, `pack`, policy YAML files, `.redact/runs/` audit artifacts, leakage checks, unsafe originals, AI-stub boundaries, or Redact CLI/source/test changes.

## Released guidance

- Supported inputs are `.txt`, `.md`, and the `-` stdin contract; current Kujo VM builds return an unsupported-runtime error for stdin rather than reading it silently.
- Supported policies are the documented flat-YAML subset with category actions, term dictionaries, and optional role mappings.
- Detection is deterministic: email, phone, URL/domain, credit card with Luhn, API key/token, money, date, configured names, and strategy phrases.
- Transformations include `remove`, `placeholder`, `role-preserve`, `generalize`, `range`, and `date-generalize`.
- Audit output lives under `.redact/runs/<timestamp>/` with manifests, detections, decisions, transformations, verifier report, policy snapshot, hashes, and warnings.

## Release boundary

This page reflects the 0.2.0 technical preview on 2026-08-11. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-redact-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-redact-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/main/SKILLS_INDEX.md)
