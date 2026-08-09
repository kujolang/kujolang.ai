---
title: "Workcell"
custom_url: workcell
description: "A stable local and CI execution harness for bounded Kujo and agent workflows in disposable Docker or Podman workspaces."
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

Workcell 1.0 validates a versioned JSON execution definition, prepares a disposable Git worktree or isolated clone, and runs the declared workload with bounded CPU, memory, process, time, output, mount, and writable-path limits. Docker and Podman are supported, with explicit `none`, `default`, or pre-created custom network selection.

## Evidence and recovery

Each lifecycle can export only declared artifacts and record structured receipts, logs, a changes patch, and a SHA-256 integrity manifest. Offline verification detects changes to immutable evidence, while ownership-scoped cleanup and failed-workspace preservation make interrupted runs inspectable and recoverable.

## Why it belongs in Kujo

Workcell turns execution authority into a visible contract. Kujo governs what a workflow is authorized to do and what evidence it must retain; the container boundary limits what the workload can physically reach.

## Operating boundary

Containers are not universal isolation. Higher-risk or multi-tenant workloads need an operator-provided stronger boundary, and deployment-specific image governance, egress controls, key custody, retention, and host hardening remain outside Workcell's v1 guarantee.

## Learn more

The repository documents the workcell definition, stable CLI and exit codes, runtime lifecycle, security model, platform compatibility, examples, verification, and release artifacts.
