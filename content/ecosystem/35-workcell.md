---
title: "Workcell"
custom_url: workcell
description: "Workcell 1.1 runs bounded Kujo and agent workflows in disposable Docker or Podman workspaces, with alpha portable-backend contracts for future remote execution."
featured_image: "/assets/images/ecosystem/workcell-contained-execution.webp"
section: "Tooling"
tags: [Tool, Execution]
order: 310
install_command: "git clone https://github.com/kujolang/workcell.git"
github_url: "https://github.com/kujolang/workcell"
launch_story: "Run agent work inside an explicit execution contract, then export only declared artifacts and durable evidence."
scope_note: "Workcell trusts the selected container engine and host kernel; it is not microVM isolation, a hosted multi-tenant runner, or compliance certification."
keywords: "Workcell, Kujo ecosystem, bounded execution, Docker, Podman"
seo_title: "Workcell — Kujo Ecosystem"
---

## What it does

Workcell 1.1 validates a versioned JSON execution definition, prepares a disposable Git worktree or isolated clone, and runs the declared workload with bounded CPU, memory, process, time, output, mount, and writable-path limits. Docker and Podman remain the stable execution backends, with explicit `none`, `default`, or pre-created custom network selection.

## Portable execution, still alpha

The 1.1 source release adds provider-neutral definitions, strict capability negotiation, portable receipts, ownership-bound recovery, compact agent summaries, and digest-pinned adapters for E2B, Vercel Sandbox, and Daytona. Those remote adapters are alpha. Offline conformance proves their contract behavior, not a provider account, region, plan, security boundary, or production deployment.

## Evidence and recovery

Each lifecycle can export only declared artifacts and record structured receipts, logs, a changes patch, and a SHA-256 integrity manifest. Offline verification detects changes to immutable evidence, while ownership-scoped cleanup and failed-workspace preservation make interrupted runs inspectable and recoverable.

## Why it belongs in Kujo

Workcell turns execution authority into a visible contract. Kujo governs what a workflow is authorized to do and what evidence it must retain; the container boundary limits what the workload can physically reach.

## Operating boundary

Containers are not universal isolation. Higher-risk or multi-tenant workloads need an operator-provided stronger boundary, and deployment-specific image governance, egress controls, key custody, retention, and host hardening remain outside Workcell's v1 guarantee.

## Learn more

The repository documents the stable and alpha contracts separately, along with runtime lifecycle, security limits, platform compatibility, verification, provider operations, and release artifacts. Download the source and checksums from the [Workcell 1.1.0 release](https://github.com/kujolang/workcell/releases/tag/v1.1.0).
