---
template: "comparison-direct"
title: "Kujo vs BAML: comparing agent development workflows"
description: "Compare current BAML and Kujo across type checking, evaluations, execution evidence, adoption and the boundaries of each toolchain."
seo_title: "Kujo vs BAML: comparing agent development workflows"
custom_url: "kujo-vs-baml"
date: "2026-10-19"
author: "1"
social_image: "/assets/images/social/kujo-vs-baml.jpg"
---

Current BAML is a language for agents, with its own runtime and bridges into other languages. Kujo is also a programming language, with separate tools for defining tasks, checking outputs and recording runs. Compare them on the same application requirement, including the work needed to integrate and maintain each option.

Last reviewed: 2026-10-19. Canonical page: https://kujolang.ai/compare/kujo-vs-baml/

## At a glance

BAML: https://boundaryml.com/

Documentation: https://boundaryml.com/quickstart

Version: Stable language toolchain and Python bridge 0.22.2 (toolchain released 2026-10-13; commit 01f5c412c73c213846ea8cb6ead89d303b053672). Runtime and generated Python client tested on macOS x86_64. The nightly channel was not tested.

Repository: https://github.com/BoundaryML/baml

## Capability matrix

### Primary purpose

Kujo — Verified supported (language and first-party ecosystem): Kujo provides a language and separate tools for defining agent tasks, checking results and keeping run evidence.

Sources: https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/main.rs, https://github.com/kujolang/spec/blob/1211f37a09314be7150734bf15a55e9b2ea6504d/src/validate.kujo, https://github.com/kujolang/eval/blob/71e66dff780d6930bcbe093c046bf31aa26411df/src/checks.kujo

BAML — Partially supported (language and toolchain): An agent-oriented language with AI functions and incremental host-language adoption.

Sources: https://boundaryml.com/

### Static diagnostics

Kujo — Verified supported (language and first-party ecosystem): In Kujo 1.8.2, `kujo check` parses and compiles without executing; it is not a complete type-enforcement gate. Interpreter type diagnostics can be warnings. Spec validates task records, and Eval checks selected outputs; none proves arbitrary programs correct.

Sources: https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/main.rs, https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/type_checker.rs, https://github.com/kujolang/spec/blob/1211f37a09314be7150734bf15a55e9b2ea6504d/src/validate.kujo, https://github.com/kujolang/eval/blob/71e66dff780d6930bcbe093c046bf31aa26411df/src/checks.kujo

BAML — Verified supported (language): Project diagnostics are implemented by the current check command.

Sources: https://github.com/BoundaryML/baml/blob/01f5c412c73c213846ea8cb6ead89d303b053672/baml_language/crates/baml_cli/src/check_command.rs

### Testing and evaluations

Kujo — Verified supported (language and first-party ecosystem): In Kujo 1.8.2, `kujo check` parses and compiles without executing; it is not a complete type-enforcement gate. Interpreter type diagnostics can be warnings. Spec validates task records, and Eval checks selected outputs; none proves arbitrary programs correct.

Sources: https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/main.rs, https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/type_checker.rs, https://github.com/kujolang/spec/blob/1211f37a09314be7150734bf15a55e9b2ea6504d/src/validate.kujo, https://github.com/kujolang/eval/blob/71e66dff780d6930bcbe093c046bf31aa26411df/src/checks.kujo

BAML — Verified supported (toolchain): Local assertions passed and failed as expected. Mock-provider response parsing accepted a valid object and rejected an invalid field; the full upstream suite was not run.

Sources: https://github.com/BoundaryML/baml/blob/01f5c412c73c213846ea8cb6ead89d303b053672/baml_language/crates/baml_cli/src/test_command.rs, https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/runtime-review-2026-10-19, https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/runtime-gap-review-2026-10-19

### Execution

Kujo — Verified supported (language): The CLI includes a bytecode VM, an interpreter and optional JIT paths. Check which backends work with the runtime version and target you choose.

Sources: https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/main.rs

BAML — Verified supported (toolchain and Python bridge): The 0.22.2 Python client passed sync/async calls, a packed executable returned 42, and loopback-provider response fixtures passed. Hosted models and other packaging targets were not tested.

Sources: https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/runtime-gap-review-2026-10-19

### Formal proof

