# Factory presentation follow-up

The owner requested a more direct product presentation after the release launch.

- Removed the homepage's “From a brief to a candidate” section.
- Factory category and detail navigation select only Factories. Detail selection uses canonical section metadata, so new factory entries inherit the behavior.
- Changed the category eyebrow to “Factories” and aligned section widths to the shared ecosystem content shell.
- Applied Departure Mono to factory card titles and supporting text.
- Made station headings larger than their supporting text. Titles can wrap rather than shrink to fit.
- Removed duplicate Factory Floor images, captions, transcripts and media implementation notes from product pages. Native videos retain posters, controls, accessible labels, download fallbacks and deferred loading. Detailed source/review records remain in the repositories and internal research.
- Added shared ecosystem-detail bottom padding without restoring the footer's duplicate margin.
- Removed the first article heading's top margin to align it with the sidebar and added image-to-title spacing on factory cards.

The browser regression suite checks these behaviors alongside responsive layout, navigation, media playback, links, discovery and automated accessibility.

## Qualification

34 source tests passed; all eight output-dependent factory tests passed. The Kujo 1.9.0 build, 1,230 responsive image variants, site contracts, 333 social cards and validation of 339 HTML files passed. The extended factory browser suite passed at 1440px and 390px: all six routes, 12 Axe audits with no violations, five videos playing, no console errors, and the requested content/navigation/layout assertions. Local evidence is retained under `tmp/factory-ux-followup/` (ignored).
