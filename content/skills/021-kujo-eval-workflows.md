---
title: "Kujo Eval Workflows"
custom_url: "kujo-eval-workflows"
description: "Use this skill when creating, running, debugging, or maintaining Kujo Eval deterministic evaluation suites: `eval.json`, `kujo run main.kujo run`, `report`, `compare`, `lint`, `list-checks`, `snapshots`, `policy-explain`, `verify-manifest`, snapshot tests, JSON/HTTP/file/command checks, Eval artifacts, policy profiles, CI gates, or Eval CLI/source/test changes."
featured_image: "/assets/images/ecosystem/skill-kujo-eval-workflows.webp"
social_image: "/assets/images/social/kujo-eval-workflows.jpg"
section: "Agent Skill"
order: "210"
install_command: "mkdir -p ~/.codex/skills && cp -R skills/kujo-eval-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-eval-workflows/SKILL.md"
launch_story: "One of 83 focused, repository-backed skills in the Kujo Skills 0.2.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.2.0"
last_updated: "2026-08-11"
keywords: "Kujo Eval Workflows, Kujo Agent Skill, kujo-eval-workflows, repository-backed agent guidance"
seo_title: "Kujo Eval Workflows — Kujo Agent Skill"
seo_description: "Use this skill when creating, running, debugging, or maintaining Kujo Eval deterministic evaluation suites: `eval.json`, `kujo run main.kujo run`, `report`, `compare`, `lint`, `list-checks`, `snapshots`, `policy-explain`, `verify-manifest`, snapshot tests, JSON/HTTP/file/command checks, Eval artifacts, policy profiles, CI gates, or Eval CLI/source/test changes."
---

## What it covers

Use this skill when creating, running, debugging, or maintaining Kujo Eval deterministic evaluation suites: `eval.json`, `kujo run main.kujo run`, `report`, `compare`, `lint`, `list-checks`, `snapshots`, `policy-explain`, `verify-manifest`, snapshot tests, JSON/HTTP/file/command checks, Eval artifacts, policy profiles, CI gates, or Eval CLI/source/test changes.

## Released guidance

- `examples/release_gate_suite.json`: minimal passing smoke/release suite.
- `examples/enterprise_cli_quality_gate.json`: policy-first CLI checks.
- `examples/enterprise_api_contract_gate.json`: fixture-backed API contract checks.
- `examples/enterprise_agent_output_gate.json`: agent output structure/content checks.
- `examples/policy_profile_release_gate.json`: profile-driven policy defaults.

## Release boundary

This page reflects the 0.2.0 technical preview on 2026-08-11. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-eval-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-eval-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/main/SKILLS_INDEX.md)