Kujo — Unknown / not verified (language): We did not establish a general dependent-type proof system in Kujo. The phrase “proves it works” should not be read as mathematical verification of arbitrary code.

Sources: https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/type_checker.rs

BAML — Unknown / not verified (language): A general dependent-type proof guarantee was not verified in the reviewed sources.

Sources: https://github.com/BoundaryML/baml/blob/01f5c412c73c213846ea8cb6ead89d303b053672/baml_language/crates/baml_cli/src/check_command.rs

### Observability

Kujo — Verified supported (first-party ecosystem): RunLedger stores supplied verdicts, commands and tests with Git metadata. Workcell records execution receipts. Follow these records to the underlying checks; a receipt or correlation ID alone does not prove the result correct.

Sources: https://github.com/kujolang/runledger/blob/334ddd4d33c8cb2612c8edab971ee69170824133/src/record.kujo, https://github.com/kujolang/workcell/blob/a276a92c6bac9279a8cb36ace9687ade34d5128f/src/receipts/receipt.kujo

BAML — Verified supported (toolchain): Local BTEL recordings and SQL queries recovered success/error outcomes and profiler counts. Trace context reached a generated-client call without leaking into the next call. Cloud delivery and overhead remain untested.

Sources: https://boundaryml.com/, https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/runtime-gap-review-2026-10-19

## Technical deep dive

Compare BAML’s AI application tools with Kujo’s workflow checks and records.

Are you adopting an AI component, or governing an entire agent change?

### Language and compiler: Check the generation you are adopting

The pinned BAML source includes compiler diagnostics and a check command. Its current positioning includes an agent language and standalone runtime, so older prompt-DSL examples are not sufficient evidence for the current toolchain.

Evaluation implication: Pin the source or release before choosing syntax, examples and integration assumptions.

Sources: https://boundaryml.com/, https://github.com/BoundaryML/baml/blob/01f5c412c73c213846ea8cb6ead89d303b053672/baml_language/crates/baml_cli/src/check_command.rs

### Tests and outputs: A valid data type can still contain the wrong answer

The inspected test command loads and runs compiled test sets. Our 0.22.2 fixture passed one assertion and failed a deliberately wrong expectation. This exercises a local test set, not the repository’s full suite. A typed or parsed AI response still needs checks for factual and domain correctness.

Evaluation implication: Pair type/shape checks with an independent domain-specific check and known wrong answers.

Sources: https://github.com/BoundaryML/baml/blob/01f5c412c73c213846ea8cb6ead89d303b053672/baml_language/crates/baml_cli/src/test_command.rs, https://github.com/BoundaryML/baml/blob/01f5c412c73c213846ea8cb6ead89d303b053672/baml_language/crates/baml_cli/src/check_command.rs, https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/runtime-review-2026-10-19

### Integration and tracing: Verify the host boundary independently

The Python bridge passed synchronous and asynchronous calls and propagated a declared error. Local tracing recorded outcomes and kept invocation context separate. Our deeper type-boundary tests distinguish static signatures, call argument checks, Pydantic class validation and model-response parsing. They also found a process crash for an invalid string passed to integer arithmetic in 0.22.2; valid arithmetic returned 42.

Evaluation implication: Test the exact host language, supported boundary types, failure propagation and retained trace data.

Sources: https://boundaryml.com/quickstart, https://boundaryml.com/, https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/runtime-gap-review-2026-10-19, https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/baml-python-boundary-2026-10-19

## Decision scenarios

Proposed evaluation criteria, not comparative benchmark results.

### One AI feature in an existing app

Kujo: Use external acceptance checks around the application output.

BAML: Evaluate typed AI functions and the documented host bridge.

Evidence to collect: A pinned host/runtime pair plus valid and invalid response fixtures.

### A generated answer must be correct

Kujo: Specify domain criteria and evaluate the actual artifact.

BAML: Use language diagnostics and tests, then validate answer semantics.

Evidence to collect: An independent check that rejects a well-typed but wrong answer.

### An agent changes code across a repo

Kujo: Compose task, evaluation and run-record tooling.

BAML: Retain application test and trace results for review.

Evidence to collect: Commands, versions, failures and evidence tied to the actual revision.

## A focused evaluation plan

Proposed steps for your own evaluation; executed fixtures are recorded separately.

### Pin the integration

