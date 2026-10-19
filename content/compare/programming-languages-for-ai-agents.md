---
template: "comparison-guide"
title: "Programming languages for AI agents: choosing the host and tools"
description: "Choose a language for building and supervising agents by tool contracts, failure handling, deployment and the evidence your workflow needs."
seo_title: "Programming languages for AI agents: choosing the host and tools"
custom_url: "programming-languages-for-ai-agents"
date: "2026-10-19"
author: "1"
social_image: "/assets/images/social/programming-languages-for-ai-agents.jpg"
---

Choose an agent’s host language by the tools it must call, the permissions those tools need and the failures it must recover from. The host coordinates the agent; the repository it edits can use another language. Test the interfaces between them before deciding whether any language change is needed.

Last reviewed: 2026-10-19. Canonical page: https://kujolang.ai/compare/programming-languages-for-ai-agents/

## Choose how your agent runs and uses tools.

Choose the agent host, its tools and the repository it edits separately.

Which component owns each action, failure and recovery?

- Agent host: Coordinates model requests, tool selection and run state.
- Tool boundary: Validates requests and controls external effects.
- Target repository: Keeps its own language, build system and acceptance checks.

## Questions to consider

### Runtime layer: The host and application can use different languages

The host chooses how to coordinate model calls and tool results; the target repository can use another language. Kujo’s Agents SDK is a library layer with explicit adapter boundaries and offline fixtures, not a reason to translate every repository it touches.

Put it into practice: Pin both runtimes and verify the data/process boundary between them.

Sources: https://github.com/kujolang/agents-sdk/blob/6c4a54e74855c605eea67253f6808b16b8c63086/README.md

### Orchestration layer: Recovery needs explicit state

Dispatch documents workflow orchestration and reviewable run state. Treat interrupted work and replay as application design concerns: know what completed, what remains uncertain and which external effects would be unsafe to repeat.

Put it into practice: Test interruption around a side effect, not only between harmless model calls.

Sources: https://github.com/kujolang/dispatch/blob/71ca927c65598ecfe7c1816068e047cf50b915e0/README.md

### Execution layer: Telemetry and authority differ

Workcell’s execution receipts and Watchdog’s telemetry address different aspects of a run. Recording an attempted operation does not itself prevent it; the configured execution boundary must enforce the intended restriction.

Put it into practice: Observe both the reported denial and the absence of the prohibited effect.

Sources: https://github.com/kujolang/workcell/blob/a276a92c6bac9279a8cb36ace9687ade34d5128f/src/receipts/receipt.kujo, https://github.com/kujolang/watchdog/blob/ad6fbc287c626539c1b3a69b4d3d31528b70edaa/README.md

## Choose the host by the interfaces it must own.

Use these criteria to evaluate your actual stack. The failure probes are proposed tests, not claims that a language automatically enforces them.

### Model adapter

Decision to make: Which provider, model and response shape must the host support?

Failure to test: Return malformed or incomplete data from an offline adapter fixture.

Evidence to keep: Pinned adapter version, input, validation outcome and error details.

Sources: https://github.com/kujolang/agents-sdk/blob/6c4a54e74855c605eea67253f6808b16b8c63086/README.md

### Tool arguments

Decision to make: Where are names, arguments and domain constraints checked?

Failure to test: Request an unknown tool and a known tool with an invalid argument.

Evidence to keep: Rejected request and confirmation that no tool effect occurred.

Sources: https://github.com/kujolang/agents-sdk/blob/6c4a54e74855c605eea67253f6808b16b8c63086/README.md

### Permission boundary

Decision to make: Which actions can run, need approval or must remain denied?

Failure to test: Attempt an operation outside the allowed scope.

Evidence to keep: Policy/configuration, denial result and independently observed side effects.

Sources: https://github.com/kujolang/agents-sdk/blob/6c4a54e74855c605eea67253f6808b16b8c63086/README.md, https://github.com/kujolang/workcell/blob/a276a92c6bac9279a8cb36ace9687ade34d5128f/src/receipts/receipt.kujo

