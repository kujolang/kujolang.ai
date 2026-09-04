# Executive summary

Audit date: 2026-09-04

## Overall status

**PASS WITH RECOMMENDATIONS.** The full rendered and production surface is crawlable, indexable, internally connected, canonicalized, schema-valid, and accessible to the tested search and AI-search crawlers. One product-owner decision and one catalog media optimization remain.

## Where the site was

The immutable baseline contained 193 canonical/indexable pages. All 193 returned 200 in production and appeared in the sitemap. Titles, descriptions, H1s, canonicals, internal links, crawl depth, image attributes, and JSON-LD parsing passed the full crawl.

## What was wrong

The animated hero dither monopolized the main thread in mobile-simulated Lighthouse runs: representative total blocking time ranged from 1.09 to 8.91 seconds, and detail-page LCP ranged from 10.90 to 12.59 seconds. `/ecosystem/` also transferred about 3.49 MB of images. Six public source/install links point to three private repositories, producing public GitHub 404 journeys.

## What changed

Hero dither work now runs at quarter layout resolution per axis and four redraws per second. Production diagnostics now accept site-specific key-route, `www`, and feed contracts and report parsed robots policy accurately. The after inventory contains 194 pages because the separately released Paperclip page landed during the audit; this was an intentional concurrent addition, not an audit-created route.

## Where the site is now

All 194 after pages return 200 in production and remain indexable, canonical, sitemap-listed, schema-valid, and free of broken internal links. Representative TBT fell to 0.15–0.83 seconds. Ability LCP fell from 10.90 to 2.73 seconds and PackWrite from 12.59 to 3.61 seconds. The image-heavy ecosystem page remains slower at 8.94 seconds LCP, and the private-repository journeys remain unresolved.

Internal heuristic scores (not platform scores): SEO health **84/100 → 89/100**; AI-search readiness **82/100 → 83/100**. The score change reflects verified technical evidence only.

## Available measurements

Full local/production crawls, redirect and crawler probes, external-link checks, JSON-LD parsing, image audits, four baseline and four after Lighthouse lab receipts, and four dated anonymous search observations are preserved here.

## Unavailable measurements

Search Console, Bing Webmaster Tools, analytics/conversions, CDN logs, field CWV, backlink authority, rank tracking, and controlled AI-answer citations are `NOT AVAILABLE — DATA ACCESS REQUIRED`.

## Next actions

Choose whether the Ability Gateway, Leash, and Ward repositories should be public or whether their public calls to action should be revised. Then add responsive catalog image derivatives and begin 7/28/60/90-day first-party measurement.