Choose one AI function and the exact host language/runtime versions. Check the current quickstart against the pinned source; do not mix generations of examples.

### Separate failure classes

Prepare malformed data, well-shaped but incorrect data, and a valid answer. Use the first to challenge representation checks and the second to challenge domain assertions.

### Exercise the host boundary

Test exceptions, timeouts and boundary types in your own application. A documented bridge is not evidence that every required type or failure mode works for your chosen combination.

### Retain the evidence

Store check/test output and the domain-specific check result with the code revision. Measure latency or token cost only with a declared model, configuration and repeated-run method.

## What the Python boundary validates

These are separate checks, not one blanket type-safety guarantee. We tested the 0.22.2 CLI and Python bridge on macOS x86_64 with Python 3.10 and Pydantic 2.14.1. Each risky call ran in its own process. Official bridge docs describe type mappings and execution; the pinned source and fixtures establish the narrower behavior below.

| Validation layer | Fixture | Observed result | Limit and evidence |
| --- | --- | --- | --- |
| Static checks | Call echo(value: int) with a string in BAML source and typed Python. | BAML check rejected the call; mypy 2.4.0 rejected the generated Python call. Valid integer controls passed. | Static checks help when callers are checked. They do not automatically validate arbitrary values received at runtime. https://developer.boundaryml.com/baml/language/functions, https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/baml-python-boundary-2026-10-19 |
| Call shape and representation | Omit an argument, duplicate it, add an unknown name, pass an unsupported object or an oversized integer. | These fixtures raised errors. | Argument names, serialization and numeric range checks are not a complete check of the declared parameter type. https://github.com/BoundaryML/baml/blob/01f5c412c73c213846ea8cb6ead89d303b053672/baml_language/sdks/python/README.md, https://github.com/BoundaryML/baml/blob/01f5c412c73c213846ea8cb6ead89d303b053672/baml_language/sdks/python/src/baml_bridge/proto.py, https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/baml-python-boundary-2026-10-19 |
| Plain values and collections | Pass a string to int identity functions, or a mixed list to int[]. | Sync and async identity calls returned the string. The mixed list also returned unchanged. An int? fixture rejected the string. | Validation varies by type and operation. The declared primitive return type did not enforce the observed result; do not generalize this to optional or class paths. https://github.com/BoundaryML/baml/blob/01f5c412c73c213846ea8cb6ead89d303b053672/baml_language/crates/bex_engine/src/conversion.rs, https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/baml-python-boundary-2026-10-19 |
| Generated classes | Construct Answer(value="bad"), or return a class with an invalid field. | Pydantic raised ValidationError. Answer(value="42") became Answer(value=42); strict validation rejected that string. | Class construction and decoding validate fields. A deliberately bypassed or later-mutated model could still yield a bad primitive field value. https://github.com/BoundaryML/baml/blob/01f5c412c73c213846ea8cb6ead89d303b053672/baml_language/sdks/python/src/baml_bridge/proto.py, https://docs.pydantic.dev/latest/concepts/strict_mode/, https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/baml-python-boundary-2026-10-19 |
| Model-response parsing | Parse objects containing value 42, "bad", "42" and 41 through the generated function specification. | 42 passed; "bad" raised ParseError; "42" was coerced to 42; 41 also passed. | Schema-aligned parsing can repair or coerce data. A structurally valid value is not proof that the answer meets a business requirement. These parser tests made no model request. https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/baml-python-boundary-2026-10-19, https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/runtime-gap-review-2026-10-19 |
| Invalid values used in arithmetic | Call plus(value: int) -> int { value + 1 } with 41 and then "bad". | 41 returned 42. The string caused SIGSEGV in separate processes, both with and without the sandbox. | This is a confirmed release/platform-specific failure, not a caught validation exception. Its native root cause and behavior on other targets remain unverified. https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/baml-python-boundary-2026-10-19 |
| Application validation | Validate the input with TypeAdapter(int).validate_python(value, strict=True) before calling BAML. | The numeric string was rejected; validated integer arithmetic returned 42. | This is an application-side guard tested for int. Validate the full input schema and retain domain-specific assertions; do not assume this one wrapper covers every BAML type. https://docs.pydantic.dev/latest/concepts/strict_mode/, https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/baml-python-boundary-2026-10-19 |

## Technical architecture

