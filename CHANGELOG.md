# Changelog

## Unreleased

- Added a homepage Agent Development Platform quickstart with focused install, create, and run commands plus direct links to the showcase and documentation.
- Added the focused agent installer to the Quick Install dialog with an independent copy control for each installation path.
- Updated the CMS ecosystem and workflow-skill pages for CMS 1.1.0, including
  framework-neutral clients, granular SEO and social tools, portable extension
  packages, identity sessions, abilities, connectors, MCP, and built-in WebMCP.
- Refreshed the CMS and CMS workflow social cards from their Howl sources.
- Updated the public installer to Kujo v1.1.0 with the focused `agent` profile,
  immutable repository pin support, and current release defaults.
- Added the Kujo Providers directory with 25 native provider integrations, local provider marks, searchable cards, accessible detail dialogs, and README-sourced starter snippets.
- Added a dithered provider-grid social promo card with the Kujo mark and all 25 provider logos.

All notable changes to Kujolang.ai are documented here. Releases follow semantic versioning.

## [Unreleased]

### Changed

- Updated the Dispatch ecosystem page for the Dispatch 1.2.0 release, including deterministic routing, persisted route evidence, and the current GitHub release link.

### Added

- Full-screen, accessible Kujo introduction video player launched from the homepage hero.
- Ecosystem pages for the eight Publishing House tools: AssetWorks, BluePencil, Dossier, GalleyPack, PressWire, ReaderSignal, StoryDesk, and VersionSeal.
- Dedicated binary Kujo dither hero art and Howl-rendered 1200×630 social cards for every Publishing House tool.
- Eight installable Publishing House workflow pages covering Daily Desk through Post-Publication Learning, each with source-grounded boundaries, custom Kujo dither hero art, and a Howl-rendered social card.
- Kujo Ecosystem Launch skill page with release-pinned source links, custom binary dither hero art, and a Howl-rendered social card.
- Kujo Way Development skill page, installation guidance, custom binary dither hero art, and a Howl-rendered social card.

### Changed

- Replaced the homepage hero's Quick Install action with a View video action while preserving Quick Install in the site navigation.
- Updated the Workflows catalog from 26 workflows in kujo-workflows 0.2.0 to 34 workflows in kujo-workflows 0.3.0.
- Synchronized the public catalog to 96 Kujo Skills and 37 Kujo Workflows from their released source repositories.
- Standardized the WebOps name across Skills, Workflows, metadata, and social sharing cards.
- Restored the animated Bayer-dither treatment across every image-backed homepage, page, catalog, skill, workflow, and ecosystem hero, with offscreen and background-tab pausing.

### Fixed

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
