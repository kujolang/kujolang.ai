---
title: "Kujo vs Bend: workflow evidence and language proofs"
description: "Compare Kujo’s language and workflow tools with current Bend’s laws, proofs and parallel execution, including scope and limitations."
seo_title: "Kujo vs Bend: workflow evidence and language proofs"
custom_url: "kujo-vs-bend"
date: "2026-10-19"
author: "1"
social_image: "/assets/images/social/kujo-vs-bend.jpg"
---

Kujo and current Bend both address trust in software written by agents, but they put important checks in different places. Bend expresses laws and checks proofs in the language. Kujo combines a programming language with explicit task, evaluation and execution-evidence tools. Choose by the property you need to establish, not by the phrase AI-native.

Last reviewed: 2026-10-19. Canonical page: https://kujolang.ai/compare/kujo-vs-bend/

## At a glance

Bend: https://bend-lang.org/

Documentation: https://github.com/bendlang/bend/blob/64230dcb96f2da2cc5a44524e42d5eb34771a6ec/guide/GUIDE.md

Version: Website v2.0.37; source 64230dcb96f2da2cc5a44524e42d5eb34771a6ec

Repository: https://github.com/bendlang/bend

## Capability matrix

### Primary purpose

Kujo — Verified supported (language and first-party ecosystem): A programming language plus separately versioned tools for explicit agent workflow contracts and inspectable outcomes.

Sources: https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/main.rs, https://github.com/kujolang/spec/blob/1211f37a09314be7150734bf15a55e9b2ea6504d/src/validate.kujo, https://github.com/kujolang/eval/blob/71e66dff780d6930bcbe093c046bf31aa26411df/src/checks.kujo

Bend — Verified supported (language): Laws and proof checking for agent-authored programs, with parallel execution.

Sources: https://github.com/bendlang/bend/blob/64230dcb96f2da2cc5a44524e42d5eb34771a6ec/guide/GUIDE.md

### Correctness checks

Kujo — Verified supported (language and first-party ecosystem): Type checking in the runtime; task schema validation and outcome checks belong to Spec and Eval. Passing these checks is not a universal correctness proof.

Sources: https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/type_checker.rs, https://github.com/kujolang/spec/blob/1211f37a09314be7150734bf15a55e9b2ea6504d/src/validate.kujo, https://github.com/kujolang/eval/blob/71e66dff780d6930bcbe093c046bf31aa26411df/src/checks.kujo

Bend — Verified supported (language): Type-level laws paired with proof definitions; open claims are rejected when used as proof.

Sources: https://github.com/bendlang/bend/blob/64230dcb96f2da2cc5a44524e42d5eb34771a6ec/guide/GUIDE.md, https://github.com/bendlang/bend/blob/64230dcb96f2da2cc5a44524e42d5eb34771a6ec/tests/check/axiom_import_warn.bend

### Formal proof

Kujo — Unknown / not verified (language): A general dependent-type proof system was not established by this review. Do not interpret the positioning “proves it works” as mathematical verification of arbitrary code.

Sources: https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/type_checker.rs

Bend — Verified supported (language): Dependent types and an optional second kernel verdict, subject to documented trust boundaries.

Sources: https://github.com/bendlang/bend/blob/64230dcb96f2da2cc5a44524e42d5eb34771a6ec/guide/GUIDE.md

### Execution

Kujo — Verified supported (language): The CLI contains bytecode VM, interpreter and optional JIT paths. Backend availability and behavior must be checked for the pinned runtime and target.

Sources: https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/main.rs

Bend — Verified supported (language): Native CPU/GPU and JavaScript targets; the JavaScript target is sequential.

Sources: https://github.com/bendlang/bend/blob/64230dcb96f2da2cc5a44524e42d5eb34771a6ec/guide/GUIDE.md

### Workflow receipts

Kujo — Verified supported (first-party ecosystem): RunLedger stores supplied verdicts, commands and tests alongside Git metadata. Workcell defines execution receipts. Neither a receipt nor a correlation ID independently proves semantic correctness.

Sources: https://github.com/kujolang/runledger/blob/334ddd4d33c8cb2612c8edab971ee69170824133/src/record.kujo, https://github.com/kujolang/workcell/blob/a276a92c6bac9279a8cb36ace9687ade34d5128f/src/receipts/receipt.kujo

Bend — Unknown / not verified (toolchain): A Kujo-style cross-tool receipt system was not verified. Proof-checker output has a different scope.

Sources: https://github.com/bendlang/bend/blob/64230dcb96f2da2cc5a44524e42d5eb34771a6ec/guide/GUIDE.md

## Technical architecture

