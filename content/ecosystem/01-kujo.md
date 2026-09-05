---
title: "Kujo"
custom_url: kujo
description: "The VM-first programming language and runtime for AI-native software, local-first automation, agentic workflows, and practical scripting."
featured_image: "/assets/images/ecosystem/kujo-language-runtime.webp"
section: "Primitives"
tags: [Core, Language]
order: 10
install_command: "curl -fsSL https://kujolang.ai/install.sh | bash -s -- --source"
github_url: "https://github.com/kujolang/kujo"
launch_story: "The ecosystem core: readable source, explicit capabilities, deterministic tooling contracts, and strong native APIs."
scope_note: "Kujo is a general-purpose language, not a sandbox. Use capability-minimal execution for untrusted scripts."
keywords: "Kujo, Kujo ecosystem, Core, Language"
seo_title: "Kujo — Kujo Ecosystem"
---

## What it does

The VM-first programming language and runtime for AI-native software, local-first automation, agentic workflows, and practical scripting.

## Why it belongs in Kujo

The ecosystem core: readable source, explicit capabilities, deterministic tooling contracts, and strong native APIs.

## Operating boundary

Kujo is a general-purpose language, not a sandbox. Use capability-minimal execution for untrusted scripts.

## Runtime upgrades (implemented, unreleased)

`kujo upgrade` is implemented on the Kujo repository's main branch. As of September 5, 2026, the latest published runtime is **v1.2.3**, which does not include the command. First install a release containing it through your existing installer or package manager once one is published.

For supported standalone installations, the command selects the latest or an exact stable release, checks its published SHA-256, and replaces only the running runtime executable. `kujo upgrade --check --json` reports availability without writing installation files. Ecosystem tools, source refs, package pins, and project dependencies keep their own update workflows.

npm, Cargo, and other recognized managed installations must use their original package manager. Successful replacements retain a backup; a crash between the Windows replacement renames can require manual recovery.

Read the [Kujo runtime upgrade guide](https://docs.kujolang.ai/upgrade/) for syntax, downgrade policy, JSON output, bootstrap steps, and recovery limits. Check [published Kujo releases](https://github.com/kujolang/kujo/releases) for availability.

## Learn more

The repository is the source of truth for current setup, commands, examples, security notes, compatibility, and verification evidence.
