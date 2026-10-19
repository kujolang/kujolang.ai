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

First trial: Read a law and its proof, then inspect the negative fixture that rejects an open claim.

## BAML

Evaluate typed AI functions and incremental adoption inside an existing application.

Evaluate for: Add an AI feature to an application through a defined interface.

Tradeoff: Choose a specific language version, then check the bridge and data types your application needs.

First trial: Inspect the current checker and test runner before adopting an example.

## Zero

Explore documented value semantics and explicit systems behavior.

Evaluate for: Build a systems component whose resource cleanup and concurrency behavior matter.

Tradeoff: Canonical source repository and numbered release remain unverified here.

First trial: Identify the compiler’s source and version before planning an integration.

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

### Zero

Predictable systems semantics

partially-supported · language: Predictable systems behavior with value semantics and structured concurrency, according to the website.

https://zero-lang.com/

## Checks & tests

Which errors can a check expose?

### Kujo

Types, task schemas and outcome checks

verified-supported · language and first-party ecosystem: The runtime checks types. Spec validates task records, and Eval checks selected outputs. Passing those checks does not prove arbitrary programs correct.

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

verified-supported · toolchain: A test runner and result parsing tests exist in the reviewed source. This review did not execute them.

https://github.com/BoundaryML/baml/blob/648ad5ed10f543c129b51789c7d02e29b64f06f7/baml_language/crates/baml_cli/src/test_command.rs

### Zero

Documented check-only compiler mode

partially-supported · language: The installation guide documents a check-only compiler mode; implementation not inspected.

https://zero-lang.com/download.html

## Formal proof

Does it establish a stated property?

### Kujo

General proof system not established

unknown · language: We did not establish a general dependent-type proof system in Kujo. The phrase “proves it works” should not be read as mathematical verification of arbitrary code.

https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/type_checker.rs

### Bend

Dependent types; bounded proof guarantees

verified-supported · language: Dependent types and an optional second kernel verdict, subject to documented trust boundaries.

https://github.com/bendlang/bend/blob/64230dcb96f2da2cc5a44524e42d5eb34771a6ec/guide/GUIDE.md

### BAML

General theorem proving not verified

unknown · language: A general dependent-type proof guarantee was not verified in the reviewed sources.

https://github.com/BoundaryML/baml/blob/648ad5ed10f543c129b51789c7d02e29b64f06f7/baml_language/crates/baml_cli/src/check_command.rs

### Zero

General theorem proving not verified

unknown · language: General theorem proving was not verified. Deterministic semantics alone do not establish it.

https://zero-lang.com/

## Execution model

Where does the program run?

### Kujo

VM, interpreter and optional JIT paths

verified-supported · language: The CLI includes a bytecode VM, an interpreter and optional JIT paths. Check which backends work with the runtime version and target you choose.

https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/main.rs

### Bend

CPU/GPU and sequential JavaScript target

verified-supported · language: Native CPU/GPU and JavaScript targets; the JavaScript target is sequential.

https://github.com/bendlang/bend/blob/64230dcb96f2da2cc5a44524e42d5eb34771a6ec/guide/GUIDE.md

### BAML

Runtime equivalence not evaluated

Not assessed; no conclusion about support.

### Zero

Interpreter, JIT, native and C++ modes documented

partially-supported · language: Interpreter, native JIT, native executable and C++ output modes are documented.

https://zero-lang.com/download.html

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

Tracing advertised; overhead not measured

partially-supported · toolchain: The current website describes tracing and profiling. Completeness and overhead were not measured here.

https://boundaryml.com/

### Zero

Agent run-receipt system not verified

unknown · toolchain: Agent task contracts and a run-receipt system were not verified.

https://zero-lang.com/
https://zero-lang.com/download.html

## Execution boundary

What constrains a running process?

### Kujo

Configured Workcell container boundary

verified-supported · first-party ecosystem: Workcell uses configured Docker/Podman execution boundaries. A normal Kujo process is not automatically a container sandbox.

https://github.com/kujolang/workcell/blob/a276a92c6bac9279a8cb36ace9687ade34d5128f/src/receipts/receipt.kujo

### Bend

Isolation not assessed in this comparison

Not assessed; no conclusion about support.

### BAML

Isolation not assessed in this comparison

Not assessed; no conclusion about support.

### Zero

Isolation not assessed in this comparison

Not assessed; no conclusion about support.

## Bend: technical brief

### Technical architecture

Bend’s guide describes a pure, affine, dependently typed language with explicit IO. It documents native CPU and GPU execution, while its JavaScript target runs parallel calls sequentially. Bend pairs laws with proof definitions; the negative fixture we inspected rejects an unfinished claim used as a proof. Kujo provides runtime execution and type diagnostics. Spec, Eval and Workcell are separate tools that check other parts of the workflow.

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

Current BAML material and older structured-output DSL tutorials may describe different generations. Choose a release or source commit before copying examples. Kujo’s separate tools also need configuration and vary in maturity. Type checking and successful parsing constrain data structure; they do not show that an AI answer is true or meets a business requirement.

## Zero: technical brief

### Technical architecture

Zero’s installation guide documents interpreter, native JIT, native executable and C++ output modes. It distinguishes the WebAssembly browser compiler from support for native libraries and code generation. We did not reproduce these capabilities locally. Kujo’s inspected CLI supports VM and interpreter execution with optional JIT paths; its workflow tools do not change the language’s memory model.

### When to choose Zero

Try Zero’s preview if its documented value semantics and systems behavior suit your workload. Explore the browser examples, then establish source access, platform support and release policy before depending on it. Resource cleanup and concurrency behavior may matter more to your application than agent-workflow tools.

### Can you use both?

A process or file interface could connect the languages, but we did not test a Kujo–Zero integration. First identify a repeatable Zero toolchain, then check its exit codes, data formats and native-library interfaces.

### Honest limitations

Without a verified source repository or release version, we cannot independently assess Zero’s implementation, security boundaries or maturity. Kujo’s evidence tools also require configuration and meaningful checks. Deterministic cleanup alone does not make network responses or builds repeatable, or create an auditable agent run.

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
- [Kujo vs Zero: workflow accountability and systems semantics](https://kujolang.ai/compare/kujo-vs-zero/)

[Artifact exercise](https://kujolang.ai/compare/evidence/README.md) · [Editorial policy](https://kujolang.ai/compare/editorial-policy.md)
