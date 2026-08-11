# Unresolved items

Audit date: 2026-08-10

1. Anonymous requests to `https://github.com/robertdevore/leash` and
   `https://github.com/robertdevore/ward` return 404. Confirm whether the
   repositories should become public, the links should change, or the project
   pages should remain published without public source access.
2. The Writing index contains no articles. Publishing launch notes, verified
   technical guides, examples, or field reports requires editorial material and
   approval; generic filler was intentionally not created.
3. Representative Lighthouse LCP remains above 2.5 seconds, especially the
   ecosystem index (6,382 ms after). CSS delivery and responsive media variants
   merit a focused performance pass. Field evidence is unavailable.
4. Search Console, Bing Webmaster Tools, analytics, request logs, backlinks,
   CrUX/RUM, and controlled AI citation sessions are
   `NOT AVAILABLE — DATA ACCESS REQUIRED`.
5. Robots currently permits search, user-fetch, and training crawlers through a
   generic allow rule. Training access is an owner policy choice and was not
   changed as an SEO side effect.
6. IndexNow is not configured. Treat it as an optional experiment only after a
   deployment-safe key and submission workflow are deliberately adopted.
