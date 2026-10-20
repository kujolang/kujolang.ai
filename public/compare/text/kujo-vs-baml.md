# Kujo vs BAML: comparing agent development workflows

Current BAML is a language for agents, with its own runtime and bridges into other languages. Kujo is also a programming language, with separate tools for defining tasks, checking outputs and recording runs. Compare them on the same application requirement, including the work needed to integrate and maintain each option.

Last reviewed: 2026-10-19. Canonical page: https://kujolang.ai/compare/kujo-vs-baml/

## At a glance

BAML: https://boundaryml.com/

Documentation: https://boundaryml.com/quickstart

Version: Stable language toolchain and Python bridge 0.22.2 (toolchain released 2026-10-13; commit 01f5c412c73c213846ea8cb6ead89d303b053672). Runtime and generated Python client tested on macOS x86_64. The nightly channel was not tested.

Repository: https://github.com/BoundaryML/baml

## Capability matrix

### Primary purpose

Kujo — Verified supported (language and first-party ecosystem): Kujo provides a language and separate tools for defining agent tasks, checking results and keeping run evidence.

Sources: https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/main.rs, https://github.com/kujolang/spec/blob/1211f37a09314be7150734bf15a55e9b2ea6504d/src/validate.kujo, https://github.com/kujolang/eval/blob/71e66dff780d6930bcbe093c046bf31aa26411df/src/checks.kujo

BAML — Partially supported (language and toolchain): An agent-oriented language with AI functions and incremental host-language adoption.

Sources: https://boundaryml.com/

### Static diagnostics

Kujo — Verified supported (language and first-party ecosystem): In Kujo 1.8.2, `kujo check` parses and compiles without executing; it is not a complete type-enforcement gate. Interpreter type diagnostics can be warnings. Spec validates task records, and Eval checks selected outputs; none proves arbitrary programs correct.

Sources: https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/main.rs, https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/type_checker.rs, https://github.com/kujolang/spec/blob/1211f37a09314be7150734bf15a55e9b2ea6504d/src/validate.kujo, https://github.com/kujolang/eval/blob/71e66dff780d6930bcbe093c046bf31aa26411df/src/checks.kujo

BAML — Verified supported (language): Project diagnostics are implemented by the current check command.

Sources: https://github.com/BoundaryML/baml/blob/648ad5ed10f543c129b51789c7d02e29b64f06f7/baml_language/crates/baml_cli/src/check_command.rs

### Testing and evaluations

Kujo — Verified supported (language and first-party ecosystem): In Kujo 1.8.2, `kujo check` parses and compiles without executing; it is not a complete type-enforcement gate. Interpreter type diagnostics can be warnings. Spec validates task records, and Eval checks selected outputs; none proves arbitrary programs correct.

Sources: https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/main.rs, https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/type_checker.rs, https://github.com/kujolang/spec/blob/1211f37a09314be7150734bf15a55e9b2ea6504d/src/validate.kujo, https://github.com/kujolang/eval/blob/71e66dff780d6930bcbe093c046bf31aa26411df/src/checks.kujo

BAML — Verified supported (toolchain): Local assertions passed and failed as expected. Mock-provider response parsing accepted a valid object and rejected an invalid field; the full upstream suite was not run.

Sources: https://github.com/BoundaryML/baml/blob/648ad5ed10f543c129b51789c7d02e29b64f06f7/baml_language/crates/baml_cli/src/test_command.rs, https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/runtime-review-2026-10-19, https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/runtime-gap-review-2026-10-19

### Formal proof

Kujo — Unknown / not verified (language): We did not establish a general dependent-type proof system in Kujo. The phrase “proves it works” should not be read as mathematical verification of arbitrary code.

Sources: https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/type_checker.rs

BAML — Unknown / not verified (language): A general dependent-type proof guarantee was not verified in the reviewed sources.

Sources: https://github.com/BoundaryML/baml/blob/648ad5ed10f543c129b51789c7d02e29b64f06f7/baml_language/crates/baml_cli/src/check_command.rs

### Observability

Kujo — Verified supported (first-party ecosystem): RunLedger stores supplied verdicts, commands and tests with Git metadata. Workcell records execution receipts. Follow these records to the underlying checks; a receipt or correlation ID alone does not prove the result correct.

Sources: https://github.com/kujolang/runledger/blob/334ddd4d33c8cb2612c8edab971ee69170824133/src/record.kujo, https://github.com/kujolang/workcell/blob/a276a92c6bac9279a8cb36ace9687ade34d5128f/src/receipts/receipt.kujo

BAML — Partially supported (toolchain): Local BTEL recordings and SQL queries recovered success/error outcomes and profiler counts. Trace context reached a generated-client call without leaking into the next call. Cloud delivery and overhead remain untested.