### Retry and replay

Decision to make: Which operations are safe to repeat and how are duplicates detected?

Failure to test: Interrupt after an external effect but before its acknowledgement.

Evidence to keep: Operation identity, recovery decision and final effect count.

Sources: https://github.com/kujolang/dispatch/blob/71ca927c65598ecfe7c1816068e047cf50b915e0/README.md

### Target build

Decision to make: How does the host build and inspect a repository in another language?

Failure to test: Return a nonzero build exit and a stale output artifact.

Evidence to keep: Actual revision, command, exit, stdout/stderr and artifact identity.

Sources: https://github.com/kujolang/workcell/blob/a276a92c6bac9279a8cb36ace9687ade34d5128f/src/receipts/receipt.kujo, https://github.com/kujolang/runledger/blob/334ddd4d33c8cb2612c8edab971ee69170824133/src/record.kujo

### Observability

Decision to make: Which run/step/tool identifiers connect the records?

Failure to test: Drop or mismatch a correlation identifier in a fixture.

Evidence to keep: Raw event chain and an explicit incomplete-evidence result.

Sources: https://github.com/kujolang/watchdog/blob/ad6fbc287c626539c1b3a69b4d3d31528b70edaa/README.md, https://github.com/kujolang/agents-sdk/blob/6c4a54e74855c605eea67253f6808b16b8c63086/README.md

## Put the decision into practice

Proposed evaluation steps; not reported benchmark results.

### 1. Map the boundaries

Draw the host, model adapter, tools and target repository as separate components. Mark each place where data or execution authority crosses a boundary.

### 2. Prove the offline path

Use deterministic model/tool fixtures and run success, denial, malformed-result and interruption cases. Label those results as fixtures, not live-provider evidence.

### 3. Add one live integration

Use a single required provider and a narrowly scoped tool. Record configuration and limits, then test the error path as well as the successful response.

### 4. Exercise recovery

Introduce timeouts and interrupted effects deliberately. Require an explicit final state and inspect whether retrying produced duplicate work before broadening the deployment.

## A retry can be correct code and the wrong action.

Illustrative scenario: an agent invokes a tool that writes an external record. Design the recovery policy before enabling automatic retries.

### Tool rejects invalid arguments before dispatch

What you can conclude: This invocation did not reach the effectful operation.

What to check next: A boundary test confirming the underlying operation was not called.

### Tool times out after dispatch

What you can conclude: A timeout leaves completion uncertain; the action may already have happened.

What to check next: Operation identity and an external status lookup or other reconciliation method.

### Host retries without reconciling the first attempt

What you can conclude: The retry could create a second record.

What to check next: Idempotency behavior or an explicit review decision before repeating the operation.

### The host records a final success message

What you can conclude: The message tells you what the host reported.

What to check next: The resulting external state and independent acceptance checks.

## Common interpretation mistakes

### Using one language does not remove the need for access controls

Shared syntax does not collapse model, tool, process and deployment boundaries. Test each separately.

### Passing a fixture does not establish provider reliability

A fixture isolates application logic. It does not measure live service availability or model behavior.

### A trace records an action but does not prevent it

An event log helps you reconstruct a run. You still need a control that rejects prohibited actions.

## Choose the agent host separately from the code it edits

The agent host coordinates model calls and tools. The repository it edits may use a different language, so choosing a host does not require rewriting the application. Record both runtimes and test how generated changes move through the build and execution process.

## Start with integration constraints

List the provider interfaces, application libraries, operating systems and deployment environments you need. Include Python or TypeScript when they already host your application, and Rust when its programming model suits the work. Check specific library versions; a language name does not guarantee an integration.

## Where Kujo fits

