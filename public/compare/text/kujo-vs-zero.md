# Kujo vs Zerolang: workflow evidence and checked graph edits

Vercel Zerolang makes the program graph the normal compiler input and lets agents submit checked semantic edits. Kujo combines language execution with separate tools for task requirements, output checks and run records. Our release 0.3.4 review tested graph patches, source refresh, conflicting edits and three-way merges. These approaches address different parts of trusting agent-written software.

Last reviewed: 2026-10-20. Canonical page: https://kujolang.ai/compare/kujo-vs-zero/

## At a glance

Zerolang: https://zerolang.ai/

Documentation: https://zerolang.ai/getting-started

Version: 0.3.4; latest published release checked 2026-10-20. Graph refresh, patch rollback and merge fixtures executed on macOS x86_64; 53 command observations repeated in a fresh run.

Repository: https://github.com/vercel-labs/zerolang

## Capability matrix

### Primary purpose

Kujo — Verified supported (language and first-party ecosystem): Kujo provides a language and separate tools for defining agent tasks, checking results and keeping run evidence.

Sources: https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/main.rs, https://github.com/kujolang/spec/blob/1211f37a09314be7150734bf15a55e9b2ea6504d/src/validate.kujo, https://github.com/kujolang/eval/blob/71e66dff780d6930bcbe093c046bf31aa26411df/src/checks.kujo

Zerolang — Verified supported (language): Graph-native programming for agent queries and checked semantic edits.

Sources: https://github.com/vercel-labs/zerolang/blob/5b3a90a7756e48ab449eb16e688044b8decec7a9/docs/articles/concepts/graph-architecture.md

### Static checks

Kujo — Verified supported (language and first-party ecosystem): In Kujo 1.8.2, `kujo check` parses and compiles without executing; it is not a complete type-enforcement gate. Interpreter type diagnostics can be warnings. Spec validates task records, and Eval checks selected outputs; none proves arbitrary programs correct.

Sources: https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/main.rs, https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/type_checker.rs, https://github.com/kujolang/spec/blob/1211f37a09314be7150734bf15a55e9b2ea6504d/src/validate.kujo, https://github.com/kujolang/eval/blob/71e66dff780d6930bcbe093c046bf31aa26411df/src/checks.kujo, https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/all-page-gap-review-2026-10-20

Zerolang — Verified supported (toolchain): Stale hashes, ill-typed patches and conflicting graph/source edits were rejected. The tested patch failures and merge conflicts preserved stored fixture files.

Sources: https://github.com/vercel-labs/zerolang/blob/5b3a90a7756e48ab449eb16e688044b8decec7a9/native/zero-c/src/program_graph_patch.c, https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/runtime-review-2026-10-19, https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/zerolang-contract-review-2026-10-20

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

Kujo — Verified supported (first-party ecosystem): RunLedger’s tested CLI records supplied verdicts, commands and test results with Git metadata. Workcell’s Linux Docker fixture exported an artifact and verified its receipt; modifying a recorded log made verification fail. These records still need to be matched to the underlying checks.

Sources: https://github.com/kujolang/runledger/blob/334ddd4d33c8cb2612c8edab971ee69170824133/src/record.kujo, https://github.com/kujolang/workcell/blob/a276a92c6bac9279a8cb36ace9687ade34d5128f/src/receipts/receipt.kujo, https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/all-page-gap-review-2026-10-20

Zerolang — Verified supported (toolchain): Graph hashes, patch outcomes, no-write projection checks and explicit conflict diagnostics provide review evidence. Import/export and three-way merge behavior were exercised; a separate end-to-end run ledger was not assessed.

Sources: https://github.com/vercel-labs/zerolang/blob/5b3a90a7756e48ab449eb16e688044b8decec7a9/native/zero-c/src/program_graph_patch.c, https://github.com/vercel-labs/zerolang/blob/5b3a90a7756e48ab449eb16e688044b8decec7a9/docs/articles/concepts/projections.md, https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/runtime-review-2026-10-19, https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/zerolang-contract-review-2026-10-20

## Technical deep dive

Compare compiler-checked graph edits with task checks and retained workflow evidence.

Do you need a safer editing interface, evidence of the outcome, or both?

### Program representation: Agents edit the compiler’s graph

The graph stores program facts rather than treating source text as the only authority. Queries expose semantic handles; patch operations change those facts. The normal package compile path loads zero.graph.

Evaluation implication: Evaluate the actual edit and query operations your agent needs; do not infer lower token cost from the architecture alone.

Sources: https://github.com/vercel-labs/zerolang/blob/5b3a90a7756e48ab449eb16e688044b8decec7a9/docs/articles/concepts/graph-architecture.md, https://github.com/vercel-labs/zerolang/blob/5b3a90a7756e48ab449eb16e688044b8decec7a9/docs/articles/concepts/compile-path.md

