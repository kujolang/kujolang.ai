---
title: "Kujo"
custom_url: kujo
description: "The VM-first programming language and runtime for AI-native software, local-first automation, agentic workflows, and practical scripting."
featured_image: "/assets/images/ecosystem/kujo-language-runtime.webp"
section: "Primitives"
tags: [Core, Language]
order: 10
install_command: "curl -fsSL https://kujolang.ai/install.sh | KUJO_RELEASE_VERSION=v1.9.0 bash"
github_url: "https://github.com/kujolang/kujo"
launch_story: "The ecosystem core: readable source, explicit capabilities, deterministic tooling contracts, and strong native APIs."
scope_note: "Kujo 1.9.0 is released for Linux x64/arm64, macOS x64/arm64 and Windows x64 through native archives and npm. The 1.8 series adds stronger optional inference and shared editor analysis, measured generator performance improvements, and expanded VM/interpreter parity coverage. Wave C beta and Wave D alpha remain experimental; participant SDK packages remain private/unpublished."
keywords: "Kujo, Kujo ecosystem, Core, Language"
seo_title: "Kujo — Kujo Ecosystem"
version: "1.9.0"
latest_release_url: "https://github.com/kujolang/kujo/releases/tag/v1.9.0"
release_status: "Version identifies the latest published GitHub Release. Unpinned clone commands select default-branch source; see scope_note for release boundaries."
last_updated: "2026-10-22"
---

## What it does

The VM-first programming language and runtime for AI-native software, local-first automation, agentic workflows, and practical scripting.

## Why it belongs in Kujo

The ecosystem core: readable source, explicit capabilities, deterministic tooling contracts, and strong native APIs.

## Operating boundary

Kujo 1.9.0 is released for Linux x64/arm64, macOS x64/arm64 and Windows x64 through native archives and npm. The 1.8 series adds stronger optional inference and shared editor analysis, measured generator performance improvements, and expanded VM/interpreter parity coverage. Wave C beta and Wave D alpha remain experimental; participant SDK packages remain private/unpublished.

## Install and maintain the runtime

On Linux and macOS, the ecosystem installer above installs the stable Kujo binary and its default tool group; verify the runtime with `kujo --version`. Windows users can use the release archive or npm. The standalone runtime runs Kujo programs without Python, Node.js, or a Rust toolchain. Source builds use Rust, and npm installations use Node.js.

Kujo v1.8.0 extends useful gradual inference across destructuring, imports, structs, async values, and callables without making dynamic programs statically mandatory. Shared analysis improves diagnostics, hover, completion, and edit invalidation. The runtime also removes measured generator-resume copying while preserving closure, task, cancellation, and effect-ordering semantics.

Use `kujo upgrade --check` to inspect a standalone runtime update, then `kujo upgrade` to install it. Package-manager installations use their original manager. Kennel and other ecosystem tools retain their own release and update workflows.

Read the [installation guide](https://docs.kujolang.ai/install/), [runtime guide](https://docs.kujolang.ai/learn/runtime/), and [Kujo v1.8.0 release](https://github.com/kujolang/kujo/releases/tag/v1.8.0).

## Install from npm

```bash
npm install --global @kujolang/kujo-runtime@1.9.0
kujo --version
```

Expected version output: `kujo 1.9.0`.

The runtime resolver and all five native npm packages are published at 1.9.0. Native archives, deterministic source, checksums and exact-source provenance are attached to the release. Package-manager installs use their original manager for upgrades.

## What changed in 1.8

- Smarter: optional inference now follows nested destructuring, known module exports, struct fields, promises and callable aliases, while unknown values retain dynamic fallback.
- Faster: generator resume reuses continuation-owned bytecode; the retained nested-generator workload improved 6.7% at the paired median, with full variance evidence published.
- Tighter: shared CLI/LSP analysis, safe transitive invalidation, longitudinal workloads, and expanded optimizer/parity regressions strengthen correctness without new syntax or migration work.
- Distribution: all five native archives, deterministic source, checksums, and six lifecycle-script-free npm packages passed published-install validation.

## Experimental companion boundaries

Wave C remains **experimental beta**, opt-in and required/deny within a bounded single-effect domain, with alpha compatibility retained. Wave D handoffs and participant SDK APIs remain **experimental alpha** under a trusted-local-host model. Participant SDK packages are private/unpublished, unlike the published runtime npm packages. Dispatch alone decides replay admission; evidence correlation does not authorize execution.

Kujo 1.8 does not claim exactly-once execution, universal rollback, general machine-loss recovery, remote authenticated participant trust, multi-effect assurance or stable participant SDK APIs. Source-blind agent adopter rehearsal passed. Human adopter usability remains post-release validation.

See the [release notes](https://github.com/kujolang/kujo/blob/main/docs/RELEASE_NOTES_1_8.md) and [publication record](https://github.com/kujolang/kujo/blob/main/release/kujo-1.8.0-publication.json) for artifact identities and observed release gates.

## Learn more

The repository is the source of truth for current setup, commands, examples, security notes, compatibility, and verification evidence.

## Runtime patch 1.8.1

[Kujo 1.8.1](https://github.com/kujolang/kujo/releases/tag/v1.8.1) is published and is the required runtime for Dispatch 1.4.0 and the Paperclip expansion. See the release for patch details; the 1.8.0 feature overview above remains historical.

## Runtime patch 1.8.2

Kujo 1.8.2 fixes dependency advisories and maintenance warnings, preserves archive and stored-credential behavior, hardens runtime capability boundaries and corrects native dictionary handling. It also provides bounded HTTP stream collection. Kujo programs keep their existing archive API; Rust embedders using `Value::ZipArchive.writer` must follow the [ZIP 9 migration guide](https://github.com/kujolang/kujo/blob/v1.8.2/docs/ZIP_9_RUST_MIGRATION.md).

See the [1.8.2 release notes](https://github.com/kujolang/kujo/blob/main/docs/RELEASE_NOTES_1_8_2.md) for compatibility and verification scope.


## Runtime release 1.9.0

Kujo 1.9.0 adds checked nested collection and struct assignment, strict UTF-8 conversion, snapshot-safe byte iteration, fallible comparator sorting, regex callbacks and match counting, headerless CSV records, fixed decimal formatting and explicit wrapping arithmetic. Shared bytecode and storage reuse reduce copying while preserving retained values and failed-write behavior.

Native installation and upgrades from 1.8.2, plus npm installation without lifecycle scripts, passed on all five supported platforms. Read the [1.9.0 release notes](https://github.com/kujolang/kujo/blob/main/docs/RELEASE_NOTES_1_9_0.md) and [publication record](https://github.com/kujolang/kujo/blob/main/release/kujo-1.9.0-publication.json). Experimental companion boundaries remain unchanged.
