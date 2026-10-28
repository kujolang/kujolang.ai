# Howl showcase receipts

All 26 requested pages use entries from the existing howl-social.json. The focused howl-language-pages.json is generated, not an independent editorial source. Run `npm run examples:generate` and `npm run howl:pages:generate` after changes, then check both projections.

Native invocation (from this repository):

```sh
export KUJO="$PWD/tmp/runtime/kujo"
../howl/bin/howl validate --manifest howl-language-pages.json
../howl/bin/howl list --manifest howl-language-pages.json
../howl/bin/howl show examples-request-hash --manifest howl-language-pages.json
../howl/bin/howl caption examples-request-hash --manifest howl-language-pages.json --platform x
../howl/bin/howl render --manifest howl-language-pages.json --out tmp/howl-language-pages --format all
node scripts/rasterize-social-cards.mjs tmp/howl-language-pages assets/images/social howl-language-pages.json
```

`showcase.zip` preserves all 79 generated files: 26 SVGs, 26 HTML pages, 26 Markdown snippets and the gallery. Extract before opening the gallery. `artifact-hashes.json` verifies every file; `determinism.json` records the identical second render. Per-card show/caption receipts cover every page; no captions were posted. The contact sheet was visually reviewed for wrapping, clipping and brand consistency. All 26 titles remain complete, including the longer workflow and structured-output titles.

Howl does not execute samples. Runtime verification is recorded separately by Loop. Checked-only examples remain labeled as such. The performance card refers to the existing bounded workload, not a new benchmark or a comparison claim. The guide YAML is generated from the visible source and is a configuration example, not an executable Kujo program.