### Patch validation: Reject stale or invalid edits before saving

The checked patch interface rejected a stale graph hash and an ill-typed return. A multi-operation patch with a valid first edit and a later failing operation also left the stored files unchanged. A valid --check-only patch reported success without saving.

Evaluation implication: Our fixtures establish rollback for the tested failures. They do not establish crash-safe writes or protection against every concurrent-writer scenario.

Sources: https://github.com/vercel-labs/zerolang/blob/5b3a90a7756e48ab449eb16e688044b8decec7a9/native/zero-c/src/program_graph_patch.c, https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/runtime-review-2026-10-19, https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/zerolang-contract-review-2026-10-20

### Human review: Keep projections and graph state consistent

The 0.3.4 runtime refreshed source-only edits, used graph-only edits with a notice, and rejected conflicting edits. ZERO_STALE=fail blocked automatic refresh. Separate-function changes merged successfully; competing edits to the same value failed without changing the destination.

Evaluation implication: Use verify-projection for a no-write drift check. Review which side should win before using import or export to resolve a conflict.

Sources: https://github.com/vercel-labs/zerolang/blob/5b3a90a7756e48ab449eb16e688044b8decec7a9/docs/articles/concepts/projections.md, https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/runtime-review-2026-10-19, https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/zerolang-contract-review-2026-10-20

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

Proposed steps for your own evaluation; executed fixtures are recorded separately.

### Pin the release

Use Zerolang 0.3.4 and record the downloaded binary hash. Check newer releases independently; do not assume main and a published binary behave identically.

### Exercise a rejected edit

Try a stale graph hash and a wrong return type. Require nonzero exits and verify that zero.graph did not change.

### Separate checks from tests

Run one passing assertion, then deliberately change its expected value. Record the failure and test count; a no-tests success is not behavioral coverage.

### Review the same program

Export and verify the projection, then change each side separately and together. Reproduce strict stale handling and explicit conflict resolution. Add task-level assertions: a consistent graph and projection can still describe the wrong behavior.

## What happens when graph and source edits disagree

We tested these workflows on Zerolang 0.3.4 with the official macOS x86_64 binary. The review contains 53 command observations, repeated in a fresh run. Before/after hashes cover the graph, manifest and source projection; they do not imply that compiler caches were untouched.

| Validation layer | Fixture | Observed result | Limit and evidence |
| --- | --- | --- | --- |
| Source-only changes | Edit the printed text in the .0 projection, then verify, check and run. | Verification rejected drift without writing. Check refreshed zero.graph; execution printed the edited text. Reversed file timestamps did not change that result. | Refresh was tested with a small edit preserving the function set. https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/zerolang-contract-review-2026-10-20, https://github.com/vercel-labs/zerolang/blob/5b3a90a7756e48ab449eb16e688044b8decec7a9/docs/articles/concepts/projections.md |
| Strict stale policy | Set ZERO_STALE=fail before checking an edited source projection. | Check returned RGP008 without changing the fixture files. Explicit import then ran the edited program. | Use this policy when automatic refresh is not appropriate for your workflow. https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/zerolang-contract-review-2026-10-20, https://github.com/vercel-labs/zerolang/blob/5b3a90a7756e48ab449eb16e688044b8decec7a9/docs/articles/concepts/projections.md |
| Graph-only changes | Patch the graph while keeping the previous source projection. | Run used the patched graph and reported the newer graph state. Export synchronized the projection; verification passed. | Review the exported text before treating it as the program that will run. https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/zerolang-contract-review-2026-10-20 |
| Conflicting changes | Edit the graph and source independently. | Check and run returned RGP006 without changing either side. Export selected the graph; import selected the source in a separate fixture. | Import and export choose an authority. Review the changes before discarding the other side. https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/zerolang-contract-review-2026-10-20, https://github.com/vercel-labs/zerolang/blob/5b3a90a7756e48ab449eb16e688044b8decec7a9/docs/articles/concepts/projections.md |
| Invalid edits and rollback | Apply a valid operation followed by an ill-typed or unknown operation; separately import an invalid return type. | Each failed operation preserved the checked files. A wrong graph hash was also rejected. A valid dry run succeeded without saving. | These results cover the named rejection paths, not interrupted writes or every patch operation. https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/zerolang-contract-review-2026-10-20, https://github.com/vercel-labs/zerolang/blob/5b3a90a7756e48ab449eb16e688044b8decec7a9/native/zero-c/src/program_graph_patch.c |
| Independent merge | Change the printed text on one branch and arithmetic in a separate function on another. | Three-way merge succeeded. Runtime printed the text edit, and an executable test confirmed the arithmetic edit: 40 minus 2 returned 38. | This closes the earlier projection-only arithmetic check. Complex multi-file merges and concurrent writers remain untested. https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/zerolang-contract-review-2026-10-20, https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/all-page-gap-review-2026-10-20 |
| Conflicting merge | Change the same printed value differently on two branches. | Merge returned RGM003 and left the destination unchanged. The destination still ran the baseline. | This was a sequential three-way merge fixture, not a simultaneous-writer test. https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/zerolang-contract-review-2026-10-20 |
| Behavioral requirements | Run a passing addition assertion, then add an incorrect expected result. | Graph check passed in both cases. The correct assertion passed; the incorrect expectation made test fail. | A checked edit and a consistent projection do not prove that the program meets your requirements. https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/zerolang-contract-review-2026-10-20, https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/runtime-review-2026-10-19 |

