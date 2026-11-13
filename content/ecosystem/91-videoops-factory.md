---
title: "VideoOps Factory"
custom_url: "videoops-factory"
description: "Turn a sourced brief into an editable video candidate."
featured_image: "/assets/images/ecosystem/videoops-factory.webp"
social_image: "/assets/images/social/videoops-factory.jpg"
section: "Factories"
template: factory
order: 910
install_command: "git clone https://github.com/kujolang/videoops-factory.git\ncd videoops-factory\ngit checkout dcf2dc4fa7311f59ba3dd16f58a227439a155979"
github_url: "https://github.com/kujolang/videoops-factory"
launch_story: "Developers and creative operators making bounded, screenshot-led launch clips."
scope_note: "Local software. Inspect the setup guide and review boundaries before authorizing live model calls."
last_updated: "2026-11-13"
seo_title: "VideoOps Factory \u2014 Kujo Factories"
release_status: "Source preview; no published GitHub Release"
version: "Source preview"
---

## What you give it

`examples/launch-brief.json` or `examples/social-brief.json`, sourced campaign text and registered local media with provenance, reuse rights and file hashes. The supplied examples use Software Factory screenshots to create silent 12-second landscape and portrait clips.

## What happens

1. The Producer checks the production contract; the Creative Director proposes a timed scene plan.
2. Asset Scout checks provenance and fit. Trusted code verifies registered file hashes.
3. Media Generator records that generation is unnecessary for the silent registered-asset route; it makes no provider call.
4. HyperFrames Editor reviews the plan. A trusted compiler writes the editable composition, and HyperFrames checks and renders it.
5. Video Critic reviews technical evidence. The review ledger keeps missing playback review visible.

## What you receive

`output/draft.mp4`, render metadata, extracted frames, check logs, role proposals, handoffs and elapsed-time evidence. The editable `production/hyperframes/` project can be reopened with HyperFrames preview or Studio. Landscape and portrait outputs are supported.

## Factory Floor and demonstration

Recorded narrated walkthrough, technically checked but still a review candidate. The runner’s included examples are silent. The screenshot below is a frame from the retained recording, not a fresh execution.

FACTORY_MEDIA

## Accountability and verification

Sequential tool-free model proposals cannot edit the renderer or execute brief instructions. A successful render ends at `REVIEW_INCOMPLETE`. Human approval remains separate from model review. A capable reviewer must watch and listen to the entire exact candidate, including intentional silence, before promotion; metadata checks and model review do not establish creative approval. Editing creates a new candidate requiring new review. Rendering and media processing run as trusted host operations; this factory does not inherit Software Factory’s Workcell isolation.

## Installation and first run

macOS or Linux, Git, Node 26.12.1 or later 26.x, Python 3.10+, FFmpeg/ffprobe 6+ with libx264/AAC, and a Codex account. Rendering downloads a browser when needed. Minimal Ubuntu also needs libatomic1. Native Windows is unsupported.

Read the [authoritative setup guide](https://github.com/kujolang/videoops-factory/blob/dcf2dc4fa7311f59ba3dd16f58a227439a155979/docs/AGENT-SETUP.md). The hero command checks out the revision described here. Install its dependencies and pinned tools:

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

Start the loopback Factory Floor with `npm start`, then open `http://127.0.0.1:4381`. In another terminal, an authorized live run uses:

```sh
npm run factory -- run examples/launch-brief.json
```

## Release status and limitations

Source preview: no published GitHub Release was present when checked on 2026-11-13. The package version 0.1.0 is not a release record. This page uses commit [`dcf2dc4fa731`](https://github.com/kujolang/videoops-factory/tree/dcf2dc4fa7311f59ba3dd16f58a227439a155979).

The first contract supports monochrome screenshot-led clips, three to five scenes, a Kujo bumper, 30 fps and 3–60-second silent output. Footage timelines, other creative formats and automatic narrated campaigns require an explicit extension. The separately authorized narrated walkthrough does not make the silent runner a speech service.

## Related tools and factories

Canonical Kujo VideoOps role contracts and review services come from pinned kujo-agents and kujo-workflows sources. Trusted factory code compiles the composition; HyperFrames checks and renders it. [Software Factory](/ecosystem/software-factory/) is independent; its screenshots are example assets. [Product Launch Factory](/ecosystem/product-launch-factory/) coordinates this video stage.

## Get started

[Read the setup guide](https://github.com/kujolang/videoops-factory/blob/dcf2dc4fa7311f59ba3dd16f58a227439a155979/docs/AGENT-SETUP.md), [inspect the source](https://github.com/kujolang/videoops-factory/tree/dcf2dc4fa7311f59ba3dd16f58a227439a155979) or [compare all five factories](/ecosystem/factories/). Kujo remains the programming language and runtime beneath this wider set of tools; [start with the language](/language/) if you want to write your own programs.
