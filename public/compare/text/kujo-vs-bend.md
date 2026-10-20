# Kujo vs Bend: workflow evidence and language proofs

Kujo and Bend check agent-written software at different levels. Bend lets you state laws and check proofs in the language. Kujo combines language checks with separate tools for task requirements, output checks and execution records. Choose based on what you need to verify, and consider using both when the requirement spans these levels.

Last reviewed: 2026-10-19. Canonical page: https://kujolang.ai/compare/kujo-vs-bend/

## At a glance

Bend: https://bend-lang.org/

Documentation: https://github.com/bendlang/bend/blob/64230dcb96f2da2cc5a44524e42d5eb34771a6ec/guide/GUIDE.md

Version: Stable v2.0.37 (2026-10-13; release commit 4ff8545f19b09b7d2b8ca2303668100eac8efd66). Release binaries tested on macOS and Linux x86_64; independent kernel built with Lean 4.34.0.

Repository: https://github.com/bendlang/bend

## Capability matrix

### Primary purpose

Kujo — Verified supported (language and first-party ecosystem): Kujo provides a language and separate tools for defining agent tasks, checking results and keeping run evidence.

Sources: https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/main.rs, https://github.com/kujolang/spec/blob/1211f37a09314be7150734bf15a55e9b2ea6504d/src/validate.kujo, https://github.com/kujolang/eval/blob/71e66dff780d6930bcbe093c046bf31aa26411df/src/checks.kujo

Bend — Verified supported (language): Laws and proof checking for agent-authored programs, with parallel execution.

Sources: https://github.com/bendlang/bend/blob/64230dcb96f2da2cc5a44524e42d5eb34771a6ec/guide/GUIDE.md

### Correctness checks

Kujo — Verified supported (language and first-party ecosystem): In Kujo 1.8.2, `kujo check` parses and compiles without executing; it is not a complete type-enforcement gate. Interpreter type diagnostics can be warnings. Spec validates task records, and Eval checks selected outputs; none proves arbitrary programs correct.

Sources: https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/main.rs, https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/type_checker.rs, https://github.com/kujolang/spec/blob/1211f37a09314be7150734bf15a55e9b2ea6504d/src/validate.kujo, https://github.com/kujolang/eval/blob/71e66dff780d6930bcbe093c046bf31aa26411df/src/checks.kujo

Bend — Verified supported (language): Type-level laws paired with proof definitions; open claims are rejected when used as proof.

Sources: https://github.com/bendlang/bend/blob/64230dcb96f2da2cc5a44524e42d5eb34771a6ec/guide/GUIDE.md, https://github.com/bendlang/bend/blob/64230dcb96f2da2cc5a44524e42d5eb34771a6ec/tests/check/axiom_import_warn.bend

### Formal proof

Kujo — Unknown / not verified (language): We did not establish a general dependent-type proof system in Kujo. The phrase “proves it works” should not be read as mathematical verification of arbitrary code.

Sources: https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/type_checker.rs

Bend — Verified supported (language): The independent BendTT kernel accepted a valid exported proof and rejected a corrupted proof body. Its guarantee still depends on the documented trust boundaries.

Sources: https://github.com/bendlang/bend/blob/64230dcb96f2da2cc5a44524e42d5eb34771a6ec/guide/GUIDE.md, https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/runtime-gap-review-2026-10-19

### Execution

Kujo — Verified supported (language): The CLI includes a bytecode VM, an interpreter and optional JIT paths. Check which backends work with the runtime version and target you choose.

Sources: https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/main.rs

Bend — Verified supported (language): Native CPU and sequential JavaScript results tested, including fork-join syntax. GPU support is documented but was not executed; no speedup was measured.

Sources: https://github.com/bendlang/bend/blob/64230dcb96f2da2cc5a44524e42d5eb34771a6ec/guide/GUIDE.md, https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/runtime-gap-review-2026-10-19

### Workflow receipts

Kujo — Verified supported (first-party ecosystem): RunLedger stores supplied verdicts, commands and tests with Git metadata. Workcell records execution receipts. Follow these records to the underlying checks; a receipt or correlation ID alone does not prove the result correct.

Sources: https://github.com/kujolang/runledger/blob/334ddd4d33c8cb2612c8edab971ee69170824133/src/record.kujo, https://github.com/kujolang/workcell/blob/a276a92c6bac9279a8cb36ace9687ade34d5128f/src/receipts/receipt.kujo

Bend — Unknown / not verified (toolchain): A Kujo-style cross-tool receipt system was not verified. Proof-checker output has a different scope.

