# Kujo vs Zero: workflow accountability and systems semantics

This page compares Kujo with the developer-preview language at zero-lang.com. Zero documents value semantics, deterministic cleanup and structured concurrency. Kujo provides a language and separate tools for checking agent work. We could not establish Zero’s official source repository or a numbered release, so its capabilities here rest on documentation rather than inspected implementation.

Last reviewed: 2026-10-19. Canonical page: https://kujolang.ai/compare/kujo-vs-zero/

## At a glance

Zero: https://zero-lang.com/

Documentation: https://zero-lang.com/download.html

Version: Developer preview; numbered release not verified

Repository: Canonical repository not verified from the reviewed official pages.

## Capability matrix

### Primary purpose

Kujo — Verified supported (language and first-party ecosystem): Kujo provides a language and separate tools for defining agent tasks, checking results and keeping run evidence.

Sources: https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/main.rs, https://github.com/kujolang/spec/blob/1211f37a09314be7150734bf15a55e9b2ea6504d/src/validate.kujo, https://github.com/kujolang/eval/blob/71e66dff780d6930bcbe093c046bf31aa26411df/src/checks.kujo

Zero — Partially supported (language): Predictable systems behavior with value semantics and structured concurrency, according to the website.

Sources: https://zero-lang.com/

### Static checks

Kujo — Verified supported (language and first-party ecosystem): The runtime checks types. Spec validates task records, and Eval checks selected outputs. Passing those checks does not prove arbitrary programs correct.

Sources: https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/type_checker.rs, https://github.com/kujolang/spec/blob/1211f37a09314be7150734bf15a55e9b2ea6504d/src/validate.kujo, https://github.com/kujolang/eval/blob/71e66dff780d6930bcbe093c046bf31aa26411df/src/checks.kujo

Zero — Partially supported (language): The installation guide documents a check-only compiler mode; implementation not inspected.

Sources: https://zero-lang.com/download.html

### Execution

Kujo — Verified supported (language): The CLI includes a bytecode VM, an interpreter and optional JIT paths. Check which backends work with the runtime version and target you choose.

Sources: https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/main.rs

Zero — Partially supported (language): Interpreter, native JIT, native executable and C++ output modes are documented.

Sources: https://zero-lang.com/download.html

### Formal proof

Kujo — Unknown / not verified (language): We did not establish a general dependent-type proof system in Kujo. The phrase “proves it works” should not be read as mathematical verification of arbitrary code.

Sources: https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/type_checker.rs

Zero — Unknown / not verified (language): General theorem proving was not verified. Deterministic semantics alone do not establish it.

Sources: https://zero-lang.com/

### Workflow evidence

Kujo — Verified supported (first-party ecosystem): RunLedger stores supplied verdicts, commands and tests with Git metadata. Workcell records execution receipts. Follow these records to the underlying checks; a receipt or correlation ID alone does not prove the result correct.

Sources: https://github.com/kujolang/runledger/blob/334ddd4d33c8cb2612c8edab971ee69170824133/src/record.kujo, https://github.com/kujolang/workcell/blob/a276a92c6bac9279a8cb36ace9687ade34d5128f/src/receipts/receipt.kujo

Zero — Unknown / not verified (toolchain): Agent task contracts and a run-receipt system were not verified.

Sources: https://zero-lang.com/, https://zero-lang.com/download.html

## Technical deep dive

Compare Zero’s systems model with Kujo’s tools for checking agent work.

Which behavior must be predictable: resources, execution, or the delivery process?

### Project identity: Check what the preview’s documentation establishes

This comparison identifies Zero by zero-lang.com. A canonical repository and numbered release were not established in the reviewed official pages. That limits independent inspection of implementation and release maturity.

Evaluation implication: Treat source identity and a reproducible compiler version as prerequisites for a production trial.

Sources: https://zero-lang.com/, https://zero-lang.com/download.html

### Systems model: Predictable cleanup does not make every outcome repeatable

The website describes value semantics, deterministic cleanup and structured concurrency. Those are programming-model claims, not evidence of reproducible builds, deterministic network responses or a recorded agent workflow.

Evaluation implication: Choose resource-lifetime and cancellation cases that matter to your application; observe them on an identified toolchain.

Sources: https://zero-lang.com/

### Execution targets: Native and browser modes have different scope

The install page describes interpreter, JIT, native executable and C++ output modes, and distinguishes the WebAssembly browser compiler from native-library and native-code generation support. These capabilities were not reproduced locally.

Evaluation implication: Validate your target and required native dependencies before treating a browser example as deployment evidence.

Sources: https://zero-lang.com/download.html

## Decision scenarios

Proposed evaluation criteria, not comparative benchmark results.

### Resource-sensitive application

Kujo: Evaluate the actual runtime behavior separately from workflow tools.

Zero: Explore the documented value, cleanup and concurrency model.

Evidence to collect: An identified compiler plus lifecycle and cancellation observations.

### Browser experiment to native delivery

Kujo: Keep artifact and deployment checks explicit for each target.

Zero: Confirm the difference between browser compiler and native modes.

Evidence to collect: Target-specific build and dependency evidence, not just a browser demo.

