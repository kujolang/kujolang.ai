---
title: "Product Launch Factory"
custom_url: "product-launch-factory"
description: "Collect a product launch around one verified source packet."
featured_image: "/assets/images/ecosystem/product-launch-factory.webp"
social_image: "/assets/images/social/product-launch-factory.jpg"
section: "Factories"
template: factory
order: 940
install_command: "git clone https://github.com/kujolang/product-launch-factory.git\ncd product-launch-factory"
github_url: "https://github.com/kujolang/product-launch-factory"
launch_story: "Product teams coordinating editorial, static-site and video candidates for a final human review."
scope_note: "Local software. Inspect the setup guide and review boundaries before authorizing live model calls."
last_updated: "2026-11-13"
seo_title: "Product Launch Factory \u2014 Kujo Factories"
release_status: "Published v0.1.0"
version: "v0.1.0"
latest_release_url: "https://github.com/kujolang/product-launch-factory/releases/tag/v0.1.0"
---

## What you give it

A launch brief such as `examples/webops-launch.json`, captured source text, verified existing evidence and up to three PNG or JPEG product images with provenance and reuse rights. Intake accepts a Software Factory export or an existing WebOps package. This release does not execute Software Factory to build an application.

## What happens

1. Source evidence verifies the incoming export or package and captures the product source texts.
2. Publishing House commissions, writes, independently edits and adapts the campaign.
3. WebOps checks the static landing page, applies bounded repairs to its copy and records browser evidence.
4. VideoOps plans, compiles, renders and checks a video from registered product images.
5. Launch review collects exact versions, detects drift and produces a local package awaiting human approval.

## What you receive

An article, newsletter, three social posts, website candidate, video MP4, editable composition, production records and exact source evidence in a versioned launch package. Five Factory Floor stations show retained handoffs, blocked states and deliverable previews.

## Factory Floor and demonstration

Approved v0.1.0 coordinator demonstration: source evidence, Publishing House, WebOps, VideoOps and launch review. This is the coordinator film, not the older generated campaign clip. The floor screenshot is the recorded example; its underlying campaign remains awaiting human review.

FACTORY_MEDIA

## Accountability and verification

Each handoff binds exact input and output bytes. Resume reuses completed handoffs only while their hashes match. Blocked work stays blocked until resolved; changed inputs require a new launch version. Editing, adding or deleting packaged files invalidates the reviewed version. Review every deliverable and play the whole video with sound before local approval.

## Installation and first run

macOS or Linux, Git, Python 3.10+, Node 26.12.1, npm, FFmpeg and Chromium operating-system libraries. A Codex login with model access is required for live work. The supplied live brief produces a silent video. Narration needs separate [configuration and explicit authorization](https://github.com/kujolang/product-launch-factory/blob/d61c7021b0469c45f909b8371205f0df3afbac8b/docs/VIDEO.md), or an existing recording. Source text goes to the configured model account.

Read the [authoritative setup guide](https://github.com/kujolang/product-launch-factory/blob/d61c7021b0469c45f909b8371205f0df3afbac8b/docs/AGENT-SETUP.md). The clone command gets the current default branch. Follow the setup guide in your checkout for current requirements. Install the dependencies and pinned tools:

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

Start the loopback Factory Floor with `npm start`, then open `http://127.0.0.1:4384`. In another terminal, an authorized live run uses:

```sh
npm run factory -- run examples/webops-launch.json
```

For a read-only recorded example, use `npm run demo` then `npm start`. This imports evidence without making model calls.

Use `npm run factory -- status`, `npm run factory -- resume RUN_ID` and `npm run factory -- verify RUN_ID` to inspect state, recover eligible work and verify bytes.

## Release status and limitations

Published GitHub release [v0.1.0](https://github.com/kujolang/product-launch-factory/releases/tag/v0.1.0). This page uses commit [`d61c7021b046`](https://github.com/kujolang/product-launch-factory/tree/d61c7021b0469c45f909b8371205f0df3afbac8b).

This release coordinates existing domain factories. It neither creates a new application nor publishes or deploys a campaign. It is a single-operator local tool. The example campaign still needs human editorial and full listening review. Approval of the coordinator demonstration does not approve the example campaign.

The retained fresh Ubuntu qualification reports 23 passing tests, CI verification, empty application caches, 67.073 seconds to pre-login setup and 69.625 seconds for full qualification. Git, Node and Python were already provisioned; sign-in and live generation were excluded. This measured earlier qualification revision is not a universal installation-time guarantee. See the [qualification evidence](https://github.com/kujolang/product-launch-factory/blob/d61c7021b0469c45f909b8371205f0df3afbac8b/docs/VERIFICATION.md).

## Related tools and factories

[Publishing House Factory](/ecosystem/publishing-house-factory/), [WebOps Factory](/ecosystem/webops-factory/) and [VideoOps Factory](/ecosystem/videoops-factory/) execute domain work at pinned revisions. [Software Factory](/ecosystem/software-factory/) supplies an export-verification boundary at a later pinned source revision than its standalone 0.1.0 release, not an application-building stage. Exact-version handoffs connect these separate systems.

## Get started

[Read the setup guide](https://github.com/kujolang/product-launch-factory/blob/d61c7021b0469c45f909b8371205f0df3afbac8b/docs/AGENT-SETUP.md), [inspect the source](https://github.com/kujolang/product-launch-factory/tree/d61c7021b0469c45f909b8371205f0df3afbac8b) or [compare all five factories](/ecosystem/factories/). Kujo remains the programming language and runtime beneath this wider set of tools; [start with the language](/language/) if you want to write your own programs.
