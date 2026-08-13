---
title: "Kujo Core Language"
custom_url: "kujo-core-language"
description: "Use this skill when writing, editing, explaining, or reviewing Kujo `.kujo` source code, including syntax, bindings, imports, functions, control flow, collections, truthiness, runtime errors, and VM-first execution defaults."
excerpt: "Use this skill when writing, editing, explaining, or reviewing Kujo `.kujo` source code, including syntax, bindings, imports, functions, control flow, collections, truthiness, runtime errors,…"
featured_image: "/assets/images/ecosystem/skill-kujo-core-language.webp"
social_image: "/assets/images/social/kujo-core-language.jpg"
section: "Agent Skill"
order: "120"
install_command: "mkdir -p ~/.codex/skills && cp -R skills/kujo-core-language ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-core-language/SKILL.md"
launch_story: "One of 83 focused, repository-backed skills in the Kujo Skills 0.2.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.2.0"
last_updated: "2026-08-11"
keywords: "Kujo Core Language, Kujo Agent Skill, kujo-core-language, repository-backed agent guidance"
seo_title: "Kujo Core Language — Kujo Agent Skill"
seo_description: "Use this skill when writing, editing, explaining, or reviewing Kujo `.kujo` source code, including syntax, bindings, imports, functions, control flow, collections, truthiness, runtime errors, and VM-first execution defaults."
---

## What it covers

Use this skill when writing, editing, explaining, or reviewing Kujo `.kujo` source code, including syntax, bindings, imports, functions, control flow, collections, truthiness, runtime errors, and VM-first execution defaults.

## Released guidance

- Write `.kujo` files using current syntax from `docs/LANGUAGE_SPEC.md` and canonical examples, not legacy expected-fail examples.
- Run ordinary scripts with `kujo run <file>`; VM is the default path.
- Use `--interpreter` only for explicit compatibility/debug isolation.
- Prefer `let` for immutable bindings, `mut` for bindings that are reassigned or mutated, and `const` for constants.
- `name := value` updates an existing mutable binding when present; otherwise it creates a mutable binding in the current scope.

## Release boundary

This page reflects the 0.2.0 technical preview on 2026-08-11. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-core-language skill on GitHub](https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-core-language/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/main/SKILLS_INDEX.md)
