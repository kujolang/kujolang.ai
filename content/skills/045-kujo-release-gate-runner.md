---
title: "Kujo Release Gate Runner"
custom_url: "kujo-release-gate-runner"
description: "Use this skill when running Kujo release gates, recurring release-readiness automation, pre-tag checks, blocker triage, or monthly gate evidence collection across ShipCheck, Eval, Fence, ChangeBucket, RunLedger, Casefile, DocGen gates, and Muzzle workflows."
excerpt: "Use this skill when running Kujo release gates, recurring release-readiness automation, pre-tag checks, blocker triage, or monthly gate evidence collection across ShipCheck, Eval, Fence,…"
featured_image: "/assets/images/ecosystem/skill-kujo-release-gate-runner.webp"
social_image: "/assets/images/social/kujo-release-gate-runner.jpg"
section: "Agent Skill"
order: "450"
install_command: "mkdir -p ~/.codex/skills && cp -R skills/kujo-release-gate-runner ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-release-gate-runner/SKILL.md"
launch_story: "One of 96 focused, repository-backed skills in the Kujo Skills 0.4.1 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.4.1"
last_updated: "2026-08-25"
keywords: "Kujo Release Gate Runner, Kujo Agent Skill, kujo-release-gate-runner, repository-backed agent guidance"
seo_title: "Kujo Release Gate Runner — Kujo Agent Skill"
seo_description: "Use this skill when running Kujo release gates, recurring release-readiness automation, pre-tag checks, blocker triage, or monthly gate evidence collection across ShipCheck, Eval, Fence, ChangeBucket, RunLedger, Casefile, DocGen gates, and Muzzle workflows."
---

## What it covers

Use this skill when running Kujo release gates, recurring release-readiness automation, pre-tag checks, blocker triage, or monthly gate evidence collection across ShipCheck, Eval, Fence, ChangeBucket, RunLedger, Casefile, DocGen gates, and Muzzle workflows.

## Released guidance

- Use before tags, releases, dependency updates, generated docs refreshes, or recurring release checks.
- Cover release readiness, eval correctness, architecture boundaries, change footprint, generated docs contracts, and failure evidence.
- Do not publish, deploy, tag, or mutate release state without explicit authorization and a supported workflow.
- Release docs and scripts, CI config, changelog, manifests, lockfiles, generated docs, test suites.
- ShipCheck, Eval, Fence, ChangeBucket, DocGen, RunLedger, and Casefile artifacts.

## Release boundary

This page reflects the 0.4.1 technical preview on 2026-08-25. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-release-gate-runner skill on GitHub](https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-release-gate-runner/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/main/SKILLS_INDEX.md)