Sources: https://boundaryml.com/, https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/runtime-gap-review-2026-10-19

## Technical deep dive

Compare BAML’s AI application tools with Kujo’s workflow checks and records.

Are you adopting an AI component, or governing an entire agent change?

### Language and compiler: Check the generation you are adopting

The pinned BAML source includes compiler diagnostics and a check command. Its current positioning includes an agent language and standalone runtime, so older prompt-DSL examples are not sufficient evidence for the current toolchain.

Evaluation implication: Pin the source or release before choosing syntax, examples and integration assumptions.

Sources: https://boundaryml.com/, https://github.com/BoundaryML/baml/blob/648ad5ed10f543c129b51789c7d02e29b64f06f7/baml_language/crates/baml_cli/src/check_command.rs

### Tests and outputs: A valid data type can still contain the wrong answer

The inspected test command loads and runs compiled test sets. Our 0.22.2 fixture passed one assertion and failed a deliberately wrong expectation. This exercises a local test set, not the repository’s full suite. A typed or parsed AI response still needs checks for factual and domain correctness.

Evaluation implication: Pair type/shape checks with an independent domain-specific check and known wrong answers.

Sources: https://github.com/BoundaryML/baml/blob/648ad5ed10f543c129b51789c7d02e29b64f06f7/baml_language/crates/baml_cli/src/test_command.rs, https://github.com/BoundaryML/baml/blob/648ad5ed10f543c129b51789c7d02e29b64f06f7/baml_language/crates/baml_cli/src/check_command.rs, https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/runtime-review-2026-10-19

### Integration and tracing: Verify the host boundary independently

The Python bridge passed synchronous and asynchronous calls and propagated a declared error. Trace context stayed within its invocation, and CLI recordings exposed success/error outcomes through local SQL queries. Host type hints did not reject a string passed to an int identity function. Cloud delivery, tracing overhead and a direct Kujo bridge remain untested.

Evaluation implication: Test the exact host language, supported boundary types, failure propagation and retained trace data.

Sources: https://boundaryml.com/quickstart, https://boundaryml.com/, https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/runtime-gap-review-2026-10-19

## Decision scenarios

Proposed evaluation criteria, not comparative benchmark results.

### One AI feature in an existing app

Kujo: Use external acceptance checks around the application output.

BAML: Evaluate typed AI functions and the documented host bridge.

Evidence to collect: A pinned host/runtime pair plus valid and invalid response fixtures.

### A generated answer must be correct

Kujo: Specify domain criteria and evaluate the actual artifact.

BAML: Use language diagnostics and tests, then validate answer semantics.

Evidence to collect: An independent check that rejects a well-typed but wrong answer.

### An agent changes code across a repo

Kujo: Compose task, evaluation and run-record tooling.

BAML: Retain application test and trace results for review.

Evidence to collect: Commands, versions, failures and evidence tied to the actual revision.

## A focused evaluation plan

Proposed steps; no competitor runtime test is claimed.

### Pin the integration

Choose one AI function and the exact host language/runtime versions. Check the current quickstart against the pinned source; do not mix generations of examples.

### Separate failure classes

Prepare malformed data, well-shaped but incorrect data, and a valid answer. Use the first to challenge representation checks and the second to challenge domain assertions.

### Exercise the host boundary

Test exceptions, timeouts and boundary types in your own application. A documented bridge is not evidence that every required type or failure mode works for your chosen combination.

### Retain the evidence

Store check/test output and the domain-specific check result with the code revision. Measure latency or token cost only with a declared model, configuration and repeated-run method.

## Technical architecture

The BAML source we reviewed contains a compiler, a check command that collects project diagnostics and a test command that runs compiled test sets. Its current website describes typed AI functions, concurrency and tracing. These claims do not establish a speed advantage over Kujo. Kujo handles language execution in its runtime and provides task contracts and run records through separately versioned tools.

## When to choose Kujo

Consider Kujo when you need explicit acceptance criteria, checks of files and processes, and run evidence you can inspect without a hosted dashboard. Include the cost of configuring and maintaining those tools. A ledger entry marked pass should link to the check output that supports it.

## When to choose BAML

Consider BAML when you need typed AI functions within an existing application. Its quickstart and language bridges offer a starting point for adding one component at a time. Before choosing a bridge, check the supported host language, runtime version and data types.

## Can you use both?

You could connect BAML application code to Kujo workflow tools through a process or service interface. We did not test a direct Kujo bridge, and support for another host language does not imply Kujo support. Define a versioned request/response format and test how failures cross the interface.

## Honest limitations

