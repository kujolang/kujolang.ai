# Comparison fact review — 2026-10-19

Verdict: corrected with explicit evidence limits. All eight pages were reviewed; this is not a certification of every runtime or deployment. The main correction concerns Kujo itself: a successful `kujo check` in 1.8.2 does not establish type correctness.

## Evidence and method

The before catalog and eight live-page hashes preserve release 21b8e66. `claim-ledger.csv` records content passages by exact catalog field, including tables, FAQs, examples and editorial trial criteria. It distinguishes source-backed explanations, documented product claims, recommendations and explicit unknowns. A paragraph can contain several related statements; the ledger is passage-level, not a count of independently executed claims. Source URLs and dates are evidence pointers, not proof that every runtime behavior was reproduced. `corrections.json` gives exact before/after fields. `source-receipts.json` records fetched source hashes. Raw source and live HTML snapshots are retained locally and excluded from Git.

The release matrix distinguishes stable tags, latest entries, reviewed source snapshots and executed runtimes. GitHub's `prerelease: false` is insufficient: BAML's latest entry contains `nightly` in its version. TypeScript's newest repository release is an editor extension, not the compiler. Both were excluded when selecting language releases. The web search cache showed obsolete Kujo 1.4.0 results; a fresh GitHub release API request established 1.8.2 instead.

## Corrections by impact

