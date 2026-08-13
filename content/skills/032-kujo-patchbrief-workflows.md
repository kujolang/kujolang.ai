---
title: "Kujo PatchBrief"
custom_url: "kujo-patchbrief-workflows"
description: "Use this skill when generating, consuming, validating, or maintaining PatchBrief structured git-diff briefs: `patchbrief.kujo`, `summarize`, `suggest-tests`, `handoff`, `--format json`, `--pretty`, implementation handoffs, reviewer notes, changed-file risk summaries, PatchBrief CLI/tests/source changes, or PatchBrief dogfood workflows."
featured_image: "/assets/images/ecosystem/skill-kujo-patchbrief-workflows.webp"
social_image: "/assets/images/social/kujo-patchbrief-workflows.jpg"
section: "Agent Skill"
order: "320"
install_command: "mkdir -p ~/.codex/skills && cp -R skills/kujo-patchbrief-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-patchbrief-workflows/SKILL.md"
launch_story: "One of 83 focused, repository-backed skills in the Kujo Skills 0.2.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.2.0"
last_updated: "2026-08-11"
keywords: "Kujo PatchBrief, Kujo Agent Skill, kujo-patchbrief-workflows, repository-backed agent guidance"
seo_title: "Kujo PatchBrief — Kujo Agent Skill"
seo_description: "Use this skill when generating, consuming, validating, or maintaining PatchBrief structured git-diff briefs: `patchbrief.kujo`, `summarize`, `suggest-tests`, `handoff`, `--format json`, `--pretty`, implementation handoffs, reviewer notes, changed-file risk summaries, PatchBrief CLI/tests/source changes, or PatchBrief dogfood workflows."
---

## What it covers

Use this skill when generating, consuming, validating, or maintaining PatchBrief structured git-diff briefs: `patchbrief.kujo`, `summarize`, `suggest-tests`, `handoff`, `--format json`, `--pretty`, implementation handoffs, reviewer notes, changed-file risk summaries, PatchBrief CLI/tests/source changes, or PatchBrief dogfood workflows.

## Released guidance

- Run PatchBrief from inside a git repository with a dirty or clean working tree.
- Always pass PatchBrief arguments after Kujo's `--` separator.
- Prefer Markdown for human-readable summaries and handoffs.
- Prefer JSON with `--pretty` when another tool or agent will parse the result.
- Start with `summarize`, then run `suggest-tests` before review, handoff, or commit decisions.

## Release boundary

This page reflects the 0.2.0 technical preview on 2026-08-11. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-patchbrief-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-patchbrief-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/main/SKILLS_INDEX.md)