Kujo’s Agents SDK provides workflow primitives as a library. Dispatch adds workflow coordination and reviewable run state. Workcell addresses configured execution boundaries, while Watchdog records telemetry. These are separate projects, not language syntax. Choose the components you need and check what each controls. Agents SDK 1.1.3 uses cooperative budget and cancellation checks; callbacks must enforce their own deadlines. The host supplies provider credentials, permissions and persistence.

## Where BAML and Bend fit

BAML describes typed AI functions and bridges into existing applications. Bend’s laws and proofs may suit a component with precisely stated invariants. Either option still requires controls on external tools, validation of their outputs and a plan for failed or interrupted operations.

## An agent-host acceptance checklist

Test that denied actions remain denied, interrupted tasks have explicit outcomes, malformed tool results are rejected and retries do not duplicate effects. Report fixture tests separately from live-provider tests. A deterministic fixture checks that path through the application; it does not establish provider reliability or production isolation.

## Start with one workflow you can test

Build one tool-calling workflow with offline fixtures, then add one live provider with explicit credentials and limits. Keep the task input, versions, tool results and independent checks. The workflow guide shows how to turn those records into evidence a reviewer can inspect.

## Frequently asked questions

### Must the agent host and target repository use the same language?

No. A host can invoke tools that inspect or build another language. Verify the process, data and permission boundaries instead of assuming shared syntax provides safety.

## References

- [Agents-Sdk scope and implementation](https://github.com/kujolang/agents-sdk/blob/6c4a54e74855c605eea67253f6808b16b8c63086/README.md) — official documentation; Agents SDK 1.1.3; source 6c4a54e74855c605eea67253f6808b16b8c63086; reviewed 2026-10-19.
- [Dispatch scope and implementation](https://github.com/kujolang/dispatch/blob/71ca927c65598ecfe7c1816068e047cf50b915e0/README.md) — official documentation; 71ca927c65598ecfe7c1816068e047cf50b915e0; reviewed 2026-10-19.
- [Workcell scope and implementation](https://github.com/kujolang/workcell/blob/a276a92c6bac9279a8cb36ace9687ade34d5128f/src/receipts/receipt.kujo) — implementation inspected; a276a92c6bac9279a8cb36ace9687ade34d5128f; reviewed 2026-10-19.
- [Watchdog scope and implementation](https://github.com/kujolang/watchdog/blob/ad6fbc287c626539c1b3a69b4d3d31528b70edaa/README.md) — official documentation; ad6fbc287c626539c1b3a69b4d3d31528b70edaa; reviewed 2026-10-19.
- [BAML current language overview](https://boundaryml.com/) — product assertions; not independently benchmarked; 648ad5ed10f543c129b51789c7d02e29b64f06f7; reviewed 2026-10-19.
- [Bend language guide](https://github.com/bendlang/bend/blob/64230dcb96f2da2cc5a44524e42d5eb34771a6ec/guide/GUIDE.md) — official documentation; Stable v2.0.37; guide from a separate pinned source snapshot; reviewed 2026-10-19.
- [Python documentation](https://docs.python.org/3/) — official documentation; Python 3.15.0 (2026-10-09); rolling documentation, not runtime-tested; reviewed 2026-10-19.
- [TypeScript documentation](https://www.typescriptlang.org/docs/) — official documentation; TypeScript 7.0.2 (2026-08-20); rolling documentation, not runtime-tested; reviewed 2026-10-19.
- [The Rust book](https://doc.rust-lang.org/book/) — official documentation; Rust 1.99.1 (2026-10-16); rolling book, not runtime-tested; reviewed 2026-10-19.

## Related pages

- [AI-native programming languages: a practical comparison](https://kujolang.ai/compare/ai-native-programming-languages/)
- [AI code verification tools: what each check can establish](https://kujolang.ai/compare/ai-code-verification-tools/)
- [Verify agent workflows: contracts, checks and reproducible evidence](https://kujolang.ai/compare/verify-agent-workflows/)

[Editorial policy](https://kujolang.ai/compare/editorial-policy.md) · [Report inaccuracies](https://github.com/kujolang/kujolang.ai/issues/new)
