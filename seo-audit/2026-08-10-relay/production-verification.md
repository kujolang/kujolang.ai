# Production verification

Verified after GitHub Pages workflow `31456533077` completed successfully on `2026-08-11` UTC.

- `https://kujolang.ai/ecosystem/relay/` returned HTTP `200` with canonical `https://kujolang.ai/ecosystem/relay/`.
- The live page exposed one `Relay` H1, unique title and description, a `SoftwareSourceCode` JSON-LD object, `codeRepository` set to `https://github.com/kujolang/relay`, and the Relay Howl social image.
- `https://kujolang.ai/ecosystem/not-a-real-tool/` returned HTTP `404`, declared `noindex,follow`, omitted a canonical link, and referenced root-absolute assets.
- The live SiteKit CSS, theme CSS, site JavaScript, Relay social card, and Relay WebP hero each returned HTTP `200` with the expected content type.
- The live sitemap and `llms.txt` each contained Relay and did not contain the synthetic missing route.
- The after crawl probed 40 canonical production pages: all 40 returned HTTP `200`; no metadata, canonical, H1, broken-link, orphan, image, or schema issues were detected.
