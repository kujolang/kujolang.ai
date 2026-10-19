# Kujo comparison overview

Reviewed 2026-10-19. Canonical: https://kujolang.ai/compare/

## Kujo

Connect an explicit task to checks and retained execution evidence.

Evaluate for: Accountability across an agent-driven development workflow.

Tradeoff: Separate tools need configuration; a passing check covers its stated conditions.

First trial: Start with one acceptance criterion and prove that an incorrect artifact fails.

## Bend

Express properties in the language and supply proofs within its supported subset.

Evaluate for: Precisely stated invariants and proof-oriented programs.

Tradeoff: Affine programming, proof maintenance, and explicit trust boundaries.

First trial: Read a law and its proof, then inspect the negative fixture that rejects an open claim.

## BAML

Evaluate typed AI functions and incremental adoption inside an existing application.

Evaluate for: An AI component with a defined host-language boundary.

Tradeoff: Pin the language generation and verify the exact bridge and boundary types.

First trial: Inspect the current checker and test runner before adopting an example.

## Zero

Explore documented value semantics and explicit systems behavior.

Evaluate for: A systems workload where cleanup and concurrency semantics matter.

Tradeoff: Canonical source repository and numbered release remain unverified here.

First trial: Establish compiler provenance and a repeatable toolchain before an integration.

## Design focus

What are you choosing it to do?

### Kujo

Task-to-outcome workflow

verified-supported · language and first-party ecosystem: A programming language plus separately versioned tools for explicit agent workflow contracts and inspectable outcomes.

https://github.com/kujolang/kujo/blob/acb9107dc38de699c540f5b78d924257def0b95e/src/main.rs
https://github.com/kujolang/spec/blob/1211f37a09314be7150734bf15a55e9b2ea6504d/src/validate.kujo
https://github.com/kujolang/eval/blob/71e66dff780d6930bcbe093c046bf31aa26411df/src/checks.kujo

### Bend

Laws, proofs and parallel programs

verified-supported · language: Laws and proof checking for agent-authored programs, with parallel execution.

https://github.com/bendlang/bend/blob/64230dcb96f2da2cc5a44524e42d5eb34771a6ec/guide/GUIDE.md

### BAML

Typed AI functions and host adoption

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

verified-supported · language and first-party ecosystem: Type checking in the runtime; task schema validation and outcome checks belong to Spec and Eval. Passing these checks is not a universal correctness proof.

https://github.com/kujolang/kujo/blob/acb9107dc38de699c540f5b78d924257def0b95e/src/type_checker.rs
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

unknown · language: A general dependent-type proof system was not established by this review. Do not interpret the positioning “proves it works” as mathematical verification of arbitrary code.

https://github.com/kujolang/kujo/blob/acb9107dc38de699c540f5b78d924257def0b95e/src/type_checker.rs

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

verified-supported · language: The CLI contains bytecode VM, interpreter and optional JIT paths. Backend availability and behavior must be checked for the pinned runtime and target.

https://github.com/kujolang/kujo/blob/acb9107dc38de699c540f5b78d924257def0b95e/src/main.rs

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

verified-supported · first-party ecosystem: RunLedger stores supplied verdicts, commands and tests alongside Git metadata. Workcell defines execution receipts. Neither a receipt nor a correlation ID independently proves semantic correctness.

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

Bend’s guide describes a pure, affine, dependently typed language with explicit IO. It documents native CPU/GPU execution and a JavaScript target whose parallel calls run sequentially. Its proof workflow pairs laws with definitions; the reviewed negative fixture rejects an unfilled claim used as a proof. Kujo’s CLI and type checker provide execution and static diagnostics, while Spec, Eval and Workcell are separate projects. These are complementary layers, not interchangeable guarantees.

### When to choose Bend

Evaluate Bend when the central requirement is a property you can state precisely and prove inside its supported language subset. Its guide makes proof construction and balanced parallel computation central concerns. That is a meaningful advantage for suitable mathematical invariants. Budget for affine programming, explicit annotations and proof maintenance rather than treating proof generation as free.

### Can you use both?

A repository can place a Bend component behind a process or file interface and use external workflow checks around it. This is an architectural option, not a tested Kujo–Bend adapter. Preserve the Bend proof-check output separately from integration tests: proving a component property does not establish that the surrounding application calls it correctly.

### Honest limitations

Bend’s guide excludes unsafe and foreign code from the stronger proof verdict and says its translation to the small kernel is not itself proven. Laws must capture the intended requirement. Kujo outcome checks cover the specified assertions and observed runs; they do not exhaust every input or execution path. Neither tool makes an incomplete specification complete.

## BAML: technical brief

### Technical architecture

The reviewed BAML repository contains a language compiler, a check command that collects project diagnostics, and a test command that loads and runs compiled test sets. Its current site describes typed AI functions, concurrency and tracing. Those product assertions are not evidence of faster execution than Kujo. Kujo’s runtime owns language execution; its task contracts and run records live in separately versioned tools.

### When to choose BAML

Consider BAML when typed AI functions and incremental integration into an existing application are the immediate need. Its current quickstart and bridge story are a useful starting point for teams adopting one component at a time. Check the exact host language, runtime version and supported boundary types before committing to an integration.

### Can you use both?

An external process or service interface could connect BAML application code to Kujo workflow tools. This review did not test a direct Kujo bridge. Do not assume that a bridge to another host language implies one exists for Kujo. Use a versioned request/response contract and test failures at the boundary.

### Honest limitations

BAML’s current website and its older structured-output DSL documentation can describe different generations. Pin a release or source commit before copying examples. Kujo’s surrounding tools require separate configuration and their maturity varies. Neither static types nor successful AI-output parsing establishes that a generated answer is factually correct or that a business requirement was met.

## Zero: technical brief

### Technical architecture

Zero’s installation guide documents interpreter, native JIT, standalone native and C++ output modes. It also distinguishes its WebAssembly browser compiler from native-library and native-code generation support. These are documented capabilities, not locally reproduced results. Kujo’s inspected CLI exposes VM and interpreter execution with optional JIT support; the surrounding workflow tools do not change the language’s memory model.

### When to choose Zero

Try Zero’s preview when value semantics and explicit systems behavior match your workload. Use the browser examples to explore the programming model, then establish source access, supported platforms and release policy before depending on it. Its documented cleanup and concurrency semantics may matter more to your application than an integrated agent workflow.

### Can you use both?

A process or artifact boundary is a plausible way to combine languages. No Kujo–Zero integration was tested. Before planning one, obtain a reproducible Zero toolchain and verify the relevant exit-code, data-format and native-library contracts.

### Honest limitations

Zero’s source identity and release version remain unverified here, so this page cannot independently substantiate its implementation, security boundary or maturity. Kujo’s evidence tools also need configuration and independently meaningful checks. Deterministic cleanup is not the same thing as deterministic network responses, reproducible builds or an auditable agent run.

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

Kujo 1.8.1 computes 6 * 7; Python independently requires an integer total of 42. Wrong values, malformed JSON, missing fields and wrong types must fail. One repetition; no cross-language benchmark or universal proof.

## Technical deep dives

- [Kujo vs Bend: workflow evidence and language proofs](https://kujolang.ai/compare/kujo-vs-bend/)
- [Kujo vs BAML: comparing agent development workflows](https://kujolang.ai/compare/kujo-vs-baml/)
- [Kujo vs Zero: workflow accountability and systems semantics](https://kujolang.ai/compare/kujo-vs-zero/)

[Artifact exercise](https://kujolang.ai/compare/evidence/README.md) · [Editorial policy](https://kujolang.ai/compare/editorial-policy.md)
