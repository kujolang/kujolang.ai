# Kujo comparison overview

Reviewed 2026-10-19. Canonical: https://kujolang.ai/compare/

## Kujo

Connect an explicit task to checks and retained execution evidence.

Evaluate for: Check what an agent changed and whether it met the task requirements.

Tradeoff: Separate tools need configuration; a passing check covers its stated conditions.

First trial: Start with one acceptance criterion and prove that an incorrect artifact fails.

## Bend

Express properties in the language and supply proofs within its supported subset.

Evaluate for: State a property precisely and check a proof that the program satisfies it.

Tradeoff: Allow time to learn affine programming, maintain proofs and review their assumptions.

First trial: Run a valid proof and a deliberately broken proof; check the separate verdict dependencies.

## BAML

Evaluate typed AI functions and incremental adoption inside an existing application.

Evaluate for: Add an AI feature to an application through a defined interface.

Tradeoff: Choose a specific language version, then check the bridge and data types your application needs.

First trial: Run a typed function, reject a type mismatch and fail an assertion on the selected release.

## Zerolang

Let agents query program facts and submit checked graph edits.

Evaluate for: Validate semantic edits and keep readable source projections for human review.

Tradeoff: Experimental release; evaluate your graph shapes, dependencies and deployment target.

First trial: Reject stale and ill-typed patches, then verify a failing behavioral test.

## Design focus

What are you choosing it to do?

### Kujo

Task requirements, output checks and run records

verified-supported · language and first-party ecosystem: Kujo provides a language and separate tools for defining agent tasks, checking results and keeping run evidence.

https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/main.rs
https://github.com/kujolang/spec/blob/1211f37a09314be7150734bf15a55e9b2ea6504d/src/validate.kujo
https://github.com/kujolang/eval/blob/71e66dff780d6930bcbe093c046bf31aa26411df/src/checks.kujo

### Bend

Laws, proofs and parallel programs

verified-supported · language: Laws and proof checking for agent-authored programs, with parallel execution.

https://github.com/bendlang/bend/blob/64230dcb96f2da2cc5a44524e42d5eb34771a6ec/guide/GUIDE.md

### BAML

Typed AI functions and integration with an existing application

partially-supported · language and toolchain: An agent-oriented language with AI functions and incremental host-language adoption.

https://boundaryml.com/

### Zerolang

Agent queries and checked graph edits

verified-supported · language: Graph-native programming for agent queries and checked semantic edits.

https://github.com/vercel-labs/zerolang/blob/5b3a90a7756e48ab449eb16e688044b8decec7a9/docs/articles/concepts/graph-architecture.md

## Checks & tests

Which errors can a check expose?

### Kujo

Compiler checks, task schemas and outcome checks

verified-supported · language and first-party ecosystem: In Kujo 1.8.2, `kujo check` parses and compiles without executing; it is not a complete type-enforcement gate. Interpreter type diagnostics can be warnings. Spec validates task records, and Eval checks selected outputs; none proves arbitrary programs correct.

https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/main.rs
https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/type_checker.rs
https://github.com/kujolang/spec/blob/1211f37a09314be7150734bf15a55e9b2ea6504d/src/validate.kujo
https://github.com/kujolang/eval/blob/71e66dff780d6930bcbe093c046bf31aa26411df/src/checks.kujo

### Bend

Type-level laws and proof definitions

verified-supported · language: Type-level laws paired with proof definitions; open claims are rejected when used as proof.

https://github.com/bendlang/bend/blob/64230dcb96f2da2cc5a44524e42d5eb34771a6ec/guide/GUIDE.md
https://github.com/bendlang/bend/blob/64230dcb96f2da2cc5a44524e42d5eb34771a6ec/tests/check/axiom_import_warn.bend

### BAML

Project diagnostics and a test runner

verified-supported · language: Project diagnostics are implemented by the current check command.

