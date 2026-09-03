# Recommendations and measurement plan

Audit date: 2026-09-02

## Immediate after deployment

- Confirm the Publishing House Operator route has no horizontal overflow at
  mobile and desktop widths on the public edge.
- Confirm its title, description, canonical, Open Graph image, X card, schema,
  sitemap entry, and internal links match the generated source.
- Confirm the corresponding docs pages expose the live adapter and recovery
  commands and return HTTP 200.

## 7-day checks

- Inspect Google Search Console and Bing Webmaster Tools for crawl errors,
  canonical selection, mobile usability, and sitemap processing if those
  consoles are connected.
- Review site health and post-publish WebOps findings; create StoryDesk work only
  for stable, evidence-backed issues.

## 28-, 60-, and 90-day comparisons

- Compare impressions, clicks, indexed state, referrals, AI citations, and
  engagement only where first-party exports are available.
- Separate technical eligibility from search or audience outcomes; do not infer
  causation from the page change alone.

## Editorial decisions

- Keep the page outcome-led. Installation-specific provider and credential gates
  belong in a deployment section rather than a devaluing hero disclaimer.
- Do not describe authenticated Git publication as bundled until a PressWire
  provider has been configured and proven in the target repository.
