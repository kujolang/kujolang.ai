# Changelog

All notable changes to Kujolang.ai are documented here. Releases follow semantic versioning.

## Unreleased

### Changed

- Updated the Workcell ecosystem page for the 1.1.0 source release, its stable Docker and Podman lifecycle, and the alpha boundary around portable contracts and remote adapters.

## [1.2.9] - 2026-09-04

### Added

- Deterministic 640 px, 960 px, and 1280 px WebP derivatives, responsive `srcset` and `sizes` markup, and build-time contracts for local featured and catalog images.

### Changed

- Production and local preview builds now generate responsive media before validating or publishing the site.

### Fixed

- Corrected the Workflows catalog summary to report the 38 released `kujo-workflows 0.4.0` kits, with a generated-site contract that prevents the visible count and release label from drifting again.

## [1.2.8] - 2026-09-04

### Added

- Reproducible full-site SEO and AI-search audit evidence for all 194 canonical pages, including production, crawler, link, schema, media, search-observation, and representative browser-performance datasets.

### Changed

- Reduced animated hero dither work to a quarter-resolution canvas at four frames per second, preserving the visual treatment while materially reducing main-thread scripting cost.
- Generalized production diagnostics so sibling sites can supply their canonical key route and explicitly omit non-contract `www` or feed probes without creating false findings.

## [1.2.7] - 2026-09-04

### Added

- Added Kujo for Paperclip to the Tooling catalog with direct installation and first-use guidance, documented safety boundaries, dedicated Kujo dither hero art, and a Howl social card.

## [1.2.6] - 2026-09-04

### Added

- A homepage Agent Development Platform quickstart with focused install, create, and run commands plus direct links to the showcase and documentation.
- The focused agent installer in the Quick Install dialog, with an independent copy control for each installation path.
- A Kujo Providers directory with 25 native provider integrations, local provider marks, searchable cards, accessible detail dialogs, and README-sourced starter snippets.
- A dithered provider-grid social promo card with the Kujo mark and all 25 provider logos.
- A Howl social card and generated-site contract coverage for all 38 workflow routes.
- Kujo Ability 1.0.1 ecosystem page with source-grounded contract, runtime, CMS, SSG, Agents SDK, MCP, Codex, Cursor, VS Code, Kujo Pi, deployment, and safety boundaries.
- Reciprocal Ability integration sections on the Agents SDK, MCP, CMS, and SSG pages.
- Pure black-and-white Ability hero artwork and a Howl-rendered 1200×630 social card.
- Dated before/after SEO and AI-search audit evidence for the 190-page production baseline and the expanded launch inventory.
- Full-screen, accessible Kujo introduction video player launched from the homepage hero.
- Ecosystem pages for the eight Publishing House tools: AssetWorks, BluePencil, Dossier, GalleyPack, PressWire, ReaderSignal, StoryDesk, and VersionSeal.
- Dedicated binary Kujo dither hero art and Howl-rendered 1200×630 social cards for every Publishing House tool.
- Eight installable Publishing House workflow pages covering Daily Desk through Post-Publication Learning, each with source-grounded boundaries, custom Kujo dither hero art, and a Howl-rendered social card.
- Kujo Ecosystem Launch skill page with release-pinned source links, custom binary dither hero art, and a Howl-rendered social card.
- Kujo Way Development skill page, installation guidance, custom binary dither hero art, and a Howl-rendered social card.

### Changed

