---
title: "Software Factory"
custom_url: "software-factory"
description: "Turn a software mission into a locally verified candidate."
featured_image: "/assets/images/ecosystem/software-factory.webp"
social_image: "/assets/images/social/software-factory.jpg"
section: "Factories"
template: factory
order: 900
install_command: "git clone https://github.com/kujolang/software-factory.git\ncd software-factory"
github_url: "https://github.com/kujolang/software-factory"
launch_story: "Developers who can define a bounded Node API or static browser application and review its contract."
scope_note: "Local software. Inspect the setup guide and review boundaries before authorizing live model calls."
last_updated: "2026-11-13"
seo_title: "Software Factory \u2014 Kujo Factories"
release_status: "Published 0.1.0"
version: "0.1.0"
latest_release_url: "https://github.com/kujolang/software-factory/releases/tag/0.1.0"
---

## What you give it

A mission file such as `factory/mission.txt`, plus a reviewed and sealed software pack when changing the product. The issue tracker is the default contract; the shipped converter and notes packs show other supported API and browser behavior. Packs supply tests as data; they cannot change the sandbox.

## What happens

1. A commander interprets the mission. An architect scopes backend and frontend work.
2. Proposal workers produce allowed files concurrently through Dispatch. The controller rejects files outside their scope.
3. An independent reviewer examines the proposal. Trusted API and browser checks execute generated applications inside rootless Workcell containers. Bounded corrections retain failures.
4. A separate release review repeats checks and binds the local candidate to the source and test-harness hashes.

## What you receive

Proposed `application/` files, an approved local `build/` only after release gates pass, `run.json`, ordered `events.jsonl`, native `dispatch/` state, role handoffs and usage evidence under `artifacts/`. `node factory/export.mjs /absolute/run/directory /new/export/directory` exports a valid run for inspection.

## Factory Floor and demonstration

See a software team scope an application, build a candidate and review the result on the Factory Floor.

FACTORY_MEDIA

## Accountability and verification

Workers cannot run commands. The controller admits scoped files and keeps credentials, the Docker socket and host evidence out of candidates. Workcell restricts network, filesystem, processes, memory and runtime. Review the sealed pack and final candidate yourself: a source hash identifies bytes, not software correctness or test quality.

## Installation and first run

Git, Node 26.12.1 or later 26.x, a Codex account, and a local rootless Docker engine with seccomp. Linux/WSL2 is required for Windows users; native Windows is unsupported. Follow the [engine guide](https://github.com/kujolang/software-factory/blob/cfddc146e225229a9c15d3bf8ad2bfc01e2c8e24/docs/ENGINE.md) to configure the required rootless engine before building its image. Live isolation qualification was recorded on macOS with Colima; native Linux, ARM and WSL2 live-engine paths remain unqualified. Setup installs pinned Kujo and Codex CLIs.

Read the [authoritative setup guide](https://github.com/kujolang/software-factory/blob/cfddc146e225229a9c15d3bf8ad2bfc01e2c8e24/docs/AGENT-SETUP.md). The clone command gets the current default branch. Follow the setup guide in your checkout for current requirements. Install the dependencies and pinned tools:

```sh
npm ci
npm run setup
```

Authenticate separately with `npm run login`. Live execution uses your provider allowance and needs your authorization. Authentication reuse, where supported, copies only auth into the factory’s private ignored home, not personal tools or hooks.

Run local checks:

```sh
npm run image:build
npm run doctor
npm run verify
npm run smoke
```

Start the loopback Factory Floor with `npm start`, then open `http://127.0.0.1:4380`. In another terminal, an authorized live run uses:

```sh
npm run factory -- run factory/mission.txt
```

## Release status and limitations

Published GitHub release [0.1.0](https://github.com/kujolang/software-factory/releases/tag/0.1.0). This page uses commit [`cfddc146e225`](https://github.com/kujolang/software-factory/tree/cfddc146e225229a9c15d3bf8ad2bfc01e2c8e24).

Single operator only. No hosted multi-tenant service, public deployment or unattended crash recovery is qualified. Never execute proposed application JavaScript on the host. The 0.1.0 release does not include the later ecosystem-integration branch: do not infer shipped Eval, ShipCheck, RunLedger, Casefile, Spec or alternate-runtime integrations from that branch.

## Related tools and factories

[Dispatch](/ecosystem/dispatch/) schedules bounded work; [Workcell](/ecosystem/workcell/) isolates candidate execution. Canonical Kujo agent contracts supply roles. [Product Launch Factory](/ecosystem/product-launch-factory/) can consume verified software exports through a separately pinned, later evidence verifier; Software Factory is a separate system, not its application-building stage.

## Get started

[Read the setup guide](https://github.com/kujolang/software-factory/blob/cfddc146e225229a9c15d3bf8ad2bfc01e2c8e24/docs/AGENT-SETUP.md), [inspect the source](https://github.com/kujolang/software-factory/tree/cfddc146e225229a9c15d3bf8ad2bfc01e2c8e24) or [compare all five factories](/ecosystem/factories/). Kujo remains the programming language and runtime beneath this wider set of tools; [start with the language](/language/) if you want to write your own programs.
