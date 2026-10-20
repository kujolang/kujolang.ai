# Competitor repository and runtime review — 2026-10-19

Scope: follow-up to the eight-page fact review, focused on Bend, BAML and Vercel Zerolang. This is a source-backed review with positive and negative execution fixtures, not an exhaustive compiler/security audit or a comparative benchmark. Raw attempts are retained, including fixture and environment failures.

## Identity and release baseline

| Project | Official repository | Tested published release | Source identity |
|---|---|---|---|
| Bend | https://github.com/bendlang/bend | 2.0.37 | release commit `4ff8545f19b09b7d2b8ca2303668100eac8efd66` |
| BAML | https://github.com/BoundaryML/baml | baml-language-0.22.2 | `01f5c412c73c213846ea8cb6ead89d303b053672` |
| Vercel Zerolang | https://github.com/vercel-labs/zerolang | 0.3.4 | `5b3a90a7756e48ab449eb16e688044b8decec7a9` |

Official release metadata was retrieved on the review date. BAML's 0.22.3 nightly was not treated as stable. Zerolang's inspected main commit `7e1a64d27cc37671df31c6370890bce86f5135e1` was not substituted for release behavior. zerolang.ai links the Vercel repository, and its installer names that repository. The earlier page's zero-lang.com preview is a different project; its C++/value-semantics claims do not apply to Vercel Zerolang. The route remains `/compare/kujo-vs-zero/` and now explicitly identifies the project.

## Environment and provenance

Actual host: macOS 26.6.2, **x86_64**. The earlier fact-review narrative incorrectly said arm64; its machine-readable runtime evidence had the correct architecture. Treat this as an explicit erratum, not a different test environment. An initial Bend arm64 download failed with `Bad CPU type` and was replaced with the x64 release before the reported tests.

Binaries came from official GitHub release assets. Receipts contain executable SHA-256 hashes. Bend x64 archive SHA-256: `93eea3f54b7b91f28ea15a1b9f2d825afa58c1fcd417c11024a62f8c3506b813`. BAML archive SHA-256: `a13b4c004ee011b334bfed31439ba8fb61278e4850b0277774328873deb47ddc`, verified against the publisher's checksum. A computed hash alone is not a publisher signature.

Commands ran without provider credentials, with a scrubbed environment and a macOS sandbox denying network access, user-file reads outside the fixture directory, and writes outside the fixture directory and temporary area. The sandbox belongs to this review harness; it does not establish isolation supplied by a competitor. Zerolang projection export was repeated in a dedicated `/private/tmp/zero-review-*` package because the original sandbox path inspection failed. That controlled retry passed.

## Observed outcomes

| Runtime | Positive cases | Negative cases | Limits |
|---|---|---|---|
| Bend 2.0.37 | Valid proof accepted by `--check-only`; arithmetic returned 42 via evaluator, generated JS/Node and native executable | Broken proof, wrong return type, affine double-use, unfilled law used as proof rejected | `--verdict` blocked: Lean 4.34.0 or built BENDTT kernel unavailable; GPU/parallel performance not tested |
| BAML 0.22.2 | Local typed function returned 42; one assertion passed; Python/Pydantic2 client generation completed | Wrong expected result exited 2; wrong return type and syntax error exited 4 | No provider calls, generated-client execution, tracing or model-quality assessment; packaging blocked by disk exhaustion |
| Zerolang 0.3.4 | Graph initialization/patch/run; one addition test; projection export and verification | Stale graph hash and Bool return in i32 function rejected with graph unchanged; wrong expectation failed test; edited projection failed verification | No cross-target, merge/conflict, concurrency, full standard-library or production-security assessment |

Zerolang `check` succeeded while a deliberately wrong behavioral assertion failed `test`. An earlier `test` command returned success with zero test blocks; that is not counted as behavioral coverage. The later receipt explicitly reports one passing test. Initial string-type patch input had invalid quoting and was only a parser rejection; the corrected Bool/i32 fixture produced TYP003 and preserved graph bytes. The two cases must not be conflated.

BAML raw `expected_exit: 1` entries meant an anticipated rejection, but the actual release uses 2 for test failures and 4 for compiler failures. These were successful negative checks, not exact-code matches. The internal `baml-cli` executable warns that the public launcher is preferred; this review used the official extracted internal binary. Its current release command is `generate add python/pydantic2`, then `generate`. We did not execute a generated Python bridge. Standalone packaging failed with `No space left on device`; the incomplete output's subsequent failure is not a BAML runtime defect or a packaging pass.

## Repository inspection

