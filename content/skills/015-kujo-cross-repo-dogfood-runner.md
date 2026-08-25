---
title: "Kujo Cross-Repo Dogfood Runner"
custom_url: "kujo-cross-repo-dogfood-runner"
description: "Use this skill when running recurring cross-repo Kujo dogfood checks, weekly/monthly ecosystem automation, tool interoperability audits, or multi-repo evidence collection using Concord, Fence, Scout, ChangeBucket, PatchBrief, Scent, RunLedger, Casefile, DocGen, and Muzzle."
excerpt: "Use this skill when running recurring cross-repo Kujo dogfood checks, weekly/monthly ecosystem automation, tool interoperability audits, or multi-repo evidence collection using Concord, Fence, Scout,…"
featured_image: "/assets/images/ecosystem/skill-kujo-cross-repo-dogfood-runner.webp"
social_image: "/assets/images/social/kujo-cross-repo-dogfood-runner.jpg"
section: "Agent Skill"
order: "150"
install_command: "mkdir -p ~/.codex/skills && cp -R skills/kujo-cross-repo-dogfood-runner ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-cross-repo-dogfood-runner/SKILL.md"
launch_story: "One of 96 focused, repository-backed skills in the Kujo Skills 0.4.1 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.4.1"
last_updated: "2026-08-25"
keywords: "Kujo Cross-Repo Dogfood Runner, Kujo Agent Skill, kujo-cross-repo-dogfood-runner, repository-backed agent guidance"
seo_title: "Kujo Cross-Repo Dogfood Runner — Kujo Agent Skill"
seo_description: "Use this skill when running recurring cross-repo Kujo dogfood checks, weekly/monthly ecosystem automation, tool interoperability audits, or multi-repo evidence collection using Concord, Fence, Scout, ChangeBucket, PatchBrief, Scent, RunLedger, Casefile, DocGen, and Muzzle."
---

## What it covers

Use this skill when running recurring cross-repo Kujo dogfood checks, weekly/monthly ecosystem automation, tool interoperability audits, or multi-repo evidence collection using Concord, Fence, Scout, ChangeBucket, PatchBrief, Scent, RunLedger, Casefile, DocGen, and Muzzle.

## Released guidance

- Use for recurring ecosystem checks across selected Kujo repos.
- Cover artifact drift, boundary checks, repo intelligence, change footprint, diffs, handoff packs, run receipts, failure bundles, and DocGen health.
- Keep each run bounded by repo list, time window, and check list.
- Do not make broad repo-wide rewrites unless the user explicitly scopes them.
- Repo docs, `AGENTS.md`, tests, scripts, entrypoint `*.kujo` files, manifests, lockfiles, CI config.

## Release boundary

This page reflects the 0.4.1 technical preview on 2026-08-25. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-cross-repo-dogfood-runner skill on GitHub](https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-cross-repo-dogfood-runner/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/main/SKILLS_INDEX.md)
