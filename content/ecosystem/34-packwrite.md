---
title: "PackWrite"
custom_url: packwrite
description: "Compile project intent and bounded repository context into deterministic, validated execution packs for implementation agents and reviewers."
featured_image: "/assets/images/ecosystem/packwrite-execution-pack.webp"
section: "Tooling"
tags: [Tool, Agents]
order: 260
install_command: "git clone https://github.com/kujolang/packwrite.git"
github_url: "https://github.com/kujolang/packwrite"
launch_story: "Turn one large project brief into a reviewable operating manual that agents can execute phase by phase."
scope_note: "PackWrite compiles planning artifacts locally; it does not implement the project, host models, deploy code, or replace review."
keywords: "PackWrite, Kujo ecosystem, Tool, Execution Packs"
seo_title: "PackWrite — Kujo Ecosystem"
version: "1.1.0"
last_updated: 2026-09-04
---

## What it does

PackWrite is an AI-assisted, local-first workflow-pack compiler. Give it a repository-level `MEGA_PROMPT.md`; it collects lightweight, secret-aware repository context, calls an OpenAI-compatible model endpoint, and writes a deterministic `agent/` pack for implementation and independent review.

```text
strategy AI → MEGA_PROMPT.md → PackWrite → agent/ pack → implementation agent → reviewer
```

The model fills the content. PackWrite owns and validates the structure, output boundary, and failure behavior.

## Why it belongs in Kujo

Long agent tasks drift when intent, constraints, and evidence requirements live only in chat. PackWrite makes the operating contract explicit, versionable, inspectable, and reusable beside the code.

## Five-minute workflow

```bash
cd your-project
packwrite doctor --strict
packwrite init MEGA_PROMPT.md --dry-run
packwrite init MEGA_PROMPT.md --provider deepseek --model deepseek-v4-pro
packwrite validate
packwrite summary
packwrite prompt deepseek
packwrite prompt codex-review
```

`doctor --strict` checks the prompt, provider, endpoint, API-key environment, and output state before a paid model call. `--dry-run` runs generation and manifest validation without writing. `summary`, `validate --json`, and `doctor --strict --json` provide deterministic local and CI-readable status.

## What the pack contains

```text
agent/
  MASTER.md
  TODO.md
  HANDOFF.md
  DECISIONS.md
  REVIEW_CHECKLIST.md
  DEEPSEEK_START.md
  CODEX_REVIEW_PROMPT.md
  phases/00-project-brief.md
  phases/01-*.md
```

The stable master brief, scoped phase files, mutable handoff and decision records, review checklist, and ready-to-paste prompts give downstream agents an explicit path from intent to verified completion.

## Current 1.1 capabilities

- Generate, validate, summarize, inspect configuration, diagnose setup, and print clean handoff prompts from one CLI.
- Select DeepSeek, OpenAI, or a local OpenAI-compatible endpoint; route other providers through an explicit compatible gateway.
- Configure prompt, output, model, repository-context, and optional pack surfaces through `packwrite.toml`.
- Run offline and in CI with a fake-response manifest, deterministic validation, quiet output, and machine-readable JSON.
- Clean-replace an existing pack with `--overwrite`, pruning stale files only after a staged replacement validates.
- Reject path traversal, symlink escapes, control characters, credentialed endpoints, secret-looking generated paths, unsafe output directories, oversized model responses, and invalid manifests before promotion.

## Provider and privacy boundary

API keys come from environment variables only. PackWrite sends a bounded repository summary rather than the full checkout, skips common dependency/build directories and secret-looking paths by default, and requires every generated path to stay inside the configured output directory.

The adapter speaks the OpenAI-compatible chat-completions protocol. Anthropic is not a native endpoint in 1.1; Claude and other non-compatible providers require an OpenAI-compatible gateway.

## Operating boundary

PackWrite creates plans, prompts, and handoffs. It is not a hosted agent runtime, deployment system, organization policy service, signing system, or implementation agent. Review the generated pack before code changes begin, and use the repository's real tests and release gates during execution.

## Release

PackWrite 1.1.0 is the current released version. It adds `summary`, JSON and quiet modes, stronger staged-write and endpoint controls, nested output support, bounded diagnostics, a golden offline pack fixture, and the official release checklist.

## Learn more

The [PackWrite repository](https://github.com/kujolang/packwrite) contains the CLI, complete configuration reference, end-to-end guide, troubleshooting material, tests, and [v1.1.0 release](https://github.com/kujolang/packwrite/releases/tag/v1.1.0).
