---
title: "SiteProbe"
custom_url: siteprobe
description: "A deterministic, bounded website crawler for pages, links, redirects, metadata, structured data, sitemaps, robots evidence, and comparable runs."
featured_image: "/assets/images/ecosystem/siteprobe-website-crawler.webp"
section: "Tooling"
tags: [Tool, Website Intelligence]
order: 360
install_command: "git clone https://github.com/kujolang/siteprobe.git"
github_url: "https://github.com/kujolang/siteprobe"
launch_story: "Model a website as a crawlable information system and preserve the evidence needed to inspect changes over time."
scope_note: "SiteProbe 0.1 is a read-only crawler for static and server-rendered HTML; it is not a JavaScript renderer, security scanner, or search-engine emulator."
keywords: "SiteProbe, Kujo ecosystem, website crawler, website intelligence, links, redirects, metadata, structured data"
seo_title: "SiteProbe — Kujo Ecosystem"
---

## What it does

SiteProbe crawls a bounded same-origin surface and records versioned run, page, link, redirect, metadata, structured-data, sitemap, robots, finding, and human-report artifacts. It can inspect a single URL, validate a run, compare two runs, and expose focused link or sitemap inventories.

## Bounded crawl evidence

Crawls enforce page, depth, concurrency, timeout, retry, response-byte, artifact-byte, and report-token budgets. Same-origin redirects and robots rules are checked by default, deterministic mode produces comparable fixture reruns, and offline commands fail closed where a live crawl would be required.

## Why it belongs in Kujo

SiteProbe supplies the website evidence layer for Kujo WebOps. Scout understands source repositories and Lens verifies browser behavior; SiteProbe captures the crawlable public structure between them so later analysis can start from durable local artifacts.

## Operating boundary

Version 0.1 focuses on static and server-rendered HTML. Near-duplicate signals use deterministic text fingerprints and metadata duplication rather than semantic judgment. SiteProbe never submits forms, publishes content, or performs effecting actions against the target.

## Learn more

The repository documents artifact schemas, security boundaries, agent integration, release dogfood, deterministic fixtures, and verification commands for version 0.1.0.
