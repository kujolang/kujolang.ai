---
title: "Publishing House Operator"
custom_url: "publishing-house-operator"
description: "Run the Kujo Publishing House as a resumable, policy-bound editorial control loop."
featured_image: "/assets/images/ecosystem/workflow-publishing-house-daily-desk.webp"
social_image: "/assets/images/social/publishing-house-operator.jpg"
section: "production-capable control plane"
order: "390"
install_command: "git clone https://github.com/kujolang/kujo-workflows.git && cd kujo-workflows && publishing-house-operator/bin/publishing-house --json init"
github_url: "https://github.com/kujolang/kujo-workflows/tree/main/publishing-house-operator"
launch_story: "A local-first control layer that moves publication-specific work through bounded editorial workflows without turning agents into the scheduler or state store."
scope_note: "Production-capable, provider-portable control plane with explicit adapters, checksum-bound receipts, bounded retries, and fail-closed publication authority."
version: "0.4.0"
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

For live work, the operator invokes one explicitly configured phase adapter instead of embedding a model provider or repository credential in the control plane:

```bash
export PUBLISHING_HOUSE_PHASE_ADAPTER=/absolute/path/to/phase-adapter
export PUBLISHING_HOUSE_PHASE_TIMEOUT_SECONDS=900
publishing-house-operator/bin/publishing-house --json tick --limit 4
```

The adapter receives a bounded JSON request and must return a checksum-bound receipt for the matching item, phase, and artifact. Only the approval/publication phase may report an external effect, and that effect still belongs to PressWire. The operator verifies the receipt before advancing state.

## Control and safety

Ticks are lease-protected, idempotent, retry-bounded, checkpointed, and safe to resume. Dependencies, the per-tick work limit, and approval gates constrain eligible work; plan records preserve publication windows for workflow policy. Failures block the affected item without granting unrelated work additional authority. After the cause is corrected, `publishing-house resume ITEM_ID` releases only that item back to the queue.

Exact-version human approval remains the default. Profiles may narrowly opt low-risk classes such as canonical agent-site sync, metadata repair, or strongly sourced documentation corrections into automatic flow. Any changed checksum invalidates approval. Only PressWire may report a publication effect, and a push is not success until the configured public verification passes.

Event intake records policy-selected StoryDesk candidates for releases, CLI or API changes, agent changes, site problems, stale evidence, search opportunities, and performance shifts. It does not silently commission or publish every change. ReaderSignal and WebOps observations return evidence-linked candidates to StoryDesk instead of rewriting published work.

## Production operation

The checked-in operator includes the live execution boundary, checksum validation, bounded provider retries, blocked-item recovery, durable state, and exact-version authority needed to run as a production control plane. Deterministic mode remains available for rehearsal and clean-machine verification; it is not the only execution path.

A deployment supplies its selected model and retrieval workers through the phase adapter. Sites that authorize automated Git effects configure an authenticated PressWire Git/static provider, and enabled measurement sources configure their ReaderSignal or WebOps credentials. Those are installation-specific authority and credential gates, not missing editorial architecture. If one is absent, the affected item stops with an explicit exception instead of falling back to a fixture or claiming a false success.

## Source

- [Publishing House Operator 0.4.0 source](https://github.com/kujolang/kujo-workflows/tree/v0.4.0/publishing-house-operator)
- [Kujo Workflows 0.4.0 release](https://github.com/kujolang/kujo-workflows/releases/tag/v0.4.0)
