# Executive summary

Audit date: 2026-08-14

## Overall status

PASS WITH RECOMMENDATIONS — all eight Publishing House tool pages, the Ecosystem overview, the Tooling catalog, dropdown navigation, metadata, schema, Howl sharing images, sitemap, RSS autodiscovery, robots policy, and `llms.txt` passed source, generated-output, browser, and HTTP verification. Search outcomes and field performance require provider data and elapsed time.

## Where the site was

The immutable baseline contained 165 canonical, indexable, sitemap-listed production pages. All 165 returned 200 with no title, description, H1, canonical, internal-link, orphan, image, or schema defects. Each new tool route was linked from both Ecosystem and Tooling, used one unique H1 and description, exposed valid `SoftwareSourceCode` JSON-LD, referenced its correct public GitHub repository, and used a 1200×630 Howl JPEG sharing image.

## What was wrong

- `llms.txt` listed every project but omitted the three section catalogs: Primitives, Tooling, and Showcase.
- A continuously animated canvas re-dithered already-dithered hero artwork and a page-wide text scan initialized the scramble effect. Mobile Lighthouse recorded 1,130–2,920 ms total blocking time across the three audited templates.
- The mobile menu's visible `Menu` label was not contained in its accessible name.

## What changed

The generator now publishes the three section catalogs in `llms.txt`. The site uses the original Kujo-dithered WebP hero files directly, removes the redundant continuous canvas workload, scopes text scrambling to intentional display elements, and aligns the mobile menu's visible and accessible labels. Deterministic contracts now cover all eight new routes across GitHub links, social metadata, sitemap, `llms.txt`, and volatile-version rejection.

## Where the site is now

The deployed site retains 165 canonical/indexable routes with zero crawler issues. Representative post-fix production Lighthouse runs kept Accessibility, Best Practices, and SEO at 100; total blocking time fell to 28 ms on Ecosystem, 62 ms on Tooling, and 36 ms on AssetWorks. Lab Performance rose from 53 to 91, 39 to 84, and 62 to 92 respectively.

## Available measurements

Repository source, generated HTML, production HTTP responses, live crawler-user-agent probes, redirect behavior, external destinations, browser interaction, and Lighthouse lab evidence were available.

## Unavailable measurements

Google Search Console, Bing Webmaster Tools, analytics, request logs, field Core Web Vitals, rankings, and controlled AI-answer citation data are `NOT AVAILABLE — DATA ACCESS REQUIRED`.

## Next actions

Add responsive catalog thumbnails to reduce image transfer on the Ecosystem and Tooling collections; confirm or replace the inherited unavailable Leash and Ward repository destinations; and compare discovery/outcome evidence at 7, 28, 60, and 90 days when provider access exists.
