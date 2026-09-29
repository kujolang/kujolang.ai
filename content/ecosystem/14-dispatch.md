---
title: "Dispatch"
custom_url: dispatch
description: "Dispatch 1.3.0 orchestrates resumable, routed, approved, and auditable AI workflows with persisted evidence."
featured_image: "/assets/images/ecosystem/dispatch-workflow-orchestration.webp"
section: "Primitives"
tags: [Primitive, Orchestration]
order: 60
install_command: "kennel add dispatch"
github_url: "https://github.com/kujolang/dispatch"
launch_story: "Dispatch 1.3.0 routes bounded AI work through policy constraints, approvals, resumable state, and inspectable evidence."
scope_note: "Dispatch 1.3.0 requires Kujo 1.6.0. Durable review, process-owned locks, policy-preserving resume and evidence inspection are included. Wave C beta assurance and Wave D alpha interoperability remain experimental and opt-in."
keywords: "Dispatch, Kujo ecosystem, Primitive, Orchestration"
seo_title: "Dispatch — Kujo Ecosystem"
version: "1.3.0"
last_updated: "2026-09-29"
latest_release_url: "https://github.com/kujolang/dispatch/releases/tag/v1.3.0"
release_status: "Version identifies the published release. The Kennel command selects the latest stable registry package; see scope_note for release boundaries."
---

## What it does

Dispatch 1.3.0 runs resumable multi-step workflows with templates, retries, approvals, persisted state, traces, reports, policy controls, signed bundles, and deterministic agent/provider/model routing.

## Why it belongs in Kujo

Auditable workflow orchestration for missions that must pause, resume, and preserve operator control.

## Operating boundary

Dispatch 1.3.0 requires Kujo 1.6.0. Durable review, process-owned locks, policy-preserving resume and evidence inspection are included. Wave C beta assurance and Wave D alpha interoperability remain experimental and opt-in.

## Release

Dispatch 1.3.0 is the current release. It adds durable review checkpoints, restart-safe control, persisted assurance negotiation, retrieval preferences, and bounded participant evidence correlation. Dispatch alone decides replay; a handoff or successful correlation does not authorize an effect. Install from the [v1.3.0 GitHub release](https://github.com/kujolang/dispatch/releases/tag/v1.3.0) or follow the repository's pinned release instructions.

## Learn more

The repository is the source of truth for current setup, commands, examples, security notes, compatibility, and verification evidence.

## Experimental integration boundary

The SQLite, Workcell Git CAS and Ability assurance profiles support the bounded
single-effect required/deny beta domain. Alpha assurance remains compatible.
Agents SDK, MCP, HTTP, process and external participant integrations carry
references into Dispatch; they do not become controllers. Participant SDKs remain
alpha and unpublished. Effect-set diagnostics are read-only and do not authorize
multi-effect replay. This release does not provide exactly-once effects, universal
rollback, remote participant trust or general machine-loss recovery.
