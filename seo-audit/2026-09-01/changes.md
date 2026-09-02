# Implemented changes

Audit started: 2026-09-01. Deployment verification: 2026-09-02.

## Content and architecture

- Added `/ecosystem/ability/` for Kujo Ability 1.0.1 without changing the writing section.
- Added Ability integration context to Agents SDK, MCP, CMS, and SSG pages.
- Added Ability to the Primitives catalog and updated the verified project counts.

## Search and machine discovery

- Added a unique title, description, H1, canonical, Open Graph and X metadata.
- Added SoftwareSourceCode JSON-LD aligned with visible page claims.
- Added the canonical route to the sitemap, `llms.txt`, and generated WebMCP catalog.
- Preserved the public `mcp.kujolang.ai` boundary as a read-only catalog; the page does not claim privileged hosted execution.

## Visual and social package

- Added a 1916-by-821 monochrome dither hero with intrinsic dimensions and useful alt text.
- Added the Ability entry to the 191-card Howl manifest.
- Rendered and verified the deterministic 1200-by-630 Ability social card.
- Corrected the repository-local Howl path and updated the social-card count gate.

## Verification

- Built the complete site with the pinned Kujo-compatible runtime.
- Passed site-contract, generated-output, HTML, image, social metadata, and Howl-card checks.
- Crawled the complete after output and compared its canonical set with the immutable production baseline.
- Probed the deployed production route and sitemap after GitHub Pages completed.
