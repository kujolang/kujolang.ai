---
title: "SSG"
custom_url: ssg
description: "Deterministic static publishing for Markdown, templates, taxonomies, metadata, feeds, sitemaps, robots, llms.txt, and starter content."
featured_image: "/assets/images/ecosystem/ssg-static-sites.webp"
section: "Showcase"
tags: [Showcase, Publishing]
order: 430
install_command: "git clone https://github.com/kujolang/ssg.git"
github_url: "https://github.com/kujolang/ssg"
launch_story: "An agent-inspectable publishing pipeline where content and generated output remain visible."
scope_note: "SSG is a generator and showcase, not a hosted deployment service or a guarantee of SEO and accessibility outcomes."
keywords: "SSG, Kujo ecosystem, Showcase, Publishing"
seo_title: "SSG — Kujo Ecosystem"
---

## What it does

Deterministic static publishing for Markdown, templates, taxonomies, metadata, feeds, sitemaps, robots, llms.txt, and starter content.

## Why it belongs in Kujo

An agent-inspectable publishing pipeline where content and generated output remain visible.

## Operating boundary

SSG is a generator and showcase, not a hosted deployment service or a guarantee of SEO and accessibility outcomes.

## Ability integration

SSG can expose build inspection and validation through canonical Abilities, then add file-writing, network, or publishing operations only behind explicit effects, approval, and idempotency policy. This keeps the same operation usable from Agents SDK, Codex, Cursor, VS Code, Kujo Pi, or another MCP host without making the generated static site an execution server.

Browser-facing WebMCP should remain public and read-only. Build and deploy Abilities belong in a trusted local process or authenticated application gateway.

[See how Ability separates portable operation meaning from execution authority](/ecosystem/ability/).

## Learn more

The repository is the source of truth for current setup, commands, examples, security notes, compatibility, and verification evidence.
