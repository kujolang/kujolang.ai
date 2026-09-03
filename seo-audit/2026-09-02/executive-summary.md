# Executive summary

Audit date: 2026-09-02

## Overall status

PASS — the complete generated site, changed-route browser checks, Howl cards,
repository contracts, GitHub Pages deployment, and public edge verification
pass.

## Where the site was

The immutable public baseline contained 192 canonical, indexable URLs. The main
ecosystem catalog passed a 390px Chromium check, but the Publishing House
Operator detail route did not.

## What was wrong

On the operator route, Lens measured a 1,059px document inside a 390px mobile
viewport. The article column and descendants expanded to 1,039px because the
mobile grid used an auto minimum track while the article contained long command
content. The page also led with a fixture-only label that no longer described
the implemented live control-plane boundary.

## What changed

The shared detail-page grid now permits its article column to shrink to the
viewport, while code blocks keep contained horizontal scrolling. The operator
now exposes an executable live phase adapter, validates checksum-bound receipts,
retries provider failures within a fixed bound, reports adapter readiness, and
requires an explicit resume after hard blockers. Site and docs copy now describes
that production control plane first and keeps model, Git-effect, measurement,
and credential setup as explicit deployment gates.

## Where the site is now

The generated site retains 192 canonical, indexable pages with no missing or
duplicate titles or descriptions, H1 errors, canonical mismatches, broken
internal links, orphan pages, schema parse errors, missing image alt text, or
missing intrinsic image dimensions. The changed route now fits exactly within
its 390px viewport, and its automated accessibility check passes. All 192
shareable routes have generated Howl social cards.

The deployed public site returned HTTP 200 for all 192 canonical pages. Both the
ecosystem catalog and the Publishing House Operator route fit exactly inside a
390px production viewport. The changed route passed Lens accessibility, link,
network, console, and overflow gates. The synchronized docs route also returned
HTTP 200 and passed its production mobile accessibility and link check.

## Available measurements

Repository source, all 192 public baseline pages, local generated output, Lens
browser evidence, Howl manifests and rendered cards, metadata, schema, sitemap,
robots rules, redirects, links, images, and WebOps fixture receipts were
available and preserved.

## Unavailable measurements

Search Console, Bing Webmaster Tools, analytics, conversion, CDN/RUM, backlink,
rank-tracking, and authenticated AI-answer data were unavailable. No search or
audience outcome is inferred.

## Next actions

Configure the selected model/retrieval phase adapter, authenticated PressWire
Git/static provider for repositories that authorize Git effects, and enabled
ReaderSignal/WebOps providers in each production installation. Then perform one
controlled, approval-bound live publication and preserve its PressWire and
public-verification receipts.
