---
title: "Commerce"
custom_url: "commerce"
description: "Provider-agnostic commerce for static sites: trusted catalogs, hosted purchase links, optional checkout and verified webhooks."
featured_image: "/assets/images/ecosystem/workflows-evidence-routing-bench.webp"
social_image: "/assets/images/social/commerce.jpg"
section: "Tooling"
tags: ["Tools","commerce"]
order: 560
install_command: "npm install @kujolang/commerce@0.4.0"
github_url: "https://github.com/kujolang/commerce"
launch_story: "Provider-agnostic commerce for static sites: trusted catalogs, hosted purchase links, optional checkout and verified webhooks."
scope_note: "Pre-1.0 package with frozen v1 wire contracts. Static hosted links need no server; dynamic checkout and verified webhooks need an operator-deployed runtime. Providers own payment and inventory truth."
version: "0.4.0"
latest_release_url: "https://github.com/kujolang/commerce/releases/tag/v0.4.0"
release_status: "published GitHub Release; see scope_note for newer source work"
last_updated: "2026-09-09"
keywords: "Commerce, Kujo ecosystem, Provider-agnostic commerce for static sites: trusted catalogs, hosted purchase links, optional checkout and verified webhooks."
seo_title: "Commerce — Kujo Ecosystem"
seo_description: "Provider-agnostic commerce for static sites: trusted catalogs, hosted purchase links, optional checkout and verified webhooks."
---

## What it does

Provider-agnostic commerce for static sites: trusted catalogs, hosted purchase links, optional checkout and verified webhooks.

## Getting started

Run `npx kujo-commerce init --site .` to start in zero-runtime static mode, then validate and build the catalog. Select hybrid mode explicitly for dynamic checkout. Browser requests carry SKU and quantity; the runtime resolves trusted pricing and provider identifiers. Provider sandbox evidence remains bounded.

## Operating boundary

Pre-1.0 package with frozen v1 wire contracts. Static hosted links need no server; dynamic checkout and verified webhooks need an operator-deployed runtime. Providers own payment and inventory truth.

## Reference

Read the [usage guide](https://docs.kujolang.ai/tools/commerce/) and [published release](https://github.com/kujolang/commerce/releases/tag/v0.4.0).
