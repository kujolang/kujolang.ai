---
title: "SiteKit"
custom_url: sitekit
description: "A source-driven design system for accessible, semantic, token-based static websites and web interfaces."
featured_image: "/assets/images/ecosystem/sitekit-interface-system.webp"
section: "Tooling"
tags: [Tool, Design System]
order: 330
install_command: "git clone https://github.com/kujolang/site-kit.git"
github_url: "https://github.com/kujolang/site-kit"
launch_story: "Give people and agents a stable set of tokens, schemas, semantic templates, components, and page recipes to build from."
scope_note: "SiteKit provides tested source components and distribution assets, not accessibility certification for arbitrary downstream pages or a hosted component service."
keywords: "SiteKit, Kujo ecosystem, design system, accessible components, static websites"
seo_title: "SiteKit — Kujo Ecosystem"
---

## What it does

SiteKit 1.0 generates a stable `dist/` distribution from design tokens, bundled themes, component schemas, semantic HTML templates, component CSS, layout recipes, and documented accessibility and responsive contracts. Consumers vendor the distribution and load `sitekit.css`; optional `sitekit.js` progressively enhances documented interactive hooks.

## Built for durable pages

The supported distribution includes light and dark themes, Departure Mono font assets, static HTML compositions, and progressive behaviors for dropdowns, popovers, drawers, dialogs, tooltips, and theme controls. Semantic HTML, native controls, content, layout, and CSS remain usable without JavaScript.

## Why it belongs in Kujo

SiteKit makes interface construction source-readable and agent-inspectable. Schemas, tokens, templates, examples, and generated assets create a shared contract between design intent, implementation, and browser verification. Kujolang.ai itself is built with SiteKit.

## Operating boundary

WCAG 2.2 AA is the design and automated-test baseline for supported source components and reference compositions. Consumers remain responsible for their content, application state, custom contrast, framework integration, assistive-technology testing, and complete downstream accessibility.

## Learn more

The repository contains the component index, themes, layouts, recipes, generation pipeline, browser-support matrix, accessibility boundary, deterministic release archive, and clean-consumer verification guidance.
