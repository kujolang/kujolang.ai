# Kujo vs BAML: comparing agent development workflows

Current BAML is presented as a language for agents, with a standalone runtime and bridges into other languages. Reducing it to a prompt wrapper would be misleading. Kujo is also a programming language; its separate ecosystem emphasizes explicit task contracts, evaluations and inspectable workflow records. Both deserve a trial on the same application requirement.

Last reviewed: 2026-10-19. Canonical page: https://kujolang.ai/compare/kujo-vs-baml/

## At a glance

BAML: https://boundaryml.com/

Documentation: https://boundaryml.com/quickstart

Version: Source 648ad5ed10f543c129b51789c7d02e29b64f06f7; release API observed baml-language-0.22.3-nightly.20261018.a (not runtime-tested)

Repository: https://github.com/BoundaryML/baml

## Capability matrix

### Primary purpose

Kujo — Verified supported (language and first-party ecosystem): A programming language plus separately versioned tools for explicit agent workflow contracts and inspectable outcomes.

Sources: https://github.com/kujolang/kujo/blob/acb9107dc38de699c540f5b78d924257def0b95e/src/main.rs, https://github.com/kujolang/spec/blob/1211f37a09314be7150734bf15a55e9b2ea6504d/src/validate.kujo, https://github.com/kujolang/eval/blob/71e66dff780d6930bcbe093c046bf31aa26411df/src/checks.kujo

BAML — Partially supported (language and toolchain): An agent-oriented language with AI functions and incremental host-language adoption.

Sources: https://boundaryml.com/

### Static diagnostics

Kujo — Verified supported (language and first-party ecosystem): Type checking in the runtime; task schema validation and outcome checks belong to Spec and Eval. Passing these checks is not a universal correctness proof.

Sources: https://github.com/kujolang/kujo/blob/acb9107dc38de699c540f5b78d924257def0b95e/src/type_checker.rs, https://github.com/kujolang/spec/blob/1211f37a09314be7150734bf15a55e9b2ea6504d/src/validate.kujo, https://github.com/kujolang/eval/blob/71e66dff780d6930bcbe093c046bf31aa26411df/src/checks.kujo

BAML — Verified supported (language): Project diagnostics are implemented by the current check command.

Sources: https://github.com/BoundaryML/baml/blob/648ad5ed10f543c129b51789c7d02e29b64f06f7/baml_language/crates/baml_cli/src/check_command.rs

### Testing and evaluations

Kujo — Verified supported (language and first-party ecosystem): Type checking in the runtime; task schema validation and outcome checks belong to Spec and Eval. Passing these checks is not a universal correctness proof.

Sources: https://github.com/kujolang/kujo/blob/acb9107dc38de699c540f5b78d924257def0b95e/src/type_checker.rs, https://github.com/kujolang/spec/blob/1211f37a09314be7150734bf15a55e9b2ea6504d/src/validate.kujo, https://github.com/kujolang/eval/blob/71e66dff780d6930bcbe093c046bf31aa26411df/src/checks.kujo

BAML — Verified supported (toolchain): A test runner and result parsing tests exist in the reviewed source. This review did not execute them.

Sources: https://github.com/BoundaryML/baml/blob/648ad5ed10f543c129b51789c7d02e29b64f06f7/baml_language/crates/baml_cli/src/test_command.rs

### Formal proof

Kujo — Unknown / not verified (language): A general dependent-type proof system was not established by this review. Do not interpret the positioning “proves it works” as mathematical verification of arbitrary code.

Sources: https://github.com/kujolang/kujo/blob/acb9107dc38de699c540f5b78d924257def0b95e/src/type_checker.rs

BAML — Unknown / not verified (language): A general dependent-type proof guarantee was not verified in the reviewed sources.

Sources: https://github.com/BoundaryML/baml/blob/648ad5ed10f543c129b51789c7d02e29b64f06f7/baml_language/crates/baml_cli/src/check_command.rs

### Observability

Kujo — Verified supported (first-party ecosystem): RunLedger stores supplied verdicts, commands and tests alongside Git metadata. Workcell defines execution receipts. Neither a receipt nor a correlation ID independently proves semantic correctness.

Sources: https://github.com/kujolang/runledger/blob/334ddd4d33c8cb2612c8edab971ee69170824133/src/record.kujo, https://github.com/kujolang/workcell/blob/a276a92c6bac9279a8cb36ace9687ade34d5128f/src/receipts/receipt.kujo

BAML — Partially supported (toolchain): The current website describes tracing and profiling. Completeness and overhead were not measured here.

Sources: https://boundaryml.com/

## Technical deep dive

Typed AI application code. Explicit workflow accountability.

Are you adopting an AI component, or governing an entire agent change?

### Language and compiler: Check the generation you are adopting

The pinned BAML source includes compiler diagnostics and a check command. Its current positioning includes an agent language and standalone runtime, so older prompt-DSL examples are not sufficient evidence for the current toolchain.

Evaluation implication: Pin the source or release before choosing syntax, examples and integration assumptions.

Sources: https://boundaryml.com/, https://github.com/BoundaryML/baml/blob/648ad5ed10f543c129b51789c7d02e29b64f06f7/baml_language/crates/baml_cli/src/check_command.rs

### Tests and outputs: Representation is one layer of correctness

