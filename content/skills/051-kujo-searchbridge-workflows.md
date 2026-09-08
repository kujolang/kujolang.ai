---
title: "Kujo SearchBridge"
custom_url: "kujo-searchbridge-workflows"
description: "Use this skill when running, validating, installing, or maintaining SearchBridge 1.x: doctor, capability preflight, provider tiers, fixture/live evidence reads, batch reads, evidence-query, signed adapters, replay/cache, SDK bundles, OpenTelemetry, MCP surfaces, or explicit ACT submission."
excerpt: "Use this skill when running, validating, installing, or maintaining SearchBridge 1.x."
featured_image: "/assets/images/ecosystem/skill-kujo-searchbridge-workflows.webp"
social_image: "/assets/images/social/kujo-searchbridge-workflows.jpg"
section: "Agent Skill"
order: "510"
install_command: "git clone --branch v0.7.0 --depth 1 https://github.com/kujolang/kujo-skills.git && mkdir -p ~/.codex/skills && cp -R kujo-skills/skills/kujo-searchbridge-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/v0.7.0/skills/kujo-searchbridge-workflows/SKILL.md"
launch_story: "One of 135 focused, repository-backed skills in the Kujo Skills 0.7.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.7.0"
last_updated: "tag v0.7.0 Tagger: Robert DeVore <deviodigital@gmail.com> Kujo Skills v0.7.0: reusable video styles 2026-09-08"
keywords: "Kujo SearchBridge, Kujo Agent Skill, kujo-searchbridge-workflows, repository-backed agent guidance"
seo_title: "Kujo SearchBridge — Kujo Agent Skill"
seo_description: "Use this skill when running, validating, installing, or maintaining SearchBridge 1.x: doctor, capability preflight, provider tiers, fixture/live evidence reads, batch reads, evidence-query, signed adapters, replay/cache, SDK bundles, OpenTelemetry, MCP surfaces, or explicit ACT submission."
---

## What it covers

Use this skill when running, validating, installing, or maintaining SearchBridge 1.x: doctor, capability preflight, provider tiers, fixture/live evidence reads, batch reads, evidence-query, signed adapters, replay/cache, SDK bundles, OpenTelemetry, MCP surfaces, or explicit ACT submission.

Run the install command from a new working directory. If you already have the released checkout, copy the complete skill folder from it instead of cloning again.

## Released guidance

- normalized `searchbridge.result/v1` evidence.
- capability matrix.
- ACT `searchbridge.submission/v1` receipt.
- batch partial-success records, replay/cache records, SDK/generated type artifacts, MCP records, or OTLP file output when explicitly requested.

## Release boundary

This page reflects the 0.7.0 technical preview on tag v0.7.0
Tagger: Robert DeVore <deviodigital@gmail.com>

Kujo Skills v0.7.0: reusable video styles
2026-09-08. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-searchbridge-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/v0.7.0/skills/kujo-searchbridge-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/v0.7.0/SKILLS_INDEX.md)
