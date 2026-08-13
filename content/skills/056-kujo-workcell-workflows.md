---
title: "Kujo Workcell Workflows"
custom_url: "kujo-workcell-workflows"
description: "Use this skill when initializing, validating, inspecting, running, verifying, cleaning, or maintaining Workcell local Docker/Podman execution sandboxes: `workcell.json`, `bin/workcell`, `doctor`, `init`, `validate`, `inspect`, `run`, `verify`, `clean`, `.workcell/runs/`, receipts, manifests, artifacts, runtime boundaries, release reports, or Workcell source/docs changes."
featured_image: "/assets/images/ecosystem/skill-kujo-workcell-workflows.webp"
social_image: "/assets/images/social/kujo-workcell-workflows.jpg"
section: "Agent Skill"
order: "560"
install_command: "mkdir -p ~/.codex/skills && cp -R skills/kujo-workcell-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-workcell-workflows/SKILL.md"
launch_story: "One of 83 focused, repository-backed skills in the Kujo Skills 0.2.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.2.0"
last_updated: "2026-08-11"
keywords: "Kujo Workcell Workflows, Kujo Agent Skill, kujo-workcell-workflows, repository-backed agent guidance"
seo_title: "Kujo Workcell Workflows — Kujo Agent Skill"
seo_description: "Use this skill when initializing, validating, inspecting, running, verifying, cleaning, or maintaining Workcell local Docker/Podman execution sandboxes: `workcell.json`, `bin/workcell`, `doctor`, `init`, `validate`, `inspect`, `run`, `verify`, `clean`, `.workcell/runs/`, receipts, manifests, artifacts, runtime boundaries, release reports, or Workcell source/docs changes."
---

## What it covers

Use this skill when initializing, validating, inspecting, running, verifying, cleaning, or maintaining Workcell local Docker/Podman execution sandboxes: `workcell.json`, `bin/workcell`, `doctor`, `init`, `validate`, `inspect`, `run`, `verify`, `clean`, `.workcell/runs/`, receipts, manifests, artifacts, runtime boundaries, release reports, or Workcell source/docs changes.

## Released guidance

- Workcell rejects dirty source repos by default so user changes are not silently omitted from disposable worktrees.
- `workcell validate --schema` emits the definition contract; `workcell help --json` emits the CLI/exit-code contract.
- `workcell run` writes `.workcell/runs/<run-id>/` with `receipt.json`, logs, integrations, patch/change records including untracked files, integrity manifest, and artifacts.
- `workcell verify --run <run-directory> --json` verifies immutable evidence hashes without exposing secret values.
- The default `contained-standard` profile uses no network, non-root host-mapped UID/GID, read-only root, bounded CPU/memory/PIDs/time/output, no new privileges, dropped capabilities, no devices, no host namespaces, no Docker socket, explicit env, and one disposable workspace mount.

## Release boundary

This page reflects the 0.2.0 technical preview on 2026-08-11. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-workcell-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-workcell-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/main/SKILLS_INDEX.md)
