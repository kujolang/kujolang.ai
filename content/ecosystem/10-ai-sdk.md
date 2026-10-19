---
title: "AI SDK"
custom_url: ai-sdk
description: "Provider-normalized chat and embeddings contracts with presets, fixtures, retries, streaming, redaction, budgets, and telemetry hooks."
featured_image: "/assets/images/ecosystem/ai-sdk-provider-network.webp"
section: "Primitives"
tags: [Primitive, AI]
order: 90
install_command: "kennel add ai-sdk@1.2.0"
github_url: "https://github.com/kujolang/ai-sdk"
launch_story: "Call chat and embedding models through one Kujo response contract."
scope_note: "Requires Kujo 1.6.0 or newer. Strict accounting is opt-in; memory state is process-local. Incremental chunk callbacks require a runtime with http_stream_collect and are unavailable in published Kujo 1.5/1.6. Provider credentials are needed for live calls."
keywords: "AI SDK, Kujo ecosystem, Primitive, AI"
seo_title: "AI SDK — Kujo Ecosystem"
version: "1.2.0"
latest_release_url: "https://github.com/kujolang/ai-sdk/releases/tag/v1.2.0"
release_status: "Version identifies the published release. The Kennel command selects the latest stable registry package; see scope_note for release boundaries."
last_updated: "2026-10-13"
---

## What it does

AI SDK 1.2.0 gives Kujo applications one chat and embedding response contract across provider presets, custom OpenAI-compatible endpoints, and native drivers. It handles retries, timeouts, redaction, usage budgets, and offline fixtures.

This release keeps client counters across calls, charges completed usage before rejecting a budget overrun, and adds state inspection and cleanup. Optional strict accounting holds backend ownership through each request and rejects uncertain writes. Fallback options cannot bypass that guard.

## Install

Use Kujo 1.6.0 or newer and Kennel 1.1.0 or newer. Run `kennel add ai-sdk@1.2.0`, then `kennel install`. Response, driver, and model-catalog contracts remain at 1.0.0.

## Transport and state

Native downloads enforce configured response limits, and endpoint allowlists disable redirects. Existing buffered streaming remains supported. The optional `on_transport_chunk` hook needs a runtime with `http_stream_collect`; published Kujo 1.5.0 and 1.6.0 reject it before network I/O. Verified source backports are documented in the release notes.

Memory state lasts for the process lifetime or until explicit cleanup. Shared budgets across processes require a durable backend with fenced ownership. Strict accounting is optional; legacy best-effort behavior remains the default.

## Verification

The full local gate passes 185 Kujo tests on both published 1.5.0 and 1.6.0, plus HTTP, wrapper, schema, example, and benchmark checks. Offline fixtures need no secrets. Check the release notes for the separate live-provider evidence status.

## Learn more

Read the [1.2.0 release notes](https://github.com/kujolang/ai-sdk/blob/v1.2.0/docs/RELEASE_1_2_0.md), [SDK documentation](https://docs.kujolang.ai/tools/ai-sdk/), or [source repository](https://github.com/kujolang/ai-sdk).

### Runtime for incremental HTTP collection

Kujo 1.8.2 includes `http_stream_collect`, supporting the optional transport-chunk callback. Older published 1.5/1.6 runtime limitations remain historical compatibility boundaries; upgrading the runtime does not change provider credentials or application retry and streaming policy.
