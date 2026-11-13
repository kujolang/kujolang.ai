# Factory releases and presentation follow-up

The owner authorized publishing the three missing factory releases and refining the website presentation on 2026-11-13. VideoOps, Publishing House and WebOps v0.1.0 were published at the exact source revisions already audited for the website. The tag targets were independently read back through GitHub's Git refs API. Publication receipts and exact-commit CI links are in [releases-2026-11-13.json](releases-2026-11-13.json).

Local release verification (`npm run verify`) passed: VideoOps 15 tests, Publishing House 12 tests, WebOps 17 tests, plus their documentation checks. No provider calls, new renders or campaign publication were performed. Existing review boundaries remain in the release notes and website copy.

The category features Software Factory across two of three desktop columns, followed by a three-card second row. The comparison headings and station titles use Departure Mono. Stations have equal-height white cards without title numbers. Both supporting notes are smaller and centered. Factories uses the shared ecosystem carousel, including accessible previous/next controls and the shared unadorned section-title link.

The shared source panel now uses the header-aware sticky offset, and the footer no longer adds another section-sized top margin. Factory clone examples follow the current default branch; source evidence and documented release boundaries remain pinned for auditability. Future source changes do not silently expand those claims.

The factory browser suite now checks card geometry, station heights/backgrounds/fonts, note typography, sidebar/header clearance, footer margin, carousel navigation and heading decoration, in addition to the existing desktop/mobile media, navigation, discovery and automated accessibility checks.

## Verification

- Site Node tests: 34 passed; the output-dependent test passed separately with `npm run factories:verify` (8 tests).
- Kujo 1.9.0 production build: 73 pages; responsive pipeline: 1,230 variants.
- `scripts/verify-site-contract.sh output`: passed, including SiteKit integrity and 333 social cards.
- `scripts/validate-generated-output.sh output`: 339 HTML files passed.
- `npm run social:verify`: passed.
- Extended factory browser suite: all six routes at 1440px and 390px passed, with 12 Axe audits reporting no violations, five videos advancing in native playback, no console errors, and the requested layout assertions passing. Automated accessibility results are not a full conformance certification.
- Local receipts and screenshots: `tmp/factory-release-polish/` (ignored).
