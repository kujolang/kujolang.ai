---
title: "Kujo PatchBrief"
custom_url: "kujo-patchbrief-workflows"
description: "Use this skill when generating, consuming, validating, or maintaining PatchBrief structured git-diff briefs: `patchbrief.kujo`, `summarize`, `suggest-tests`, `handoff`, `--format json`, `--pretty`, implementation handoffs, reviewer notes, changed-file risk summaries, PatchBrief CLI/tests/source changes, or PatchBrief dogfood workflows."
excerpt: "Use this skill when generating, consuming, validating, or maintaining PatchBrief structured git-diff briefs."
featured_image: "/assets/images/ecosystem/skill-kujo-patchbrief-workflows.webp"
social_image: "/assets/images/social/kujo-patchbrief-workflows.jpg"
section: "Agent Skill"
order: "370"
install_command: "git clone --branch v0.7.0 --depth 1 https://github.com/kujolang/kujo-skills.git && mkdir -p ~/.codex/skills && cp -R kujo-skills/skills/kujo-patchbrief-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/v0.7.0/skills/kujo-patchbrief-workflows/SKILL.md"
launch_story: "One of 135 focused, repository-backed skills in the Kujo Skills 0.7.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.7.0"
last_updated: "tag v0.7.0 Tagger: Robert DeVore <deviodigital@gmail.com> Kujo Skills v0.7.0: reusable video styles 2026-09-08"
keywords: "Kujo PatchBrief, Kujo Agent Skill, kujo-patchbrief-workflows, repository-backed agent guidance"
seo_title: "Kujo PatchBrief — Kujo Agent Skill"
seo_description: "Use this skill when generating, consuming, validating, or maintaining PatchBrief structured git-diff briefs: `patchbrief.kujo`, `summarize`, `suggest-tests`, `handoff`, `--format json`, `--pretty`, implementation handoffs, reviewer notes, changed-file risk summaries, PatchBrief CLI/tests/source changes, or PatchBrief dogfood workflows."
---

## What it covers

Use this skill when generating, consuming, validating, or maintaining PatchBrief structured git-diff briefs: `patchbrief.kujo`, `summarize`, `suggest-tests`, `handoff`, `--format json`, `--pretty`, implementation handoffs, reviewer notes, changed-file risk summaries, PatchBrief CLI/tests/source changes, or PatchBrief dogfood workflows.

Run the install command from a new working directory. If you already have the released checkout, copy the complete skill folder from it instead of cloning again.

## Released guidance

- Run PatchBrief from inside a git repository with a dirty or clean working tree.
- Always pass PatchBrief arguments after Kujo's `--` separator.
- Prefer Markdown for human-readable summaries and handoffs.
- Prefer JSON with `--pretty` when another tool or agent will parse the result.
- Start with `summarize`, then run `suggest-tests` before review, handoff, or commit decisions.

## Release boundary

This page reflects the 0.7.0 technical preview on tag v0.7.0
Tagger: Robert DeVore <deviodigital@gmail.com>

Kujo Skills v0.7.0: reusable video styles
2026-09-08. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-patchbrief-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/v0.7.0/skills/kujo-patchbrief-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/v0.7.0/SKILLS_INDEX.md)
