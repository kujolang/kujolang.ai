---
title: "Kujo for Paperclip"
custom_url: paperclip
description: "A local Paperclip plugin for focused context, change review, and reproducible failure evidence backed by Kujo tools."
featured_image: "/assets/images/ecosystem/paperclip-workspace-intelligence.webp"
social_image: "/assets/images/social/paperclip.jpg"
section: "Tooling"
tags: [Tool, Agents]
order: 550
install_command: "npx paperclipai plugin install @kujolang/paperclip"
github_url: "https://github.com/kujolang/paperclip"
launch_story: "Give Paperclip agents a small, visible workspace for choosing context, reviewing changes, and preserving failure evidence."
scope_note: "The plugin runs local Kujo components inside Paperclip. It does not execute arbitrary commands, replace repository tests, or claim suggested checks have run."
version: "0.1.7"
last_updated: "2026-09-04"
keywords: "Kujo Paperclip plugin, Paperclip agents, context pack, change review, failure evidence"
seo_title: "Kujo for Paperclip — Context, Review, and Failure Evidence"
seo_description: "Install the Kujo plugin for Paperclip to select focused context, review change scope, and save redacted failure evidence from the current task view."
---

## What it does

Kujo adds a workspace to Paperclip's current task view and a shared Kujo tab on project, issue, and run pages. Agents can select a bounded Context Pack, measure a change and prepare a Review Pack, or save supplied command output as redacted Failure Evidence.

## Install it

You need Paperclip `2026.824.1` or later and Node.js `24.11.0` or later.

```bash
npx paperclipai plugin install @kujolang/paperclip
```

Restart Paperclip if it is already running, then open an issue. The Kujo workspace appears in the task view. The package includes Kujo runtime binaries for supported macOS, Linux, and Windows systems. It needs no separate Kujo install or Kujo API key.

## A simple workflow

1. Create a Context Pack before the agent reads the repository broadly.
2. Make and test the change with the project's normal tools.
3. Create a Review Pack to inspect scope, risk signals, and suggested checks.
4. If a command fails, save its bounded output as Failure Evidence.

The plugin stores the latest result in Paperclip plugin state. It does not write reports into the project repository.

## Kujo components inside

- **Scent** selects a small, task-specific file set.
- **ChangeBucket** measures change size and risk signals.
- **PatchBrief** prepares the review handoff.
- **CaseFile** records bounded, redacted failure evidence.

The package pins and checksums these components. It does not download component code while installing or running.

## Operating boundary

The plugin reads only a canonical Paperclip workspace. Its content tool can open only files already selected by the matching Context Pack, and it rejects traversal, symlink escapes, binary files, and oversized files. Failure Evidence records text supplied by the caller; it never acts as a command runner.

Current Paperclip releases require the unversioned package name shown above. An upstream fix for exact scoped versions is under review in [paperclipai/paperclip#12745](https://github.com/paperclipai/paperclip/pull/12745). This does not block normal installation or use.

## Learn more

Read the [full installation and usage guide](https://github.com/kujolang/paperclip#install-in-30-seconds), inspect the [v0.1.7 release](https://github.com/kujolang/paperclip/releases/tag/v0.1.7), or install the package from [npm](https://www.npmjs.com/package/@kujolang/paperclip).
