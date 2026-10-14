---
title: "Agent City"
custom_url: agent-city
description: "Run and review AI-agent tasks in a pixel-art city, with observed tool activity, evidence, and replay."
featured_image: "/assets/images/ecosystem/agent-city-live-run.webp"
section: "Showcase"
tags: [Showcase, AI, Agents]
order: 480
install_command: "curl --proto '=https' --tlsv1.2 -fsSL https://github.com/kujolang/agent-city/releases/download/v0.2.0/install.sh | sh"
github_url: "https://github.com/kujolang/agent-city"
launch_story: "Give an agent a task, follow its work through the city, and ask a separate agent to review the result. Every semantic activity links to observed Kujo evidence."
scope_note: "Agent City 0.2.0 runs locally on macOS and Linux. Bring your own model connection. Container execution and media generation require separate setup and explicit permission."
keywords: "Kujo Agent City, AI agent workspace, pixel-art agent city, agent task review, observed agent activity, semantic replay"
seo_title: "Agent City — Run and Review AI-Agent Tasks"
seo_description: "Run local AI-agent tasks in Agent City. Follow retrievals, tool calls, reviews, and checks through a pixel-art city, then inspect evidence or replay a recorded run."
version: "0.2.0"
latest_release_url: "https://github.com/kujolang/agent-city/releases/tag/v0.2.0"
release_status: "Published local application for macOS Intel and Apple Silicon, Linux x64 and ARM64. A model connection is required; hosted multi-user operation is outside this release."
last_updated: "2026-10-08"
---

## Watch the work happen

Agent City turns observed agent activity into a readable pixel-art world. Work appears in the Workshop, retrievals in the Library, tool calls in the MCP Terminal Center, and checks in the Dojo. Dispatch tracks tasks; the Meeting Hall represents supported handoffs.

Choose a writing or code task, connect a model, and start a mission. Built-in author and reviewer profiles let you try a two-agent workflow without importing a team. Follow one execution through streets and interiors, read its actual responses, and answer questions in Mission Conversation.

The city follows runtime evidence. Animation never decides whether work succeeded or delays an operation. A completed retrieval may appear as **RECENT** while its visual visit finishes. Unknown or stale source data stays labeled.

## A real Kujo tool, from task to review

[Watch the full 53-second game-only recording](https://github.com/kujolang/agent-city/blob/main/evidence/reviewed-release-tool/repaired/release-notes-live.mp4). The agents create and check a Kujo script that reads a change list and writes Markdown release notes. The recording shows an actual run, not a simulated task.

[Inspect the task, generated source, and execution evidence](https://github.com/kujolang/agent-city/tree/main/evidence/reviewed-release-tool). A reviewer response is separate from an execution or test result, and failed attempts remain in history.

## Start locally

The installer above supplies Agent City, pinned Kujo dependencies, and a private Node runtime when needed. It starts the local app at `http://127.0.0.1:5178`, or the address printed in the terminal. Installation does not submit work.

Connect a local Ollama model or the included connector for an authenticated Codex CLI. Then choose **Writing + review**, **JavaScript + review**, or **Kujo + senior review (real MCP)** in Mission Command. Tools, project files, and execution checks require explicit selection.

Read the [Agent City setup guide](https://docs.kujolang.ai/showcases/agent-city/) for the first task, provider setup, and permissions.

## Review, replay, and record

The inspector separates current truth from visual activity and links operations to their evidence. Archive lets you browse runs, compare attempts, inspect artifacts, and replay pinned activity. Replay reads recorded events; it does not call a model or run tools.

Game-only recording captures the canvas for up to five minutes or 64 MiB. It excludes conversation panels and audio. Optional VideoOps workflows can render separate videos from approved media; external audio services require their own credentials and authorization.

## How it uses Kujo

The TypeScript and Pixi application observes Kujo Agents SDK, Dispatch, RAG, MCP, Workcell, and evaluation activity through Watchdog telemetry. The gateway projects that evidence into a semantic world. RunLedger supplies run correlation and evidence.

Agent City has its own installer. It is not a Kennel package, and importing an agent profile does not install or authorize every tool that profile names. See the [workflow support guide](https://github.com/kujolang/agent-city/blob/main/docs/workflow-support.md) before connecting a custom team.

## Operating boundary

Agent City is a local application, not a hosted multi-user service. Model requests and permitted tools can contact external services. Selected project context goes to the chosen model; provider credentials stay in private server configuration.

Workcell execution needs a compatible container engine with seccomp and AppArmor. Long-duration reliability has not been qualified by an eight-hour soak. Review generated work and check results before applying or publishing them.

## Learn more

- [Agent City documentation](https://docs.kujolang.ai/showcases/agent-city/)
- [Version 0.2.0 release](https://github.com/kujolang/agent-city/releases/tag/v0.2.0)
- [Source repository](https://github.com/kujolang/agent-city)
- [Installation and container setup](https://github.com/kujolang/agent-city/blob/main/installer/README.md)
- [First-task walkthrough](https://github.com/kujolang/agent-city/blob/main/TRY-AGENT-CITY.md)
