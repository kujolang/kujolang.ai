---
title: "Kujo Security Hardening"
custom_url: "kujo-security-hardening"
description: "Use this skill when writing or reviewing Kujo scripts that touch files, processes, shell commands, network, databases, archives, HTML/static serving, AI provider egress, secrets, or untrusted input; it enforces Kujo's conservative native API security posture."
excerpt: "Use this skill when writing or reviewing Kujo scripts that touch files, processes, shell commands, network, databases, archives, HTML/static serving, AI provider egress, secrets,…"
featured_image: "/assets/images/ecosystem/skill-kujo-security-hardening.webp"
social_image: "/assets/images/social/kujo-security-hardening.jpg"
section: "Agent Skill"
order: "520"
install_command: "git clone --branch v0.7.0 --depth 1 https://github.com/kujolang/kujo-skills.git && mkdir -p ~/.codex/skills && cp -R kujo-skills/skills/kujo-security-hardening ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/v0.7.0/skills/kujo-security-hardening/SKILL.md"
launch_story: "One of 135 focused, repository-backed skills in the Kujo Skills 0.7.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.7.0"
last_updated: "tag v0.7.0 Tagger: Robert DeVore <deviodigital@gmail.com> Kujo Skills v0.7.0: reusable video styles 2026-09-08"
keywords: "Kujo Security Hardening, Kujo Agent Skill, kujo-security-hardening, repository-backed agent guidance"
seo_title: "Kujo Security Hardening — Kujo Agent Skill"
seo_description: "Use this skill when writing or reviewing Kujo scripts that touch files, processes, shell commands, network, databases, archives, HTML/static serving, AI provider egress, secrets, or untrusted input; it enforces Kujo's conservative native API security posture."
---

## What it covers

Use this skill when writing or reviewing Kujo scripts that touch files, processes, shell commands, network, databases, archives, HTML/static serving, AI provider egress, secrets, or untrusted input; it enforces Kujo's conservative native API security posture.

Run the install command from a new working directory. If you already have the released checkout, copy the complete skill folder from it instead of cloning again.

## Released guidance

- `kujo run` and `kujo test-run` default to trusted mode.
- Trusted mode means host-effect APIs run with ambient process privileges.
- For untrusted code, start with `--untrusted` and add only the required `--allow-*` flags.
- `--allow-*` flags imply restricted baseline with only those capabilities enabled.
- Treat `--allow-all` as trusted/full ambient-host execution.

## Release boundary

This page reflects the 0.7.0 technical preview on tag v0.7.0
Tagger: Robert DeVore <deviodigital@gmail.com>

Kujo Skills v0.7.0: reusable video styles
2026-09-08. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-security-hardening skill on GitHub](https://github.com/kujolang/kujo-skills/blob/v0.7.0/skills/kujo-security-hardening/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/v0.7.0/SKILLS_INDEX.md)
