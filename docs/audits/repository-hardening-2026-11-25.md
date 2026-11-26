# Kujolang.ai repository hardening

## Repository

- Branch `main`
- Starting commit `82f1b092cfc28fcff4b423cdf00b9029ffb6c847`
- Verified implementation commit `fbea2f9f4df40d6840078efdd0aa5ad5f83d49ec`
- Public static site with a vendored Kujo SSG build, a SiteKit distribution, image tooling via Sharp, and GitHub Pages deployment. AI SDK certification drives the provider projection. The website publishes the installer maintained in `kujolang/kujo`.

## Findings

| ID | Priority | Area | Finding and evidence | Action | Status |
| --- | --- | --- | --- | --- | --- |
| SITE-01 | P0 | Installer credential handling | The alternate HTTPS manifest fetch shared the authenticated download helper without an origin scope. | Scope authorization to supported GitHub hosts and require HTTPS redirects. Use the matching canonical installer from `kujolang/kujo@c03152db53339c7c9303a6666d9feb4b98a9ce44`. | Fixed in source and verified against the generated installer |
| SITE-02 | P1 | Published artifact proof | The Bash gate printed success before running its final checks. The SiteKit verifier selected the default build directory and trusted each output's manifest independently. | Enforce the final verdict after all checks, inspect the requested output and compare it with the vendored manifest. Stop the unbounded alias search at its first result and handle missing social files explicitly. | Fixed |
| SITE-03 | P1 | Keyboard accessibility | Provider modal opening delayed focus to the next animation frame. The baseline browser run could press Escape while focus was still on the trigger. Backward tabbing from the dialog container could also leave both provider and installer dialogs. | Move focus synchronously, wrap backward tabbing from the dialog itself, and skip disabled installer controls. Exercise focus entry, containment, Escape and focus restoration. | Fixed |
| SITE-04 | P2 | Audit accuracy | The delivery probe treated a 404 from a required endpoint as expected, accepted a URL prefix as a canonical origin, and recorded a lost query outside the issues field. | Verify endpoint-specific status, exact canonical scheme/authority/path and query preservation. | Fixed |
| SITE-05 | P2 | Release verification | Pages checked rendered comparisons but skipped the authored-source drift check, and the browser registration harness remained outside CI. | Gate comparison freshness, Python regressions and the generated WebMCP runtime in Pages. | Fixed |
| SITE-06 | Needs more evidence | Shared WebMCP request lifecycle | `webmcp_runtime_source` caches one fetch with the initiating tool call's signal. The current test checks one cancelled call and cache reuse. The same loader exists in `kujolang/ssg`. | Trace concurrent caller cancellation in the SSG pass and promote any common fix to the website copy. | Open |

## Audit coverage

