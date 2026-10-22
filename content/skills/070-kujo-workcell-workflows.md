---
title: "Kujo Workcell"
custom_url: "kujo-workcell-workflows"
description: "Use this skill when initializing, validating, inspecting, running, verifying, cleaning, recovering, or maintaining Workcell 1.2 execution harnesses: `workcell.json`, `bin/workcell`, `doctor`, `init`, `validate`, `inspect`, `run`, `verify`, `clean`, `backends`, `recover`, `.workcell/runs/`, summaries, receipts, manifests, artifacts, Docker/Podman boundaries, preservation, alpha backend adapters, release reports, or Workcell source/docs changes."
excerpt: "Use this skill when initializing, validating, inspecting, running, verifying, cleaning, recovering, or maintaining Workcell 1.2 execution harnesses."
featured_image: "/assets/images/ecosystem/skill-kujo-workcell-workflows.webp"
social_image: "/assets/images/social/kujo-workcell-workflows.jpg"
section: "Agent Skill"
order: "700"
install_command: "git clone --branch v0.7.1 --depth 1 https://github.com/kujolang/kujo-skills.git && mkdir -p ~/.codex/skills && cp -R kujo-skills/skills/kujo-workcell-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/v0.7.1/skills/kujo-workcell-workflows/SKILL.md"
launch_story: "One of 135 focused, repository-backed skills in the Kujo Skills 0.7.1 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.7.1"
last_updated: "2026-10-22"
keywords: "Kujo Workcell, Kujo Agent Skill, kujo-workcell-workflows, repository-backed agent guidance"
seo_title: "Kujo Workcell — Kujo Agent Skill"
seo_description: "Use this skill when initializing, validating, inspecting, running, verifying, cleaning, recovering, or maintaining Workcell 1.2 execution harnesses: `workcell.json`, `bin/workcell`, `doctor`, `init`, `validate`, `inspect`, `run`, `verify`, `clean`, `backends`, `recover`, `.workcell/runs/`, summaries, receipts, manifests, artifacts, Docker/Podman boundaries, preservation, alpha backend adapters, release reports, or Workcell source/docs changes."
---

## What it covers

Use this skill when initializing, validating, inspecting, running, verifying, cleaning, recovering, or maintaining Workcell 1.2 execution harnesses: `workcell.json`, `bin/workcell`, `doctor`, `init`, `validate`, `inspect`, `run`, `verify`, `clean`, `backends`, `recover`, `.workcell/runs/`, summaries, receipts, manifests, artifacts, Docker/Podman boundaries, preservation, alpha backend adapters, release reports, or Workcell source/docs changes.

Run the install command from a new working directory. If you already have the released checkout, copy the complete skill folder from it instead of cloning again.

## Released guidance

- Workcell rejects dirty source repos by default so user changes are not silently omitted from disposable worktrees.
- `workcell validate --schema` emits `workcell-definition/v1`; `workcell help --json` emits the CLI/exit-code contract.
- Agent-facing `inspect --summary` and `run --summary` emit compact `workcell-inspect-summary/v1` and `workcell-run-summary/v1` pointers. Read `receipt.json` only when detailed evidence is needed, and verify persisted evidence with `verify --json`.
- Pass invocation correlation through a bounded `workcell-caller-context/v1` file with `run --context`; never put credentials or provider options in caller context.
- `workcell run` writes `.workcell/runs/<run-id>/` with `receipt.json`, logs, integrations, patch/change records including untracked files, integrity manifest, and artifacts.

## Release boundary

This page reflects the 0.7.1 technical preview on 2026-10-22. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-workcell-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/v0.7.1/skills/kujo-workcell-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/v0.7.1/SKILLS_INDEX.md)
