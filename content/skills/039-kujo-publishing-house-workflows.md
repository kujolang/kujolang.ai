---
title: "Kujo Publishing House"
custom_url: "kujo-publishing-house-workflows"
description: "Use when installing, running, inspecting, recovering, integrating, or maintaining the Kujo Publishing House workflow suite: daily desk, governance, commissioning, evidence dossiers, primary pieces, asset production, editorial review, adaptation, format production, approval/publication, post-publication learning, fixture/live modes, capability preflight, exact compatibility locks, agent-step receipts, Dispatch state, or Publishing House workflow source/tests."
excerpt: "Use when installing, running, inspecting, recovering, integrating, or maintaining the Kujo Publishing House workflow suite."
featured_image: "/assets/images/ecosystem/skill-kujo-publishing-house-workflows.webp"
social_image: "/assets/images/social/kujo-publishing-house-workflows.jpg"
section: "Agent Skill"
order: "390"
install_command: "git clone --branch v0.7.0 --depth 1 https://github.com/kujolang/kujo-skills.git && mkdir -p ~/.codex/skills && cp -R kujo-skills/skills/kujo-publishing-house-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/v0.7.0/skills/kujo-publishing-house-workflows/SKILL.md"
launch_story: "One of 135 focused, repository-backed skills in the Kujo Skills 0.7.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.7.0"
last_updated: "tag v0.7.0 Tagger: Robert DeVore <deviodigital@gmail.com> Kujo Skills v0.7.0: reusable video styles 2026-09-08"
keywords: "Kujo Publishing House, Kujo Agent Skill, kujo-publishing-house-workflows, repository-backed agent guidance"
seo_title: "Kujo Publishing House — Kujo Agent Skill"
seo_description: "Use when installing, running, inspecting, recovering, integrating, or maintaining the Kujo Publishing House workflow suite: daily desk, governance, commissioning, evidence dossiers, primary pieces, asset production, editorial review, adaptation, format production, approval/publication, post-publication learning, fixture/live modes, capability preflight, exact compatibility locks, agent-step receipts, Dispatch state, or Publishing House workflow source/tests."
---

## What it covers

Use when installing, running, inspecting, recovering, integrating, or maintaining the Kujo Publishing House workflow suite: daily desk, governance, commissioning, evidence dossiers, primary pieces, asset production, editorial review, adaptation, format production, approval/publication, post-publication learning, fixture/live modes, capability preflight, exact compatibility locks, agent-step receipts, Dispatch state, or Publishing House workflow source/tests.

Run the install command from a new working directory. If you already have the released checkout, copy the complete skill folder from it instead of cloning again.

## Released guidance

- Treat `OBSERVE`, `PROPOSE`, and `ACT` as upper bounds. Only Publishing Operations may perform the exact publication action authorized by a valid VersionSeal decision.
- Treat credentials as capability, never authority. Never infer approval from a status, prompt, conversation, or available adapter.
- Bind approval to the exact GalleyPack checksum, destination, action, conditions, and expiry. Any reviewed-byte change requires a new package and approval.
- Resume only the same paused run with its exact VersionSeal result. Repeating a completed run must be an idempotent read.
- Preserve `unsupported`, `unavailable`, `blocked`, `rejected`, `skipped`, `failed`, `paused`, and `completed` as distinct outcomes.

## Release boundary

This page reflects the 0.7.0 technical preview on tag v0.7.0
Tagger: Robert DeVore <deviodigital@gmail.com>

Kujo Skills v0.7.0: reusable video styles
2026-09-08. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-publishing-house-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/v0.7.0/skills/kujo-publishing-house-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/v0.7.0/SKILLS_INDEX.md)
