---
template: "comparison-direct"
title: "Kujo vs Zerolang: workflow evidence and checked graph edits"
description: "Compare Kujo with Vercel Zerolang: task evidence, graph patches, type checks, executable tests and source projections, with pinned runtime results."
seo_title: "Kujo vs Zerolang: workflow evidence and checked graph edits"
custom_url: "kujo-vs-zero"
date: "2026-10-19"
author: "1"
social_image: "/assets/images/social/kujo-vs-zero.jpg"
---

Vercel Zerolang makes the program graph the normal compiler input and lets agents submit checked semantic edits. Kujo combines language execution with separate tools for task requirements, output checks and run records. We inspected Zerolang’s repository and exercised release 0.3.4, including rejected patches and failing tests. These approaches address different parts of trusting agent-written software.

Last reviewed: 2026-10-19. Canonical page: https://kujolang.ai/compare/kujo-vs-zero/

## At a glance

Zerolang: https://zerolang.ai/

Documentation: https://zerolang.ai/getting-started

Version: 0.3.4; latest published release checked 2026-10-19

Repository: https://github.com/vercel-labs/zerolang

## Capability matrix

### Primary purpose

Kujo — Verified supported (language and first-party ecosystem): Kujo provides a language and separate tools for defining agent tasks, checking results and keeping run evidence.

Sources: https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/main.rs, https://github.com/kujolang/spec/blob/1211f37a09314be7150734bf15a55e9b2ea6504d/src/validate.kujo, https://github.com/kujolang/eval/blob/71e66dff780d6930bcbe093c046bf31aa26411df/src/checks.kujo

Zerolang — Verified supported (language): Graph-native programming for agent queries and checked semantic edits.

Sources: https://github.com/vercel-labs/zerolang/blob/5b3a90a7756e48ab449eb16e688044b8decec7a9/docs/articles/concepts/graph-architecture.md

### Static checks

Kujo — Verified supported (language and first-party ecosystem): In Kujo 1.8.2, `kujo check` parses and compiles without executing; it is not a complete type-enforcement gate. Interpreter type diagnostics can be warnings. Spec validates task records, and Eval checks selected outputs; none proves arbitrary programs correct.

Sources: https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/main.rs, https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/type_checker.rs, https://github.com/kujolang/spec/blob/1211f37a09314be7150734bf15a55e9b2ea6504d/src/validate.kujo, https://github.com/kujolang/eval/blob/71e66dff780d6930bcbe093c046bf31aa26411df/src/checks.kujo

Zerolang — Verified supported (toolchain): Stale-hash and wrong-return-type patches were rejected without changing the graph in our 0.3.4 fixtures.

Sources: https://github.com/vercel-labs/zerolang/blob/5b3a90a7756e48ab449eb16e688044b8decec7a9/native/zero-c/src/program_graph_patch.c, https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/runtime-review-2026-10-19

### Execution

Kujo — Verified supported (language): The CLI includes a bytecode VM, an interpreter and optional JIT paths. Check which backends work with the runtime version and target you choose.

Sources: https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/main.rs

Zerolang — Verified supported (language): The graph-backed package ran a greeting and an arithmetic test on macOS x64. Other targets were not executed.

Sources: https://github.com/vercel-labs/zerolang/blob/5b3a90a7756e48ab449eb16e688044b8decec7a9/docs/articles/concepts/compile-path.md, https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/runtime-review-2026-10-19

### Formal proof

Kujo — Unknown / not verified (language): We did not establish a general dependent-type proof system in Kujo. The phrase “proves it works” should not be read as mathematical verification of arbitrary code.

Sources: https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/type_checker.rs

Zerolang — Unknown / not verified (language): General theorem proving was not established. Graph validation and executable tests answer narrower questions.

Sources: https://github.com/vercel-labs/zerolang/blob/5b3a90a7756e48ab449eb16e688044b8decec7a9/docs/articles/concepts/graph-architecture.md, https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/runtime-review-2026-10-19

### Workflow evidence

Kujo — Verified supported (first-party ecosystem): RunLedger stores supplied verdicts, commands and tests with Git metadata. Workcell records execution receipts. Follow these records to the underlying checks; a receipt or correlation ID alone does not prove the result correct.

Sources: https://github.com/kujolang/runledger/blob/334ddd4d33c8cb2612c8edab971ee69170824133/src/record.kujo, https://github.com/kujolang/workcell/blob/a276a92c6bac9279a8cb36ace9687ade34d5128f/src/receipts/receipt.kujo

Zerolang — Verified supported (toolchain): Graph hashes, structured patch outcomes and projection checks provide review evidence. A separate end-to-end run ledger was not assessed.

Sources: https://github.com/vercel-labs/zerolang/blob/5b3a90a7756e48ab449eb16e688044b8decec7a9/native/zero-c/src/program_graph_patch.c, https://github.com/vercel-labs/zerolang/blob/5b3a90a7756e48ab449eb16e688044b8decec7a9/docs/articles/concepts/projections.md, https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/runtime-review-2026-10-19

