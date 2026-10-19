---
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

Download [produce.kujo](/compare/evidence/produce.kujo) and [verify.py](/compare/evidence/verify.py) into the same directory. Run `KUJO_BIN=/path/to/kujo python3 verify.py`. The harness expects Kujo 1.8.1, checks a correct result, checks an intentionally wrong result, and writes evidence.json with command outcomes, environment details and hashes. It makes no network requests and uses no model credentials. See the [methodology](/compare/evidence/README.md).

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