Current BAML material and older structured-output DSL tutorials may describe different generations. Choose a release or source commit before copying examples. Kujo’s separate tools also need configuration and vary in maturity. Type checking and successful parsing constrain data structure; they do not show that an AI answer is true or meets a business requirement. In the tested 0.22.2 CLI, Python client setup uses generate add python/pydantic2 followed by generate; do not substitute a command from a newer quickstart without checking the installed help. The generated Python bridge returned a string passed to an int identity function in our fixture. Do not assume generated type hints enforce every host argument at runtime; validate the boundary separately.

## Examples and benchmark evidence

BAML 0.22.2 passed local function and assertion tests and rejected invalid source. Its generated Python client returned 42 synchronously and asynchronously; a standalone packed executable also returned 42. A local mock provider returned a typed object, while an invalid field and HTTP 401 produced distinct errors. Local trace queries recovered successful and failed runs with matching profiler counts. These fixtures do not test hosted models, cloud trace delivery, model quality or performance.

## Frequently asked questions

### Is BAML just an LLM wrapper?

That description does not match the current project. The reviewed repository contains language checking and execution tooling; verify which generation of BAML a tutorial targets.

### Does typed output prove an AI answer is right?

No. Type checks and structured parsing constrain representation. Domain correctness needs assertions, reference data or another suitable validation method.

## References

- [BAML current language overview](https://boundaryml.com/) — product assertions; not independently benchmarked; 648ad5ed10f543c129b51789c7d02e29b64f06f7; reviewed 2026-10-19.
- [BAML check command](https://github.com/BoundaryML/baml/blob/648ad5ed10f543c129b51789c7d02e29b64f06f7/baml_language/crates/baml_cli/src/check_command.rs) — implementation inspected; 648ad5ed10f543c129b51789c7d02e29b64f06f7; reviewed 2026-10-19.
- [BAML test runner and result tests](https://github.com/BoundaryML/baml/blob/648ad5ed10f543c129b51789c7d02e29b64f06f7/baml_language/crates/baml_cli/src/test_command.rs) — implementation and tests inspected; not executed; 648ad5ed10f543c129b51789c7d02e29b64f06f7; reviewed 2026-10-19.
- [BAML quickstart](https://boundaryml.com/quickstart) — official documentation; Documentation snapshot; no release version asserted; reviewed 2026-10-19.
- [Kujo runtime and CLI source](https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/main.rs) — implementation inspected; Kujo 1.8.2 source snapshot; reviewed 2026-10-19.
- [Kujo type checker](https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/type_checker.rs) — implementation inspected; 549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1; reviewed 2026-10-19.
- [Spec scope and implementation](https://github.com/kujolang/spec/blob/1211f37a09314be7150734bf15a55e9b2ea6504d/src/validate.kujo) — implementation inspected; 1211f37a09314be7150734bf15a55e9b2ea6504d; reviewed 2026-10-19.
- [Eval scope and implementation](https://github.com/kujolang/eval/blob/71e66dff780d6930bcbe093c046bf31aa26411df/src/checks.kujo) — implementation inspected; 71e66dff780d6930bcbe093c046bf31aa26411df; reviewed 2026-10-19.
- [Runledger scope and implementation](https://github.com/kujolang/runledger/blob/334ddd4d33c8cb2612c8edab971ee69170824133/src/record.kujo) — implementation inspected; 334ddd4d33c8cb2612c8edab971ee69170824133; reviewed 2026-10-19.
- [BAML stable language toolchain](https://github.com/BoundaryML/baml/releases/tag/baml-language-0.22.2) — official release metadata; 0.22.2; released 2026-10-13; reviewed 2026-10-19.
- [Kujo stable release](https://github.com/kujolang/kujo/releases/tag/v1.8.2) — official release metadata; 1.8.2; released 2026-10-19; reviewed 2026-10-19.
- [Competitor runtime fixtures and raw outcomes](https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/runtime-review-2026-10-19) — local execution receipts; bounded fixtures; Bend 2.0.37; BAML 0.22.2; Zerolang 0.3.4; macOS x86_64; reviewed 2026-10-19.
- [Bend kernel and BAML integration runtime tests](https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/runtime-gap-review-2026-10-19) — release binaries executed; positive and negative fixtures; local mock provider; Bend 2.0.37 with Lean 4.34.0 on Linux x86_64; BAML and Python bridge 0.22.2 on macOS x86_64; reviewed 2026-10-19.

## Related pages

- [AI-native programming languages: a practical comparison](https://kujolang.ai/compare/ai-native-programming-languages/)
- [AI code verification tools: what each check can establish](https://kujolang.ai/compare/ai-code-verification-tools/)
- [Verify agent workflows: contracts, checks and reproducible evidence](https://kujolang.ai/compare/verify-agent-workflows/)

[Editorial policy](https://kujolang.ai/compare/editorial-policy.md) · [Report inaccuracies](https://github.com/kujolang/kujolang.ai/issues/new)
