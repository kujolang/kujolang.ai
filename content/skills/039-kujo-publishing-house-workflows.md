---
title: "Kujo Publishing House"
custom_url: "kujo-publishing-house-workflows"
description: "Use when installing, running, inspecting, recovering, integrating, or maintaining the Kujo Publishing House workflow suite: daily desk, governance, commissioning, evidence dossiers, primary pieces, asset production, editorial review, adaptation, format production, approval/publication, post-publication learning, fixture/live modes, capability preflight, exact compatibility locks, agent-step receipts, Dispatch state, or Publishing House workflow source/tests."
excerpt: "Use when installing, running, inspecting, recovering, integrating, or maintaining the Kujo Publishing House workflow suite."
featured_image: "/assets/images/ecosystem/skill-kujo-publishing-house-workflows.webp"
social_image: "/assets/images/social/kujo-publishing-house-workflows.jpg"
section: "Agent Skill"
order: "390"
install_command: "mkdir -p ~/.codex/skills && cp -R skills/kujo-publishing-house-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-publishing-house-workflows/SKILL.md"
launch_story: "One of 96 focused, repository-backed skills in the Kujo Skills 0.4.1 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.4.1"
last_updated: "2026-08-25"
keywords: "Kujo Publishing House, Kujo Agent Skill, kujo-publishing-house-workflows, repository-backed agent guidance"
seo_title: "Kujo Publishing House — Kujo Agent Skill"
seo_description: "Use when installing, running, inspecting, recovering, integrating, or maintaining the Kujo Publishing House workflow suite: daily desk, governance, commissioning, evidence dossiers, primary pieces, asset production, editorial review, adaptation, format production, approval/publication, post-publication learning, fixture/live modes, capability preflight, exact compatibility locks, agent-step receipts, Dispatch state, or Publishing House workflow source/tests."
---

## What it covers

Use when installing, running, inspecting, recovering, integrating, or maintaining the Kujo Publishing House workflow suite: daily desk, governance, commissioning, evidence dossiers, primary pieces, asset production, editorial review, adaptation, format production, approval/publication, post-publication learning, fixture/live modes, capability preflight, exact compatibility locks, agent-step receipts, Dispatch state, or Publishing House workflow source/tests.

## Released guidance

- Treat `OBSERVE`, `PROPOSE`, and `ACT` as upper bounds. Only Publishing Operations may perform the exact publication action authorized by a valid VersionSeal decision.
- Treat credentials as capability, never authority. Never infer approval from a status, prompt, conversation, or available adapter.
- Bind approval to the exact GalleyPack checksum, destination, action, conditions, and expiry. Any reviewed-byte change requires a new package and approval.
- Resume only the same paused run with its exact VersionSeal result. Repeating a completed run must be an idempotent read.
- Preserve `unsupported`, `unavailable`, `blocked`, `rejected`, `skipped`, `failed`, `paused`, and `completed` as distinct outcomes.

## Release boundary

This page reflects the 0.4.1 technical preview on 2026-08-25. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-publishing-house-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-publishing-house-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/main/SKILLS_INDEX.md)
