---
title: "Kujo Scout"
custom_url: "kujo-scout-workflows"
description: "Use this skill when running, interpreting, extending, or maintaining Scout, the Kujo-native codebase intelligence tool: `kujo run scout.kujo`, repo context packs, `FILE_TREE.md`, `llms.txt`, `AGENTS.md`, `CHECKLIST.md`, `intelligence.json`, `scan_manifest.json`, security exports, baseline suppression, Kennel metadata, Scout fixtures, snapshots, or Scout regression scripts."
excerpt: "Use this skill when running, interpreting, extending, or maintaining Scout, the Kujo-native codebase intelligence tool."
featured_image: "/assets/images/ecosystem/skill-kujo-scout-workflows.webp"
social_image: "/assets/images/social/kujo-scout-workflows.jpg"
section: "Agent Skill"
order: "500"
install_command: "git clone --branch v0.7.0 --depth 1 https://github.com/kujolang/kujo-skills.git && mkdir -p ~/.codex/skills && cp -R kujo-skills/skills/kujo-scout-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/v0.7.0/skills/kujo-scout-workflows/SKILL.md"
launch_story: "One of 135 focused, repository-backed skills in the Kujo Skills 0.7.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.7.0"
last_updated: "tag v0.7.0 Tagger: Robert DeVore <deviodigital@gmail.com> Kujo Skills v0.7.0: reusable video styles 2026-09-08"
keywords: "Kujo Scout, Kujo Agent Skill, kujo-scout-workflows, repository-backed agent guidance"
seo_title: "Kujo Scout — Kujo Agent Skill"
seo_description: "Use this skill when running, interpreting, extending, or maintaining Scout, the Kujo-native codebase intelligence tool: `kujo run scout.kujo`, repo context packs, `FILE_TREE.md`, `llms.txt`, `AGENTS.md`, `CHECKLIST.md`, `intelligence.json`, `scan_manifest.json`, security exports, baseline suppression, Kennel metadata, Scout fixtures, snapshots, or Scout regression scripts."
---

## What it covers

Use this skill when running, interpreting, extending, or maintaining Scout, the Kujo-native codebase intelligence tool: `kujo run scout.kujo`, repo context packs, `FILE_TREE.md`, `llms.txt`, `AGENTS.md`, `CHECKLIST.md`, `intelligence.json`, `scan_manifest.json`, security exports, baseline suppression, Kennel metadata, Scout fixtures, snapshots, or Scout regression scripts.

Run the install command from a new working directory. If you already have the released checkout, copy the complete skill folder from it instead of cloning again.

## Released guidance

- Start with `scan_manifest.json` for artifact paths, schema version, and run metadata.
- Use `README.md` for the human report: metrics, routes, dependencies, and security findings.
- Use `llms.txt` for compact context injection.
- Use `AGENTS.md` when preparing an AI coding assistant to work in the scanned repo.
- Use `CHECKLIST.md` for review follow-up, especially security-highlighted items.

## Release boundary

This page reflects the 0.7.0 technical preview on tag v0.7.0
Tagger: Robert DeVore <deviodigital@gmail.com>

Kujo Skills v0.7.0: reusable video styles
2026-09-08. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-scout-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/v0.7.0/skills/kujo-scout-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/v0.7.0/SKILLS_INDEX.md)
