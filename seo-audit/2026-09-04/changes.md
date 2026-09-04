# Implemented changes

Audit date: 2026-09-04

- Reduced the animated hero Bayer-dither canvas from half to quarter layout resolution per axis and capped redraws at four frames per second. The visible treatment remains animated while each frame touches one quarter as many pixels and scheduling falls from 14 to 4 Hz.
- Preserved crawler policy: search/user-fetch crawlers remain allowed; GPTBot and ClaudeBot training crawlers remain disallowed.
- Added this dated evidence workspace. No claims, repository visibility, DNS, or training policy changed.
- Generalized the production probe's key route, `www`, and feed assumptions so sibling-site audits do not record non-contract surfaces as defects; crawler policy labels now reflect the parsed robots decision.
