---
title: "CMS"
custom_url: cms
description: "A framework-neutral CMS backend with first-class content, administration, SEO, extensions, identity, AI abilities, MCP, and WebMCP."
featured_image: "/assets/images/ecosystem/cms-content-infrastructure.webp"
section: "Showcase"
tags: [Showcase, Content, Agents, WebMCP]
order: 400
install_command: "git clone https://github.com/kujolang/cms.git"
github_url: "https://github.com/kujolang/cms"
launch_story: "Give people, developers, integrations, and agents one inspectable content contract without prescribing the frontend stack."
scope_note: "CMS 1.1.0 is production-oriented backend software, but each deployment still requires environment-specific identity, infrastructure, storage, security, recovery, and governance proof."
version: "1.1.0"
last_updated: 2026-08-30
keywords: "Kujo CMS, open source CMS, agent-ready CMS, WebMCP CMS, MCP content management, headless CMS, theme and plugin packages"
seo_title: "Kujo CMS 1.1.0 — Agent-Ready Content Management"
seo_description: "Explore Kujo CMS 1.1.0: framework-neutral content, SEO, social sharing, themes, plugins, identities, abilities, MCP, WebMCP, APIs, and CLI workflows."
---

## What it does

Kujo CMS 1.1.0 is a framework-neutral content backend with a separate, complete
administration and frontend example. It manages content types, entries,
taxonomies, media, menus, users, sessions, permissions, SEO, social sharing,
themes, plugins, abilities, connectors, delivery APIs, and production operations.

Use the core from Next.js, Astro, PHP, a native application, a terminal harness,
or another frontend stack. The official dependency-free JavaScript and PHP
clients expose the same contracts used by the example application.

## First-class agent access

Agents do not need to imitate a person clicking through the backend. The
Abilities API publishes structured input and output schemas, required
permissions, mutation boundaries, confirmation requirements, and audit
receipts. Plugins can add abilities and connectors without creating a second
private automation system.

WebMCP is built into the CMS and enabled by default for read-only public site
information, search, published-content listings, and exact published records.
MCP-ready tool descriptors and the connector layer let traditional MCP clients
work alongside WebMCP. Drafts and mutations stay behind the CMS authorization
boundary.

## Administration without API-only compromises

The [CMS Example](https://github.com/kujolang/cms-example) turns the same core
contracts into a full frontend and administration experience. Editors can
manage content, taxonomies, users, registration, granular SEO issues, bulk SEO
updates, social networks, account attribution, themes, plugins, abilities, and
connectors from dedicated screens.

Every core operation remains available through the API, and focused terminal
helpers cover SEO, content, media, extensions, abilities, and connectors. This
keeps people and agents on the same permission and audit path.

## Portable themes and plugins

Theme and plugin packages use versioned manifests with compatibility,
distribution, settings, author, branding, and administration metadata. Guarded
ZIP installation checks size, expanded size, file count, structure, manifest
placement, and SHA-256 integrity before registering a package. Installation
does not execute uploaded package code.

The standalone [Field Notes theme](https://github.com/kujolang/cms-field-notes-theme)
and [contact form plugin](https://github.com/kujolang/cms-contact-form) are
forkable examples of the package contracts.

## Why it belongs in Kujo

CMS shows what an AI-native application looks like when agents are first-class
consumers instead of browser automation bolted on later: clear contracts,
scoped authority, human confirmation, observable actions, and equal access
through the interface, API, and terminal.

## Operating boundary

The backend includes scoped authentication, revocable sessions, role-derived
capabilities, audit logs, rate-limit support, idempotency, migrations, jobs,
webhooks, dead-letter recovery, backup and restore workflows, and a complete
release gate. A real deployment still needs its own identity adapter, rotated
secrets, trusted ingress, durable storage, monitoring, recovery objectives,
compliance review, and governance controls.

## Learn more

- [CMS 1.1.0 release](https://github.com/kujolang/cms/releases/tag/v1.1.0)
- [CMS repository](https://github.com/kujolang/cms)
- [CMS Example 1.1.0 release](https://github.com/kujolang/cms-example/releases/tag/v1.1.0)
- [Complete CMS documentation](https://docs.kujolang.ai/showcases/cms/)