https://github.com/BoundaryML/baml/blob/648ad5ed10f543c129b51789c7d02e29b64f06f7/baml_language/crates/baml_cli/src/check_command.rs

verified-supported · toolchain: Local assertions passed and failed as expected. Mock-provider response parsing accepted a valid object and rejected an invalid field; the full upstream suite was not run.

https://github.com/BoundaryML/baml/blob/648ad5ed10f543c129b51789c7d02e29b64f06f7/baml_language/crates/baml_cli/src/test_command.rs
https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/runtime-review-2026-10-19
https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/runtime-gap-review-2026-10-19

### Zerolang

Patch rejection and executable tests

verified-supported · toolchain: Stale-hash and wrong-return-type patches were rejected without changing the graph in our 0.3.4 fixtures.

https://github.com/vercel-labs/zerolang/blob/5b3a90a7756e48ab449eb16e688044b8decec7a9/native/zero-c/src/program_graph_patch.c
https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/runtime-review-2026-10-19

## Formal proof

Does it establish a stated property?

### Kujo

General proof system not established

unknown · language: We did not establish a general dependent-type proof system in Kujo. The phrase “proves it works” should not be read as mathematical verification of arbitrary code.

https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/type_checker.rs

### Bend

Dependent types; bounded proof guarantees

verified-supported · language: The independent BendTT kernel accepted a valid exported proof and rejected a corrupted proof body. Its guarantee still depends on the documented trust boundaries.

https://github.com/bendlang/bend/blob/64230dcb96f2da2cc5a44524e42d5eb34771a6ec/guide/GUIDE.md
https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/runtime-gap-review-2026-10-19

### BAML

General theorem proving not verified

unknown · language: A general dependent-type proof guarantee was not verified in the reviewed sources.

https://github.com/BoundaryML/baml/blob/648ad5ed10f543c129b51789c7d02e29b64f06f7/baml_language/crates/baml_cli/src/check_command.rs

### Zerolang

General theorem proving not established

unknown · language: General theorem proving was not established. Graph validation and executable tests answer narrower questions.

https://github.com/vercel-labs/zerolang/blob/5b3a90a7756e48ab449eb16e688044b8decec7a9/docs/articles/concepts/graph-architecture.md
https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/runtime-review-2026-10-19

## Execution model

Where does the program run?

### Kujo

VM, interpreter and optional JIT paths

verified-supported · language: The CLI includes a bytecode VM, an interpreter and optional JIT paths. Check which backends work with the runtime version and target you choose.

https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/main.rs

### Bend

CPU/GPU and sequential JavaScript target

verified-supported · language: Native CPU and sequential JavaScript results tested, including fork-join syntax. GPU support is documented but was not executed; no speedup was measured.

https://github.com/bendlang/bend/blob/64230dcb96f2da2cc5a44524e42d5eb34771a6ec/guide/GUIDE.md
https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/runtime-gap-review-2026-10-19

### BAML

Python client, packed binary and mock-provider responses tested

verified-supported · language: Project diagnostics are implemented by the current check command.

https://github.com/BoundaryML/baml/blob/648ad5ed10f543c129b51789c7d02e29b64f06f7/baml_language/crates/baml_cli/src/check_command.rs

### Zerolang

Graph-backed macOS x64 execution tested

verified-supported · language: The graph-backed package ran a greeting and an arithmetic test on macOS x64. Other targets were not executed.

https://github.com/vercel-labs/zerolang/blob/5b3a90a7756e48ab449eb16e688044b8decec7a9/docs/articles/concepts/compile-path.md
https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/runtime-review-2026-10-19

## Evidence & tracing

What can a reviewer inspect afterward?

### Kujo

Run metadata and execution receipts

verified-supported · first-party ecosystem: RunLedger stores supplied verdicts, commands and tests with Git metadata. Workcell records execution receipts. Follow these records to the underlying checks; a receipt or correlation ID alone does not prove the result correct.

