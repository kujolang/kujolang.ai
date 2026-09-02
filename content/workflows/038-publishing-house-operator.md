---
title: "Publishing House Operator"
custom_url: "publishing-house-operator"
description: "Run the Kujo Publishing House as a resumable, policy-bound editorial control loop."
featured_image: "/assets/images/ecosystem/workflow-publishing-house-daily-desk.webp"
social_image: "/assets/images/social/publishing-house-operator.jpg"
section: "production capable with limitations"
order: "380"
install_command: "git clone https://github.com/kujolang/kujo-workflows.git && cd kujo-workflows && publishing-house-operator/bin/publishing-house --json init"
github_url: "https://github.com/kujolang/kujo-workflows/tree/main/publishing-house-operator"
launch_story: "A local-first control layer that moves publication-specific work through bounded editorial workflows without turning agents into the scheduler or state store."
scope_note: "Fixture-operational today. Live model/retrieval workers and authenticated Git publication effects remain fail-closed until their adapters and credentials are configured."
version: "0.3.0"
last_updated: "2026-09-02"
keywords: "Kujo Publishing House operator, editorial automation, StoryDesk, Dispatch, autonomous publishing workflow"
seo_title: "Publishing House Operator | Kujo Workflows"
seo_description: "Run resumable, publication-profile-driven editorial work with durable state, exact-version approvals, bounded effects, and exception-based operation."
---

## Outcome

The Publishing House Operator is the small, durable control loop above Kujo's eleven Publishing House workflow kits. A manual, scheduled, or event-driven invocation reads StoryDesk work, acquires a local lease, selects eligible items, launches only the bounded workers needed for the current phase, records checkpoints and receipts, and exits.

StoryDesk remains the editorial control desk. Dispatch owns resumable workflow execution. Dossier, BluePencil, GalleyPack, AssetWorks, VersionSeal, PressWire, and ReaderSignal retain their existing evidence, review, version, asset, approval, publication, and learning authority. The operator stores scheduling state and references; it is not an agent, publication database, approval authority, or deployment system.

## Publication profiles and intake

Portable profiles currently describe four targets: the personal blog, `kujolang.ai`, `docs.kujolang.ai`, and `agents.kujolang.ai`. Each profile supplies its source-of-truth paths, voice, formats, evidence rules, assets, build and validation commands, deployment contract, approval policy, verification, measurement, refresh, and correction behavior. New publications are configuration rather than framework forks.

SourcePack intake preserves original notes and files before producing a normalized editorial view. Weekly, monthly, campaign, release, and evergreen plans import deterministic commissions into StoryDesk with priorities, windows, dependencies, series, clusters, adaptations, and refresh lineage.

```bash
publishing-house-operator/bin/publishing-house --json intake \
  --publication personal-blog \
  --format technical-essay \
  --source ./rambled-notes.md

publishing-house-operator/bin/publishing-house --json plan import ./september-2026.json
publishing-house-operator/bin/publishing-house --json tick --limit 4
publishing-house-operator/bin/publishing-house --json status
```

## Control and safety

Ticks are lease-protected, idempotent, retry-bounded, checkpointed, and safe to resume. Dependencies, publication windows, daily limits, per-publication limits, and approval gates constrain eligible work. Failures block the affected item without granting unrelated work additional authority.

Exact-version human approval remains the default. Profiles may narrowly opt low-risk classes such as canonical agent-site sync, metadata repair, or strongly sourced documentation corrections into automatic flow. Any changed checksum invalidates approval. Only PressWire may report a publication effect, and a push is not success until the configured public verification passes.

Event intake records policy-selected StoryDesk candidates for releases, CLI or API changes, agent changes, site problems, stale evidence, search opportunities, and performance shifts. It does not silently commission or publish every change. ReaderSignal and WebOps observations return evidence-linked candidates to StoryDesk instead of rewriting published work.

## Readiness boundary

Deterministic fixture mode proves intake, planning, routing, approvals, adaptation lineage, resumability, duplicate prevention, local publication effects, and verification across the eleven Publishing House workflows. Live Agents SDK model and retrieval adapters, authenticated Git push/PR/merge effects, and live measurement credentials are not configured in the checked-in operator. Missing capabilities fail closed and emit an exception rather than substituting fixtures.

## Source

- [Publishing House Operator on GitHub](https://github.com/kujolang/kujo-workflows/tree/main/publishing-house-operator)
- [Kujo Workflows](https://github.com/kujolang/kujo-workflows)