## Which Zero is being compared?

This page covers Vercel’s experimental Zerolang at zerolang.ai and vercel-labs/zerolang. The earlier page covered the unrelated systems-language preview at zero-lang.com. Its C++ and value-semantics descriptions do not describe this repository. We now pin this comparison to published Zerolang 0.3.4, rather than mixing its release behavior with current main.

## Technical architecture

Zerolang stores declarations, types, calls and related facts in zero.graph. Agents query and patch that graph; humans can export readable .0 projections. In our 0.3.4 fixtures, source-only edits refreshed the graph before execution, graph-only edits ran from the graph, and conflicting edits stopped with RGP006. Kujo’s separate workflow tools check task contracts and observed outcomes; they do not provide this graph-editing model.

## When to choose Kujo

Evaluate Kujo when your main need is to define acceptance criteria, check generated artifacts or process outcomes, and retain evidence across a workflow. Plan the separate tools and their configuration. A successful kujo check in 1.8.2 is not a complete type-correctness guarantee.

## When to choose Zerolang

Evaluate Zerolang when compiler-aware agent edits, graph queries and reviewable source projections fit your development process. Its checked patch interface gives agents a narrower editing surface than unrestricted text replacement. Treat it as an experiment: validate the graph shapes, platform and dependencies your application needs before adopting it.

## Can you use both?

A process or file boundary could connect a Zerolang component to external acceptance checks and run records. No direct Kujo integration was tested. Keep the graph hash, compiler version, test output and projection state together so a reviewer can connect a checked edit to the artifact that ran.

## Honest limitations

A valid graph can still implement the wrong behavior: our graph check passed while an incorrect expected result made zero test fail. Import and export resolve source/graph conflicts by selecting a side; they do not combine both intentions. We did not test simultaneous writers, interrupted writes, complex multi-file merges or other runtime targets. Runtime capability facts are not a substitute for an operating-system isolation boundary.

## Examples and benchmark evidence

Our deeper review recorded 53 command observations and repeated them in a fresh run. Failed patches and conflicting merges preserved the checked files. Independent function edits merged, while explicit import and export selected the intended side of a source/graph conflict. Valid graph checks still passed when an incorrect test expectation failed. These are bounded correctness checks on macOS x86_64, not a performance benchmark or an exhaustive compiler audit.

## What this review tested

The extended merge test executed both independent edits: main printed the edited text, and a generated test confirmed that the merged arithmetic returned 38 for 40 and 2. The 55 command observations include the earlier refresh, conflict and rollback controls. Concurrent writers, power-loss recovery and complex multi-file merges remain untested.

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
- [Zerolang graph, projection and merge runtime review](https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/zerolang-contract-review-2026-10-20) — 53 command observations repeated in a fresh run; file hashes, diagnostics and executed outputs; Zerolang 0.3.4 / 5b3a90a7756e48ab449eb16e688044b8decec7a9; macOS x86_64; reviewed 2026-10-20.
- [All-page runtime gap review and retained evidence](https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/all-page-gap-review-2026-10-20) — Pinned ecosystem fixtures; Linux Docker execution; extended Zerolang merge and BAML nightly tests; Kujo 1.8.2 local; Workcell Docker with Kujo 1.6.0; Zerolang 0.3.4; BAML nightly 20261019.a; reviewed 2026-10-20.

## Related pages

- [AI-native programming languages: a practical comparison](https://kujolang.ai/compare/ai-native-programming-languages/)
- [AI code verification tools: what each check can establish](https://kujolang.ai/compare/ai-code-verification-tools/)
- [Verify agent workflows: contracts, checks and reproducible evidence](https://kujolang.ai/compare/verify-agent-workflows/)

[Editorial policy](https://kujolang.ai/compare/editorial-policy.md) · [Report inaccuracies](https://github.com/kujolang/kujolang.ai/issues/new)
