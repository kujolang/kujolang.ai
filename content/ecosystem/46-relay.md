---
title: "Relay"
custom_url: relay
description: "A local, operator-controlled composition and execution layer for bounded agent missions, policy-checked tools, and verifiable evidence."
featured_image: "/assets/images/ecosystem/relay-mission-orchestration.webp"
section: "Showcase"
tags: [Showcase, Orchestration]
order: 460
install_command: "git clone https://github.com/kujolang/relay.git"
github_url: "https://github.com/kujolang/relay"
launch_story: "Compose a bounded mission, run it in a repository or detached worktree, control its lifecycle, and retain evidence that can be inspected and verified."
scope_note: "Relay 1.0 is stable for local or operator-controlled use; it is not hosted orchestration, a multi-tenant service, hostile-code isolation, or enterprise certification."
keywords: "Relay, Kujo ecosystem, agent missions, local orchestration, verifiable evidence"
seo_title: "Relay — Kujo Ecosystem"
---

## What it does

Relay 1.0 composes and executes bounded agent missions through a Kujo-native CLI. It supports deterministic fixture chat and model probes, environment and agent validation, and mission runs in an existing repository or an isolated Git worktree. Operators can create, run, inspect, pause, resume, repair, cancel, clean up, and report on a mission without granting unrestricted shell access.

## Policy-bound execution

Mission actions are declarative and checked before execution. Writes require both an explicit write policy and approval; commands use direct argument arrays, fixed executable paths, bounded environments, allowlists, and hashes for repository scripts. Capabilities bind a run, session, workspace, nonce, expiry, and call count, then reject reuse or revocation violations.

## Durable mission evidence

Relay records run state, events, receipts, PackWrite packets, tool results, ChangeBucket measurements, Eval results, and RunLedger lifecycle evidence. Complete exports can be rebuilt, inspected, watched, and verified against SHA-256 integrity data. Partial exports stay visibly incomplete and never claim valid integrity.

## Why it belongs in Kujo

Relay demonstrates how Kujo's local-first ecosystem composes into an operator-controlled mission layer. Fixture mode stays deterministic and offline; live provider calls must travel through Watchdog, while Agents SDK policies, explicit budgets, cooperative cancellation, detached worktrees, and verifiable artifacts keep execution authority visible.

## Operating boundary

Git worktrees separate source changes but are not containers or virtual machines. Relay's local evidence store is not replicated multi-host storage, and SHA-256 seals detect tampering rather than proving identity or custody. Provider compatibility, infrastructure hardening, authentication, tenancy, retention, and production approval remain deployment responsibilities.

## Learn more

The repository documents the stable CLI and machine contracts, mission formats, evidence schemas, security model, integration matrix, compatibility policy, examples, platform support, and release verification gates.
