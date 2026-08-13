---
title: "Kujo Testing And Release Gates"
custom_url: "kujo-testing-release-gates"
description: "Use this skill when testing Kujo scripts, examples, docs, security behavior, runtime parity, CLI contracts, or Rust implementation changes, and when preparing or reviewing release-gate readiness."
excerpt: "Use this skill when testing Kujo scripts, examples, docs, security behavior, runtime parity, CLI contracts, or Rust implementation changes, and when preparing or reviewing…"
featured_image: "/assets/images/ecosystem/skill-kujo-testing-release-gates.webp"
social_image: "/assets/images/social/kujo-testing-release-gates.jpg"
section: "Agent Skill"
order: "520"
install_command: "mkdir -p ~/.codex/skills && cp -R skills/kujo-testing-release-gates ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-testing-release-gates/SKILL.md"
launch_story: "One of 83 focused, repository-backed skills in the Kujo Skills 0.2.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.2.0"
last_updated: "2026-08-11"
keywords: "Kujo Testing And Release Gates, Kujo Agent Skill, kujo-testing-release-gates, repository-backed agent guidance"
seo_title: "Kujo Testing And Release Gates — Kujo Agent Skill"
seo_description: "Use this skill when testing Kujo scripts, examples, docs, security behavior, runtime parity, CLI contracts, or Rust implementation changes, and when preparing or reviewing release-gate readiness."
---

## What it covers

Use this skill when testing Kujo scripts, examples, docs, security behavior, runtime parity, CLI contracts, or Rust implementation changes, and when preparing or reviewing release-gate readiness.

## Released guidance

- Do not change behavior without tests and docs.
- Do not blindly update snapshots. Inspect expected vs actual output first.
- For CLI JSON output changes, update contract docs, tests, and changelog.
- For native API capability changes, update standard library docs and security posture.
- For AI helper or AI egress changes, update `docs/AI_RUNTIME.md`, `docs/SECURE_AI_SCRIPTING.md`, security posture docs, replay fixtures, and enterprise evidence docs together.

## Release boundary

This page reflects the 0.2.0 technical preview on 2026-08-11. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-testing-release-gates skill on GitHub](https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-testing-release-gates/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/main/SKILLS_INDEX.md)
