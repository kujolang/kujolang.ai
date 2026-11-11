---
title: "Source"
custom_url: source
description: "Connect Git changes to tasks, agent sessions, evidence and authorized review decisions. Run Source locally or promote accepted changes to Cloudflare Artifacts."
featured_image: "/assets/images/ecosystem/source-review-evidence-vault.webp"
section: "Primitives"
tags: [Foundation, Git, Collaboration, Agents]
order: 30
install_command: "git clone --branch v0.2.0 https://github.com/kujolang/source.git"
github_url: "https://github.com/kujolang/source"
launch_story: "Make the path from an agent's proposal to accepted code explicit and inspectable."
scope_note: "Source 0.2.0 is an experimental self-hosted Node.js application. Use Git and npm, not kennel add. Local demos use scripted contributors. The Cloudflare profile runs review locally and canonical Git on Artifacts. Exposed deployments require the documented storage, TLS and writer controls."
keywords: "Source, Kujo, Git review, agent collaboration, evidence, Cloudflare Artifacts"
seo_title: "Source — Git Review for Agent Contributions"
version: "0.2.0"
latest_release_url: "https://github.com/kujolang/source/releases/tag/v0.2.0"
release_status: "Published MIT feature release. Experimental 0.x software; publication does not certify production readiness."
last_updated: "2026-11-10"
---

## What it does

Source connects a Git change to the task that requested it, the agent session that produced it, the checks that support it and the review decision that accepts it. Its server, browser UI, CLI and HTTP API share the same workflow:

```text
Work → Session → Change → Evidence → Decision → Canonical Git
```

Contributors receive scoped permissions to propose changes and submit evidence. An authorized reviewer decides what can enter the accepted history. Source rejects stale promotion attempts and preserves the record of revisions and conflicts.

## Try Source 0.2.0

Install Node.js 22.23.4+, 24.22.1+, or 26.12.1+ on supported branches, npm and Git, then run:

```bash
git clone --branch v0.2.0 https://github.com/kujolang/source.git
cd source
npm ci
npm run demo:contest -- --trace
```

The demo runs three scripted contributors through real commits, review and conflict recovery. It needs no Cloudflare account, PostgreSQL server or model API key. To inspect the result, run `npm run demo:serve -- .contest-demo/run-XXXXXX` using the printed directory. Open http://127.0.0.1:8787 and read that run's local `operator.json` for login details.

Source is installed through Git and npm. It is not a Kennel-installable Kujo package.

## Integration and recovery in 0.2.0

Source can assemble compatible concurrent proposals into a Git candidate, schedule verification on separate PostgreSQL workers, and promote only the exact candidate covered by current evidence and authorized acceptance. Verification identities include the relevant policy, tools, environment and inputs; reuse is conditional on those identities remaining valid.

Keep GitHub as `origin` and use Source as a secondary remote. `source sync` copies local branches and tags atomically without force or deletion. `source submit` selects the Source remote and submits committed work for review. On PostgreSQL, an authenticated `--submission-key` and read-only `--recover` let contributors retrieve a committed result after a lost response without creating another contribution.

See the [secondary-remote setup](https://github.com/kujolang/source/blob/v0.2.0/README.md#keep-github-as-origin) and [submission recovery contract](https://github.com/kujolang/source/blob/v0.2.0/docs/source/18-source-submit.md). Initial sync copies Git refs; it does not create review evidence or replace protected promotion.

## Cloudflare integration

An authenticated Worker creates Artifacts repositories and issues short-lived credentials. Source promotes an accepted change only when the remote branch matches its expected commit. If a push acknowledgment is lost, a retry checks the remote result before closing the work.

The [recorded live profile](https://github.com/kujolang/source/blob/v0.2.0/docs/contest/CLOUDFLARE_LIVE.md) runs Source and review data locally, with Workers and canonical Git live on Cloudflare. The separate `npm run demo:hybrid` rehearsal emulates Artifacts; it is not a live deployment test.

## Operating boundary

Version 0.2.0 is an experimental release for evaluation and integration. JSON storage is single-process. Exposed deployments require PostgreSQL, shared durable Git storage, TLS and writer controls. Synchronous PostgreSQL maintenance lacks atomic rollback across records, and a worker timeout does not guarantee cancellation of arbitrary action handlers.

Local validation includes actual Source history, isolated component tests, browser staging, worker crash recovery and coordinated restore. Those proofs do not certify deployment failover, sustained production capacity or 1,000-agent end-to-end operation.

The [hardening report](https://github.com/kujolang/source/blob/v0.2.0/docs/audits/repository-hardening.md) records fixes, tests, measured effects, upgrade guidance and remaining work. Publication is not a production-readiness certification.

## Learn more

- [Source documentation](https://docs.kujolang.ai/tools/source/)
- [Source 0.2.0 release](https://github.com/kujolang/source/releases/tag/v0.2.0)
- [Deployment and local runbook](https://github.com/kujolang/source/blob/v0.2.0/docs/contest/RUNBOOK.md)
- [Kujo Eval](/ecosystem/eval/) for evidence and [Workcell](/ecosystem/workcell/) for bounded execution.
