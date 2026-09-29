---
title: "SSG"
custom_url: ssg
description: "Deterministic static publishing for Markdown, templates, taxonomies, metadata, feeds, sitemaps, robots, llms.txt, and starter content."
featured_image: "/assets/images/ecosystem/ssg-static-sites.webp"
section: "Showcase"
tags: [Showcase, Publishing]
order: 430
install_command: "kennel add ssg"
github_url: "https://github.com/kujolang/ssg"
launch_story: "An agent-inspectable publishing pipeline where content and generated output remain visible."
scope_note: "SSG 1.1.0 enables experimental, public read-only WebMCP by default and includes ten local Ability workflows. The independently versioned Ability pack is 1.0.0; builds require approval and keyed idempotency. No hosted deployment service or deploy Ability is included."
keywords: "SSG, Kujo ecosystem, Showcase, Publishing"
seo_title: "SSG — Kujo Ecosystem"
version: "1.1.0"
latest_release_url: "https://github.com/kujolang/ssg/releases/tag/v1.1.0"
release_status: "Version identifies the published release. The Kennel command selects the latest stable registry package; see scope_note for release boundaries."
last_updated: "2026-09-29"
---

## What it does

Deterministic static publishing for Markdown, templates, taxonomies, metadata, feeds, sitemaps, robots, llms.txt, and starter content.

## Why it belongs in Kujo

An agent-inspectable publishing pipeline where content and generated output remain visible.

## Operating boundary

SSG is a generator and showcase, not a hosted deployment service or a guarantee of SEO and accessibility outcomes.

## Release 1.1.0

The September 29, 2026 release adds experimental WebMCP, an executable local Ability pack, and fixes for output cleanup, dates, metadata escaping, numeric ordering, post indexes, image size, and plain sitemap XML.

### Public browser tools

WebMCP is enabled by default. It emits `.well-known/kujo-site-index.json` and a same-origin browser adapter with four read-only tools: `get_site_info`, `search_site`, `list_content`, and `get_content`. Unsupported browsers retain the normal site. Set `webmcp: false` or pass `--no-webmcp` to opt out.

Drafts never enter the public agent index, even with `--drafts`. `search_exclude` hides a public record from search, not exact retrieval; it is not an access-control setting.

### Ability integration

SSG ships ten executable local Ability workflows for inspection, source validation, full and sharded builds (including approved draft previews), output validation and inspection, comparison, deployment readiness, and deterministic artifact export. The independent pack version is 1.0.0 with a commit-pinned Ability 1.0.1 dependency.

Writes require explicit approval and keyed idempotency. MCP and agent hosts bind the pack inside a trusted local process or authenticated application gateway. Generated static pages receive no execution authority. Publication requires a separate provider-owned deployment pack; SSG includes no publish or deploy Ability.

[See how Ability separates portable operation meaning from execution authority](/ecosystem/ability/).

## Learn more

The repository is the source of truth for current setup, commands, examples, security notes, compatibility, and verification evidence.