## Technical deep dive

Compare compiler-checked graph edits with task checks and retained workflow evidence.

Do you need a safer editing interface, evidence of the outcome, or both?

### Program representation: Agents edit the compiler’s graph

The graph stores program facts rather than treating source text as the only authority. Queries expose semantic handles; patch operations change those facts. The normal package compile path loads zero.graph.

Evaluation implication: Evaluate the actual edit and query operations your agent needs; do not infer lower token cost from the architecture alone.

Sources: https://github.com/vercel-labs/zerolang/blob/5b3a90a7756e48ab449eb16e688044b8decec7a9/docs/articles/concepts/graph-architecture.md, https://github.com/vercel-labs/zerolang/blob/5b3a90a7756e48ab449eb16e688044b8decec7a9/docs/articles/concepts/compile-path.md

### Patch validation: Reject stale or invalid edits before saving

The inspected patch implementation checks the expected graph hash and validates graph shape. Executed release fixtures also rejected a Bool return in an i32 function. Both negative cases preserved the stored graph byte for byte.

Evaluation implication: This verifies two rejection paths, not every patch operation or concurrent-writer scenario.

Sources: https://github.com/vercel-labs/zerolang/blob/5b3a90a7756e48ab449eb16e688044b8decec7a9/native/zero-c/src/program_graph_patch.c, https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/runtime-review-2026-10-19

### Human review: Keep projections and graph state consistent

Export produces readable .0 text. Verify-projection detects divergence. Pinned documentation also describes automatic refresh when only source text changed, conflict errors when both sides changed, and ZERO_STALE=fail for stricter behavior.

Evaluation implication: Our export and drift fixtures passed. Automatic refresh, conflict resolution and merge behavior were inspected in documentation but not exercised.

Sources: https://github.com/vercel-labs/zerolang/blob/5b3a90a7756e48ab449eb16e688044b8decec7a9/docs/articles/concepts/projections.md, https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/runtime-review-2026-10-19

## Decision scenarios

Proposed evaluation criteria, not comparative benchmark results.

### Agent changes a function

Kujo: Use external checks to enforce the task’s expected outcome.

Zerolang: Query graph facts and submit a patch with stale-state protection.

Evidence to collect: Before/after graph identity, patch result and independent acceptance output.

### Human reviews an agent edit

Kujo: Retain the artifact and check output in a run record.

Zerolang: Export .0 text and verify projection consistency.

Evidence to collect: Readable diff plus a passing projection check; resolve conflicts explicitly.

### Release to a new platform

Kujo: Check the chosen deployment environment and isolation configuration.

Zerolang: Test the required backend, graph shape and target locally.

Evidence to collect: Target-specific build and execution evidence; our review covered macOS x64 only.

## A focused evaluation plan

Proposed steps; no competitor runtime test is claimed.

### Pin the release

Use Zerolang 0.3.4 and record the downloaded binary hash. Check newer releases independently; do not assume main and a published binary behave identically.

### Exercise a rejected edit

Try a stale graph hash and a wrong return type. Require nonzero exits and verify that zero.graph did not change.

### Separate checks from tests

Run one passing assertion, then deliberately change its expected value. Record the failure and test count; a no-tests success is not behavioral coverage.

### Review the same program

Export and verify the projection, then introduce drift and observe the diagnostic. Add your own task-level acceptance checks before considering deployment.

## Which Zero is being compared?

This page covers Vercel’s experimental Zerolang at zerolang.ai and vercel-labs/zerolang. The earlier page covered the unrelated systems-language preview at zero-lang.com. Its C++ and value-semantics descriptions do not describe this repository. We now pin this comparison to published Zerolang 0.3.4, rather than mixing its release behavior with current main.

## Technical architecture

Zerolang stores declarations, types, calls and related facts in zero.graph. Agents query and patch that graph; humans can export readable .0 projections. The normal package compile path consumes the graph. Our stale-hash and wrong-return-type patches failed without changing the stored graph. Kujo’s separate workflow tools check task contracts and observed outcomes; they do not provide this graph-editing model.

## When to choose Kujo

Evaluate Kujo when your main need is to define acceptance criteria, check generated artifacts or process outcomes, and retain evidence across a workflow. Plan the separate tools and their configuration. A successful kujo check in 1.8.2 is not a complete type-correctness guarantee.

## When to choose Zerolang

Evaluate Zerolang when compiler-aware agent edits, graph queries and reviewable source projections fit your development process. Its checked patch interface gives agents a narrower editing surface than unrestricted text replacement. Treat it as an experiment: validate the graph shapes, platform and dependencies your application needs before adopting it.

## Can you use both?

A process or file boundary could connect a Zerolang component to external acceptance checks and run records. No direct Kujo integration was tested. Keep the graph hash, compiler version, test output and projection state together so a reviewer can connect a checked edit to the artifact that ran.

## Honest limitations

