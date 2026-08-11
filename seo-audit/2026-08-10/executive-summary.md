# Executive summary

Audit date: 2026-08-10

## Overall status

PASS WITH RECOMMENDATIONS

## Where the site was

The untouched production build exposed 38 canonical, indexable pages. All 38
returned HTTP 200 in production, appeared in the sitemap, had a unique title,
one H1, a canonical URL, parseable JSON-LD, crawlable HTML, and no broken
internal links or orphans. Search and AI crawler user agents received HTTP 200
for robots.txt, the home page, a key ecosystem page, and the sitemap.

The internal SEO health heuristic was 71/100 and the AI-search readiness
heuristic was 65/100. These are transparent audit trend scores, not scores from
Google, Bing, OpenAI, Anthropic, or Perplexity.

## What was wrong

- Flat `.html` output aliases caused GitHub Pages to serve duplicate nested
  pages at extensionless non-trailing-slash and `.html` URLs without a redirect.
- 71 rendered images lacked intrinsic dimensions, including above-the-fold hero
  media and ecosystem cards.
- 33 ecosystem project pages were labeled `BlogPosting`; four non-home routes
  were labeled `WebSite`; project schemas omitted the visible source repository.
- The home title was brand-only, the ecosystem index reused the home
  description, and all pages emitted the obsolete meta-keywords tag.
- Brand links targeted `index.html` rather than the canonical root.
- Anonymous production requests confirmed two GitHub destinations return 404:
  Leash and Ward. Their repositories may be private; no substitute URL was
  inferred.
- The Writing index has no published articles. Field Core Web Vitals, search
  console data, analytics, request logs, backlinks, and controlled AI-answer
  citations were unavailable.

## What changed

The build now emits only clean directory routes, canonical root links,
page-purpose-aligned schema (`CollectionPage`, `AboutPage`, `ContactPage`,
`WebPage`, and `SoftwareSourceCode`), repository properties on software pages,
intrinsic image dimensions, high-priority hero loading, a descriptive home
title, a unique ecosystem description, a consistent Kujo site name, and no
meta-keywords tag. Contracts enforce these behaviors. Reusable crawl,
production-probe, and Lighthouse-normalization scripts make future comparisons
repeatable.

## Where the site is now

The rebuilt output still contains 38 canonical/indexable pages with zero
missing or duplicate titles/descriptions, zero H1/canonical/sitemap errors,
zero broken internal links, zero orphans, zero missing alt attributes, zero
missing dimensions, and zero JSON-LD parse failures. The internal SEO heuristic
is 86/100 and AI-search readiness is 74/100.

Comparable one-run mobile Lighthouse measurements improved from 71 to 86 on
the home template, 55 to 70 on the ecosystem index, and 76 to 87 on an ecosystem
detail page. The ecosystem LCP decreased from 7,903 ms to 6,382 ms, but all
three representative LCP values remain above 2.5 seconds in these lab runs.
This is immediate technical evidence, not proof of ranking, traffic, citation,
or field Core Web Vitals improvement.

## Available measurements

- Immutable untouched generated baseline plus SHA-256 manifests
- Local before/after crawls for all 38 canonical routes
- Baseline live page, redirect, DNS, external-link, and crawler receipts
- Comparable Lighthouse 13.0.1 receipts for three representative templates
- Dated web-search observations and an explicit unavailable AI benchmark

## Unavailable measurements

Google Search Console, Bing Webmaster Tools, analytics, CDN/request logs, CrUX
or first-party RUM, backlink tools, authenticated ranking APIs, and controlled
AI-answer sessions are `NOT AVAILABLE — DATA ACCESS REQUIRED`.

## Next actions

Resolve whether Leash and Ward should be publicly accessible, publish useful
first-party Writing material when editorially ready, reduce render-blocking CSS
and representative LCP, and collect the 7/28/60/90-day measurements defined in
`recommendations.md` before making any outcome claim.
