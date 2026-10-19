---
title: "Kujo vs BAML: comparing agent development workflows"
description: "Compare current BAML and Kujo across type checking, evaluations, execution evidence, adoption and the boundaries of each toolchain."
seo_title: "Kujo vs BAML: comparing agent development workflows"
custom_url: "kujo-vs-baml"
date: "2026-10-19"
author: "1"
social_image: "/assets/images/social/kujo-vs-baml.jpg"
---

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
