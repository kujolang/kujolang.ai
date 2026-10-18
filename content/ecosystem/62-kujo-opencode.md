---
title: "Kujo OpenCode"
custom_url: "kujo-opencode"
description: "Run Kujo tools inside OpenCode 2 with six focused specialists, native approvals, and receipts you can inspect."
featured_image: "/assets/images/ecosystem/opencode-approval-workbench.webp"
social_image: "/assets/images/social/kujo-opencode.jpg"
section: "Tooling"
tags: ["Tools", "OpenCode", "Agents", "Ability"]
order: 620
install_command: "npm install --global @kujolang/kujo-opencode@0.2.0"
github_url: "https://github.com/kujolang/kujo-opencode"
launch_story: "Understand a repository, build and test Kujo programs, review changes, and prepare release evidence without leaving OpenCode."
scope_note: "Version 0.2.0 supports OpenCode 2 from 2.0.31. Setup installs pinned Kujo sources and a runtime; optional browsers and services require explicit setup. OpenCode owns the model connection and human approval decisions. Live specialist tests used ChatGPT on macOS; free GLM and DeepSeek specialist access is not verified."
version: "0.2.0"
latest_release_url: "https://github.com/kujolang/kujo-opencode/releases/tag/v0.2.0"
release_status: "Published on npm and GitHub. Registry installation, upgrades, signatures, provenance, and release asset digests are verified."
last_updated: "2026-10-18"
keywords: "Kujo OpenCode, OpenCode 2 plugin, Kujo tools, local agents, approvals, receipts"
seo_title: "Kujo OpenCode — Kujo Tools Inside OpenCode"
seo_description: "Install Kujo OpenCode 0.2.0 for six specialists, 62 scoped capabilities, native approvals, source tools, browser checks, and workflow receipts."
---

## Start with one project

Install the npm package above. From the project you want to work on, run:

```sh
kujo-opencode setup
kujo-opencode doctor
kujo-opencode demo
opencode
```

You need Node.js 20 or newer, npm, Git, and OpenCode 2 version 2.0.31 or newer.
Setup downloads 28 pinned source repositories and the Kujo runtime. It needs
internet access and does not require a separate global Kujo installation.
The demo runs a read-only ShipCheck scan without calling a model.

Open `/kujo` inside OpenCode to choose a profile, enable capabilities, select a
specialist, or inspect evidence. Essentials starts with five tools; Full exposes
62 supported capabilities. Enabling a tool does not approve its actions.

## Six specialists

- **Understand:** inspect repositories and assemble useful context.
- **Build:** inspect Kujo source, create starters, and run reviewed source and tests.
- **Review:** examine changes, contracts, architecture, and change size.
- **Browser:** validate browser flows and run checks with optional Lens Chromium.
- **Workflow:** validate and run Dispatch workflows, inspect runs, and review checkpoints.
- **Ship:** gather release checks, evaluations, and RunLedger evidence. It does not publish for you.

## The tools behind the work

The integration uses supported operations from 28 pinned Kujo projects:

- **Understand:** Scout, Scent, RAG, and Kujo Skills.
- **Build and connect:** Ability, Agents SDK, MCP, CRUD API, and Kennel.
- **Review and verify:** PatchBrief, ChangeBucket, Fence, Spec, Eval, Concord, and Lens.
- **Run and track:** Dispatch, RunLedger, Watchdog, Muzzle, and PackWrite.
- **Evidence and release work:** Casefile, Dossier, Redact, Tribunal, VersionSeal, ShipCheck, and Howl.

These are scoped integrations, not every feature of each product. Browser
installation, telemetry, remote gateways, and private services stay explicit.

## Approval and recovery

OpenCode presents the requested operation and its effects before you choose
Allow once or Reject. Kujo binds the approval to that request and records a
receipt. Profile changes do not bypass approval or specialist scope.

Inspect Dispatch runs after a lost response before deciding whether to retry.
Use Doctor, repair, and recovery commands to diagnose installations. Updates
preserve profiles, overrides, and receipts; project versions remain isolated.

## Connect your model

Use OpenCode's provider settings. For ChatGPT, choose OpenAI and Sign in with
ChatGPT, then select a model offered by your account. Kujo does not copy model
credentials, proxy inference, or switch providers for you.

All six specialists passed 50 live operation checks on macOS x64 with OpenCode
2.0.32 and `openai/gpt-5.6-sol`. Native and rendered host checks cover Linux,
macOS, and Windows on OpenCode 2.0.31 and 2.0.32. These are separate test scopes;
free GLM and DeepSeek specialist access remains unverified.

## Learn more

- [Installation and daily use](https://docs.kujolang.ai/tools/kujo-opencode/)
- [Published npm package](https://www.npmjs.com/package/@kujolang/kujo-opencode/v/0.2.0)
- [Release archive and verification evidence](https://github.com/kujolang/kujo-opencode/releases/tag/v0.2.0)
- [Walkthrough and demo source](https://github.com/kujolang/kujo-opencode/tree/v0.2.0/docs/walkthrough)
