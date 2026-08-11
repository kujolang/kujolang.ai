# Recommendations and measurement plan

Audit date: 2026-08-10

## Immediate after deployment

- Re-run `scripts/probe_site.py`; confirm HTTP/www and extensionless nested
  variants resolve in one permanent hop to canonical HTTPS routes, retired
  `.html` aliases return 404, and the missing-route response remains a true 404.
- Validate the home, ecosystem, and one software page in Schema Markup
  Validator. Rich Results Test eligibility is a separate question and is not
  expected for every Schema.org type.
- Submit `https://kujolang.ai/sitemap.xml` in Google Search Console and Bing
  Webmaster Tools when access is available; do not infer submission status.
- Decide the Leash/Ward public-source disposition and training-crawler policy.

## 7-day checks

- Search Console: indexing status, sitemap processing, canonical selection,
  crawl errors, query/page impressions and clicks.
- Bing Webmaster Tools: sitemap processing, indexed URLs, crawl errors, and
  optional IndexNow evaluation.
- Request logs: status by path/host/user agent, redirect chains, bot access,
  and previously unknown 404/5xx URLs.
- Repeat the same dated branded/non-branded search and AI question sets without
  treating a single observation as universal rank.

## 28-, 60-, and 90-day comparisons

For each window, compare the same page/query/country/device dimensions:
impressions, clicks, CTR, average position, indexed canonical pages, search
appearances, conversions, crawl volume/errors, field LCP/INP/CLS, ChatGPT UTM
referrals, other identifiable AI referrals, and controlled AI mentions/citations.
Record provider, date, locale, cited URL, competitors, accuracy, and limitations.
Do not claim causation from correlation.

## Editorial decisions

- Publish first-party Writing only when it adds verified examples, measurements,
  release evidence, implementation detail, or maintainer perspective.
- Add visible dates/bylines only when accurate and maintainable.
- Consider a concise project-status/source-availability signal on ecosystem
  pages after the owner confirms the maturity and public-access facts.
- Conduct a focused performance pass on CSS critical-path reduction and
  responsive hero/card image variants, then repeat at least three comparable
  lab runs and collect field data.
