---
title: "Kujo AI SDK"
custom_url: "kujo-ai-sdk-workflows"
description: "Use this skill when building, testing, integrating, or maintaining Kujo AI SDK provider primitives: OpenAI-compatible chat/embeddings contracts, native provider drivers, provider presets, model catalogs, fixture mode, streaming callbacks, retries/backoff, redaction, live provider smoke tests, Watchdog telemetry bridge examples, benchmark quality gates, release gates, provider package contracts, or `ai-sdk` source/docs changes."
excerpt: "Use this skill when building, testing, integrating, or maintaining Kujo AI SDK provider primitives."
featured_image: "/assets/images/ecosystem/skill-kujo-ai-sdk-workflows.webp"
social_image: "/assets/images/social/kujo-ai-sdk-workflows.jpg"
section: "Agent Skill"
order: "30"
install_command: "git clone --branch v0.7.0 --depth 1 https://github.com/kujolang/kujo-skills.git && mkdir -p ~/.codex/skills && cp -R kujo-skills/skills/kujo-ai-sdk-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/v0.7.0/skills/kujo-ai-sdk-workflows/SKILL.md"
launch_story: "One of 135 focused, repository-backed skills in the Kujo Skills 0.7.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.7.0"
last_updated: "tag v0.7.0 Tagger: Robert DeVore <deviodigital@gmail.com> Kujo Skills v0.7.0: reusable video styles 2026-09-08"
keywords: "Kujo AI SDK, Kujo Agent Skill, kujo-ai-sdk-workflows, repository-backed agent guidance"
seo_title: "Kujo AI SDK — Kujo Agent Skill"
seo_description: "Use this skill when building, testing, integrating, or maintaining Kujo AI SDK provider primitives: OpenAI-compatible chat/embeddings contracts, native provider drivers, provider presets, model catalogs, fixture mode, streaming callbacks, retries/backoff, redaction, live provider smoke tests, Watchdog telemetry bridge examples, benchmark quality gates, release gates, provider package contracts, or `ai-sdk` source/docs changes."
---

## What it covers

Use this skill when building, testing, integrating, or maintaining Kujo AI SDK provider primitives: OpenAI-compatible chat/embeddings contracts, native provider drivers, provider presets, model catalogs, fixture mode, streaming callbacks, retries/backoff, redaction, live provider smoke tests, Watchdog telemetry bridge examples, benchmark quality gates, release gates, provider package contracts, or `ai-sdk` source/docs changes.

Run the install command from a new working directory. If you already have the released checkout, copy the complete skill folder from it instead of cloning again.

## Released guidance

- Fixture mode must remain deterministic and safe without provider secrets.
- Live provider smoke may skip during ordinary local runs when no provider key is configured, but release/prerelease validation requires at least one configured provider secret unless a manual workflow explicitly allows the skip.
- Response contracts, API contract policy, and tests must move together. Streaming requests set `stream_options.include_usage`, and normalized usage accepts both `prompt_tokens`/`completion_tokens` and `input_tokens`/`output_tokens`.
- Native provider packages attach a validated `ai-sdk-provider-driver` 1.0.0 function bundle. Drivers encode bounded request descriptors and decode provider-native responses; they never perform network I/O or select transport.
- `src/model_catalog.kujo` owns provider-owned model metadata for deterministic routing. Persist catalog ID, version, hash, provider, model, preference class, and source; do not fabricate prices, token limits, or measurements.

## Release boundary

This page reflects the 0.7.0 technical preview on tag v0.7.0
Tagger: Robert DeVore <deviodigital@gmail.com>

Kujo Skills v0.7.0: reusable video styles
2026-09-08. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-ai-sdk-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/v0.7.0/skills/kujo-ai-sdk-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/v0.7.0/SKILLS_INDEX.md)
