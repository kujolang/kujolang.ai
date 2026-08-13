---
title: "Kujo AI SDK"
custom_url: "kujo-ai-sdk-workflows"
description: "Use this skill when building, testing, integrating, or maintaining Kujo AI SDK provider primitives: OpenAI-compatible chat/embeddings contracts, provider presets, fixture mode, streaming callbacks, retries/backoff, redaction, live provider smoke tests, telemetry bridge examples, benchmark quality gates, release gates, or `ai-sdk` source/docs changes."
featured_image: "/assets/images/ecosystem/skill-kujo-ai-sdk-workflows.webp"
social_image: "/assets/images/social/kujo-ai-sdk-workflows.jpg"
section: "Agent Skill"
order: "30"
install_command: "mkdir -p ~/.codex/skills && cp -R skills/kujo-ai-sdk-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-ai-sdk-workflows/SKILL.md"
launch_story: "One of 83 focused, repository-backed skills in the Kujo Skills 0.2.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.2.0"
last_updated: "2026-08-11"
keywords: "Kujo AI SDK, Kujo Agent Skill, kujo-ai-sdk-workflows, repository-backed agent guidance"
seo_title: "Kujo AI SDK — Kujo Agent Skill"
seo_description: "Use this skill when building, testing, integrating, or maintaining Kujo AI SDK provider primitives: OpenAI-compatible chat/embeddings contracts, provider presets, fixture mode, streaming callbacks, retries/backoff, redaction, live provider smoke tests, telemetry bridge examples, benchmark quality gates, release gates, or `ai-sdk` source/docs changes."
---

## What it covers

Use this skill when building, testing, integrating, or maintaining Kujo AI SDK provider primitives: OpenAI-compatible chat/embeddings contracts, provider presets, fixture mode, streaming callbacks, retries/backoff, redaction, live provider smoke tests, telemetry bridge examples, benchmark quality gates, release gates, or `ai-sdk` source/docs changes.

## Released guidance

- Fixture mode must remain deterministic and safe without provider secrets.
- Live provider smoke may skip during ordinary local runs when no provider key is configured, but release/prerelease validation requires at least one configured provider secret unless a manual workflow explicitly allows the skip.
- Response contracts, API contract policy, and tests must move together. Streaming requests set `stream_options.include_usage`, and normalized usage accepts both `prompt_tokens`/`completion_tokens` and `input_tokens`/`output_tokens`.
- Keep endpoint allowlists, protected-header policy, structured-output schema validation, response-size limits, fallback providers, benchmark thresholds, and provider capability metadata aligned with README and tests.
- Use SDK-owned `resolve_model_preference(provider, preference)` when callers need provider-neutral model intent. Provider presets own class-to-model mappings; downstream orchestration should persist the returned `provider`, `model`, `preference_class`, and `source` instead of duplicating routing tables.

## Release boundary

This page reflects the 0.2.0 technical preview on 2026-08-11. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-ai-sdk-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-ai-sdk-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/main/SKILLS_INDEX.md)
