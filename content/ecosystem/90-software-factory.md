---
title: "Software Factory"
custom_url: "software-factory"
description: "Turn a software brief or GitHub issue into a tested local candidate with evidence your team can verify offline."
featured_image: "/assets/images/ecosystem/software-factory.webp"
social_image: "/assets/images/social/software-factory.jpg"
section: "Factories"
template: factory
order: 900
install_command: "git clone --branch 0.2.0 https://github.com/kujolang/software-factory.git && cd software-factory && npm ci && npm run setup"
github_url: "https://github.com/kujolang/software-factory"
launch_story: "Give a team of agents a brief, review what they built, and see exactly which checks passed before sharing a candidate."
scope_note: "Run locally with a configured provider and rootless Workcell for live checks. Release evidence supports a human delivery decision."
last_updated: "2026-11-20"
seo_title: "Software Factory — Kujo Factories"
release_status: "Published 0.2.0"
version: "0.2.0"
latest_release_url: "https://github.com/kujolang/software-factory/releases/tag/0.2.0"
tags: ["agents", "software", "testing", "workcell", "verification", "releases"]
---

## Inputs and what you get

Start with a brief, reviewed specification, committed repository, or GitHub issue. Software Factory takes a supported mission through planning, implementation, and independent checks. You get a local candidate for review, a record of failed and passing attempts, and an evidence bundle another operator can verify offline.

## Workflows and outputs

- **Settle requirements before writing code.** Freeze a reviewed Spec and map requirements to acceptance checks. Pick from all 28 Chain of Command roles and 136 pinned skills. The mission activates relevant roles and skills.
- **Build or repair software locally.** Construct Node APIs and static interfaces, use a locked React 18 static profile, or build a CLI with a qualified Python, TypeScript, Go, Rust, or Kujo profile. Other routes cover repository repair, dependency upgrades, disposable SQLite migrations, and documentation review.
- **See what actually passed.** Dispatch coordinates work and rootless Workcell runs trusted checks separately from implementation proposals. Native Eval, Lens, and ShipCheck contribute evaluation, browser evidence, and release-policy checks. RunLedger tracks observed usage, and Casefile preserves failures.
- **Hand off evidence someone else can check.** Compare the proposed files and test results in the Factory Floor, inspect status through local MCP, and verify an export independently of the original running factory.

## Factory Floor and demonstration

Follow a recorded software team as it scopes an application, builds a candidate, and reviews the result. The current Factory Floor exposes mission status, agent and tool observations, failed gates, and source-bound evidence.

FACTORY_MEDIA

## Installation and first run

Use Git and Node 26.12.1 or later 26.x. Live checks need a local rootless Docker engine with seccomp. Model-backed work uses a separately configured provider.

```sh
git clone --branch 0.2.0 https://github.com/kujolang/software-factory.git
cd software-factory
npm ci
npm run setup
npm run doctor -- --offline
```

Follow the [setup guide](https://github.com/kujolang/software-factory/blob/0.2.0/docs/AGENT-SETUP.md) to configure the engine and provider. Start with the bundled converter or notes contract. Open the loopback Factory Floor with `npm start`, or connect a compatible local MCP host using `node bin/software-factory.mjs mcp`.

## Release verification and delivery limits

Independent approval binds the local candidate to the tested source. Pull request publication, merge, deployment, and production migrations require separate authorization. The 0.2.0 profiles cover documented project shapes, and provider support depends on the qualified path. See the [release notes](https://github.com/kujolang/software-factory/releases/tag/0.2.0), [evidence guide](https://github.com/kujolang/software-factory/blob/0.2.0/docs/EVIDENCE.md), the [hardening audit](https://github.com/kujolang/software-factory/blob/08f261ea9d6f48182dd929b4e27fa902534a0aaa/docs/audits/repository-hardening.md), and [known limitations](https://github.com/kujolang/software-factory/blob/0.2.0/docs/KNOWN-LIMITATIONS.md).

## Related tools and factories

[Dispatch](/ecosystem/dispatch/) coordinates bounded work. [Workcell](/ecosystem/workcell/) isolates candidate execution. [Product Launch Factory](/ecosystem/product-launch-factory/) can consume verified Software Factory exports through its separately pinned verifier. [Compare the five factories](/ecosystem/factories/) to choose the right starting point.
