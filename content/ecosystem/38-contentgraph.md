---
title: "ContentGraph"
custom_url: contentgraph
description: "A deterministic, inspectable network of website content, internal links, topic clusters, overlaps, orphan candidates, and link opportunities."
featured_image: "/assets/images/ecosystem/contentgraph-content-network.webp"
section: "Tooling"
tags: [Tool, Content Intelligence]
order: 340
install_command: "git clone https://github.com/kujolang/contentgraph.git"
github_url: "https://github.com/kujolang/contentgraph"
launch_story: "Turn crawls and source files into a local content graph that exposes relationships without automating editorial decisions."
scope_note: "ContentGraph 0.1 uses deterministic lexical relationships; overlaps and opportunities are review candidates, not proof or authorization to change content."
keywords: "ContentGraph, Kujo ecosystem, content graph, internal links, topic clusters, content intelligence"
seo_title: "ContentGraph — Kujo Ecosystem"
version: "0.3.0"
latest_release_url: "https://github.com/kujolang/contentgraph/releases/tag/v0.3.0"
release_status: "Version identifies the latest published GitHub Release. Unpinned clone commands select default-branch source; see scope_note for release boundaries."
last_updated: "2026-09-09"
---

## What it does

ContentGraph builds a versioned network from SiteProbe runs, Markdown, HTML, JSON, text, and optional SearchBridge evidence. It writes inspectable nodes, edges, clusters, overlaps, orphan candidates, link opportunities, metadata, and reports with stable identifiers and explicit relationship methods.

## Deterministic content relationships

The graph uses deterministic TF-IDF and cosine relationships alongside existing internal links. Operators can inspect a node, find related content, review weakly connected pages, explore clusters, compare graph revisions, and export JSON or GraphML without handing the corpus to a hosted service.

## Why it belongs in Kujo

ContentGraph connects Kujo WebOps evidence into a reviewable content model. Bounded inputs, explicit artifact and report budgets, immutable sources, byte-comparable fixture runs, and offline operation keep the analysis reproducible and operator-controlled.

## Operating boundary

Topic labels are representative terms rather than a human taxonomy. Similarity does not establish search intent, cannibalization, editorial quality, or a mandate to publish. ContentGraph has no network, publish, submit, or effecting command.

## Learn more

The repository documents the graph contract, methodology, agent integration, security boundaries, release qualification, fixtures, and verification commands for version 0.1.0.
