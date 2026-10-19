# Implementation inventory — 2026-10-19

Scope: source-level inventory, not ecosystem certification. Runtime exercise and website builds are the only executed results claimed by the launch report. All listed tools are separate first-party projects unless explicitly identified as the core language.

## kujo
Language runtime, compiler and type checker. Optional backend support varies; no universal proof guarantee established.

Commit: `acb9107dc38de699c540f5b78d924257def0b95e`. Source-level review; full project suites not rerun.

- [src/main.rs](https://github.com/kujolang/kujo/blob/acb9107dc38de699c540f5b78d924257def0b95e/src/main.rs)
- [src/type_checker.rs](https://github.com/kujolang/kujo/blob/acb9107dc38de699c540f5b78d924257def0b95e/src/type_checker.rs)

## spec
Task schema and acceptance-contract validation. Schema validity is not implementation correctness.

Commit: `1211f37a09314be7150734bf15a55e9b2ea6504d`. Source-level review; full project suites not rerun.

- [src/validate.kujo](https://github.com/kujolang/spec/blob/1211f37a09314be7150734bf15a55e9b2ea6504d/src/validate.kujo)
- [tests/run_tests.sh](https://github.com/kujolang/spec/blob/1211f37a09314be7150734bf15a55e9b2ea6504d/tests/run_tests.sh)

## eval
Outcome checks against commands, files and structured data. Coverage depends on configured assertions; command checks are not a sandbox.

Commit: `71e66dff780d6930bcbe093c046bf31aa26411df`. Source-level review; full project suites not rerun.

- [src/checks.kujo](https://github.com/kujolang/eval/blob/71e66dff780d6930bcbe093c046bf31aa26411df/src/checks.kujo)
- [tests/contract_tests.kujo](https://github.com/kujolang/eval/blob/71e66dff780d6930bcbe093c046bf31aa26411df/tests/contract_tests.kujo)

## dispatch
Workflow routing, persisted run state and approval boundaries. Experimental assurance and participant surfaces are opt-in; correlation is not replay permission.

Commit: `71ca927c65598ecfe7c1816068e047cf50b915e0`. Source-level review; full project suites not rerun.

- [dispatch.kujo](https://github.com/kujolang/dispatch/blob/71ca927c65598ecfe7c1816068e047cf50b915e0/dispatch.kujo)
- [tests/graph_attempt_contract_tests.kujo](https://github.com/kujolang/dispatch/blob/71ca927c65598ecfe7c1816068e047cf50b915e0/tests/graph_attempt_contract_tests.kujo)

## workcell
Bounded execution definitions and structured receipts. Isolation depends on configured container/backend; offline conformance is not provider certification.

Commit: `a276a92c6bac9279a8cb36ace9687ade34d5128f`. Source-level review; full project suites not rerun.

- [src/receipts/receipt.kujo](https://github.com/kujolang/workcell/blob/a276a92c6bac9279a8cb36ace9687ade34d5128f/src/receipts/receipt.kujo)
- [tests/workcell_test.kujo](https://github.com/kujolang/workcell/blob/a276a92c6bac9279a8cb36ace9687ade34d5128f/tests/workcell_test.kujo)

## runledger
Local run records, supplied verdicts and Git metadata. Does not independently run or judge all tests recorded by callers.

Commit: `334ddd4d33c8cb2612c8edab971ee69170824133`. Source-level review; full project suites not rerun.

- [src/record.kujo](https://github.com/kujolang/runledger/blob/334ddd4d33c8cb2612c8edab971ee69170824133/src/record.kujo)
- [tests/runledger_test.kujo](https://github.com/kujolang/runledger/blob/334ddd4d33c8cb2612c8edab971ee69170824133/tests/runledger_test.kujo)

## shipcheck
Repository release checks and blocking gate. Readiness signals do not certify a release or prove tests passed.

Commit: `ee4cfd052c0522eebedc0eead223cbb22490b357`. Source-level review; full project suites not rerun.

- [src/checks.kujo](https://github.com/kujolang/shipcheck/blob/ee4cfd052c0522eebedc0eead223cbb22490b357/src/checks.kujo)
- [tests/cli-output-contract.sh](https://github.com/kujolang/shipcheck/blob/ee4cfd052c0522eebedc0eead223cbb22490b357/tests/cli-output-contract.sh)

## changebucket
Git change footprint counts and budgets. Counts are not semantic correctness or a universal risk score.

Commit: `030eea63c60449f82c9ba2680227485d318fdb6d`. Source-level review; full project suites not rerun.

- [src/analyze.kujo](https://github.com/kujolang/changebucket/blob/030eea63c60449f82c9ba2680227485d318fdb6d/src/analyze.kujo)
- [tests/changebucket_test.kujo](https://github.com/kujolang/changebucket/blob/030eea63c60449f82c9ba2680227485d318fdb6d/tests/changebucket_test.kujo)

## patchbrief
Diff summary and suggested tests. Heuristics and bounded diff inspection are not a code correctness review.

Commit: `34000d62d6dd7d2422e40faecf65120af1a138dc`. Source-level review; full project suites not rerun.

- [src/summarize.kujo](https://github.com/kujolang/patchbrief/blob/34000d62d6dd7d2422e40faecf65120af1a138dc/src/summarize.kujo)
- [tests/patchbrief_tests.kujo](https://github.com/kujolang/patchbrief/blob/34000d62d6dd7d2422e40faecf65120af1a138dc/tests/patchbrief_tests.kujo)

## casefile
Local command/log debugging bundles. Capturing a failed command may itself return success; preserve child outcome.

Commit: `3d8da7d76445cb554fe193ea0d3a8b5a557962d7`. Source-level review; full project suites not rerun.

- [src/capture.kujo](https://github.com/kujolang/casefile/blob/3d8da7d76445cb554fe193ea0d3a8b5a557962d7/src/capture.kujo)
- [tests/casefile_cli_test_v2.kujo](https://github.com/kujolang/casefile/blob/3d8da7d76445cb554fe193ea0d3a8b5a557962d7/tests/casefile_cli_test_v2.kujo)

## fence
Configured import-boundary checks. Supported import parsing and configured zones limit coverage.

Commit: `d3173049b5365af975624fddd48e943d39738c75`. Source-level review; full project suites not rerun.

- [fence.kujo](https://github.com/kujolang/fence/blob/d3173049b5365af975624fddd48e943d39738c75/fence.kujo)
- [tests/fence_tests.kujo](https://github.com/kujolang/fence/blob/d3173049b5365af975624fddd48e943d39738c75/tests/fence_tests.kujo)

## leash
Mobile supervision with policy and agent adapters. Mixed Rust/Kujo/Kotlin implementation; no phone/device integration tested here.

Commit: `56c59c90b81433482683e72a411748ca82a61b24`. Source-level review; full project suites not rerun.

- [policy/leash.policy.kujo](https://github.com/kujolang/leash/blob/56c59c90b81433482683e72a411748ca82a61b24/policy/leash.policy.kujo)
- [policy/test_runner.kujo](https://github.com/kujolang/leash/blob/56c59c90b81433482683e72a411748ca82a61b24/policy/test_runner.kujo)

## watchdog
Local request telemetry and proxy integration. Telemetry is not authorization; costs are estimates, not invoices.

Commit: `ad6fbc287c626539c1b3a69b4d3d31528b70edaa`. Source-level review; full project suites not rerun.

- [telemetry_native_adapter.kujo](https://github.com/kujolang/watchdog/blob/ad6fbc287c626539c1b3a69b4d3d31528b70edaa/telemetry_native_adapter.kujo)
- [tests/contract_manifest_check.js](https://github.com/kujolang/watchdog/blob/ad6fbc287c626539c1b3a69b4d3d31528b70edaa/tests/contract_manifest_check.js)

## mcp
MCP server scaffolding and guarded tools/resources. Remote auth, ingress and deployment limits require environment-specific review.

Commit: `90f264f55274a99e0ca0aba079e1c94fd024552d`. Source-level review; full project suites not rerun.

- [server.kujo](https://github.com/kujolang/mcp/blob/90f264f55274a99e0ca0aba079e1c94fd024552d/server.kujo)
- [tests/test_01_permission_checks.kujo](https://github.com/kujolang/mcp/blob/90f264f55274a99e0ca0aba079e1c94fd024552d/tests/test_01_permission_checks.kujo)

## agents-sdk
Library-first agent workflow runtime primitives. Fixture checks do not certify live-provider behavior.

Commit: `5a9d5525e511a293b743b1c44d9ef270fd491f9f`. Source-level review; full project suites not rerun.

- [src/agents/runner.kujo](https://github.com/kujolang/agents-sdk/blob/5a9d5525e511a293b743b1c44d9ef270fd491f9f/src/agents/runner.kujo)
- [tests/runner_result_event_contract_tests.kujo](https://github.com/kujolang/agents-sdk/blob/5a9d5525e511a293b743b1c44d9ef270fd491f9f/tests/runner_result_event_contract_tests.kujo)

## ssg
Static content, templates, metadata and machine-readable index. Site vendors a customized SSG; preserve its local conventions.

Commit: `615bdb30abd3aba1b1fdc640e934931327c1e083`. Source-level review; full project suites not rerun.

- [build.kujo](https://github.com/kujolang/ssg/blob/615bdb30abd3aba1b1fdc640e934931327c1e083/build.kujo)
- [scripts/test-generated-contract.sh](https://github.com/kujolang/ssg/blob/615bdb30abd3aba1b1fdc640e934931327c1e083/scripts/test-generated-contract.sh)

## Website and SiteKit
Website baseline: kujolang/kujolang.ai db3f698cbb5eef73fe746bce3a8fee17e5250cfa. The customized build.kujo renders Markdown collections through templates, copies assets/public, generates sitemap.xml, robots.txt, RSS and llms.txt, and emits an experimental public WebMCP index. Templates use vendored SiteKit classes and tokens; no framework is added. The available SiteKit site is sitekit.kujolang.ai; the actual integration source of truth is the vendored assets/css/sitekit.css and assets/js/sitekit.js with SITEKIT-LICENSE.txt.

No analytics beacon was found in the reviewed layout, site JavaScript or builder. Search-console data and production edge logs were not available. No tracking provider or training-crawler policy was changed.

Existing educational coverage: this checkout contains no content/posts directory. Ecosystem pages already explain Spec, Eval, RunLedger, Workcell and related tools; those pages are linked and selectively cross-linked rather than duplicated. One new workflow guide consolidates the five educational themes.