1. **P1 — Kujo type-enforcement overstatement.** A function declared `-> int` returning a string passed `kujo check` and VM execution with exit 0. Interpreter execution printed a return-type warning and exited 0. Invalid syntax failed with exit 3. The CLI source confirms that check parses/compiles and interpreter diagnostics are non-fatal. Shared facts, the hub, Bend comparison and verification/category guides now state the limit. This is a content correction, not a runtime repair. See `kujo-check-receipts.json` and the reproducible fixture below.
2. **P2 — BAML stable release omitted.** The stable language toolchain is [0.22.2, released October 13](https://github.com/BoundaryML/baml/releases/tag/baml-language-0.22.2). The October 19 release entry is `0.22.3-nightly.20261018.a`; it remains a nightly despite its API flag. Both source snapshots contain checker and test-runner implementations. Neither compiler was executed here. No speed, tracing-completeness or isolation guarantee is inferred.
3. **P2 — Bend release and source conflated.** Stable [2.0.37](https://github.com/bendlang/bend/releases/tag/v2.0.37) points to `4ff8545…`, while the reviewed guide is `64230dc…`. The page now names both separately. The latest main guide at `881cb2e…` is byte-identical to the reviewed guide. Laws, affine values, termination constraints, explicit IO and sequential JavaScript remain documented. The optional BendTT verdict excludes unsafe/foreign dependencies and trusts an unproven translation. The negative fixture was inspected, not executed.
4. **P2 — Agents SDK evidence was stale.** Updated the source reference from 1.1.2 to [1.1.3](https://github.com/kujolang/agents-sdk/releases/tag/v1.1.3). Added the documented cooperative cancellation/deadline boundary: the host and callbacks still own provider permissions, deadlines and persistence.
5. **P2 — Workcell isolation citation was too narrow.** The receipt module alone did not support the deployment claim. Added its pinned README and distinguished stable Docker/Podman execution from alpha provider-neutral/remote adapters, with host and daemon limits.
6. **P3 — Established-language versions were unspecified.** Recorded Python 3.15.0, TypeScript 7.0.2 and Rust 1.99.1 with official release dates. These remain alternatives for workload evaluation, not ranked competitors or tested migration targets. The exercise's installed Python version is separately recorded.

## Per-page outcome

| Page | Outcome | Remaining boundary |
|---|---|---|
| Compare hub | Corrected compiler-check label; shared facts and source versions refreshed | No cross-language performance result |
| Kujo vs Bend | Corrected Kujo check scope and release/source provenance | Bend fixture inspected, not executed; kernel translation remains a documented trust boundary |
| Kujo vs BAML | Added stable/nightly distinction and stable source inspection | Runtime, bridges, tracing and model calls not executed |
| Kujo vs Zero | Documentation claims rechecked; unknown identity retained | Official repository and numbered release remain unverified |
| AI-native programming languages | Corrected Kujo assurance language; refreshed alternative version evidence | Recommendations are workload-dependent judgments |
| Programming languages for AI agents | Updated SDK source and cooperative cancellation caveat | Offline/source evidence is not provider or deployment certification |
| AI code verification tools | Corrected static-check expectations and reran JSON examples | No claim that finite checks prove arbitrary code |
| Verify agent workflows | Reran published positive/negative exercise; retained pinned version | No agent or comparative benchmark was run |

## Reproduction

Kujo official 1.8.2 on macOS arm64; exact platform, Python version, runtime hash, commands, source/output hashes and outcomes are in `artifact-evidence.json`. The producer returned integer 42. The independent checker accepted it and rejected 41, string `"42"`, boolean, floating-point 42.0, missing field and malformed JSON. This verifies only those specified cases.

Additional local fixture:

```kujo
func wrong() -> int {
    return "wrong"
}
print(wrong())
```

Run the pinned binary with `check FILE`, `run FILE`, and `run FILE --interpreter`. The recorded results are exit 0, exit 0, and warning plus exit 0. These are observations, not a general statement that all type errors are ignored. The source is [Kujo 1.8.2 CLI](https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/main.rs#L1657).

Competitor runtimes were not downloaded or executed. The local disk had only 160–237 MiB available during research; source inspection and release checks were feasible, but installing additional toolchains safely was not. No competitor fixture is labeled passed. Zero's unidentified release is an additional reproducibility blocker.

## Fairness and unresolved questions

- **High impact for adopters:** determine which Kujo checks must fail a release gate. Do not use exit 0 from `kujo check` as a complete type-safety claim. Content now makes this explicit; any runtime policy change belongs in Kujo's repository.
- **Medium:** establish Zero's canonical compiler repository, numbered build and release policy from its publisher before a production dependency decision. Missing evidence is not proof of missing capability.
- **Medium:** execute Bend proof controls and BAML stable checker/test/bridge cases on an isolated pinned toolchain before strengthening documentation-only conclusions. No comparative benchmark is justified by this review.
- **Deployment-specific:** Workcell boundaries and SDK provider deadlines require actual host/provider tests. A documented interface or offline fixture cannot certify those environments.

No winner was assigned. Bend's proof model, BAML's typed AI/application integration, Zero's documented systems model and established-language integration costs remain distinct choices.

## Search, presentation and maintenance

This is a factual follow-up to `seo-audit/comparison-quality/2026-10-19`, not a new ranking audit. Preserve canonicals, metadata, visible-content schema parity, Markdown parity, Departure Mono headings, the eyebrow-free heroes and the header without Compare. Howl cards carry no affected version/type-enforcement claims, so their copy and JPEGs do not require replacement. Validate the existing cards and output contracts after regeneration.

Rankings, indexing, traffic, AI citations, field Core Web Vitals and search-console outcomes: **NOT AVAILABLE — DATA ACCESS REQUIRED**. Crawl access is not evidence of indexing. Official guidance remains [Google AI features](https://developers.google.com/search/docs/appearance/ai-features); no special AI ranking guarantee is added.

Recheck on language/tool releases, documentation-generation changes, new bridges or proof-boundary changes; otherwise review quarterly. Watch the official release URLs in `version-matrix.csv`. Resolve tags to commits, reject nightly/preview/editor-extension tags when selecting a stable language, record source and runtime separately, rerun negative controls, review every affected catalog reference, regenerate, run contracts and verify live output. Do not automatically refresh review dates or create schedules.

Verification and publication receipts are recorded in `verification.json` after completion.