The inspected test command loads and runs compiled test sets; result parsing tests are also present. A typed or parsed AI response can still contain the wrong domain answer. The source review establishes implementation presence, not successful execution of a local suite.

Evaluation implication: Pair type/shape checks with an independent domain oracle and known wrong answers.

Sources: https://github.com/BoundaryML/baml/blob/648ad5ed10f543c129b51789c7d02e29b64f06f7/baml_language/crates/baml_cli/src/test_command.rs, https://github.com/BoundaryML/baml/blob/648ad5ed10f543c129b51789c7d02e29b64f06f7/baml_language/crates/baml_cli/src/check_command.rs

### Integration and tracing: Verify the host boundary independently

The current quickstart presents incremental adoption and host-language bridges; the website describes tracing and profiling. This review did not measure their completeness or overhead, and did not verify a direct Kujo bridge.

Evaluation implication: Test the exact host language, supported boundary types, failure propagation and retained trace data.

Sources: https://boundaryml.com/quickstart, https://boundaryml.com/

## Decision scenarios

Proposed evaluation criteria, not comparative benchmark results.

### One AI feature in an existing app

Kujo: Use external acceptance checks around the application output.

BAML: Evaluate typed AI functions and the documented host bridge.

Evidence to collect: A pinned host/runtime pair plus valid and invalid response fixtures.

### A generated answer must be correct

Kujo: Specify domain criteria and evaluate the actual artifact.

BAML: Use language diagnostics and tests, then validate answer semantics.

Evidence to collect: A domain oracle that rejects a well-typed but wrong answer.

### An agent changes code across a repo

Kujo: Compose task, evaluation and run-record tooling.

BAML: Retain application test and trace results as inputs to review.

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

Store check/test output and the domain oracle result with the code revision. Measure latency or token cost only with a declared model, configuration and repeated-run method.

## Technical architecture

The reviewed BAML repository contains a language compiler, a check command that collects project diagnostics, and a test command that loads and runs compiled test sets. Its current site describes typed AI functions, concurrency and tracing. Those product assertions are not evidence of faster execution than Kujo. Kujo’s runtime owns language execution; its task contracts and run records live in separately versioned tools.

## When to choose Kujo

Consider Kujo when you want to assemble a local workflow around explicit acceptance criteria, file and process checks, and artifacts you can inspect outside a hosted dashboard. Evaluate the maintenance cost of that composition. A ledger entry saying pass must still link to the real check output.

## When to choose BAML

Consider BAML when typed AI functions and incremental integration into an existing application are the immediate need. Its current quickstart and bridge story are a useful starting point for teams adopting one component at a time. Check the exact host language, runtime version and supported boundary types before committing to an integration.

## Can you use both?

An external process or service interface could connect BAML application code to Kujo workflow tools. This review did not test a direct Kujo bridge. Do not assume that a bridge to another host language implies one exists for Kujo. Use a versioned request/response contract and test failures at the boundary.

## Honest limitations

BAML’s current website and its older structured-output DSL documentation can describe different generations. Pin a release or source commit before copying examples. Kujo’s surrounding tools require separate configuration and their maturity varies. Neither static types nor successful AI-output parsing establishes that a generated answer is factually correct or that a business requirement was met.

## Examples and benchmark evidence

No comparative latency, token-cost or reliability numbers are asserted. The BAML check and test implementations were read, including result parsing tests, but were not built here. The linked workflow exercise checks artifact contents with a pinned Kujo runtime; it is an evidence pattern, not a BAML performance comparison.

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
- [Kujo runtime and CLI source](https://github.com/kujolang/kujo/blob/acb9107dc38de699c540f5b78d924257def0b95e/src/main.rs) — implementation inspected; Kujo 1.8.1 source snapshot; reviewed 2026-10-19.
- [Kujo type checker](https://github.com/kujolang/kujo/blob/acb9107dc38de699c540f5b78d924257def0b95e/src/type_checker.rs) — implementation inspected; acb9107dc38de699c540f5b78d924257def0b95e; reviewed 2026-10-19.
- [Spec scope and implementation](https://github.com/kujolang/spec/blob/1211f37a09314be7150734bf15a55e9b2ea6504d/src/validate.kujo) — implementation inspected; 1211f37a09314be7150734bf15a55e9b2ea6504d; reviewed 2026-10-19.
- [Eval scope and implementation](https://github.com/kujolang/eval/blob/71e66dff780d6930bcbe093c046bf31aa26411df/src/checks.kujo) — implementation inspected; 71e66dff780d6930bcbe093c046bf31aa26411df; reviewed 2026-10-19.
- [Runledger scope and implementation](https://github.com/kujolang/runledger/blob/334ddd4d33c8cb2612c8edab971ee69170824133/src/record.kujo) — implementation inspected; 334ddd4d33c8cb2612c8edab971ee69170824133; reviewed 2026-10-19.

## Related pages

- [AI-native programming languages: a practical comparison](https://kujolang.ai/compare/ai-native-programming-languages/)
- [AI code verification tools: what each check can establish](https://kujolang.ai/compare/ai-code-verification-tools/)
- [Verify agent workflows: contracts, checks and reproducible evidence](https://kujolang.ai/compare/verify-agent-workflows/)

[Editorial policy](https://kujolang.ai/compare/editorial-policy.md) · [Report inaccuracies](https://github.com/kujolang/kujolang.ai/issues/new)
