---
title: "Commerce"
custom_url: "commerce"
description: "Commerce for static and dynamic sites: hosted checkout, verified webhooks, optional PostgreSQL processing, and Square payment and recovery tools."
featured_image: "/assets/images/ecosystem/workflows-evidence-routing-bench.webp"
social_image: "/assets/images/social/commerce.jpg"
section: "Tooling"
tags: ["Tools","commerce"]
order: 560
install_command: "npm install https://github.com/kujolang/commerce/releases/download/v0.5.0/kujolang-commerce-0.5.0.tgz"
github_url: "https://github.com/kujolang/commerce"
launch_story: "Commerce for static and dynamic sites: hosted checkout, verified webhooks, optional PostgreSQL processing, and Square payment and recovery tools."
scope_note: "Pre-1.0 package with frozen v1 wire contracts. Static hosted links need no server. Durable processing needs operator-managed storage and workers. Advanced Square features require their own acceptance checks; npm registry publication is pending."
version: "0.5.0"
latest_release_url: "https://github.com/kujolang/commerce/releases/tag/v0.5.0"
release_status: "GitHub Release 0.5.0 is published with a package tarball, SBOM and build provenance. The install command uses that tarball while npm still serves 0.4.0."
last_updated: "2026-10-10"
keywords: "Commerce, Kujo, Square, Stripe, checkout, PostgreSQL, webhooks, refunds, reconciliation"
seo_title: "Commerce — Kujo Ecosystem"
seo_description: "Commerce for static and dynamic sites: hosted checkout, verified webhooks, optional PostgreSQL processing, and Square payment and recovery tools."
---

## What it does

Start with product catalogs and ordinary hosted purchase links. Add a browser cart, provider-hosted checkout, customer portals, and verified webhooks when your store needs them. Commerce works with Kujo SSG and other static or dynamic sites.

## New in 0.5.0

- **Durable processing:** an optional PostgreSQL adapter adds webhook receipts, worker leases, retries, dead letters, replay, and signed downstream events.
- **Square payments:** scoped orders, direct payments, partial/full refunds, delayed capture, cancellation, and reconciliation for uncertain outcomes.
- **Embedded checkout:** Square SDK card entry with transient tokens, server-controlled prices, duplicate-submit protection, and explicit checkout restarts.
- **Cards and billing:** separate stored-card and recurring consent, supported monthly subscriptions, and approved invoice workflows.
- **Merchant connections:** encrypted Square OAuth tokens, serialized refresh, location selection, and revocation handling.
- **Optional integrations:** application fees, catalog/inventory tools, Terminal, and dispute/payout reporting remain off by default.

## Getting started

Use the install command above to install the published 0.5.0 GitHub tarball. npm registry publication is pending; `npm install @kujolang/commerce` still selects 0.4.0 as checked on October 10, 2026.

Run `npx kujo-commerce init --site .` to start in Static Mode, then validate and build the catalog. Choose `init --mode hybrid` for dynamic checkout. Browser requests carry SKU and quantity; the runtime resolves trusted pricing and provider identifiers. Node.js 20 or later is required.

## Upgrading and operating

Static and hosted-link configurations need no changes. Runtime and custom-adapter users should read the [0.5 migration guide](https://github.com/kujolang/commerce/blob/v0.5.0/docs/migration-0.5.md) and preserve existing provider operation keys and v1 records.

The maintainer has confirmed working Square and Stripe integrations. Advanced modules still need checks for the features and deployment being enabled; this release does not certify every provider or lifecycle path. Your deployment supplies authentication, durable storage, workers, monitoring, and fulfillment policy. Fulfill orders from verified payment evidence, not a browser redirect.

## Reference

Read the [usage guide](https://docs.kujolang.ai/tools/commerce/), [published release](https://github.com/kujolang/commerce/releases/tag/v0.5.0), and [feature acceptance status](https://github.com/kujolang/commerce/blob/v0.5.0/docs/square-implementation-status.md).
