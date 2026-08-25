---
title: "Kujo AI Chat"
custom_url: "kujo-ai-chat-workflows"
description: "Use this skill when running, configuring, testing, extending, or maintaining the AI Chat local multi-provider chat app: `npm run dev`, `npm run smoke`, SQLite chat state, provider profiles, encrypted API keys, SSE streaming, transcription, `bridge_chat.kujo`, HTTP/API contracts, smoke tests, or `ai-chat` source/docs changes."
excerpt: "Use this skill when running, configuring, testing, extending, or maintaining the AI Chat local multi-provider chat app."
featured_image: "/assets/images/ecosystem/skill-kujo-ai-chat-workflows.webp"
social_image: "/assets/images/social/kujo-ai-chat-workflows.jpg"
section: "Agent Skill"
order: "20"
install_command: "mkdir -p ~/.codex/skills && cp -R skills/kujo-ai-chat-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-ai-chat-workflows/SKILL.md"
launch_story: "One of 96 focused, repository-backed skills in the Kujo Skills 0.4.1 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.4.1"
last_updated: "2026-08-25"
keywords: "Kujo AI Chat, Kujo Agent Skill, kujo-ai-chat-workflows, repository-backed agent guidance"
seo_title: "Kujo AI Chat — Kujo Agent Skill"
seo_description: "Use this skill when running, configuring, testing, extending, or maintaining the AI Chat local multi-provider chat app: `npm run dev`, `npm run smoke`, SQLite chat state, provider profiles, encrypted API keys, SSE streaming, transcription, `bridge_chat.kujo`, HTTP/API contracts, smoke tests, or `ai-chat` source/docs changes."
---

## What it covers

Use this skill when running, configuring, testing, extending, or maintaining the AI Chat local multi-provider chat app: `npm run dev`, `npm run smoke`, SQLite chat state, provider profiles, encrypted API keys, SSE streaming, transcription, `bridge_chat.kujo`, HTTP/API contracts, smoke tests, or `ai-chat` source/docs changes.

## Released guidance

- Runtime database, browser artifacts, benchmark runs, export outputs, and backup outputs live under configured data paths; do not commit runtime data.
- `/api/chat/stream` emits SSE `token`, `thinking`, transient sanitized `tool`, terminal `done`, and terminal `error` events. Preserve complete upstream text/thinking streams plus final metadata, trace IDs, Watchdog trace references, tool artifact metadata, and usage detail payloads when changing bridge or route plumbing.
- Provider profiles include managed Watchdog paths for OpenRouter and Ollama TUD, a managed local `Codex` profile seeded from the cached Codex model catalog when available, pane profiles for repeated comparisons, and a benchmark runner that creates one chat per test under `data/benchmark-runs/`. The bundled OpenRouter and Ollama Cloud model suggestions are the July 28, 2026 catalog snapshot.
- Scheduled chat automations run daily, weekdays, or weekly in a selected local timezone; they persist durable chats per run and should not inherit runtime tools unless explicitly configured.
- Long-chat handling keeps saved transcripts intact while compacting older turns only for provider requests that exceed the active `MAX_MESSAGES_PER_REQUEST` or character windows.

## Release boundary

This page reflects the 0.4.1 technical preview on 2026-08-25. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-ai-chat-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-ai-chat-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/main/SKILLS_INDEX.md)
