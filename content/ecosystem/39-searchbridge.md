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
scope_note: "SearchBridge 0.1 fixture-verifies normalization and bounded adapters; live correctness, quotas, credentials, and provider authorization remain external."
keywords: "SearchBridge, Kujo ecosystem, search data, analytics, PageSpeed, CrUX, backlinks, IndexNow"
seo_title: "SearchBridge — Kujo Ecosystem"
---

## What it does

SearchBridge normalizes evidence from Google Search Console, Bing Webmaster, Google Analytics 4, PageSpeed Insights, CrUX, Ahrefs, IndexNow, and Bing submission contracts. Every result records its provider, capability, retrieval mode, target, timing, and normalized rows in a versioned schema.

## Capability-scoped providers

Credentials become narrow capabilities instead of a single all-or-nothing integration. Missing analytics access does not block PageSpeed or fixture work, scheduled runs can skip unavailable capabilities, and live requests have bounded timeouts, retries, rows, bytes, and report tokens. Credentials are accepted at runtime and are never written to artifacts.

## Why it belongs in Kujo

SearchBridge gives agents comparable, provenance-rich WebOps measurements while preserving the operator's control over cost-bearing and effecting actions. Deterministic fixtures keep offline work testable, and provider failures stay isolated at the capability level.

## Operating boundary

Evidence commands are read-only with respect to providers. Submission is separate and requires the exact capability, `--act`, `--yes`, and provider authorization on every invocation; a submission receipt never claims that a URL was indexed.

## Learn more

The repository documents provider contracts, authentication, security, normalized outputs, fixture coverage, release qualification, and verification commands for version 0.1.0.