Previous pinned Bend guide/negative fixture and BAML check/test implementation inspection remains in `../fact-review-2026-10-19/`. This follow-up connects those claims to published runtime behavior without claiming a full test-suite run or source build.

Zerolang release-pinned source excerpts and documentation are retained in `zero-source/`. Reviewed:

- `program_graph_patch.c`: expected graph hash comparison, operation application, graph identity finalization, shape validation and failure paths.
- `program_graph_projection_validate.c`: source projection matching and cached semantic-verdict helpers.
- Graph architecture, compile path and projection documents: graph authority, text projection, explicit import/export, source refresh and conflict boundaries.

The docs describe automatic refresh when only projection text changes, conflict failure when both sides change, and `ZERO_STALE=fail`. Only export, matching projection and deliberate divergence were executed here. No general atomicity, thread-safety, theorem-proving or memory-safety conclusion follows from these fixtures. The byte comparison establishes preservation for the two rejected patch cases only.

## Reproduction and evidence

Use a disposable workspace on a supported machine. Download the pinned official release assets, verify publisher checksums where available, and inspect each runner before executing it. Scripts expect binaries under a sibling `bend/`, `baml/bin/`, or `zero` path and an isolated `home/`. Update the absolute fixture allowlist in `isolate.sb` to your workspace. Do not reuse another user's filesystem path.

Run the base review scripts, then the negative and completion scripts in order. The completion script moves a copy of the Zerolang package to a unique temporary directory for projection checks. Raw receipts preserve original attempts; use their observed `exit`, output, graph comparison and this interpretation rather than treating every initial expected value as an assertion. Initial Bend syntax corrections and sandbox Node-metadata retries remain recorded. No timing-based ranking is published.

`outcome-index.json` is a compact command/exit index. `*-receipts.json` contains stdout/stderr and identity evidence. `sha256.json` hashes the captured evidence files (before this report was added). The scripts and fixtures are research artifacts, not a newly supported cross-platform test framework.

## Content and verification scope

Updated the hub, three direct comparisons and AI-native discovery page; regenerated all eight routes' projections through the shared catalog. Preserved typography, hero wording/no eyebrows and the removed header link. The source links and FAQ now distinguish project identity, source inspection, executed fixtures and untested claims. Search ranking, traffic and AI citation measurements: **NOT AVAILABLE — DATA ACCESS REQUIRED**. Existing SEO baseline and earlier eight-card Howl review remain preserved; the changed Zerolang card is regenerated in this follow-up.

Website build/deployment/live receipts are recorded separately after validation. No claim of complete runtime coverage is made.

## Evidence self-check

Run `python3 verify-evidence.py` in this directory. It verifies 102 retained file hashes and 23 bounded outcome assertions (125 checks total). This checks the captured record, not a fresh runtime execution. The user subsequently confirmed Vercel Labs Zerolang as the intended competitor.

## Delivery corrections

The first complete build at `f75d24f` passed. Its Pages deployment initially returned HTTP 500; retrying only the failed deployment job succeeded. All eight live pages then matched the updated content, but Cloudflare still returned the old social-image bytes at the unchanged `kujo-vs-zero.jpg` URL. A versioned request returned the correct new bytes. Captured headers reported a cache HIT and `max-age=14400`; this was a delivery-cache difference, not an incorrect build artifact.

Commit `4dd5dc1` gives the card the fresh `kujo-vs-zerolang.jpg` URL, with matching Howl card ID and page metadata. The comparison route stays unchanged. The generator supports a validated optional `socialCard` ID; its new path-traversal rejection test brings the Node suite to 23 passing tests. Final live verification checks the exact new metadata asset URL without a cache-busting query. No cache settings or DNS policy were changed.

## Final verification

Website release `4dd5dc11c0c5343ddeabe349d5b7c44b6e0710bf` passed the fresh pinned Kujo 1.8.2 build, tests, site/HTML/comparison contracts and GitHub Pages deployment: https://github.com/kujolang/kujolang.ai/actions/runs/39344498247. Live verification at 2026-10-20T00:05:04.625584+00:00 passed all eight comparison routes and 48 unique URLs, exact Markdown parity, current social metadata and the exact new Zerolang image bytes. No cache-busting query was needed for the final image check. Local checks: 23 Node tests, four Python tests, 435 internal links, 255 social routes, 256 HTML files, eight mobile layouts and 125 evidence assertions/hash checks.

The host disk interrupted earlier full local asset copies, so the successful scoped preview served source assets separately and was checked against an immutable prior CI graph. Production CI independently built the full site. Runtime coverage limits above remain; website delivery has no unresolved blocker. SignalBox: no captures warranted for this completed follow-up.
