---
title: "Publishing House Factory"
custom_url: "publishing-house-factory"
description: "Turn sourced editorial material into a reviewable content package."
featured_image: "/assets/images/ecosystem/publishing-house-factory.webp"
social_image: "/assets/images/social/publishing-house-factory.jpg"
section: "Factories"
template: factory
order: 920
install_command: "git clone https://github.com/kujolang/publishing-house-factory.git\ncd publishing-house-factory\ngit checkout 38e7900a16f8482d12ad6b8b6a15f538d7ee3099"
github_url: "https://github.com/kujolang/publishing-house-factory"
launch_story: "Technical writers and product teams preparing a sourced campaign for human editorial review."
scope_note: "Local software. Inspect the setup guide and review boundaries before authorizing live model calls."
last_updated: "2026-11-13"
seo_title: "Publishing House Factory \u2014 Kujo Factories"
release_status: "Source preview; no published GitHub Release"
version: "Source preview"
---

## What you give it

A brief such as `examples/videoops-launch.json` with audience, voice, objective, constraints and 1–10 local UTF-8 source files, each at most 100 KB, beneath the brief directory. HTTPS source URLs record provenance; the factory does not fetch them. The example preserves VideoOps README and onboarding evidence; it does not turn a measured setup time into a universal promise.

## What happens

1. Publishing House Operator owns phase checkpoints, leases and bounded retries. StoryDesk records the commission; a Commissioning Editor proposes its angle and outline.
2. A Standards & Evidence Editor maps claims to captured excerpts in Dossier. A Technical Editor/Writer drafts the article.
3. A separate Standards & Evidence Editor call reviews the draft through BluePencil, with at most two writer revisions. The text-only assets stage calls no image provider.
4. A Franchise & Adaptation Editor creates the newsletter, three social posts and landing copy. A Copy Chief reviews adaptations with at most two revisions.
5. Trusted code renders escaped HTML. GalleyPack freezes the manifest and VersionSeal records an approval request. The operator stops at approval_required.

## What you receive

An article, newsletter, three social posts and local landing-page preview, plus source snapshots, claim references, model proposals, independent review records and a hashed package manifest. The Factory Floor has six campaign previews and a review desk for tracing revisions.

## Factory Floor and demonstration

Recorded live editorial campaign and narrated walkthrough. The real Factory Floor screenshot shows retained campaign state; it does not grant publication approval.

FACTORY_MEDIA

## Accountability and verification

Model proposals are sequential and tool-free. An excerpt match proves that text exists in a source, not that the claim is true. Model review is not human approval. Package verification re-hashes source snapshots, outputs and proposal evidence. No command in this version approves or publishes the campaign. Source text goes to the configured model account; do not supply material you cannot share with that provider.

## Installation and first run

macOS or Linux, including compatible WSL, Git, Python 3.10+, Node 26.12.1 or later 26.x and a Codex account. Setup downloads pinned sources and the Kujo runtime. No Docker, FFmpeg, database or sibling checkout is needed. Minimal Linux may need libatomic1.

Read the [authoritative setup guide](https://github.com/kujolang/publishing-house-factory/blob/38e7900a16f8482d12ad6b8b6a15f538d7ee3099/docs/AGENT-SETUP.md). The hero command checks out the revision described here. Install its dependencies and pinned tools:

```sh
npm ci
npm run setup
```

Authenticate separately with `npm run login`. Live execution uses your provider allowance and needs your authorization. Authentication reuse, where supported, copies only auth into the factory’s private ignored home, not personal tools or hooks.

Run local checks:

```sh
npm run doctor
npm run verify
```

Start the loopback Factory Floor with `npm start`, then open `http://127.0.0.1:4382`. In another terminal, an authorized live run uses:

```sh
npm run factory -- run examples/videoops-launch.json
```

Use `npm run factory -- status`, `npm run factory -- resume RUN_ID` and `npm run factory -- verify RUN_ID` to inspect state, recover eligible work and verify bytes.

## Release status and limitations

Source preview: no published GitHub Release was present when checked on 2026-11-13. The package version 0.1.0 is not a release record. This page uses commit [`38e7900a16f8`](https://github.com/kujolang/publishing-house-factory/tree/38e7900a16f8482d12ad6b8b6a15f538d7ee3099).

The contract is text-only and supports the listed campaign formats. New destinations or formats require an extension. Resume preserves completed work after a blocked cause is fixed; changed inputs or exhausted review revisions require a fresh run. Publication-phase adapter requests are rejected.

## Related tools and factories

[StoryDesk](/ecosystem/storydesk/) commissions work, [Dossier](/ecosystem/dossier/) records evidence, [BluePencil](/ecosystem/bluepencil/) records review, [GalleyPack](/ecosystem/galleypack/) packages bytes and [VersionSeal](/ecosystem/versionseal/) records the approval request. The [Publishing House Operator](/ecosystem/workflows/publishing-house-operator/) owns execution. Installed Dispatch and Agents SDK sources support the operator’s dependency layout; this adapter calls Codex directly. PressWire is installed for compatibility, but runs no publication effects. [Product Launch Factory](/ecosystem/product-launch-factory/) consumes the reviewed editorial package.

## Get started

[Read the setup guide](https://github.com/kujolang/publishing-house-factory/blob/38e7900a16f8482d12ad6b8b6a15f538d7ee3099/docs/AGENT-SETUP.md), [inspect the source](https://github.com/kujolang/publishing-house-factory/tree/38e7900a16f8482d12ad6b8b6a15f538d7ee3099) or [compare all five factories](/ecosystem/factories/). Kujo remains the programming language and runtime beneath this wider set of tools; [start with the language](/language/) if you want to write your own programs.