The BAML source we reviewed contains a compiler, a check command that collects project diagnostics and a test command that runs compiled test sets. Its current website describes typed AI functions, concurrency and tracing. These claims do not establish a speed advantage over Kujo. Kujo handles language execution in its runtime and provides task contracts and run records through separately versioned tools.

## When to choose Kujo

Consider Kujo when you need explicit acceptance criteria, checks of files and processes, and run evidence you can inspect without a hosted dashboard. Include the cost of configuring and maintaining those tools. A ledger entry marked pass should link to the check output that supports it.

## When to choose BAML

Consider BAML when you need typed AI functions within an existing application. Its quickstart and language bridges offer a starting point for adding one component at a time. Before choosing a bridge, check the supported host language, runtime version and data types.

## Can you use both?

You could connect BAML application code to Kujo workflow tools through a process or service interface. We did not test a direct Kujo bridge, and support for another host language does not imply Kujo support. Define a versioned request/response format and test how failures cross the interface.

## Honest limitations

BAML’s type declarations, generated Python signatures, Pydantic models and model-response parser validate different parts of a call. In 0.22.2, an int identity function returned an invalid Python string unchanged, while an int-addition function given that string crashed an isolated Python process. Optional values and class decoding rejected other invalid fixtures. Use static checking and explicit validation for untrusted host inputs; the dedicated Python boundary review records which paths we tested. These results do not establish behavior in other releases, bridges or operating systems.

## Examples and benchmark evidence

BAML 0.22.2 passed local function and assertion tests and rejected invalid source. Its generated Python client returned 42 synchronously and asynchronously; a standalone packed executable also returned 42. A local mock provider returned a typed object, while an invalid field and HTTP 401 produced distinct errors. Local trace queries recovered successful and failed runs with matching profiler counts. These fixtures do not test hosted models, cloud trace delivery, model quality or performance.

## Frequently asked questions

### Is BAML just an LLM wrapper?

That description does not match the current project. The reviewed repository contains language checking and execution tooling; verify which generation of BAML a tutorial targets.

### Does typed output prove an AI answer is right?

No. Type checks and structured parsing constrain representation. Domain correctness needs assertions, reference data or another suitable validation method.

### Does the generated Python signature validate every runtime value?

No. In our 0.22.2 fixtures, static checking caught a wrong argument, but a direct Python identity call returned the wrong primitive type unchanged. Pydantic class decoding, optional values and model-response parsing had separate validation behavior. An invalid arithmetic input crashed the process. Validate untrusted host inputs explicitly and test the exact bridge version.

## References

