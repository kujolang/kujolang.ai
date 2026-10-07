---
title: "AI Chat"
custom_url: ai-chat
description: "A local multi-provider agent workspace with live code review, durable supervision, isolated worktrees, scoped tools, and persistent multi-chat tabs."
featured_image: "/assets/images/ecosystem/ai-chat-conversation.webp"
section: "Showcase"
tags: [Showcase, AI]
order: 420
install_command: "git clone https://github.com/kujolang/ai-chat.git"
github_url: "https://github.com/kujolang/ai-chat"
launch_story: "Run and supervise multiple coding and content agents with reviewable changes, explicit permissions, durable evidence, and provider-neutral controls."
scope_note: "AI Chat 1.3.0 adds live per-pane diffs, checkpoints, plans and steering, managed Git worktrees, attachments, execution artifacts, scoped MCP connections, an attention inbox, a command palette, and persistent chat tabs. Use Node 22.17.0, npm ci, and matching database/encryption backups. The historical eight-hour soak remains incomplete; browser execution requires supported OS containment."
keywords: "AI Chat, Kujo ecosystem, Showcase, AI"
seo_title: "AI Chat — Kujo Ecosystem"
version: "1.3.0"
latest_release_url: "https://github.com/kujolang/ai-chat/releases/tag/v1.3.0"
release_status: "Version identifies the latest published GitHub Release. Unpinned clone commands select default-branch source; see scope_note for release boundaries."
last_updated: "2026-10-06"
---

## What it does

A local multi-provider agent workspace with encrypted profiles, durable SQLite state, multi-pane comparison, persistent chat tabs, live code diffs, checkpoints, plans and steering, scoped MCP tools, and reviewable execution evidence.

## Why it belongs in Kujo

Run coding, review, content, and operations agents side by side while keeping permissions, changes, tool evidence, and recovery controls visible and inspectable.

## Operating boundary

AI Chat 1.3.0 is a local-first showcase, not a managed service or deployed production certification. Use Node 22.17.0 and `npm ci`; back up the database with its matching encryption secret and preserve uncommitted managed worktrees before upgrading. Local writes, shell execution, MCP connections, desktop notifications, browser execution, and ChatGPT plan access remain explicit opt-ins. The historical eight-hour soak remains incomplete, and browser execution still requires supported OS containment.

## Release

[AI Chat 1.3.0](https://github.com/kujolang/ai-chat/releases/tag/v1.3.0) ships harness roadmap items HR-01 through HR-10, including actionable diff review, encrypted checkpoints, worktree isolation, typed attachments, execution artifacts, MCP management, attention notifications, and the command palette. It also updates `proxy-addr` to 2.0.8 and hardens the documented forwarded-IP proxy topology. Follow the [versioned upgrade procedure](https://github.com/kujolang/ai-chat/blob/v1.3.0/SETUP_AND_INSTALL.md#upgrading-to-130).

## Learn more

The repository is the source of truth for current setup, commands, examples, security notes, compatibility, and verification evidence.
