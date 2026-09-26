---
title: "Kujo Pi"
custom_url: "kujo-pi"
description: "An opt-in Pi integration for Kujo repository intelligence, checks, workflows, retrieval, approvals and receipts."
featured_image: "/assets/images/ecosystem/workflows-evidence-routing-bench.webp"
social_image: "/assets/images/social/kujo-pi.jpg"
section: "Tooling"
tags: ["Tools","kujo-pi"]
order: 570
install_command: "pi install npm:@kujolang/kujo-pi@1.1.0"
github_url: "https://github.com/kujolang/kujo-pi"
launch_story: "An opt-in Pi integration for Kujo repository intelligence, checks, workflows, retrieval, approvals and receipts."
scope_note: "Version 1.1.0 includes approval-gated Ability tools, opt-in Watchdog v2 metadata, bounded telemetry queues, and hardened operation receipts. Requires the Pi host and a separate Kujo runtime; private services and execution remain explicitly configured and permission-gated."
version: "1.1.0"
latest_release_url: "https://github.com/kujolang/kujo-pi/releases/tag/v1.1.0"
release_status: "Version identifies the latest published GitHub Release. Unpinned clone commands select default-branch source; see scope_note for release boundaries."
last_updated: "2026-09-26"
keywords: "Kujo Pi, Kujo ecosystem, An opt-in Pi integration for Kujo repository intelligence, checks, workflows, retrieval, approvals and receipts."
seo_title: "Kujo Pi — Kujo Ecosystem"
seo_description: "An opt-in Pi integration for Kujo repository intelligence, checks, workflows, retrieval, approvals and receipts."
---

## What it does

An opt-in Pi integration for Kujo repository intelligence, checks, workflows, retrieval, approvals and receipts.

## Getting started

Start Pi in a trusted repository and run `/kujo setup`, then enable only the task pack you need. Configure `KUJO_BIN` or put Kujo on PATH. The integration does not install Kujo or start service daemons during startup. Install the pinned npm package above for the released 1.1.0 contract. Run `kujo_doctor` to inspect configuration, integration availability, and telemetry health.

## What is new in 1.1.0

- Discover authorized application Abilities and invoke them through Pi approval and the gateway's independent authorization controls.
- Send metadata-only lifecycle batches to Watchdog v2 when explicitly enabled in a trusted project.
- Keep telemetry queues and artifact inspection bounded; preserve successful operation outcomes when optional receipt storage fails.
- Recover owned crash-orphan temporary files while preserving live writers, and surface deferred cleanup or telemetry loss in Doctor.

## Operating boundary

Version 1.1.0 includes approval-gated Ability tools, opt-in Watchdog v2 metadata, bounded telemetry queues, and hardened operation receipts. Requires the Pi host and a separate Kujo runtime; private services and execution remain explicitly configured and permission-gated.

## Reference

Read the [usage guide](https://github.com/kujolang/kujo-pi/blob/v1.1.0/docs/pi-onboarding.md) and [published release](https://github.com/kujolang/kujo-pi/releases/tag/v1.1.0).

See the [Kujo Pi documentation](https://docs.kujolang.ai/tools/kujo-pi/) for setup, telemetry limits, and compatibility.