A valid graph can still implement the wrong behavior. Our graph check passed while a deliberately incorrect expected result made zero test fail. We did not establish general theorem proving, production sandbox security, cross-target support or a speed advantage. Runtime capability facts are not a substitute for an operating-system isolation boundary.

## Examples and benchmark evidence

On macOS x86_64, release 0.3.4 initialized a package, applied a valid graph patch and ran a greeting. An addition test passed; changing its expectation failed. Stale and ill-typed patches left the graph unchanged. Projection export and verification passed, and edited projection text failed verification. These are small contract checks, not a workload benchmark or exhaustive compiler audit.

## Frequently asked questions

### Is Zerolang an AI-native language?

Vercel explicitly designs Zerolang for agents: they query a compiler-owned graph and submit checked edits. This design goal does not establish better productivity or correctness on every task.

### Is this the Zero language at zero-lang.com?

No. This page now covers zerolang.ai and vercel-labs/zerolang. They are different projects, and the old systems-preview claims should not be carried across.

### Does a checked graph prove the program meets its requirements?

No. Our valid graph passed check while a deliberately wrong test expectation failed. Keep type and structural validation separate from behavioral tests and external acceptance criteria.

## References

- [Vercel Zerolang graph architecture](https://github.com/vercel-labs/zerolang/blob/5b3a90a7756e48ab449eb16e688044b8decec7a9/docs/articles/concepts/graph-architecture.md) — pinned official documentation; v0.3.4; 5b3a90a7756e48ab449eb16e688044b8decec7a9; reviewed 2026-10-19.
- [Zerolang graph compile path](https://github.com/vercel-labs/zerolang/blob/5b3a90a7756e48ab449eb16e688044b8decec7a9/docs/articles/concepts/compile-path.md) — pinned official documentation; v0.3.4; 5b3a90a7756e48ab449eb16e688044b8decec7a9; reviewed 2026-10-19.
- [Zerolang patch validation implementation](https://github.com/vercel-labs/zerolang/blob/5b3a90a7756e48ab449eb16e688044b8decec7a9/native/zero-c/src/program_graph_patch.c) — implementation inspected; selected release cases executed; v0.3.4; 5b3a90a7756e48ab449eb16e688044b8decec7a9; reviewed 2026-10-19.
- [Zerolang projection synchronization](https://github.com/vercel-labs/zerolang/blob/5b3a90a7756e48ab449eb16e688044b8decec7a9/docs/articles/concepts/projections.md) — documentation inspected; export and drift checks executed; v0.3.4; 5b3a90a7756e48ab449eb16e688044b8decec7a9; reviewed 2026-10-19.
- [Zerolang published release](https://github.com/vercel-labs/zerolang/releases/tag/v0.3.4) — official release metadata; macOS x64 binary exercised; 0.3.4; released 2026-06-13; reviewed 2026-10-19.
- [Competitor runtime fixtures and raw outcomes](https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/runtime-review-2026-10-19) — local execution receipts; bounded fixtures; Bend 2.0.37; BAML 0.22.2; Zerolang 0.3.4; macOS x86_64; reviewed 2026-10-19.
- [Kujo runtime and CLI source](https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/main.rs) — implementation inspected; Kujo 1.8.2 source snapshot; reviewed 2026-10-19.
- [Kujo type checker](https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/type_checker.rs) — implementation inspected; 549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1; reviewed 2026-10-19.
- [Spec scope and implementation](https://github.com/kujolang/spec/blob/1211f37a09314be7150734bf15a55e9b2ea6504d/src/validate.kujo) — implementation inspected; 1211f37a09314be7150734bf15a55e9b2ea6504d; reviewed 2026-10-19.
- [Eval scope and implementation](https://github.com/kujolang/eval/blob/71e66dff780d6930bcbe093c046bf31aa26411df/src/checks.kujo) — implementation inspected; 71e66dff780d6930bcbe093c046bf31aa26411df; reviewed 2026-10-19.
- [Runledger scope and implementation](https://github.com/kujolang/runledger/blob/334ddd4d33c8cb2612c8edab971ee69170824133/src/record.kujo) — implementation inspected; 334ddd4d33c8cb2612c8edab971ee69170824133; reviewed 2026-10-19.
- [Workcell scope and implementation](https://github.com/kujolang/workcell/blob/a276a92c6bac9279a8cb36ace9687ade34d5128f/src/receipts/receipt.kujo) — implementation inspected; a276a92c6bac9279a8cb36ace9687ade34d5128f; reviewed 2026-10-19.

## Related pages

- [AI-native programming languages: a practical comparison](https://kujolang.ai/compare/ai-native-programming-languages/)
- [AI code verification tools: what each check can establish](https://kujolang.ai/compare/ai-code-verification-tools/)
- [Verify agent workflows: contracts, checks and reproducible evidence](https://kujolang.ai/compare/verify-agent-workflows/)

[Editorial policy](https://kujolang.ai/compare/editorial-policy.md) · [Report inaccuracies](https://github.com/kujolang/kujolang.ai/issues/new)