### Auditable agent changes

Kujo: Use task, check and execution-evidence tools around deliverables.

Zero: A comparable receipt system was not verified in this review.

Evidence to collect: Independent checks and records; unknown support is not an absence claim.

## A focused evaluation plan

Proposed steps; no competitor runtime test is claimed.

### Resolve the baseline

Establish the compiler revision, supported platform and source/release provenance before running a dependency decision. This review leaves the repository and numbered release unknown.

### Choose a lifecycle case

Use an example involving resource ownership, cleanup or cancellation. Write down the expected behavior before observing the program. This is a proposed evaluation, not a reported result.

### Verify the deployment target

Test the chosen interpreter, native or generated-code mode on the required platform. Validate native-library support independently of browser examples.

### Add external acceptance checks

Check artifacts and process failures with an independent checker, retain the toolchain identity, and keep documentation claims distinct from your measured outcomes.

## Which Zero is being compared?

This page covers only the language at zero-lang.com and the compiler described on its installation page. It does not cover other languages, databases or sync tools named Zero. The official pages and search results we reviewed did not identify an official repository, so we have not guessed a GitHub link.

## Technical architecture

Zero’s installation guide documents interpreter, native JIT, native executable and C++ output modes. It distinguishes the WebAssembly browser compiler from support for native libraries and code generation. We did not reproduce these capabilities locally. Kujo’s inspected CLI supports VM and interpreter execution with optional JIT paths; its workflow tools do not change the language’s memory model.

## When to choose Kujo

Evaluate Kujo when you need to define an agent’s task, check its deliverables and keep a reviewable run record. Its separate tools address those needs. This does not establish an advantage over Zero in numerical performance or memory behavior.

## When to choose Zero

Try Zero’s preview if its documented value semantics and systems behavior suit your workload. Explore the browser examples, then establish source access, platform support and release policy before depending on it. Resource cleanup and concurrency behavior may matter more to your application than agent-workflow tools.

## Can you use both?

A process or file interface could connect the languages, but we did not test a Kujo–Zero integration. First identify a repeatable Zero toolchain, then check its exit codes, data formats and native-library interfaces.

## Honest limitations

Without a verified source repository or release version, we cannot independently assess Zero’s implementation, security boundaries or maturity. Kujo’s evidence tools also require configuration and meaningful checks. Deterministic cleanup alone does not make network responses or builds repeatable, or create an auditable agent run.

## Examples and benchmark evidence

We did not run a Zero example or comparative benchmark. The official installation page includes an assertion-based example, but reproducing it requires an identified compiler revision. This page therefore describes the documented architecture without presenting it as tested behavior.

## Frequently asked questions

### Is Zero an AI-native language?

The reviewed Zero homepage emphasizes systems semantics. This page does not infer an AI-agent design goal from its name or from inclusion in a comparison list.

### Why is the repository missing?

The official pages reviewed did not establish a canonical repository. Keeping that field unknown is more useful than linking a different project with the same name.

## References

- [Zero language overview](https://zero-lang.com/) — official documentation; implementation not inspected; Developer preview; release identifier unverified; reviewed 2026-10-19.
- [Zero execution modes](https://zero-lang.com/download.html) — official documentation; implementation not inspected; Documentation snapshot; no release version asserted; reviewed 2026-10-19.
- [Kujo runtime and CLI source](https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/main.rs) — implementation inspected; Kujo 1.8.2 source snapshot; reviewed 2026-10-19.
- [Spec scope and implementation](https://github.com/kujolang/spec/blob/1211f37a09314be7150734bf15a55e9b2ea6504d/src/validate.kujo) — implementation inspected; 1211f37a09314be7150734bf15a55e9b2ea6504d; reviewed 2026-10-19.
- [Eval scope and implementation](https://github.com/kujolang/eval/blob/71e66dff780d6930bcbe093c046bf31aa26411df/src/checks.kujo) — implementation inspected; 71e66dff780d6930bcbe093c046bf31aa26411df; reviewed 2026-10-19.
- [Runledger scope and implementation](https://github.com/kujolang/runledger/blob/334ddd4d33c8cb2612c8edab971ee69170824133/src/record.kujo) — implementation inspected; 334ddd4d33c8cb2612c8edab971ee69170824133; reviewed 2026-10-19.
- [Workcell scope and implementation](https://github.com/kujolang/workcell/blob/a276a92c6bac9279a8cb36ace9687ade34d5128f/src/receipts/receipt.kujo) — implementation inspected; a276a92c6bac9279a8cb36ace9687ade34d5128f; reviewed 2026-10-19.

## Related pages

- [AI-native programming languages: a practical comparison](https://kujolang.ai/compare/ai-native-programming-languages/)
- [AI code verification tools: what each check can establish](https://kujolang.ai/compare/ai-code-verification-tools/)
- [Verify agent workflows: contracts, checks and reproducible evidence](https://kujolang.ai/compare/verify-agent-workflows/)

[Editorial policy](https://kujolang.ai/compare/editorial-policy.md) · [Report inaccuracies](https://github.com/kujolang/kujolang.ai/issues/new)
