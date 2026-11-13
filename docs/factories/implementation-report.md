# Factories integration · 2026-11-13

## Pages

These are the canonical routes built by this branch. They are not a claim of production deployment.

- https://kujolang.ai/ecosystem/factories/
- https://kujolang.ai/ecosystem/software-factory/
- https://kujolang.ai/ecosystem/videoops-factory/
- https://kujolang.ai/ecosystem/publishing-house-factory/
- https://kujolang.ai/ecosystem/webops-factory/
- https://kujolang.ai/ecosystem/product-launch-factory/

## Integration

The category has an input/output/environment/evidence/review comparison, five-station launch explanation and local onboarding path. Each detail page covers actual inputs, roles, artifacts, Factory Floor, review, setup, release state, limits and related tools.

Factories appears in homepage discovery without changing the language-first hero, shared desktop/mobile navigation, the ecosystem catalog, footer and nine relevant tool pages. Existing search/WebMCP, sitemap, canonical, social and JSON-LD generation include the six routes. See [the surface inventory](integration-inventory.md) for every reviewed surface and intentionally unchanged content.

Canonical product metadata remains in `content/ecosystem/`. The category card renderer reads those entries. `templates/factories-intro.html` holds category editorial layout; `content/pages/factories.md` owns category metadata. Existing skills/workflows synchronization preserves these sources and Howl cards; a real isolated Git-fixture test exercises the normal sync script. No separate public product catalog or frontend framework was introduced.

## Capability mapping

| Factory | Verified roles and tools | Accountability boundary |
| --- | --- | --- |
| Software | Commander, architect, backend/frontend workers, independent/release reviewers; Dispatch and rootless Workcell | Allowed-file admission and source/harness-bound executable checks; local candidate, no deployment. Later accountability-tool integrations are not claimed for release 0.1.0. |
| VideoOps | Producer, Creative Director, Asset Scout, no-generation Media Generator stage, HyperFrames Editor, Video Critic | Registered-media hashes, trusted compilation and technical review; full playback/listening and creative review remain separate. |
| Publishing House | Canonical operator; commissioning/evidence/writing/adaptation/copy roles; StoryDesk, Dossier, BluePencil, GalleyPack, VersionSeal | Preserved excerpts and revisions, independent model review and exact-package approval request; no publication. |
| WebOps | Metadata, accessibility and link-health specialists plus independent reviewer; SiteProbe and Lens | Four allowed repairs to a bounded static copy; before/after checks, screenshots and diff; no original-site mutation or deployment. |
| Product Launch | Source evidence, Publishing House, WebOps, VideoOps, launch review | Pinned child factories and versioned handoffs; drift detection and local human approval. Software export verification is intake, not application construction. |

[Machine-readable capability matrix](capability-matrix.json), [readable matrix](capability-matrix.md) and [dependency graph](dependency-map.md) contain exact relationship classes, source links, dependency pins and artifact producer/consumer/rejection boundaries.

## Artwork and media

Six distinct heroes were generated through ChatGPT's built-in image generation, one call per target, using the fixed dither visual-contract JSON with the object substitutions in [`assets/prompts/factory-heroes.json`](../../assets/prompts/factory-heroes.json). Finalization produced 1916×821 lossless WebP with decoded channel values only 0 and 255. All were visually inspected. The six matching 1200×630 Howl cards were inspected together; the complete 333-card set was rendered. Four unrelated existing card raster differences were excluded from the change.

Heroes are `assets/images/ecosystem/{factories,software-factory,videoops-factory,publishing-house-factory,webops-factory,product-launch-factory}.webp`; corresponding cards are under `assets/images/social/` with `.jpg` extensions. The established responsive generator creates 640/960/1280 variants.

Five authentic floor images are under `assets/images/factories/`. Software uses its retained historical frame; VideoOps uses second 3 of its canonical demonstration; the other factories use their actual retained floor PNGs. [Image provenance](media-provenance.json) records source revisions and transformations.

Players use native controls, posters, `preload="none"`, no autoplay, direct upstream download fallbacks and available source narration scripts. GitHub streaming produced an observed connection reset in Chrome, so the site serves byte-identical canonical video mirrors under `public/media/factories/`. [Mirror provenance](video-mirrors.json) records every source URL, hash, variant and byte size. The three available mobile films reduce transfer size. Product Launch is the exact approved v0.1.0 coordinator asset, SHA-256 `60102b8d687173399387df3cd4bb1f4e37446538ef7705cabc524e94dc28fa45`; it is not the generated campaign clip. Script text does not claim synchronized caption or listening verification.

## Source traceability

| Repository | Audited commit | Published release at audit |
| --- | --- | --- |
| software-factory | `cfddc146e225229a9c15d3bf8ad2bfc01e2c8e24` | `0.1.0` |
| videoops-factory | `dcf2dc4fa7311f59ba3dd16f58a227439a155979` | None; source preview |
| publishing-house-factory | `38e7900a16f8482d12ad6b8b6a15f538d7ee3099` | None; source preview |
| webops-factory | `a2aba2c63777f37bf47d64dc93748949658b977b` | None; source preview |
| product-launch-factory | `d61c7021b0469c45f909b8371205f0df3afbac8b` | `v0.1.0` |

Original factory checkouts were not modified. Research used isolated public source checkouts. Product Launch's software-verifier dependency is separately pinned to `259aff26e3ca627873eec6b40a89d6942b039d7c`; it is not conflated with the Software Factory 0.1.0 page. The launch onboarding observation belongs to its retained earlier qualification revision and excludes prerequisites already provisioned, sign-in and live generation.

## Verification and delivery

See [qualification](qualification.md), [public URL checks](public-link-verification.json), [actual browser search results](discovery-verification.json), and the committed browser receipt under `.loop-engineering/evidence/factories-browser/`.

The initial checkout was clean `main` at `5fad198eadcb5fcff0b185c952ca8748d7bb5ba1`. A separate archive of that baseline built successfully with Kujo 1.9.0 (72 pages). The first attempted baseline used an older local Kujo 1.5.0 and was stopped; it is not reported as passing. The final site uses the repository's qualified 1.9.0 runtime and generates 73 page records plus its collection routes.

Work is delivered on `feat/factories-ecosystem`, draft [PR #7](https://github.com/kujolang/kujolang.ai/pull/7). Production deployment remains restricted to `main`; this work neither merged nor deployed. The pull-request build trigger now checks the same build gates without publishing.

Commits before final qualification:

- `3baf69a` — pinned research and integration boundaries.
- `d33b435` — category, product pages, site integration, dither heroes and authentic visuals.
- `45c1bc6` — Howl social assets.
- `25571ce` — regression checks and hash-verified canonical demo mirrors.
- `b0e65ea` — fixed-header breadcrumb clearance, regression assertions and public media verification.

The final browser pass covered 12 desktop/mobile page cases, 12 Axe audits with zero violations, 20 internal links and all five native MP4 players. No unresolved implementation defect was found. This is not a claim of complete accessibility certification or human creative approval.

SignalBox: no captures warranted. Source limitations are documented product boundaries; merging/deploying this review branch is a delivery decision, not an unresolved defect.
