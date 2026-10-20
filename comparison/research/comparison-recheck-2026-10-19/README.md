# All-page comparison fact recheck — 2026-10-19

Scope: the comparison hub, Bend, BAML, Vercel Zerolang and all four populated guides. This pass checks published claims, references, release selection and consistency with the existing runtime evidence. It is not a full upstream source/security audit, a new cross-platform runtime campaign or a benchmark.

## What changed

- The hub's BAML execution cell described client, packaging and mock-provider tests but cited the static-diagnostics dimension. A dedicated execution dimension now points to the actual runtime receipts.
- Shared BAML limitations prose referred to “the table below,” although the hub does not render that table. It now points to the dedicated Python boundary review. The hub's proposed trial distinguishes BAML source checks from dynamic host input validation.
- Bend's guide and BAML's check/test references now use the releases that were executed. Bend's guide and BAML's test runner were byte-identical to the previous snapshots. BAML's later check-command snapshot had changed handling of internal lowering errors; it must not stand in for 0.22.2 behavior.
- The workflow exercise's exact integer checks, version check and hashes now cite its actual Python runner rather than Eval or other workflow tools. The verification-tools guide also links that checker. The exercise was rerun: producer and positive check passed, and every specified wrong-value/malformed/wrong-type control was rejected.
- The AI-native and agent-host guides link the BAML boundary findings. The host guide now states that Workcell 1.2.0 documents its own Kujo 1.6.0 runtime pin. The website's Kujo 1.8.2 baseline does not establish compatibility for every separately versioned tool.
- Rolling BAML website sources no longer display an unrelated repository commit as their version. The initial data-availability document now identifies itself as historical and links here; its earlier unverified-Zero and unexecuted-runtime observations are superseded, not silently erased.

## Versions and evidence

`versions.json` records 16 projects/languages, their stable release and source. The checked stable releases still match the comparison: Kujo 1.8.2, Bend 2.0.37, BAML language 0.22.2, Vercel Zerolang 0.3.4, Python 3.15.0, TypeScript 7.0.2 and Rust 1.99.1; the nine cited Kujo tools retain their recorded versions.

Do not select BAML stable releases using GitHub's `prerelease` flag alone: `baml-language-0.22.3-nightly.20261018.a` is explicitly a nightly tag despite `prerelease=false`. The first automatic selection in this pass exposed that mismatch; `versions.json` uses the explicitly numbered stable language channel instead. The nightly runtime was not tested. TypeScript's separate `vscode-typescript` releases are also excluded from the language version.

Forty existing source URLs were fetched successfully; `source-checks.json` retains URLs and response/content hashes. `additional-source-checks.json` records three release-aligned source files and the official Python release page. Large response bodies remain in the local research cache, not in the generated site. `catalog-before.json` preserves the starting content; `text-inventory.json` identifies 1,047 post-edit catalog string fields. This is an inventory, not 1,047 independent tests or automated truth verdicts. `page-review.json` records the fact groups and disposition for every page.

The source review covered Spec schema checks, Eval selected assertions, RunLedger supplied outcomes, ShipCheck's test-presence checks, Fence import rules, Agents SDK cooperative limits, Dispatch recovery and Workcell/Watchdog execution versus telemetry. Recommendations and suggested trial cases remain labeled as editorial proposals. No claim of comparative performance, universal proof, market leadership or production isolation was added.

All three retained runtime-evidence verifiers passed again. Those commands validate recorded outcomes and hashes; they do not rerun the competitor runtimes. The newly executed public artifact exercise is recorded separately in `artifact-rerun.json`. Earlier environment failures remain historical evidence rather than competitor defects.

## Remaining limits

The BAML 0.22.2 Python integer-arithmetic SIGSEGV remains unresolved, with the previously captured sandboxed and unsandboxed controls. No new crash root cause, exploitability or cross-platform claim was established. Bend GPU execution, measured parallel speedup, hosted model calls, cloud tracing, full upstream suites, and Zerolang's documented automatic-refresh/conflict paths remain outside executed coverage. The comparison continues to state those limits.

The prior SignalBox crash and Kujo type-check findings already cover the open issues; this pass produced no additional unresolved finding that warrants another capture.

## Evidence map

- [Original runtime review](../runtime-review-2026-10-19/README.md)
- [Bend kernel and BAML integration follow-up](../runtime-gap-review-2026-10-19/README.md)
- [BAML Python boundary tests](../baml-python-boundary-2026-10-19/README.md)
- [Official BAML stable release](https://github.com/BoundaryML/baml/releases/tag/baml-language-0.22.2)
- [Official Python 3.15.0 release](https://www.python.org/downloads/release/python-3150/)

Publication verification is recorded in the closeout after deployment.
