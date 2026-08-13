---
title: "Kujo Scout Workflows"
custom_url: "kujo-scout-workflows"
description: "Use this skill when running, interpreting, extending, or maintaining Scout, the Kujo-native codebase intelligence tool: `kujo run scout.kujo`, repo context packs, `FILE_TREE.md`, `llms.txt`, `AGENTS.md`, `CHECKLIST.md`, `intelligence.json`, `scan_manifest.json`, security exports, baseline suppression, Kennel metadata, Scout fixtures, snapshots, or Scout regression scripts."
featured_image: "/assets/images/ecosystem/skill-kujo-scout-workflows.webp"
social_image: "/assets/images/social/kujo-scout-workflows.jpg"
section: "Agent Skill"
order: "410"
install_command: "mkdir -p ~/.codex/skills && cp -R skills/kujo-scout-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-scout-workflows/SKILL.md"
launch_story: "One of 83 focused, repository-backed skills in the Kujo Skills 0.2.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.2.0"
last_updated: "2026-08-11"
keywords: "Kujo Scout Workflows, Kujo Agent Skill, kujo-scout-workflows, repository-backed agent guidance"
seo_title: "Kujo Scout Workflows — Kujo Agent Skill"
seo_description: "Use this skill when running, interpreting, extending, or maintaining Scout, the Kujo-native codebase intelligence tool: `kujo run scout.kujo`, repo context packs, `FILE_TREE.md`, `llms.txt`, `AGENTS.md`, `CHECKLIST.md`, `intelligence.json`, `scan_manifest.json`, security exports, baseline suppression, Kennel metadata, Scout fixtures, snapshots, or Scout regression scripts."
---

## What it covers

Use this skill when running, interpreting, extending, or maintaining Scout, the Kujo-native codebase intelligence tool: `kujo run scout.kujo`, repo context packs, `FILE_TREE.md`, `llms.txt`, `AGENTS.md`, `CHECKLIST.md`, `intelligence.json`, `scan_manifest.json`, security exports, baseline suppression, Kennel metadata, Scout fixtures, snapshots, or Scout regression scripts.

## Released guidance

- Start with `scan_manifest.json` for artifact paths, schema version, and run metadata.
- Use `README.md` for the human report: metrics, routes, dependencies, and security findings.
- Use `llms.txt` for compact context injection.
- Use `AGENTS.md` when preparing an AI coding assistant to work in the scanned repo.
- Use `CHECKLIST.md` for review follow-up, especially security-highlighted items.

## Release boundary

This page reflects the 0.2.0 technical preview on 2026-08-11. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-scout-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-scout-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/main/SKILLS_INDEX.md)
