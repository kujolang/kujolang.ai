---
title: "Workcell"
custom_url: workcell
description: "Run bounded Kujo and agent workflows in disposable workspaces with explicit policy, selective artifact export, and verifiable evidence."
featured_image: "/assets/images/ecosystem/workcell-contained-execution.webp"
section: "Tooling"
tags: [Tool, Execution]
order: 310
install_command: "git clone https://github.com/kujolang/workcell.git"
github_url: "https://github.com/kujolang/workcell"
launch_story: "Run agent work inside an explicit execution contract, then export only declared artifacts and durable evidence."
scope_note: "Workcell 1.1.0 keeps Docker/Podman stable. Portable contracts and E2B, Vercel Sandbox, and Daytona adapters remain alpha pending live certification. Honor its exact runtime pin and run doctor on the target host."
keywords: "Workcell, Kujo ecosystem, bounded execution, Docker, Podman"
seo_title: "Workcell — Kujo Ecosystem"
version: "1.1.0"
latest_release_url: "https://github.com/kujolang/workcell/releases/tag/v1.1.0"
release_status: "Version identifies the latest published GitHub Release. Unpinned clone commands select default-branch source; see scope_note for release boundaries."
last_updated: "2026-09-09"
---

## What it does

Workcell runs Kujo and agent workflows inside disposable Docker or Podman workspaces. A strict execution definition sets resource limits, filesystem access, network policy, environment variables, commands, and the artifacts allowed to leave the workspace.

## How it works

Workcell validates the definition before it starts, prepares a clean Git worktree or isolated clone, runs the workload with bounded CPU, memory, processes, time, output, mounts, and writable paths, then removes resources it owns. Network access can be disabled, use the engine default, or use an operator-managed network.

## Portable backends

Provider-neutral definitions can move the same workload between host profiles without putting provider settings in the workload itself. Workcell negotiates required capabilities before provisioning and records what the backend accepted, enforced, observed, or could not prove.

Docker and Podman provide the supported execution path. Adapters for E2B, Vercel Sandbox, and Daytona are available as previews and require live certification in the operator's account before production use.

## Evidence and recovery

Each run exports only declared artifacts and records a structured receipt, logs, a changes patch, and a SHA-256 integrity manifest. Offline verification detects changed evidence. Ownership-scoped cleanup and failed-workspace preservation keep interrupted runs inspectable and recoverable.

## Why it belongs in Kujo

Workcell turns execution authority into a visible contract. Kujo governs what a workflow is authorized to do and what evidence it must retain; the container boundary limits what the workload can physically reach.

## Operating boundary

Workcell 1.1.0 keeps Docker/Podman stable. Portable contracts and E2B, Vercel Sandbox, and Daytona adapters remain alpha pending live certification. Honor its exact runtime pin and run doctor on the target host.

## Learn more

The [Workcell repository](https://github.com/kujolang/workcell) includes installation, examples, contract references, security limits, platform compatibility, provider operations, and verified release artifacts.
