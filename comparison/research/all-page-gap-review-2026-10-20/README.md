# All-page testable-gap review — 2026-10-20

Reviewed the comparison hub, three direct comparisons and four guides. `page-review.json` maps each page to its evidence and remaining limits. `text-inventory.json` inventories catalog strings, not independent factual claims. Earlier reviews remain historical evidence; the findings below extend their coverage rather than replacing their original outcomes.

## New executed evidence

| Claim | Execution and control | Result and limit |
| --- | --- | --- |
| Spec validates task records | Valid JSON contract; same shape missing required goal | Accepted valid record; rejected missing goal with exit 1. Does not assess whether requirements are sufficient. |
| Eval checks selected output values | JSON total 42; expected 42 versus expected 41 | Exit 0/pass and exit 1/fail. This is Eval's own checker, separate from the public Python exercise. |
| Fence checks imports | Pinned upstream contract suite | 317 assertions passed. No general security or runtime correctness claim. |
| RunLedger records supplied results | Pinned unit and CLI suites | 81 unit assertions and CLI controls passed, including manually recorded command/test results. It remains a receipt store, not an independent judge. |
| ShipCheck checks release signals | Upstream CLI suite; repository with a deliberately failing test | CLI suite passed. Gate passed with warnings when tests were present; executing the fixture test separately exited 7. Presence does not mean execution or success. |
| Agents SDK has cooperative run controls | Budget and basic-runner suites | 6 budget and 32 runner tests passed, including cancellation, timeout, retries and approval denial with offline callbacks. No preemption or live-provider guarantee. |
| Dispatch persists workflow state | Offline demo and resume of completed run | Nine steps completed with state/trace/report paths; resume recognized the completed run. This does not test interruption after an external side effect. |
| Watchdog records proxy activity | Upstream loopback stub suite | Passed passthrough/override and recorded-telemetry checks. No hosted provider or cloud delivery claim. |
| Workcell executes containers and verifies retained evidence | Linux Docker, Kujo 1.6.0, pinned Workcell source | Expected artifact exported; intact receipt accepted; changed log rejected with exit 8; failed workload returned 7; source repo unchanged. Separate local offline receipt/recovery suites passed 7 and 25 assertions on Kujo 1.8.2. This does not certify all 1.8.2 compatibility, Podman, remote adapters or host/daemon security. |
| Public exercise rejects process failure and wrong runtime | Valid producer; producer printing correct JSON then exiting 7; Kujo 1.8.0 | Positive passed; failed process and wrong runtime rejected. Existing wrong-value/malformed/type controls also passed. |
| Zerolang executes both independent merged edits | Extended pinned 0.3.4 review | 55 command observations. Main printed the changed text; a generated test executed merged subtraction and accepted 40 − 2 = 38. This closes the earlier projection-only arithmetic limitation. |
| BAML's newer nightly handles the known Python boundary | 32 existing isolated cases on CLI 0.22.3-nightly.20261019.a / bridge 0.22.3.dev2026101900 | Exit and stdout outcomes exactly matched the previous nightly. Invalid integer arithmetic still exited with SIGSEGV (-11). No debugger/security analysis added. Issue #5332 was open when checked. |

[Workcell Linux run](https://github.com/kujolang/kujolang.ai/actions/runs/39453238913) succeeded. Artifact ID: 12279750271. The checked stable releases remained unchanged across 15 GitHub projects; Python 3.15.0 was separately checked against its official release page. All 45 existing source URLs were fetched successfully. The newer BAML nightly was treated as nightly despite its release metadata, not as a replacement stable release.

## Reproduction and provenance

`provenance.json` pins all nine ecosystem source commits and records the local runtime hash. Extract those commits into separate temporary checkouts before replaying the command arrays in `receipts/`. `$WORKSPACE` denotes the original workspace root. Upstream tests and examples are used unchanged; their commit pins identify their exact contents. Install the Kujo runtime named by each record. The local ecosystem tests used Kujo 1.8.2, not an inferred claim that every tool release supports every newer runtime.

Copy the small Spec/Eval inputs from `fixtures/` into the corresponding temporary source roots. The ShipCheck CLI suite expects a Git repository; initialize the extracted source checkout before running it. The first attempt lacked `.git` and failed; the corrected attempt passed. This was test setup, not a product defect. The supplemental ShipCheck fixture needs README, VERSION, CHANGELOG and a tests directory in an initialized Git repository; its test body is retained.

`zero-extended.py --binary /path/to/zero --output /tmp/zero-evidence` reproduces the extended Zerolang run with fresh temporary projects. For BAML use the prior review's `main.baml`, `baml.toml` and `run-probes.py`, generate the Python client with the new CLI, and use the exact bridge and dependency versions in `baml-nightly/provenance.json`. The release archive was checked against its published SHA-256 file. Probes isolate each call in its own process.

`workcell-live.py` is driven by `.github/workflows/comparison-workcell.yml`, with immutable Workcell and runtime-action pins. It uses the documented 1.6.0 runtime and a digest-pinned base image. The local Docker availability probe timed out; live container testing was therefore moved to Linux CI. No skipped local probe is counted as a pass.

Run `python3 verify-evidence.py` to validate retained outcomes and hashes. This verifies receipts, not fresh execution. Publication checks and deployment are recorded separately in the closeout.

## Remaining boundaries

- Bend GPU execution needs suitable GPU hardware and tooling; parallel speedup needs a defined benchmark and repeated measurements. No speed ranking is published.
- Hosted BAML model responses, cloud trace delivery, other bridges and other operating systems are not established by the Python/mock-provider tests. The known crash remains unresolved upstream.
- Zerolang concurrent writers, power-loss recovery, complex multi-file merges and additional targets remain untested. No corresponding production-readiness guarantee is published.
- Workcell Podman/remote-provider certification and deployment security need their own environments and review. Docker execution evidence is narrower.
- Direct Kujo–Bend/BAML adapters are hypothetical composition suggestions, not shipped integrations. Python/TypeScript/Rust are documented alternatives, not benchmarked candidates.
- Universal correctness, absence of a proof system, market leadership, agent productivity and every possible input cannot be established by these finite fixtures. Unknown remains unknown.
- Guide trial checklists are proposed application tests, not assertions that every named tool already enforces them. In particular, interrupted external effects need application-specific reconciliation tests.

No new upstream issue was posted. Existing BAML and Kujo type-check findings already cover the unresolved defects; no duplicate SignalBox capture is warranted. An older RunLedger skill incorrectly described command/test fields as reserved; the pinned source and passing CLI tests take precedence, and the published claim was retained.
