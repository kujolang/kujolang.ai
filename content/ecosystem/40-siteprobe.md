---
title: "SiteProbe"
custom_url: siteprobe
description: "Native Kujo website crawling with bounded same-origin requests, robots enforcement, signed artifacts, and deterministic comparisons."
featured_image: "/assets/images/ecosystem/siteprobe-website-crawler.webp"
section: "Tooling"
tags: [Tool, Website Intelligence]
order: 360
install_command: "git clone --branch v0.3.0 --depth 1 https://github.com/kujolang/siteprobe.git"
github_url: "https://github.com/kujolang/siteprobe"
launch_story: "Model a website as a crawlable information system and preserve the evidence needed to inspect changes over time."
scope_note: "SiteProbe 0.3.0 is a native Kujo, read-only crawler for static and server-rendered HTML; it is not a JavaScript renderer, security scanner, or search-engine emulator."
keywords: "SiteProbe, Kujo ecosystem, website crawler, website intelligence, links, redirects, metadata, structured data"
seo_title: "SiteProbe — Native Kujo Website Crawler"
last_updated: "2026-09-09"
version: "0.3.0"
latest_release_url: "https://github.com/kujolang/siteprobe/releases/tag/v0.3.0"
release_status: "published GitHub Release; see scope_note for newer source work"
---

## What it does

SiteProbe 0.3.0 is a native Kujo website crawler. It records versioned run, page, link, redirect, metadata, structured-data, sitemap, robots, finding, and report artifacts. Inspect one URL, validate and digest-verify a run, compare baselines, or read focused link and sitemap inventories without repeating the crawl.

## Bounded crawl evidence

Crawls enforce page, depth, concurrency, timeout, retry, response-byte, artifact-byte, and report budgets. Every redirect is checked against same-origin and robots policy. Isolated async workers overlap requests at the configured concurrency while preserving origin pacing and ordered evidence.

Large artifacts and compressed sitemaps use bounded streaming mechanisms. Runs publish atomically to a new directory, include SHA-256 manifests, and can be signed with HMAC-SHA-256. Existing v1 artifact schemas and CLI contracts remain compatible.

## Install and verify

The [0.3.0 release](https://github.com/kujolang/siteprobe/releases/tag/v0.3.0) provides checksummed source ZIPs qualified on Linux x64, macOS Intel/ARM64, and Windows x64. They do not bundle a runtime. Install the exact Kujo revision in `KUJO_REVISION`, then set `KUJO_BIN` to its executable; an older generic Kujo release may lack required primitives.

Follow the [installation and crawl guide](https://docs.kujolang.ai/tools/siteprobe/) for the pinned build, platform launchers, and validation commands. The [release audit](https://github.com/kujolang/siteprobe/blob/v0.3.0/docs/audits/repository-hardening.md) preserves regression checks and complete native 10,000-page fixtures at concurrency 1, 4, 8, and 16. Those are measured fixtures, not universal throughput guarantees.

## Why it belongs in Kujo

SiteProbe supplies the website evidence layer for Kujo WebOps. Scout understands source repositories and Lens verifies browser behavior; SiteProbe captures the crawlable public structure between them so later analysis can start from durable local artifacts.

## Operating boundary

SiteProbe handles static and server-rendered HTML. It is GET-only, blocks private-network targets by default, and never submits forms or publishes content to the target. It is not a JavaScript renderer, security scanner, or search-engine emulator. Near-duplicate signals use deterministic text fingerprints and metadata duplication rather than semantic judgment.

## Learn more

Read the [versioned command and artifact reference](https://github.com/kujolang/siteprobe/tree/v0.3.0), or continue to the [SiteProbe documentation](https://docs.kujolang.ai/tools/siteprobe/).