Bend’s guide describes a pure, affine, dependently typed language with explicit IO. It documents native CPU/GPU execution and a JavaScript target whose parallel calls run sequentially. Its proof workflow pairs laws with definitions; the reviewed negative fixture rejects an unfilled claim used as a proof. Kujo’s CLI and type checker provide execution and static diagnostics, while Spec, Eval and Workcell are separate projects. These are complementary layers, not interchangeable guarantees.

## When to choose Kujo

Evaluate Kujo when the deliverable is a complete local automation workflow: a reviewable task contract, checks against files or command results, and retained execution artifacts. Start with one real acceptance criterion and a failing control. The cost is selecting, configuring and pinning multiple ecosystem tools; installing the language does not automatically enforce a release gate.

## When to choose Bend

Evaluate Bend when the central requirement is a property you can state precisely and prove inside its supported language subset. Its guide makes proof construction and balanced parallel computation central concerns. That is a meaningful advantage for suitable mathematical invariants. Budget for affine programming, explicit annotations and proof maintenance rather than treating proof generation as free.

## Can you use both?

A repository can place a Bend component behind a process or file interface and use external workflow checks around it. This is an architectural option, not a tested Kujo–Bend adapter. Preserve the Bend proof-check output separately from integration tests: proving a component property does not establish that the surrounding application calls it correctly.

## Honest limitations

Bend’s guide excludes unsafe and foreign code from the stronger proof verdict and says its translation to the small kernel is not itself proven. Laws must capture the intended requirement. Kujo outcome checks cover the specified assertions and observed runs; they do not exhaust every input or execution path. Neither tool makes an incomplete specification complete.

## Examples and benchmark evidence

No speed ranking or equivalent cross-language benchmark is published here. A proof about every natural number is not comparable to a finite set of runtime assertions. Inspect the linked Bend negative fixture and Kujo checker implementation, then use the reproducible local evidence exercise in the workflow guide. The competitor fixture was inspected, not executed in this review.

## Frequently asked questions

### Is Bend only the older HVM language?

This comparison uses the project linked by bend-lang.org today: bendlang/bend and its current laws-and-proofs guide. Older HVM-era descriptions do not establish the capabilities of this reviewed version.

### Does Kujo offer the same proof guarantee?

This review did not establish an equivalent general proof system in Kujo. Kujo’s task and outcome checks should be judged by the concrete conditions they validate.

## References

- [Bend language guide](https://github.com/bendlang/bend/blob/64230dcb96f2da2cc5a44524e42d5eb34771a6ec/guide/GUIDE.md) — official documentation; Bend website v2.0.37; pinned source snapshot; reviewed 2026-10-19.
- [Bend rejects an unfilled law used as proof](https://github.com/bendlang/bend/blob/64230dcb96f2da2cc5a44524e42d5eb34771a6ec/tests/check/axiom_import_warn.bend) — test source inspected; not executed; 64230dcb96f2da2cc5a44524e42d5eb34771a6ec; reviewed 2026-10-19.
- [Kujo runtime and CLI source](https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/main.rs) — implementation inspected; Kujo 1.8.2 source snapshot; reviewed 2026-10-19.
- [Kujo type checker](https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/type_checker.rs) — implementation inspected; 549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1; reviewed 2026-10-19.
- [Spec scope and implementation](https://github.com/kujolang/spec/blob/1211f37a09314be7150734bf15a55e9b2ea6504d/src/validate.kujo) — implementation inspected; 1211f37a09314be7150734bf15a55e9b2ea6504d; reviewed 2026-10-19.
- [Eval scope and implementation](https://github.com/kujolang/eval/blob/71e66dff780d6930bcbe093c046bf31aa26411df/src/checks.kujo) — implementation inspected; 71e66dff780d6930bcbe093c046bf31aa26411df; reviewed 2026-10-19.
- [Workcell scope and implementation](https://github.com/kujolang/workcell/blob/a276a92c6bac9279a8cb36ace9687ade34d5128f/src/receipts/receipt.kujo) — implementation inspected; a276a92c6bac9279a8cb36ace9687ade34d5128f; reviewed 2026-10-19.
- [Runledger scope and implementation](https://github.com/kujolang/runledger/blob/334ddd4d33c8cb2612c8edab971ee69170824133/src/record.kujo) — implementation inspected; 334ddd4d33c8cb2612c8edab971ee69170824133; reviewed 2026-10-19.

## Related pages

- [AI-native programming languages: a practical comparison](https://kujolang.ai/compare/ai-native-programming-languages/)
- [AI code verification tools: what each check can establish](https://kujolang.ai/compare/ai-code-verification-tools/)
- [Verify agent workflows: contracts, checks and reproducible evidence](https://kujolang.ai/compare/verify-agent-workflows/)

[Editorial policy](https://kujolang.ai/compare/editorial-policy.md) · [Report inaccuracies](https://github.com/kujolang/kujolang.ai/issues/new)