| Phase | Evidence and decision |
| --- | --- |
| 0. Repository | Traced `build.kujo` configuration, file copying, layout rendering and publication through `.github/workflows/pages.yml`. Read the browser scripts, installer, catalog projections, artifact contracts and supporting Python tooling. |
| 1. Baseline | Node 26.12.1 and a local Kujo 1.10.0 runtime on macOS. Node tests passed 36 with one artifact-dependent skip. Four Python tests passed. Factories, providers, guides, examples, workflows, comparisons and Howl projections passed their source gates. The production build completed in approximately 23 seconds. |
| 2. Complexity | Traced duplicate installer/browser paths and separate generated contracts. Kept native and fallback rendering paths because their compatibility role has existing consumers. |
| 3. Runtime | Reviewed native template rendering, indexed content generation and browser enhancement paths. The site is static. The provider dialog failure was caused by delayed focus, independent of rendering throughput. |
| 4. Resources | The responsive generator handled 410 original WebP files sequentially and used temporary files with cleanup. The site index loads lazily. No memory or execution-speed improvement is claimed. |
| 5–6. Build and output | Production-equivalent build generated 339 HTML files including vendored recipes. The image job generated 1,230 responsive variants. Artifact contracts cover variants, canonicals, social cards, downloadable samples and browser entrypoints. |
| 7. Token and context | Public WebMCP returns compact projections from a 218,010-byte index with 324 items and five types. The generated browser runtime lazily loads the index. Search/list limits cap results at ten. The 26,886-byte `llms.txt` links to detailed routes. No model invocation, tool replay state or handoff store exists in the site. |
| 8. Security | Reviewed the installer download boundary, registered read-only same-origin WebMCP tools, browser rendering of provider text and artifact hashes. The installer regression used a fixture token and stubbed transport. |
| 9. State and determinism | The full build resets its destination. Do not run a build alongside verifiers of the same output. Responsive variant bytes are deterministic under the existing fixture. See SITE-06 for the remaining shared request question. |
| 10. Interfaces | Installer flags, manifest syntax, site routes, site index schema and tool schemas are preserved. The verifier honors its existing output-directory parameter. Site probe status and diagnostic fields now reflect missing endpoints, incorrect targets and lost queries. |
| 11. Dependencies | `npm ci` resolved the locked image tooling. `npm audit --omit=dev` reported zero vulnerabilities. SiteKit integrity uses the vendored source manifest. The provider projection matched its pinned AI SDK certification manifest. |
| 12–13. Tests and CI | Added output selection and SiteKit integrity regressions, redirect diagnostics and a browser keyboard regression. CI runs Python, generated WebMCP and comparison freshness checks. |
| 14–15. Docs and agent workflows | The README records the installer transport contract and generated WebMCP gate. Verified the content projections and runtime checks that support discoverable examples and bounded machine-facing results. |
| 16. Dead weight | Kept release evidence, sample bundles, owned fixtures and browser snapshots because the project's existing receipts and maintenance guides refer to them. |
| 17–18. Fix and verify | See the implementation commit and verification receipt below. |

## Verification receipt

- `FACTORIES_OUTPUT="$out" npm test` passed all 37 tests. `python3 -m unittest discover -s tests -p 'test_*.py'` passed all six tests.
- The `npm run` gates `factories:check`, `providers:check`, `guides:check`, `examples:check`, `examples:verify`, `workflows:check`, `workflows:verify`, `compare:check` and `howl:pages:check` passed. The CI's pinned provider-manifest sync check passed.
- `kujo run ./build.kujo -- --site-url https://kujolang.ai --output "$out"` passed. `npm run images:responsive -- "$out"` generated 1,230 variants in the preceding artifact. The final rebuild reused these variants after byte-for-byte comparison of all 410 unchanged image sources. The generated image contract passed for 573 rendered images.
- `bash scripts/verify-site-contract.sh "$out"` and `bash scripts/validate-generated-output.sh "$out"` passed. The latter checked 339 HTML files.
- `node scripts/test-webmcp-runtime.js "$out/assets/js/kujo-webmcp.min.js" "$out/.well-known/kujo-site-index.json"` passed. `python3 scripts/verify-comparisons.py --output "$out"` passed for eight routes and 357 internal links.
- `node scripts/verify-positioning.mjs "$out"`, `node scripts/verify-social-cards.mjs "$out"`, `FACTORIES_OUTPUT="$out" node --test tests/factories.test.mjs`, and `python3 scripts/verify-language-site.py` passed. The social verifier covered 333 shareable routes. The language verifier was run from a scratch directory pointing to the final output and source example catalog.
- `node scripts/test-positioning-browser.cjs` passed against the final artifact served on loopback, including provider fallback with JavaScript disabled, a failed provider fetch, immediate modal focus, backward tab, Escape and focus restoration.
- `node --check` passed for the emitted `site.js` and `providers.js`. `bash -n public/install.sh`, byte comparisons of canonical, mirrored and emitted installers, `npm audit --omit=dev` and `git diff --check` passed.

The first overlapping baseline artifact check produced missing-file errors during an output rebuild. It was discarded as a comparison. The final production build and artifact checks ran without competing writes. Browser verification covers the positioning and provider-dialog suite on local Chrome. Broader browser visual and performance suites were outside the verified surface.

## Cross-repository follow-up

Coordinate SITE-06 with the canonical SSG implementation and keep the website installer byte-identical to the reviewed Kujo copy when updating it.
