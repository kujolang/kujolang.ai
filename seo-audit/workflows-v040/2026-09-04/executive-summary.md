# Executive summary

Audit date: 2026-09-04

## Overall status

PASS WITH RECOMMENDATIONS

## Where the site was

The preserved pre-change deployment exposed 194 canonical, indexable pages. All
194 returned 200, appeared in the sitemap, and had unique titles and
descriptions, one H1, a matching canonical, parseable structured data, and no
broken internal links. All 828 images had alt text and intrinsic dimensions.
The internal technical-readiness score was 91/100 and AI-search-readiness score
was 85/100. These are transparent audit heuristics, not search-engine scores.

## What was wrong

- The workflow catalog visibly combined a `kujo-workflows 0.4.0` badge with
  stale claims of 34 workflows in the 0.3.0 release.
- Six public link occurrences led to three GitHub repository URLs that return
  404 anonymously.
- The animated dither hero performed half-resolution pixel sampling at 14 fps
  on hero-bearing pages.
- Search-console, analytics, field-performance, backlink, and controlled
  AI-answer measurements were unavailable.

## What changed

- The workflow catalog now states 38 released workflows in 0.4.0, with
  generated-output contract assertions covering both facts.
- The concurrent site hardening reduced animated dither sampling to
  quarter-resolution at 4 fps while preserving reduced-motion and visibility
  gates.
- The exact before and after build artifacts, hashes, production probes, crawl
  tables, and desktop/mobile Lens evidence are preserved in this audit.

## Where the site is now

The clean GitHub Actions deployment and independent after crawl pass all tested
technical gates across 194 canonical pages. The workflow index and operator
pages pass automated accessibility, internal-link, console/network, and 390px
mobile-width checks. The corrected release facts are visible in production.
The internal technical-readiness score is 94/100 and AI-search-readiness score
is 87/100; the remaining deductions reflect unavailable public destinations
and outcome data, not hidden crawl failures.

## Available measurements

- Full 194-page before/after crawl and production HTTP comparison.
- Redirect, robots, sitemap, crawler-access, and external-destination probes.
- Desktop and 390px-mobile Lens evidence for the workflow catalog and operator.
- Dated anonymous search observations and an explicitly unmeasured AI-answer
  benchmark.

## Unavailable measurements

Google Search Console, Bing Webmaster Tools, analytics, origin/CDN logs, field
Core Web Vitals, backlinks, and controlled AI-answer citations remain
`NOT AVAILABLE — DATA ACCESS REQUIRED`. No ranking, traffic, or citation gain
is claimed.

## Next actions

1. Decide whether the three anonymously unavailable repositories should become
   public or point to different authoritative destinations.
2. Submit and inspect the 194-URL sitemap in Google Search Console and Bing
   Webmaster Tools.
3. Repeat the dated search and AI-answer observations after 7, 28, 60, and 90
   days when measurement access is available.
