---
template: "comparison-guide"
title: "Verify agent workflows: contracts, checks and reproducible evidence"
description: "A practical guide to verifying AI-generated code, evaluating coding agents and preserving traceable execution evidence with honest limits."
seo_title: "Verify agent workflows: contracts, checks and reproducible evidence"
custom_url: "verify-agent-workflows"
date: "2026-10-19"
author: "1"
social_image: "/assets/images/social/verify-agent-workflows.jpg"
---

Turn an agent’s completion report into a claim you can check. Freeze the requirement, evaluate the actual artifact with an independent oracle, preserve the command outcomes, and retain enough environment information to repeat the check. This guide covers code verification, agent evaluation, traceability, specifications and reproducible evidence as one workflow.

Last reviewed: 2026-10-19. Canonical page: https://kujolang.ai/compare/verify-agent-workflows/

## Make completion inspectable.

A contract, an independent check, and a trail you can replay.

Could another reviewer challenge this “done” claim?

- Contract: Observable criteria fixed before implementation.
- Oracle: A check that can reject a plausible wrong result.
- Evidence: The actual revision, environment, commands and outcomes.

## Decision lenses

### Before implementation: Define an observable contract

A structured task record can capture allowed changes and acceptance conditions. Spec validates a record’s schema; it cannot decide whether you asked for enough. Turn “generate a report” into explicit fields, values and failure behavior.

Put it into practice: Write at least one valid artifact and one plausible invalid artifact before building the solution.

Sources: https://github.com/kujolang/spec/blob/1211f37a09314be7150734bf15a55e9b2ea6504d/src/validate.kujo

### During evaluation: Keep the oracle independent

Eval can check commands, files and structured values. The exercise uses a separate Python oracle to isolate the idea: read the producer’s output, parse it and check value and type rather than trusting a success message.

Put it into practice: If an agent can rewrite its own checker, decide whether that is acceptable for your threat model.

Sources: https://github.com/kujolang/eval/blob/71e66dff780d6930bcbe093c046bf31aa26411df/src/checks.kujo

### At review: Tie the result to the deliverable

Run records and execution receipts support reconstruction when they retain the actual inputs and outcomes. A run identifier or supplied pass label is not enough to establish what was tested. Match the evidence to the artifact being reviewed.

Put it into practice: Reject stale or mismatched evidence even if the earlier run was successful.

Sources: https://github.com/kujolang/runledger/blob/334ddd4d33c8cb2612c8edab971ee69170824133/src/record.kujo, https://github.com/kujolang/workcell/blob/a276a92c6bac9279a8cb36ace9687ade34d5128f/src/receipts/receipt.kujo

## An acceptance contract you can audit row by row.

Illustrative contract for the public artifact exercise. Expected outcomes are specified here; the receipt records the outcomes of your actual run.

### Correct value

Independent check: Require total to equal 42.

Negative control: Use total 41.

Evidence to keep: Positive and wrong-value verifier exit codes.

Sources: https://github.com/kujolang/eval/blob/71e66dff780d6930bcbe093c046bf31aa26411df/src/checks.kujo

### Correct representation

Independent check: Require an exact integer, not a coerced value.

Negative control: Use a string, boolean or floating-point total.

Evidence to keep: Malformed-control results from the oracle.

Sources: https://github.com/kujolang/eval/blob/71e66dff780d6930bcbe093c046bf31aa26411df/src/checks.kujo

### Readable artifact

Independent check: Parse JSON and require the expected object field.

Negative control: Use invalid JSON or an empty object.

Evidence to keep: Actual stdout and its SHA-256 hash.

Sources: https://github.com/kujolang/eval/blob/71e66dff780d6930bcbe093c046bf31aa26411df/src/checks.kujo

### Successful producer

Independent check: Require the producer process to exit successfully.

Negative control: For a broader trial, force a process failure.

Evidence to keep: Command, exit code and stderr.

Sources: https://github.com/kujolang/workcell/blob/a276a92c6bac9279a8cb36ace9687ade34d5128f/src/receipts/receipt.kujo

### Identified toolchain

Independent check: Record the pinned runtime and environment.

