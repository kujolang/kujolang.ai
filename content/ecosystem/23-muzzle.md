---
title: "Muzzle"
custom_url: muzzle
description: "Quiet workflow execution with full disk logs, compact summaries, manifests, loop state, dry runs, and secret redaction."
featured_image: "/assets/images/ecosystem/muzzle-bounded-workflow.webp"
section: "Tooling"
tags: [Tool, Execution]
order: 200
install_command: "kennel tool install muzzle"
github_url: "https://github.com/kujolang/muzzle"
launch_story: "Keep agent context focused while retaining the complete operational record on disk."
scope_note: "Muzzle controls output shape and workflow contracts; commands retain the authority of the environment running them."
keywords: "Muzzle, Kujo ecosystem, Tool, Execution"
seo_title: "Muzzle — Kujo Ecosystem"
version: "1.1.2"
latest_release_url: "https://github.com/kujolang/muzzle/releases/tag/v1.1.2"
release_status: "Version identifies the published release. The Kennel command selects the latest stable registry package; see scope_note for release boundaries."
last_updated: "2026-10-12"
---

## What it does

Quiet workflow execution with full disk logs, compact summaries, manifests, loop state, dry runs, and secret redaction.

## Why it belongs in Kujo

Keep agent context focused while retaining the complete operational record on disk.

## Operating boundary

Muzzle controls output shape and workflow contracts; commands retain the authority of the environment running them.

## Learn more

The repository is the source of truth for current setup, commands, examples, security notes, compatibility, and verification evidence.

## Version 1.1.2

This patch release hardens initialization, cleanup, option parsing, loop state, and failure excerpts. It also reduces repeated work in argument parsing, retention selection, and workflow snapshot preparation. Existing CLI and JSON contracts remain compatible.

Install or update the command with Kennel:

```bash
kennel tool install muzzle
# For an existing unpinned installation:
kennel tool update muzzle
muzzle version
```

Expected version: `Muzzle v1.1.2`. For a project dependency, use `kennel add muzzle`.

Existing projects should add `state/` to `.muzzle/.gitignore`; initialization preserves user-owned files. Use one loop writer per project. Full logs may contain secrets, and workflow scripts retain the caller's permissions.

See the [release notes](https://github.com/kujolang/muzzle/releases/tag/v1.1.2) and [Muzzle documentation](https://docs.kujolang.ai/tools/muzzle/) for setup and compatibility details.
