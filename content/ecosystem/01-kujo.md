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
scope_note: "Kujo 1.4.0 is published with native installer primitives and isolated tool imports. The standalone runtime needs no Python, Node.js, or Rust; individual tools can have their own requirements."
keywords: "Kujo, Kujo ecosystem, Core, Language"
seo_title: "Kujo — Kujo Ecosystem"
version: "1.4.0"
latest_release_url: "https://github.com/kujolang/kujo/releases/tag/v1.4.0"
release_status: "Version identifies the latest published GitHub Release. Unpinned clone commands select default-branch source; see scope_note for release boundaries."
last_updated: "2026-09-09"
---

## What it does

The VM-first programming language and runtime for AI-native software, local-first automation, agentic workflows, and practical scripting.

## Why it belongs in Kujo

The ecosystem core: readable source, explicit capabilities, deterministic tooling contracts, and strong native APIs.

## Operating boundary

Kujo 1.4.0 is published with native installer primitives and isolated tool imports. The standalone runtime needs no Python, Node.js, or Rust; individual tools can have their own requirements.

## Install and maintain the runtime

On Linux and macOS, the ecosystem installer above installs the stable Kujo binary and its default tool group; verify the runtime with `kujo --version`. Windows users can use the release archive or npm. The standalone runtime runs Kujo programs without Python, Node.js, or a Rust toolchain. Source builds use Rust, and npm installations use Node.js.

Kujo v1.4.0 includes isolated tool imports, native filesystem and process operations, bounded web-data processing, and VM/interpreter correctness improvements. Linux and macOS package launchers can use native locks, ownership checks, atomic command links, and exact process replacement. Host capabilities and platform limits remain explicit.

Use `kujo upgrade --check` to inspect a standalone runtime update, then `kujo upgrade` to install it. Package-manager installations use their original manager. Kennel and other ecosystem tools retain their own release and update workflows.

Read the [installation guide](https://docs.kujolang.ai/install/), [runtime guide](https://docs.kujolang.ai/learn/runtime/), and [Kujo v1.4.0 release](https://github.com/kujolang/kujo/releases/tag/v1.4.0).

## Learn more

The repository is the source of truth for current setup, commands, examples, security notes, compatibility, and verification evidence.
