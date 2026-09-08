---
title: "Kujo CLI Contracts"
custom_url: "kujo-cli-contracts"
description: "Use this skill when changing Kujo CLI output, exit codes, diagnostics, `--json` payloads, `--json-runtime-diagnostics`, LSP helper JSON, formatter/linter/docgen JSON, or automation/toolchain compatibility behavior."
excerpt: "Use this skill when changing Kujo CLI output, exit codes, diagnostics, `--json` payloads, `--json-runtime-diagnostics`, LSP helper JSON, formatter/linter/docgen JSON, or automation/toolchain compatibility behavior."
featured_image: "/assets/images/ecosystem/skill-kujo-cli-contracts.webp"
social_image: "/assets/images/social/kujo-cli-contracts.jpg"
section: "Agent Skill"
order: "100"
install_command: "git clone --branch v0.7.0 --depth 1 https://github.com/kujolang/kujo-skills.git && mkdir -p ~/.codex/skills && cp -R kujo-skills/skills/kujo-cli-contracts ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/v0.7.0/skills/kujo-cli-contracts/SKILL.md"
launch_story: "One of 135 focused, repository-backed skills in the Kujo Skills 0.7.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.7.0"
last_updated: "tag v0.7.0 Tagger: Robert DeVore <deviodigital@gmail.com> Kujo Skills v0.7.0: reusable video styles 2026-09-08"
keywords: "Kujo CLI Contracts, Kujo Agent Skill, kujo-cli-contracts, repository-backed agent guidance"
seo_title: "Kujo CLI Contracts — Kujo Agent Skill"
seo_description: "Use this skill when changing Kujo CLI output, exit codes, diagnostics, `--json` payloads, `--json-runtime-diagnostics`, LSP helper JSON, formatter/linter/docgen JSON, or automation/toolchain compatibility behavior."
---

## What it covers

Use this skill when changing Kujo CLI output, exit codes, diagnostics, `--json` payloads, `--json-runtime-diagnostics`, LSP helper JSON, formatter/linter/docgen JSON, or automation/toolchain compatibility behavior.

Run the install command from a new working directory. If you already have the released checkout, copy the complete skill folder from it instead of cloning again.

## Released guidance

- `0`: success
- `1`: command/gate failure
- `2`: usage or argument parse error
- `3`: lexer/parser diagnostic failure
- `4`: runtime semantic/execution failure

## Release boundary

This page reflects the 0.7.0 technical preview on tag v0.7.0
Tagger: Robert DeVore <deviodigital@gmail.com>

Kujo Skills v0.7.0: reusable video styles
2026-09-08. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-cli-contracts skill on GitHub](https://github.com/kujolang/kujo-skills/blob/v0.7.0/skills/kujo-cli-contracts/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/v0.7.0/SKILLS_INDEX.md)