- Rebuilt the PackWrite ecosystem page around the released 1.1.0 command surface, pack structure, provider boundary, configuration, offline/CI workflow, and staged-write safety controls.
- Updated the MCP 1.1.1 page for its GitHub release, executable and reproducible portable Ability package, current host evidence, and remaining npm, mutation, recovery, signing, and enterprise boundaries.
- Updated the Ability page with native VS Code OAuth/session evidence and the optimized Cloudflare Workers Free authorization profile: 4.37 ms mean, 9 ms p95, and zero `exceededCpu` outcomes across 30 production requests.
- Promoted the Publishing House Operator page to its production-capable live phase-adapter contract, including checksum-bound receipts, bounded retries, explicit blocked-item recovery, and deployment authority gates.
- Updated the complete workflow catalog to the official kujo-workflows 0.4.0 release: 38 source-backed workflow pages, including Owned Agent Project, refreshed release metadata, and complete hero and Howl social-card coverage.
- Updated the CMS ecosystem and workflow-skill pages for CMS 1.1.0, including framework-neutral clients, granular SEO and social tools, portable extension packages, identity sessions, abilities, connectors, MCP, and built-in WebMCP.
- Refreshed the CMS and CMS workflow social cards from their Howl sources.
- Updated the public installer to Kujo v1.1.0 with the focused `agent` profile, immutable repository pin support, and current release defaults.
- Updated the Dispatch ecosystem page for the Dispatch 1.2.0 release, including deterministic routing, persisted route evidence, and the current GitHub release link.
- Replaced the homepage hero's Quick Install action with a View video action while preserving Quick Install in the site navigation.
- Updated the Workflows catalog from 26 workflows in kujo-workflows 0.2.0 to 34 workflows in kujo-workflows 0.3.0.
- Synchronized the public catalog to 96 Kujo Skills and 38 Kujo Workflows from their released source repositories.
- Standardized the WebOps name across Skills, Workflows, metadata, and social sharing cards.
- Restored the animated Bayer-dither treatment across every image-backed homepage, page, catalog, skill, workflow, and ecosystem hero, with offscreen and background-tab pausing.

### Fixed

- Intrinsic-width overflow on mobile ecosystem detail pages containing long code or command content; contained scrolling code blocks are keyboard-focusable when needed.
- Removed horizontal tears, jitter, and scanline inversion from image-backed heroes, restoring the original static-style Bayer dither treatment while retaining content-hash cache busting for the runtime.

## [1.2.0] - 2026-08-12

### Added

- Accessible Ecosystem navigation dropdown for Primitives, Tooling, Showcase, Skills, Workflows, and the external Agents site.
- 83 released Kujo Agent Skill pages and 25 released Kujo Workflow pages, each with source-grounded metadata, repository links, and dedicated Kujo dither hero art.
- Howl-rendered 1200×630 social cards for every new catalog and detail route.

### Changed

- Nested Skills and Workflows routes now participate in canonical metadata, JSON-LD, `llms.txt`, internal navigation, and the XML sitemap.
- Expanded the production site contract and SEO audit coverage to all 153 shareable routes.

## [1.1.0] - 2026-08-12

### Added

- Ecosystem pages, custom binary dither hero art, and Howl social sharing cards for ContentGraph, SearchBridge, and SiteProbe 0.1.0.
- Ecosystem pages, WebP hero art, and social sharing cards for the official Workcell, Redact, SiteKit, Tribunal, and Relay 1.0.0 releases.

### Fixed

- Nested missing routes now render the styled custom 404 with root-safe assets, useful recovery links, and explicit `noindex` handling.

### Changed

- Relay and Tribunal hero artwork now use stark, pure black-and-white dithered compositions with fragmented subjects and larger negative-space fields; their Howl social cards were regenerated from the new source art.

## [1.0.0] - 2026-08-08

The first production release of the official Kujo programming language website.

### Highlights

- Launch-ready home, Ethos, Ecosystem, Writing, and Contact experiences built with Kujo SSG and SiteKit.
- Thirty structured ecosystem pages covering Kujo primitives, tooling, and showcases.
- Responsive full-screen navigation, mobile layouts, and accessible shared page structure.
- Static flickering Bayer-dither hero imagery without wave displacement.
- Quick Install and agent-onboarding prompt modals with clipboard controls.
- Public documentation, GitHub, X, Discord, sitemap, feeds, robots, and `llms.txt` destinations.
- Deterministic generated-output and site-contract validation for release checks.