- [BAML current language overview](https://boundaryml.com/) — product assertions; not independently benchmarked; Rolling official website; release-specific behavior is documented separately; reviewed 2026-10-19.
- [BAML check command](https://github.com/BoundaryML/baml/blob/01f5c412c73c213846ea8cb6ead89d303b053672/baml_language/crates/baml_cli/src/check_command.rs) — implementation inspected; BAML 0.22.2; release commit 01f5c412c73c213846ea8cb6ead89d303b053672; reviewed 2026-10-19.
- [BAML test runner and result tests](https://github.com/BoundaryML/baml/blob/01f5c412c73c213846ea8cb6ead89d303b053672/baml_language/crates/baml_cli/src/test_command.rs) — implementation and tests inspected; not executed; BAML 0.22.2; release commit 01f5c412c73c213846ea8cb6ead89d303b053672; reviewed 2026-10-19.
- [BAML quickstart](https://boundaryml.com/quickstart) — official documentation; Rolling official website; release-specific behavior is documented separately; reviewed 2026-10-19.
- [Kujo runtime and CLI source](https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/main.rs) — implementation inspected; Kujo 1.8.2 source snapshot; reviewed 2026-10-19.
- [Kujo type checker](https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/type_checker.rs) — implementation inspected; 549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1; reviewed 2026-10-19.
- [Spec scope and implementation](https://github.com/kujolang/spec/blob/1211f37a09314be7150734bf15a55e9b2ea6504d/src/validate.kujo) — implementation inspected; 1211f37a09314be7150734bf15a55e9b2ea6504d; reviewed 2026-10-19.
- [Eval scope and implementation](https://github.com/kujolang/eval/blob/71e66dff780d6930bcbe093c046bf31aa26411df/src/checks.kujo) — implementation inspected; 71e66dff780d6930bcbe093c046bf31aa26411df; reviewed 2026-10-19.
- [Runledger scope and implementation](https://github.com/kujolang/runledger/blob/334ddd4d33c8cb2612c8edab971ee69170824133/src/record.kujo) — implementation inspected; 334ddd4d33c8cb2612c8edab971ee69170824133; reviewed 2026-10-19.
- [BAML stable language toolchain](https://github.com/BoundaryML/baml/releases/tag/baml-language-0.22.2) — official release metadata; 0.22.2; released 2026-10-13; reviewed 2026-10-19.
- [Kujo stable release](https://github.com/kujolang/kujo/releases/tag/v1.8.2) — official release metadata; 1.8.2; released 2026-10-19; reviewed 2026-10-19.
- [Competitor runtime fixtures and raw outcomes](https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/runtime-review-2026-10-19) — local execution receipts; bounded fixtures; Bend 2.0.37; BAML 0.22.2; Zerolang 0.3.4; macOS x86_64; reviewed 2026-10-19.
- [Bend kernel and BAML integration runtime tests](https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/runtime-gap-review-2026-10-19) — release binaries executed; positive and negative fixtures; local mock provider; Bend 2.0.37 with Lean 4.34.0 on Linux x86_64; BAML and Python bridge 0.22.2 on macOS x86_64; reviewed 2026-10-19.
- [BAML Python bridge package contract](https://github.com/BoundaryML/baml/blob/01f5c412c73c213846ea8cb6ead89d303b053672/baml_language/sdks/python/README.md) — official release documentation; BAML CLI/bridge 0.22.2; Python 3.10; Pydantic 2.14.1; macOS x86_64; reviewed 2026-10-19.
- [BAML Python encoding and class validation](https://github.com/BoundaryML/baml/blob/01f5c412c73c213846ea8cb6ead89d303b053672/baml_language/sdks/python/src/baml_bridge/proto.py) — official release source; installed file matched byte for byte; BAML CLI/bridge 0.22.2; Python 3.10; Pydantic 2.14.1; macOS x86_64; reviewed 2026-10-19.
- [BAML runtime argument and return conversions](https://github.com/BoundaryML/baml/blob/01f5c412c73c213846ea8cb6ead89d303b053672/baml_language/crates/bex_engine/src/conversion.rs) — official release source; targeted runtime fixtures; BAML CLI/bridge 0.22.2; Python 3.10; Pydantic 2.14.1; macOS x86_64; reviewed 2026-10-19.
- [BAML current language bridge documentation](https://developer.boundaryml.com/baml/bridges) — rolling official documentation; not a promise of universal runtime argument rejection; BAML CLI/bridge 0.22.2; Python 3.10; Pydantic 2.14.1; macOS x86_64; reviewed 2026-10-19.
- [BAML function declarations and expected types](https://developer.boundaryml.com/baml/language/functions) — rolling official documentation; BAML CLI/bridge 0.22.2; Python 3.10; Pydantic 2.14.1; macOS x86_64; reviewed 2026-10-19.
- [Pydantic coercion and strict validation](https://docs.pydantic.dev/latest/concepts/strict_mode/) — official documentation; Pydantic 2.14.1 fixtures; BAML CLI/bridge 0.22.2; Python 3.10; Pydantic 2.14.1; macOS x86_64; reviewed 2026-10-19.
- [Python type-boundary fixtures and results](https://github.com/kujolang/kujolang.ai/tree/main/comparison/research/baml-python-boundary-2026-10-19) — release-specific static, runtime, parsing and crash-control tests; BAML CLI/bridge 0.22.2; Python 3.10; Pydantic 2.14.1; macOS x86_64; reviewed 2026-10-19.

## Related pages

- [AI-native programming languages: a practical comparison](https://kujolang.ai/compare/ai-native-programming-languages/)
- [AI code verification tools: what each check can establish](https://kujolang.ai/compare/ai-code-verification-tools/)
- [Verify agent workflows: contracts, checks and reproducible evidence](https://kujolang.ai/compare/verify-agent-workflows/)

[Editorial policy](https://kujolang.ai/compare/editorial-policy.md) · [Report inaccuracies](https://github.com/kujolang/kujolang.ai/issues/new)