Sources: https://github.com/bendlang/bend/blob/64230dcb96f2da2cc5a44524e42d5eb34771a6ec/guide/GUIDE.md

## Technical deep dive

Compare what Bend can prove with what Kujo’s workflow checks can verify.

Is the requirement a mathematical property, an observed outcome, or both?

### Programming model: Bend makes effects and value reuse explicit

Bend separates pure computation from explicit IO. Affine values constrain reuse; copyable data and annotations affect how functions are written. A team coming from ordinary imperative code should trial the data model before estimating migration effort.

Evaluation implication: A proof-friendly component still needs an IO boundary and tests for its callers.

Sources: https://github.com/bendlang/bend/blob/64230dcb96f2da2cc5a44524e42d5eb34771a6ec/guide/GUIDE.md

### Assurance boundary: Review what the law actually promises

Bend checks proof definitions against type-level laws. The inspected negative fixture rejects an open claim offered as a proof. Unsafe and foreign code sit outside the stronger guarantee, and the guide identifies an unproven translation into the small kernel.

Evaluation implication: Review the law and trusted boundary as carefully as the generated implementation.

Sources: https://github.com/bendlang/bend/blob/64230dcb96f2da2cc5a44524e42d5eb34771a6ec/guide/GUIDE.md, https://github.com/bendlang/bend/blob/64230dcb96f2da2cc5a44524e42d5eb34771a6ec/tests/check/axiom_import_warn.bend

### Execution model: Match the workload to the parallel target

The guide documents CPU and GPU execution, with sequential JavaScript output. Parallel calls suit independent, balanced work; target choice and workload shape belong in the evaluation. No relative speed measurement was performed here.

Evaluation implication: Keep correctness evidence separate from target-specific latency and throughput measurements.

Sources: https://github.com/bendlang/bend/blob/64230dcb96f2da2cc5a44524e42d5eb34771a6ec/guide/GUIDE.md

## Decision scenarios

Proposed evaluation criteria, not comparative benchmark results.

### Invariant-heavy component

Kujo: Use workflow checks to verify integration artifacts and retain the run.

Bend: Evaluate a precisely stated law and its checked proof.

Evidence to collect: A proof verdict plus tests of serialization, callers and IO.

### Agent edits a repository

Kujo: Compose task criteria, file/process checks and retained evidence.

Bend: A component proof can support one part of the change.

Evidence to collect: A failing control, artifact checks and a reviewed diff.

### Parallel numerical workload

Kujo: Measure the actual Kujo workload on the intended runtime.

Bend: Trial the documented native CPU/GPU target and balanced work.

Evidence to collect: Identical inputs, target/hardware versions, outputs and timing method.

## A focused evaluation plan

Proposed steps; no competitor runtime test is claimed.

### State two contracts

Write a component law and a separate integration acceptance criterion. Explain which inputs the law quantifies over and which external effects remain outside it.

### Challenge the proof

Use the pinned guide and negative fixture as starting evidence. Our 2.0.37 trial rejected a broken proof and an unfilled law. Reproduce both on your own toolchain, and distinguish --check-only from the separate --verdict kernel step.

### Challenge the boundary

Feed a known wrong artifact to an independent check. Exercise the caller and serialization path so that a valid component cannot hide a broken integration.

### Keep distinct verdicts

Record the proof result, integration result and performance measurement separately. Accept only the guarantee each check actually establishes.

## Technical architecture

Bend’s guide describes a pure, affine, dependently typed language with explicit IO. It documents native CPU and GPU execution, while its JavaScript target runs parallel calls sequentially. Bend pairs laws with proof definitions; the negative fixture we inspected rejects an unfinished claim used as a proof. Kujo provides runtime execution and type diagnostics, but a successful `kujo check` does not establish type correctness in 1.8.2. Spec, Eval and Workcell are separate tools that check other parts of the workflow.

## When to choose Kujo

Evaluate Kujo when you need to define an automation task, check its files or command results and keep evidence of the run. Start with one acceptance criterion and an incorrect output that the checker must reject. Allow time to choose, configure and pin the separate tools: installing Kujo does not automatically set up a release gate.

## When to choose Bend

Evaluate Bend when you can state the central requirement precisely and prove it within the supported language subset. Its guide emphasizes proof construction and balanced parallel computation. This can suit mathematical invariants, but you will need to learn its affine programming model, write explicit annotations and maintain the proofs.

## Can you use both?

You could place a Bend component behind a process or file interface and check the surrounding workflow with other tools. We did not test a Kujo–Bend adapter. Keep proof results separate from integration tests: a proof about the component does not show that the application calls it correctly.

## Honest limitations

