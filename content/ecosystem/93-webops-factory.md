---
title: "WebOps Factory"
custom_url: "webops-factory"
description: "Inspect a static site and review a bounded repair candidate."
featured_image: "/assets/images/ecosystem/webops-factory.webp"
social_image: "/assets/images/social/webops-factory.jpg"
section: "Factories"
template: factory
order: 930
install_command: "git clone https://github.com/kujolang/webops-factory.git\ncd webops-factory\ngit checkout a2aba2c63777f37bf47d64dc93748949658b977b"
github_url: "https://github.com/kujolang/webops-factory"
launch_story: "Site maintainers with a static export who want to inspect a patch before applying it themselves."
scope_note: "Local software. Inspect the setup guide and review boundaries before authorizing live model calls."
last_updated: "2026-11-13"
seo_title: "WebOps Factory \u2014 Kujo Factories"
release_status: "Source preview; no published GitHub Release"
version: "Source preview"
---

## What you give it

A JSON mission such as `examples/studio.json`, pointing to a static export directory. Supported files include HTML, CSS, SVG, common images, text and XML. Intake is limited to 120 files and 8 MB; worker context is limited to 150 KB. Scripts, event handlers, frames, active embeds and symlinks are rejected.

## What happens

1. The controller copies admitted source files and runs SiteProbe and Lens. The original directory is preserved.
2. Metadata Auditor proposes missing or empty titles and descriptions. Accessibility Auditor supplies missing image alt attributes. Link Health Auditor proposes existing local targets for broken file links.
3. Trusted code accepts values for known findings and applies only the four supported operations. Agents cannot introduce commands, arbitrary HTML or new operations.
4. The controller repeats the crawl and browser checks. An independent model reviewer examines the exact patch. Failed checks or requested revisions leave the run blocked.

## What you receive

`before/` and `candidate/` directories, before/after findings JSON, retained specialist and review responses, `patches/repairs.diff`, SiteProbe and Lens artifacts under `evidence/`, and a `package.json` binding the candidate and evidence to file hashes.

## Factory Floor and demonstration

Recorded live repair demonstration with separately produced narration. The actual floor shows retained proposals, screenshots and checks. Run npm run demo to import the recorded evidence; it is not a new mission.

FACTORY_MEDIA

## Accountability and verification

The static audit examines every imported HTML page; SiteProbe adds bounded crawl evidence. Lens captures the homepage at desktop and mobile sizes. The independent review is a model judgment; a human still reviews the patch and candidate. Fixture mode uses fixed proposals with real crawl/browser checks and remains labeled. Live mode makes provider calls.

## Installation and first run

macOS or Linux, Git, Python 3.10+, Node 26.12.1 or later 26.x and a Codex account for live workers. Setup installs pinned sources, Kujo and Chromium. Linux may need Playwright system libraries; use the setup guide. Native Windows is unsupported; use a compatible WSL environment.

Read the [authoritative setup guide](https://github.com/kujolang/webops-factory/blob/a2aba2c63777f37bf47d64dc93748949658b977b/docs/AGENT-SETUP.md). The hero command checks out the revision described here. Install its dependencies and pinned tools:

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

Start the loopback Factory Floor with `npm start`, then open `http://127.0.0.1:4383`. In another terminal, an authorized live run uses:

```sh
npm run factory -- run examples/studio.json --live
```

For a read-only recorded example, use `npm run demo` then `npm start`. This imports evidence without making model calls.

Use `--fixture` instead of `--live` for fixed proposals with real checks. Verify a retained package with `npm run factory -- verify RUN_ID`.

## Release status and limitations

Source preview: no published GitHub Release was present when checked on 2026-11-13. The package version 0.1.0 is not a release record. This page uses commit [`a2aba2c63777`](https://github.com/kujolang/webops-factory/tree/a2aba2c63777f37bf47d64dc93748949658b977b).

Only missing or empty titles and descriptions, missing image alt attributes and broken internal file links are repairable. This is not general website repair or full accessibility compliance. Fragment-only links, external link health, rankings and analytics are outside scope. No automatic retry/resume, original-site mutation or deployment is implemented.

## Related tools and factories

[SiteProbe](/ecosystem/siteprobe/) inspects static content; [Lens](/ecosystem/lens/) provides browser evidence. Pinned WebOps role contracts guide proposals. The finding-to-fix workflow informs the contract, but its production-mutation step is not invoked. [Product Launch Factory](/ecosystem/product-launch-factory/) coordinates this bounded website stage.

## Get started

[Read the setup guide](https://github.com/kujolang/webops-factory/blob/a2aba2c63777f37bf47d64dc93748949658b977b/docs/AGENT-SETUP.md), [inspect the source](https://github.com/kujolang/webops-factory/tree/a2aba2c63777f37bf47d64dc93748949658b977b) or [compare all five factories](/ecosystem/factories/). Kujo remains the programming language and runtime beneath this wider set of tools; [start with the language](/language/) if you want to write your own programs.