Negative control: The harness rejects a runtime other than Kujo 1.8.2.

Evidence to keep: Runtime version/hash and Python/platform details.

Sources: https://github.com/kujolang/runledger/blob/334ddd4d33c8cb2612c8edab971ee69170824133/src/record.kujo

### Release relevance

Independent check: Map evidence to the artifact and revision under review.

Negative control: For a repository trial, present results from an older revision.

Evidence to keep: Source/artifact hashes; separately retain Git context for real repository work.

Sources: https://github.com/kujolang/shipcheck/blob/ee4cfd052c0522eebedc0eead223cbb22490b357/src/checks.kujo, https://github.com/kujolang/runledger/blob/334ddd4d33c8cb2612c8edab971ee69170824133/src/record.kujo

## Put the decision into practice

Proposed evaluation steps; not reported benchmark results.

### 1. Prepare the contract

Define the expected integer total and the invalid cases. Download the producer and verifier into the same directory; inspect them before running the exercise.

### 2. Run with the pinned runtime

Use Kujo 1.8.2 and Python 3. The command runs the producer and independent oracle, then writes evidence.json in the working directory. It requires no model provider.

### 3. Inspect every outcome

Require producer exit 0, positive verifier exit 0, wrong-value verifier nonzero and no malformed control accepted. Overall success must preserve all of those conditions.

### 4. Extend deliberately

For a repository task, add revision identity, a representative acceptance suite and explicit process-failure cases. For agent evaluation, retain every attempt, configuration and manual intervention.

## Run the smallest complete evidence loop.

Runnable artifact exercise, not a language benchmark or agent-success evaluation. The table describes expected results; your evidence.json contains the observations.

### version

Expected result: kujo 1.8.2

What to inspect: The harness fails early on a different version.

### exitCode / positiveVerifierExit

Expected result: 0 / 0

What to inspect: Both producer execution and the positive artifact check succeed.

### wrongValueVerifierExit

Expected result: Nonzero

What to inspect: The independently checked wrong-value artifact is rejected.

### malformedControlsAccepted

Expected result: Every value false

What to inspect: Missing, malformed and wrong-type controls are not accepted.

### sourceSha256 / artifactSha256

Expected result: Hashes present

What to inspect: Identify exactly what ran and what output was checked.

### passed

Expected result: true only when all required outcomes hold

What to inspect: Read the constituent outcomes rather than treating the label as standalone proof.

Download [produce.kujo](/compare/evidence/produce.kujo) and [verify.py](/compare/evidence/verify.py). From their directory, run with Kujo 1.8.2 and Python 3:

```sh
KUJO_BIN=/absolute/path/to/kujo python3 verify.py
```

Read evidence.json and the [methodology](/compare/evidence/README.md).

## Common interpretation mistakes

### Repeatable command as deterministic system

Pinned inputs help repeat a check. Live APIs, time and model sampling can still change behavior.

### One exercise as agent performance

This deterministic artifact exercise does not use a coding agent or measure a success rate.

### A valid schema as a sufficient requirement

Task schema validation says the record has the required shape. It does not establish that the criteria cover the user’s intent.

## 1. Write the acceptance contract before implementation

Describe observable behavior, allowed changes and failure cases. Spec can validate a structured task record, but schema validity does not prove that the requirement is sufficient. For example: a generated JSON artifact must contain an integer total of 42. A file merely existing is weaker than that requirement.

## 2. Evaluate the artifact independently

Use an oracle that does not simply repeat the agent’s implementation. Read the generated file, parse it, check required fields and values, and reject malformed or incorrect output. Eval provides configurable checks; the small exercise below isolates the same principle with Kujo and a standard-library Python harness. Keep the oracle outside the agent’s write scope when the threat model requires it.

## 3. Test the verifier with a known failure

Run the correct artifact, then deliberately change the expected result and require a nonzero verifier exit. If both pass, the verifier is not useful. This negative control establishes that the selected error is detectable; it does not establish coverage of every possible error or resistance to a malicious agent.

## 4. Make the run traceable