Bend excludes unsafe and foreign code from its stronger proof verdict. Its guide also says that translation into the small kernel is not itself proven. Kujo’s output checks cover the assertions and runs you define, rather than every possible input. In either case, review whether the specification expresses the requirement fully.

## Examples and benchmark evidence

Bend 2.0.37 accepted a valid proof through --verdict with its independent BendTT kernel built using Lean 4.34.0. Calling that kernel directly accepted the exported proof and rejected a corrupted proof body. Broken proof, type and affine-use fixtures also failed. A fork-join example returned 4096 through native CPU and sequential JavaScript targets. These tests check results, not parallel speedup, GPU execution or the unproven translation into the kernel.

## Frequently asked questions

### Is Bend only the older HVM language?

This comparison uses the project linked by bend-lang.org today: bendlang/bend and its current laws-and-proofs guide. Older HVM-era descriptions do not establish the capabilities of this reviewed version.

### Does Kujo offer the same proof guarantee?

This review did not establish an equivalent general proof system in Kujo. Kujo’s task and outcome checks should be judged by the concrete conditions they validate.

## References

- [Bend language guide](https://github.com/bendlang/bend/blob/64230dcb96f2da2cc5a44524e42d5eb34771a6ec/guide/GUIDE.md) — official documentation; Stable v2.0.37; guide from a separate pinned source snapshot; reviewed 2026-10-19.
- [Bend rejects an unfilled law used as proof](https://github.com/bendlang/bend/blob/64230dcb96f2da2cc5a44524e42d5eb34771a6ec/tests/check/axiom_import_warn.bend) — fixture inspected and executed against release 2.0.37; 64230dcb96f2da2cc5a44524e42d5eb34771a6ec; reviewed 2026-10-19.
- [Kujo runtime and CLI source](https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/main.rs) — implementation inspected; Kujo 1.8.2 source snapshot; reviewed 2026-10-19.
- [Kujo type checker](https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/type_checker.rs) — implementation inspected; 549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1; reviewed 2026-10-19.
- [Spec scope and implementation](https://github.com/kujolang/spec/blob/1211f37a09314be7150734bf15a55e9b2ea6504d/src/validate.kujo) — implementation inspected; 1211f37a09314be7150734bf15a55e9b2ea6504d; reviewed 2026-10-19.
- [Eval scope and implementation](https://github.com/kujolang/eval/blob/71e66dff780d6930bcbe093c046bf31aa26411df/src/checks.kujo) — implementation inspected; 71e66dff780d6930bcbe093c046bf31aa26411df; reviewed 2026-10-19.
- [Workcell scope and implementation](https://github.com/kujolang/workcell/blob/a276a92c6bac9279a8cb36ace9687ade34d5128f/src/receipts/receipt.kujo) — implementation inspected; a276a92c6bac9279a8cb36ace9687ade34d5128f; reviewed 2026-10-19.
- [Runledger scope and implementation](https://github.com/kujolang/runledger/blob/334ddd4d33c8cb2612c8edab971ee69170824133/src/record.kujo) — implementation inspected; 334ddd4d33c8cb2612c8edab971ee69170824133; reviewed 2026-10-19.
- [Bend stable release](https://github.com/bendlang/bend/releases/tag/v2.0.37) — official release metadata; 2.0.37; released 2026-10-13; reviewed 2026-10-19.
- [Kujo stable release](https://github.com/kujolang/kujo/releases/tag/v1.8.2) — official release metadata; 1.8.2; released 2026-10-19; reviewed 2026-10-19.
- [Competitor runtime fixtures and raw outcomes](https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/runtime-review-2026-10-19) — local execution receipts; bounded fixtures; Bend 2.0.37; BAML 0.22.2; Zerolang 0.3.4; macOS x86_64; reviewed 2026-10-19.
- [Bend kernel and BAML integration runtime tests](https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/runtime-gap-review-2026-10-19) — release binaries executed; positive and negative fixtures; local mock provider; Bend 2.0.37 with Lean 4.34.0 on Linux x86_64; BAML and Python bridge 0.22.2 on macOS x86_64; reviewed 2026-10-19.

## Related pages

- [AI-native programming languages: a practical comparison](https://kujolang.ai/compare/ai-native-programming-languages/)
- [AI code verification tools: what each check can establish](https://kujolang.ai/compare/ai-code-verification-tools/)
- [Verify agent workflows: contracts, checks and reproducible evidence](https://kujolang.ai/compare/verify-agent-workflows/)

[Editorial policy](https://kujolang.ai/compare/editorial-policy.md) · [Report inaccuracies](https://github.com/kujolang/kujolang.ai/issues/new)
