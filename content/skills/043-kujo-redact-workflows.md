---
title: "Kujo Redact"
custom_url: "kujo-redact-workflows"
description: "Use this skill when scanning, sanitizing, verifying, packing, or maintaining Redact local deterministic anonymization workflows: `redact.kujo`, `scan`, `sanitize`, `verify`, `pack`, policy YAML files, `.redact/runs/` audit artifacts, leakage checks, unsafe originals, AI-stub boundaries, or Redact CLI/source/test changes."
excerpt: "Use this skill when scanning, sanitizing, verifying, packing, or maintaining Redact local deterministic anonymization workflows."
featured_image: "/assets/images/ecosystem/skill-kujo-redact-workflows.webp"
social_image: "/assets/images/social/kujo-redact-workflows.jpg"
section: "Agent Skill"
order: "430"
install_command: "git clone --branch v0.7.0 --depth 1 https://github.com/kujolang/kujo-skills.git && mkdir -p ~/.codex/skills && cp -R kujo-skills/skills/kujo-redact-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/v0.7.0/skills/kujo-redact-workflows/SKILL.md"
launch_story: "One of 135 focused, repository-backed skills in the Kujo Skills 0.7.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.7.0"
last_updated: "2026-09-08"
keywords: "Kujo Redact, Kujo Agent Skill, kujo-redact-workflows, repository-backed agent guidance"
seo_title: "Kujo Redact — Kujo Agent Skill"
seo_description: "Use this skill when scanning, sanitizing, verifying, packing, or maintaining Redact local deterministic anonymization workflows: `redact.kujo`, `scan`, `sanitize`, `verify`, `pack`, policy YAML files, `.redact/runs/` audit artifacts, leakage checks, unsafe originals, AI-stub boundaries, or Redact CLI/source/test changes."
---

## What it covers

Use this skill when scanning, sanitizing, verifying, packing, or maintaining Redact local deterministic anonymization workflows: `redact.kujo`, `scan`, `sanitize`, `verify`, `pack`, policy YAML files, `.redact/runs/` audit artifacts, leakage checks, unsafe originals, AI-stub boundaries, or Redact CLI/source/test changes.

Run the install command from a new working directory. If you already have the released checkout, copy the complete skill folder from it instead of cloning again.

## Released guidance

- Supported inputs are `.txt`, `.md`, and the `-` stdin contract; current Kujo VM builds return an unsupported-runtime error for stdin rather than reading it silently.
- Supported policies are the documented flat-YAML subset with category actions, term dictionaries, and optional role mappings.
- Detection is deterministic: email, phone, URL/domain, credit card with Luhn, API key/token, money, date, configured names, and strategy phrases.
- Transformations include `remove`, `placeholder`, `role-preserve`, `generalize`, `range`, and `date-generalize`.
- Audit output lives under `.redact/runs/<timestamp>/` with manifests, detections, decisions, transformations, verifier report, policy snapshot, hashes, and warnings.

## Release boundary

This page reflects the 0.7.0 technical preview on 2026-09-08. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-redact-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/v0.7.0/skills/kujo-redact-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/v0.7.0/SKILLS_INDEX.md)
