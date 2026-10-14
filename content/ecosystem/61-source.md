---
title: "Source"
custom_url: source
description: "Connect Git changes to tasks, agent sessions, evidence and authorized review decisions. Run Source locally or promote accepted changes to Cloudflare Artifacts."
featured_image: "/assets/images/ecosystem/source-review-evidence-vault.webp"
section: "Primitives"
tags: [Foundation, Git, Collaboration, Agents]
order: 30
install_command: "git clone --branch v0.1.0 https://github.com/kujolang/source.git"
github_url: "https://github.com/kujolang/source"
launch_story: "Make the path from an agent's proposal to accepted code explicit and inspectable."
scope_note: "Source 0.1.0 is an experimental self-hosted Node.js application. Use Git and npm, not kennel add. Local demos use scripted contributors. The Cloudflare profile runs review locally and canonical Git on Artifacts. Exposed deployments require the documented storage, TLS and writer controls."
keywords: "Source, Kujo, Git review, agent collaboration, evidence, Cloudflare Artifacts"
seo_title: "Source — Git Review for Agent Contributions | Kujo"
version: "0.1.0"
latest_release_url: "https://github.com/kujolang/source/releases/tag/v0.1.0"
release_status: "First public MIT release. Experimental 0.x software; publication does not certify production readiness."
last_updated: "2026-10-14"
---

## What it does

Source connects a Git change to the task that requested it, the agent session that produced it, the checks that support it and the review decision that accepts it. Its server, browser UI, CLI and HTTP API share the same workflow:

```text
Work → Session → Change → Evidence → Decision → Canonical Git
```

Contributors receive scoped permissions to propose changes and submit evidence. An authorized reviewer decides what can enter the accepted history. Source rejects stale promotion attempts and preserves the record of revisions and conflicts.

## Try Source 0.1.0

Install Node.js 22, npm and Git, then run:

```bash
git clone --branch v0.1.0 https://github.com/kujolang/source.git
cd source
npm ci
npm run demo:contest -- --trace
```

The demo runs three scripted contributors through real commits, review and conflict recovery. It needs no Cloudflare account, PostgreSQL server or model API key. To inspect the result, run `npm run demo:serve -- .contest-demo/run-XXXXXX` using the printed directory. Open http://127.0.0.1:8787 and read that run's local `operator.json` for login details.

Source is installed through Git and npm. It is not a Kennel-installable Kujo package.

## Cloudflare integration

An authenticated Worker creates Artifacts repositories and issues short-lived credentials. Source promotes an accepted change only when the remote branch matches its expected commit. If a push acknowledgment is lost, a retry checks the remote result before closing the work.

The [recorded live profile](https://github.com/kujolang/source/blob/v0.1.0/docs/contest/CLOUDFLARE_LIVE.md) runs Source and review data locally, with Workers and canonical Git live on Cloudflare. The separate `npm run demo:hybrid` rehearsal emulates Artifacts; it is not a live deployment test.

## Operating boundary

Version 0.1.0 is an experimental release for evaluation and integration. JSON storage is single-process. Exposed deployments require PostgreSQL, shared durable Git storage, TLS and writer controls. Synchronous PostgreSQL maintenance lacks atomic rollback across records, and a worker timeout does not guarantee cancellation of arbitrary action handlers.

The [hardening report](https://github.com/kujolang/source/blob/v0.1.0/docs/audits/repository-hardening.md) records fixes, tests, measured effects, upgrade guidance and remaining work. Publication is not a production-readiness certification.

## Learn more

- [Source documentation](https://docs.kujolang.ai/tools/source/)
- [Source 0.1.0 release](https://github.com/kujolang/source/releases/tag/v0.1.0)
- [Deployment and local runbook](https://github.com/kujolang/source/blob/v0.1.0/docs/contest/RUNBOOK.md)
- [Kujo Eval](/ecosystem/eval/) for evidence and [Workcell](/ecosystem/workcell/) for bounded execution.
