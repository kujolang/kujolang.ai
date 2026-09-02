# Unresolved items

Audit started: 2026-09-01. Deployment verification: 2026-09-02.

No P0 or P1 technical launch issue remains.

Two P2 pre-existing public-link issues remain:

- `/ecosystem/leash/` links to `https://github.com/robertdevore/leash`, which returns 404 to an unauthenticated visitor.
- `/ecosystem/ward/` links to `https://github.com/robertdevore/ward`, which returns 404 to an unauthenticated visitor.

Authenticated local git access confirms the repositories exist. The owner must
either publish them, replace the destinations, or remove the public source and
clone links. This audit does not infer permission to expose private repositories.

The following evidence remains unavailable rather than failed:

- Google Search Console inspection, coverage, impression, click, and query data
- Bing Webmaster Tools and IndexNow submission history
- First-party analytics, conversions, and referral attribution
- CDN, cache, real-user performance, and Core Web Vitals telemetry
- Backlink, mention, and authenticated AI-answer citation observations

The public `mcp.kujolang.ai` service is intentionally a read-only ecosystem
catalog. A privileged multi-tenant managed Ability execution service is a
separate product and infrastructure decision requiring OAuth 2.1, tenant
isolation, durable policy and receipt stores, quotas, revocation, SLOs, and an
independent security review. Its absence is not a defect in this v1.0.1 page.
