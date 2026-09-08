---
title: "Kujo Runtime Parity"
custom_url: "kujo-runtime-parity"
description: "Use this skill when investigating VM versus interpreter behavior, deciding runtime flags, adding language/runtime surfaces, updating parity tests, or preventing accidental interpreter-default workflows."
excerpt: "Use this skill when investigating VM versus interpreter behavior, deciding runtime flags, adding language/runtime surfaces, updating parity tests, or preventing accidental interpreter-default workflows."
featured_image: "/assets/images/ecosystem/skill-kujo-runtime-parity.webp"
social_image: "/assets/images/social/kujo-runtime-parity.jpg"
section: "Agent Skill"
order: "480"
install_command: "git clone --branch v0.7.0 --depth 1 https://github.com/kujolang/kujo-skills.git && mkdir -p ~/.codex/skills && cp -R kujo-skills/skills/kujo-runtime-parity ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/v0.7.0/skills/kujo-runtime-parity/SKILL.md"
launch_story: "One of 135 focused, repository-backed skills in the Kujo Skills 0.7.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.7.0"
last_updated: "2026-09-08"
keywords: "Kujo Runtime Parity, Kujo Agent Skill, kujo-runtime-parity, repository-backed agent guidance"
seo_title: "Kujo Runtime Parity — Kujo Agent Skill"
seo_description: "Use this skill when investigating VM versus interpreter behavior, deciding runtime flags, adding language/runtime surfaces, updating parity tests, or preventing accidental interpreter-default workflows."
---

## What it covers

Use this skill when investigating VM versus interpreter behavior, deciding runtime flags, adding language/runtime surfaces, updating parity tests, or preventing accidental interpreter-default workflows.

Run the install command from a new working directory. If you already have the released checkout, copy the complete skill folder from it instead of cloning again.

## Released guidance

- Day-to-day script: `kujo run <file>`.
- Debug/compat isolation: `kujo run --interpreter <file>`.
- Fixture compatibility sweep: `kujo test --runtime dual`.
- Strict VM gate: `kujo test --runtime vm`.
- Parity drift suite: `cargo test --test vm_interpreter_parity_surfaces`.

## Release boundary

This page reflects the 0.7.0 technical preview on 2026-09-08. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-runtime-parity skill on GitHub](https://github.com/kujolang/kujo-skills/blob/v0.7.0/skills/kujo-runtime-parity/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/v0.7.0/SKILLS_INDEX.md)