https://github.com/kujolang/runledger/blob/334ddd4d33c8cb2612c8edab971ee69170824133/src/record.kujo
https://github.com/kujolang/workcell/blob/a276a92c6bac9279a8cb36ace9687ade34d5128f/src/receipts/receipt.kujo

### Bend

Proof output; broader run ledger unverified

unknown · toolchain: A Kujo-style cross-tool receipt system was not verified. Proof-checker output has a different scope.

https://github.com/bendlang/bend/blob/64230dcb96f2da2cc5a44524e42d5eb34771a6ec/guide/GUIDE.md

### BAML

Local trace queries tested; cloud delivery untested

partially-supported · toolchain: Local BTEL recordings and SQL queries recovered success/error outcomes and profiler counts. Trace context reached a generated-client call without leaking into the next call. Cloud delivery and overhead remain untested.

https://boundaryml.com/
https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/runtime-gap-review-2026-10-19

### Zerolang

Graph hashes, patch results and projection checks

verified-supported · toolchain: Graph hashes, structured patch outcomes and projection checks provide review evidence. A separate end-to-end run ledger was not assessed.

https://github.com/vercel-labs/zerolang/blob/5b3a90a7756e48ab449eb16e688044b8decec7a9/native/zero-c/src/program_graph_patch.c
https://github.com/vercel-labs/zerolang/blob/5b3a90a7756e48ab449eb16e688044b8decec7a9/docs/articles/concepts/projections.md
https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/runtime-review-2026-10-19

## Execution boundary

What constrains a running process?

### Kujo

Configured Workcell container boundary

verified-supported · first-party ecosystem: Workcell 1.2.0’s stable execution boundary uses configured Docker/Podman containers. Its provider-neutral and remote-adapter contracts remain alpha. A normal Kujo process is not automatically a container sandbox; host and daemon security remain outside this guarantee.

https://github.com/kujolang/workcell/blob/a276a92c6bac9279a8cb36ace9687ade34d5128f/src/receipts/receipt.kujo
https://github.com/kujolang/workcell/blob/a276a92c6bac9279a8cb36ace9687ade34d5128f/README.md

### Bend

Isolation not assessed in this comparison

Not assessed; no conclusion about support.

### BAML

Isolation not assessed in this comparison

Not assessed; no conclusion about support.

### Zerolang

Isolation not assessed in this comparison

Not assessed; no conclusion about support.

## Bend: technical brief

### Technical architecture

Bend’s guide describes a pure, affine, dependently typed language with explicit IO. It documents native CPU and GPU execution, while its JavaScript target runs parallel calls sequentially. Bend pairs laws with proof definitions; the negative fixture we inspected rejects an unfinished claim used as a proof. Kujo provides runtime execution and type diagnostics, but a successful `kujo check` does not establish type correctness in 1.8.2. Spec, Eval and Workcell are separate tools that check other parts of the workflow.

### When to choose Bend

Evaluate Bend when you can state the central requirement precisely and prove it within the supported language subset. Its guide emphasizes proof construction and balanced parallel computation. This can suit mathematical invariants, but you will need to learn its affine programming model, write explicit annotations and maintain the proofs.

### Can you use both?

You could place a Bend component behind a process or file interface and check the surrounding workflow with other tools. We did not test a Kujo–Bend adapter. Keep proof results separate from integration tests: a proof about the component does not show that the application calls it correctly.

### Honest limitations

Bend excludes unsafe and foreign code from its stronger proof verdict. Its guide also says that translation into the small kernel is not itself proven. Kujo’s output checks cover the assertions and runs you define, rather than every possible input. In either case, review whether the specification expresses the requirement fully.

## BAML: technical brief

### Technical architecture

The BAML source we reviewed contains a compiler, a check command that collects project diagnostics and a test command that runs compiled test sets. Its current website describes typed AI functions, concurrency and tracing. These claims do not establish a speed advantage over Kujo. Kujo handles language execution in its runtime and provides task contracts and run records through separately versioned tools.

