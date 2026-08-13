# Changelog

All notable changes to Kujolang.ai are documented here. Releases follow semantic versioning.

## [Unreleased]

### Added

- Full-screen, accessible Kujo introduction video player launched from the homepage hero.

### Changed

- Replaced the homepage hero's Quick Install action with a View video action while preserving Quick Install in the site navigation.

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