Record the repository commit, runtime version, exact commands, exit codes and artifact hashes. Keep raw stdout and stderr when useful, with deliberate secret handling and retention. RunLedger can store run metadata and supplied results; Workcell can provide bounded execution receipts. A caller-supplied pass verdict should never be presented as independently observed execution.

## 5. Separate repeatability from determinism

A pinned command and input make a check easier to repeat. External APIs, model sampling, time and mutable dependencies can still change outcomes. Use offline fixtures for deterministic checks and separately report live runs. Do not label a replayed fixture a fresh provider result.

## 6. Decide whether to ship

Review the actual diff and the evidence that maps to each acceptance criterion. ShipCheck can add release-readiness signals, while a human or authorized gate owns the final decision. Missing evidence is an explicit unresolved condition, not a reason to infer success.

## Run the artifact verification exercise

Download [produce.kujo](/compare/evidence/produce.kujo) and [verify.py](/compare/evidence/verify.py) into the same directory. Run `KUJO_BIN=/path/to/kujo python3 verify.py`. The harness expects Kujo 1.8.2, checks a correct result, checks an intentionally wrong result, and writes evidence.json with command outcomes, environment details and hashes. It makes no network requests and uses no model credentials. See the [methodology](/compare/evidence/README.md).

## Interpret the result narrowly

A successful exercise demonstrates the local artifact-checking pattern on a small deterministic task. It does not compare languages, measure coding-agent quality or prove application correctness. To evaluate an agent, repeat a representative task set, keep the model and harness configuration, report all attempts and include manual interventions. Do not extrapolate this exercise to a universal success rate.

## Frequently asked questions

### How do I prove an agent completed a task?

Map every acceptance criterion to an independently checked deliverable, preserve the results and review any remaining conditions. A final chat message or recorded pass label alone is not that evidence.

### Why combine these topics in one guide?

Specifications, output evaluation, traceability and reproducibility are successive steps of the same workflow. One worked example makes their boundaries clearer than five overlapping introductions.

## References

- [Spec scope and implementation](https://github.com/kujolang/spec/blob/1211f37a09314be7150734bf15a55e9b2ea6504d/src/validate.kujo) — implementation inspected; 1211f37a09314be7150734bf15a55e9b2ea6504d; reviewed 2026-10-19.
- [Eval scope and implementation](https://github.com/kujolang/eval/blob/71e66dff780d6930bcbe093c046bf31aa26411df/src/checks.kujo) — implementation inspected; 71e66dff780d6930bcbe093c046bf31aa26411df; reviewed 2026-10-19.
- [Runledger scope and implementation](https://github.com/kujolang/runledger/blob/334ddd4d33c8cb2612c8edab971ee69170824133/src/record.kujo) — implementation inspected; 334ddd4d33c8cb2612c8edab971ee69170824133; reviewed 2026-10-19.
- [Workcell scope and implementation](https://github.com/kujolang/workcell/blob/a276a92c6bac9279a8cb36ace9687ade34d5128f/src/receipts/receipt.kujo) — implementation inspected; a276a92c6bac9279a8cb36ace9687ade34d5128f; reviewed 2026-10-19.
- [Shipcheck scope and implementation](https://github.com/kujolang/shipcheck/blob/ee4cfd052c0522eebedc0eead223cbb22490b357/src/checks.kujo) — implementation inspected; ee4cfd052c0522eebedc0eead223cbb22490b357; reviewed 2026-10-19.
- [Evaluating coding agents](https://vercel.com/i/evaluating-ai-coding-agents) — official documentation; Documentation snapshot; no release version asserted; reviewed 2026-10-19.

## Related pages

- [AI-native programming languages: a practical comparison](https://kujolang.ai/compare/ai-native-programming-languages/)
- [Programming languages for AI agents: choosing the host and tools](https://kujolang.ai/compare/programming-languages-for-ai-agents/)
- [AI code verification tools: what each check can establish](https://kujolang.ai/compare/ai-code-verification-tools/)

[Editorial policy](https://kujolang.ai/compare/editorial-policy.md) · [Report inaccuracies](https://github.com/kujolang/kujolang.ai/issues/new)
