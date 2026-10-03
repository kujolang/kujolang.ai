---
title: "Presentations"
custom_url: presentations
description: "Browser-native slide decks with static routes, reading and print editions, presenter tools, and optional motion."
featured_image: "/assets/images/ecosystem/presentations-browser-native-decks.webp"
section: "Showcase"
tags: [Showcase, Publishing, Presentations]
order: 470
install_command: "git clone https://github.com/kujolang/presentations.git"
github_url: "https://github.com/kujolang/presentations"
launch_story: "Turn structured deck source into static slide URLs, an overview, a reading edition, print output, and presenter tools without locking content inside a presentation app."
scope_note: "Presentations 0.3.0 is a source-distributed preview. Native authoring and builds are verified on macOS and Linux, not Windows; hosting, access control, factual review, and human accessibility and language review remain deployment responsibilities."
keywords: "Kujo Presentations, browser-native slide decks, static presentation site, presentation generator, presenter console, accessible reading edition"
seo_title: "Kujo Presentations 0.3.0 — Browser-Native Slide Decks"
seo_description: "Build browser-native slide decks with Kujo: static slide routes, overview and reading pages, print and PDF output, presenter tools, local themes, and optional motion."
version: "0.3.0"
latest_release_url: "https://github.com/kujolang/presentations/releases/tag/v0.3.0"
release_status: "Version identifies the published preview source release. The npm package remains private; clone the repository to use the authoring and build tools."
last_updated: "2026-10-03"
---

## What it does

Kujo Presentations turns structured deck source into a browser-native static site. Each deck gets numbered slide URLs, an overview, a reading edition, print and PDF output, and an optional presenter console. The source stays in normal files instead of a proprietary presentation format.

Start with the `investor`, `live-talk`, or `sales` starter, or build from the included layouts. Authors edit `deck.json`, `BRIEF.md`, local assets, and theme CSS. Agents can use the repository's deck-creation guide, starter catalog, JSON Schema, and layout limits to work inside the same contract.

## Static output with a useful fallback

Slides are real HTML pages with direct links and browser history. The overview and reading edition work without JavaScript. The viewer adds keyboard and touch navigation, slide-only fullscreen, and optional local Motion bundles while respecting reduced-motion preferences.

The reading edition gives the deck a normal document flow for small screens, browser zoom, assistive technology, and reference. The print route creates one 16:9 slide per page, and the repeatable Chromium exporter produces a visual PDF.

## Presenter tools and private notes

The presenter console shows current and next slides, direct slide selection, an audience-window control, and an elapsed timer. Private speaker notes load from a local JSON file into the presenter tab. They are not included in generated HTML, sent to the audience window, placed in URLs, or saved to browser storage.

## Why it belongs in Kujo

Presentations shows how Kujo's publishing stack can support designed, reviewable communication. SSG supplies static routes and asset copying. SiteKit supplies tokens, layout utilities, controls, and focus styles. Presentations owns the slide layouts, validation, canvas geometry, viewer, presenter tools, and motion. Neither upstream project depends on it.

## Operating boundary

Version 0.3.0 is a preview distributed as source through GitHub releases; it is not published to npm. Native authoring and build tools are verified on macOS and Linux, not Windows. Automated browser, geometry, and accessibility checks do not replace factual review, visual review, a human screen-reader session, or fluent-language review.

Generated decks are static files. Presentations does not provide accounts, tenant isolation, hosted rendering, or server-side authorization. Build trusted projects in a private workspace, keep private files outside the published asset tree, and protect confidential decks at the host.

## See it in use

[Explore the live presentation examples](https://presentations.kujolang.ai/) for investor, sales, live-talk, and original media decks built from the repository's source.

## Learn more

- [Presentations 0.3.0 release](https://github.com/kujolang/presentations/releases/tag/v0.3.0)
- [Presentations repository](https://github.com/kujolang/presentations)
- [Presentations documentation](https://docs.kujolang.ai/showcases/presentations/)
- [Getting started](https://github.com/kujolang/presentations/blob/v0.3.0/docs/getting-started.md)
- [Authoring guide](https://github.com/kujolang/presentations/blob/v0.3.0/docs/authoring.md)
- [Support matrix](https://github.com/kujolang/presentations/blob/v0.3.0/docs/support-matrix.md)
