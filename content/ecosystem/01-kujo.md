---
title: "Kujo"
custom_url: kujo
description: "The VM-first programming language and runtime for AI-native software, local-first automation, agentic workflows, and practical scripting."
featured_image: "/assets/images/ecosystem/kujo-language-runtime.webp"
section: "Primitives"
tags: [Core, Language]
order: 10
install_command: "curl -fsSL https://kujolang.ai/install.sh | bash"
github_url: "https://github.com/kujolang/kujo"
launch_story: "The ecosystem core: readable source, explicit capabilities, deterministic tooling contracts, and strong native APIs."
scope_note: "Kujo 1.7.0 is released for Linux x64/arm64, macOS x64/arm64 and Windows x64 through native archives and npm. It adds native absolute-path validation, opt-in Windows child-process lifetime ownership and first-party MCP generation. Wave C beta and Wave D alpha remain experimental; participant SDK packages remain private/unpublished."
keywords: "Kujo, Kujo ecosystem, Core, Language"
seo_title: "Kujo — Kujo Ecosystem"
version: "1.7.0"
latest_release_url: "https://github.com/kujolang/kujo/releases/tag/v1.7.0"
release_status: "Version identifies the latest published GitHub Release. Unpinned clone commands select default-branch source; see scope_note for release boundaries."
last_updated: "2026-09-28"
---

## What it does

The VM-first programming language and runtime for AI-native software, local-first automation, agentic workflows, and practical scripting.

## Why it belongs in Kujo

The ecosystem core: readable source, explicit capabilities, deterministic tooling contracts, and strong native APIs.

## Operating boundary

Kujo 1.7.0 is released for Linux x64/arm64, macOS x64/arm64 and Windows x64 through native archives and npm. It adds native absolute-path validation, opt-in Windows child-process lifetime ownership and first-party MCP generation. Wave C beta and Wave D alpha remain experimental; participant SDK packages remain private/unpublished.

## Install and maintain the runtime

On Linux and macOS, the ecosystem installer above installs the stable Kujo binary and its default tool group; verify the runtime with `kujo --version`. Windows users can use the release archive or npm. The standalone runtime runs Kujo programs without Python, Node.js, or a Rust toolchain. Source builds use Rust, and npm installations use Node.js.

Kujo v1.7.0 includes isolated tool imports, native filesystem and process operations, bounded web-data processing, and VM/interpreter correctness improvements. Linux and macOS package launchers can use native locks, ownership checks, atomic command links, and exact process replacement. Host capabilities and platform limits remain explicit.

Use `kujo upgrade --check` to inspect a standalone runtime update, then `kujo upgrade` to install it. Package-manager installations use their original manager. Kennel and other ecosystem tools retain their own release and update workflows.

Read the [installation guide](https://docs.kujolang.ai/install/), [runtime guide](https://docs.kujolang.ai/learn/runtime/), and [Kujo v1.7.0 release](https://github.com/kujolang/kujo/releases/tag/v1.7.0).

## Install from npm

```bash
npm install --global @kujolang/kujo-runtime@1.7.0
kujo --version
```

Expected version output: `kujo 1.7.0`.

The runtime resolver and all five native npm packages are published at 1.7.0. Native archives, checksums and exact-source provenance are attached to the release. Package-manager installs use their original manager for upgrades.

## What changed in 1.6

- Runtime correctness: closure/upvalue hardening, generator/task/async improvements, VM/interpreter parity work, and the optimized loop/conditional early-return fix.
- Durable execution: companion Dispatch workflows provide review checkpoints, restart/resume and replay admission; these remain separate from the language runtime.
- Observability: runtime measurements and Watchdog/RunLedger evidence correlation preserve observation as a separate responsibility from control.
- Experimental effect assurance and participant interoperability: SQLite, Git and Ability effect families, a generic correlation core, and independent TypeScript/Python participant adoption.

## Experimental companion boundaries

Wave C remains **experimental beta**, opt-in and required/deny within a bounded single-effect domain, with alpha compatibility retained. Wave D handoffs and participant SDK APIs remain **experimental alpha** under a trusted-local-host model. Participant SDK packages are private/unpublished, unlike the published runtime npm packages. Dispatch alone decides replay admission; evidence correlation does not authorize execution.

Kujo 1.6 does not claim exactly-once execution, universal rollback, general machine-loss recovery, remote authenticated participant trust, multi-effect assurance or stable participant SDK APIs. Source-blind agent adopter rehearsal passed. Human adopter usability remains post-release validation.

See the [publication record](https://github.com/kujolang/kujo/blob/main/docs/KUJO_1_6_RELEASE.md) for artifact identities and observed release gates.

## Learn more

The repository is the source of truth for current setup, commands, examples, security notes, compatibility, and verification evidence.
