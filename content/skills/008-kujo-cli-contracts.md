---
title: "Kujo CLI Contracts"
custom_url: "kujo-cli-contracts"
description: "Use this skill when changing Kujo CLI output, exit codes, diagnostics, `--json` payloads, `--json-runtime-diagnostics`, LSP helper JSON, formatter/linter/docgen JSON, or automation/toolchain compatibility behavior."
featured_image: "/assets/images/ecosystem/skill-kujo-cli-contracts.webp"
social_image: "/assets/images/social/kujo-cli-contracts.jpg"
section: "Agent Skill"
order: "80"
install_command: "mkdir -p ~/.codex/skills && cp -R skills/kujo-cli-contracts ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-cli-contracts/SKILL.md"
launch_story: "One of 83 focused, repository-backed skills in the Kujo Skills 0.2.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.2.0"
last_updated: "2026-08-11"
keywords: "Kujo CLI Contracts, Kujo Agent Skill, kujo-cli-contracts, repository-backed agent guidance"
seo_title: "Kujo CLI Contracts — Kujo Agent Skill"
seo_description: "Use this skill when changing Kujo CLI output, exit codes, diagnostics, `--json` payloads, `--json-runtime-diagnostics`, LSP helper JSON, formatter/linter/docgen JSON, or automation/toolchain compatibility behavior."
---

## What it covers

Use this skill when changing Kujo CLI output, exit codes, diagnostics, `--json` payloads, `--json-runtime-diagnostics`, LSP helper JSON, formatter/linter/docgen JSON, or automation/toolchain compatibility behavior.

## Released guidance

- `0`: success
- `1`: command/gate failure
- `2`: usage or argument parse error
- `3`: lexer/parser diagnostic failure
- `4`: runtime semantic/execution failure

## Release boundary

This page reflects the 0.2.0 technical preview on 2026-08-11. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-cli-contracts skill on GitHub](https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-cli-contracts/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/main/SKILLS_INDEX.md)