### When to choose BAML

Consider BAML when you need typed AI functions within an existing application. Its quickstart and language bridges offer a starting point for adding one component at a time. Before choosing a bridge, check the supported host language, runtime version and data types.

### Can you use both?

You could connect BAML application code to Kujo workflow tools through a process or service interface. We did not test a direct Kujo bridge, and support for another host language does not imply Kujo support. Define a versioned request/response format and test how failures cross the interface.

### Honest limitations

Current BAML material and older structured-output DSL tutorials may describe different generations. Choose a release or source commit before copying examples. Kujo’s separate tools also need configuration and vary in maturity. Type checking and successful parsing constrain data structure; they do not show that an AI answer is true or meets a business requirement. In the tested 0.22.2 CLI, Python client setup uses generate add python/pydantic2 followed by generate; do not substitute a command from a newer quickstart without checking the installed help. The generated Python bridge returned a string passed to an int identity function in our fixture. Do not assume generated type hints enforce every host argument at runtime; validate the boundary separately.

## Zerolang: technical brief

### Technical architecture

Zerolang stores declarations, types, calls and related facts in zero.graph. Agents query and patch that graph; humans can export readable .0 projections. The normal package compile path consumes the graph. Our stale-hash and wrong-return-type patches failed without changing the stored graph. Kujo’s separate workflow tools check task contracts and observed outcomes; they do not provide this graph-editing model.

### When to choose Zerolang

Evaluate Zerolang when compiler-aware agent edits, graph queries and reviewable source projections fit your development process. Its checked patch interface gives agents a narrower editing surface than unrestricted text replacement. Treat it as an experiment: validate the graph shapes, platform and dependencies your application needs before adopting it.

### Can you use both?

A process or file boundary could connect a Zerolang component to external acceptance checks and run records. No direct Kujo integration was tested. Keep the graph hash, compiler version, test output and projection state together so a reviewer can connect a checked edit to the artifact that ran.

### Honest limitations

A valid graph can still implement the wrong behavior. Our graph check passed while a deliberately incorrect expected result made zero test fail. We did not establish general theorem proving, production sandbox security, cross-target support or a speed advantage. Runtime capability facts are not a substitute for an operating-system isolation boundary.

## Kujo workflow composition

Separate tools; not an automatic pipeline.

### Specify — Spec

Write observable acceptance criteria. A valid task record can still describe an incomplete requirement.

https://kujolang.ai/ecosystem/spec/

### Check — Eval

Evaluate files and command outcomes. A passing assertion covers that assertion, not every possible input.

https://kujolang.ai/ecosystem/eval/

### Execute — Workcell

Configure an execution boundary and retain receipts. A normal language process is not automatically sandboxed.

https://kujolang.ai/ecosystem/workcell/

### Record — RunLedger

Connect supplied results to commands and Git context. A recorded pass verdict is not an independent correctness proof.

https://kujolang.ai/ecosystem/runledger/

### Review — ShipCheck

Bring release-readiness signals to the decision. A human or explicitly authorized gate still owns the release.

https://kujolang.ai/ecosystem/shipcheck/

## Artifact exercise

Kujo 1.8.2 computes 6 * 7; Python independently requires an integer total of 42. Wrong values, malformed JSON, missing fields and wrong types must fail. One repetition; no cross-language benchmark or universal proof.

## Technical deep dives

- [Kujo vs Bend: workflow evidence and language proofs](https://kujolang.ai/compare/kujo-vs-bend/)
- [Kujo vs BAML: comparing agent development workflows](https://kujolang.ai/compare/kujo-vs-baml/)
- [Kujo vs Zerolang: workflow evidence and checked graph edits](https://kujolang.ai/compare/kujo-vs-zero/)

[Artifact exercise](https://kujolang.ai/compare/evidence/README.md) · [Editorial policy](https://kujolang.ai/compare/editorial-policy.md)
