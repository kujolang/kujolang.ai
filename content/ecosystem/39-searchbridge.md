---
title: "SearchBridge"
custom_url: searchbridge
description: "A normalized external-data layer for search, analytics, page performance, field data, backlinks, keyword evidence, and explicit index submission."
featured_image: "/assets/images/ecosystem/searchbridge-provider-relay.webp"
section: "Tooling"
tags: [Tool, WebOps Data]
order: 350
install_command: "git clone https://github.com/kujolang/searchbridge.git"
github_url: "https://github.com/kujolang/searchbridge"
launch_story: "Bring optional provider measurements into Kujo WebOps through scoped capabilities, normalized evidence, and explicit effect boundaries."
scope_note: "SearchBridge 1.0.0 is a released local CLI and SDK with live-qualified Google search, analytics, PageSpeed, and CrUX reads; Cloudflare and IndexNow remain fixture-only pending the v1.1 review."
version: "1.0.0"
last_updated: "2026-09-04"
keywords: "SearchBridge, Kujo ecosystem, search data, analytics, PageSpeed, CrUX, backlinks, IndexNow"
seo_title: "SearchBridge — Kujo Ecosystem"
---

## What it does

SearchBridge 1.0.0 fetches and normalizes evidence from Google Search Console, Bing Webmaster, Google Analytics 4, PageSpeed Insights, CrUX, Cloudflare, Ahrefs, IndexNow, and other bounded provider contracts. Every result records its provider, capability, retrieval mode, timing, provenance, and normalized rows in a versioned schema without interpreting SEO performance.

## Capability-scoped providers

Credentials become narrow capabilities instead of a single all-or-nothing integration. Missing analytics access does not block PageSpeed or fixture work, scheduled runs can skip unavailable capabilities, and live requests have bounded timeouts, retries, rows, bytes, and report tokens. Credentials are accepted at runtime and are never written to artifacts.

The `stable-live` v1.0 tier—Google Search Console, Google Analytics 4, PageSpeed Insights, and Chrome UX Report—passed an owner-authorized 16-case live matrix before release. Cloudflare, IndexNow, Bing Webmaster, Ahrefs, DataForSEO, and SerpApi remain `fixture-only`; Plausible is an external signed-adapter reference and Semrush is disabled. The three-run weekly history, Cloudflare dataset proof, and controlled IndexNow exercise are explicitly deferred to v1.1.

## Why it belongs in Kujo

SearchBridge gives agents comparable, provenance-rich WebOps measurements while preserving the operator's control over cost-bearing and effecting actions. Deterministic fixtures keep offline work testable, and provider failures stay isolated at the capability level.

## Operating boundary

Evidence commands are read-only with respect to providers. Submission is separate and requires the exact capability, `--act`, `--yes`, and provider authorization on every invocation; a submission receipt never claims that a URL was indexed.

## Learn more

Download the checksum-verified [SearchBridge 1.0.0 release](https://github.com/kujolang/searchbridge/releases/tag/v1.0.0), review its [support matrix](https://github.com/kujolang/searchbridge/blob/v1.0.0/docs/support-matrix.md), or browse the [source repository](https://github.com/kujolang/searchbridge).
