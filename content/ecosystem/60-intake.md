---
title: "Intake"
custom_url: intake
description: "Collect email, webhooks, files, and manual input into a local work queue with rules, approvals, and recovery."
featured_image: "/assets/images/ecosystem/showcase-application-gallery.webp"
section: "Showcase"
tags: [Showcase, Intake, Approvals]
order: 490
install_command: "git clone --branch v0.3.0 https://github.com/kujolang/intake.git"
github_url: "https://github.com/kujolang/intake"
launch_story: "Keep incoming work, original payloads, proposed actions, and operator decisions together in local files."
scope_note: "Intake 0.3.0 is a Node.js source release for local operators. Requires patched Node.js 22.23.4+, 24.22.1+, or 26.12.1+. Not published to npm or Kennel; live providers and shared deployments need their own validation."
keywords: "Kujo Intake, local work queue, email intake, webhook intake, action approvals, recovery"
seo_title: "Intake 0.3.0 — Local Intake and Action Review"
seo_description: "Collect email, webhooks, files, and manual input. Route work through rules and policy, review actions, and recover interrupted local writes."
version: "0.3.0"
latest_release_url: "https://github.com/kujolang/intake/releases/tag/v0.3.0"
release_status: "GitHub source release with inbox filtering and dashboard refinements. The npm manifest remains private; no Kennel install is advertised."
last_updated: "2026-10-22"
---

## What it does

Intake turns incoming messages and events into local work items. It supports manual input, file drops, email, webhooks, Slack, GitHub, Jira, Linear, and ClickUp. Rules route each item to a queue; policy controls which actions need approval.

The dashboard provides review queues, ownership, snooze, drafts, source health, and audit views. The CLI uses the same records and policy checks. Reviewed learnings can be exported to Strata and TotalRecall-compatible files.

## Install the release

Use patched Node.js 22.23.4+, 24.22.1+, or 26.12.1+:

```sh
git clone --branch v0.3.0 https://github.com/kujolang/intake.git
cd intake
npm ci
npm link
intake init
intake dashboard
```

Intake is implemented in JavaScript. It does not require the Kujo runtime and is not a Kennel package. The GitHub release includes a tracked-file archive and checksum; the npm manifest remains private.

## Recovery and action safety

Receiver receipts preserve classification and operator changes across retries. Store locks and journals protect interrupted restore and configuration imports. Invalid metadata remains available for inspection instead of being silently rewritten.

Direct sending is blocked by default. Review uncertain outbound effects before retrying; store recovery never replays them. Keep secrets in environment variables or Keychain, and stop writers before maintenance.

## Operating limits

This release supports local operation and adapter development. It does not establish enterprise readiness, exactly-once provider delivery, or machine-power-loss durability. Validate live providers and deployment access controls for your environment.

## Learn more

- [Intake 0.3.0 release](https://github.com/kujolang/intake/releases/tag/v0.3.0)
- [Release and upgrade notes](https://github.com/kujolang/intake/blob/v0.3.0/docs/releases/0.3.0.md)
- [Intake documentation](https://docs.kujolang.ai/showcases/intake/)
- [Source and README](https://github.com/kujolang/intake)
