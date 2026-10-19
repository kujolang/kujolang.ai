# AI code verification tools: what each check can establish

Verify AI-generated code with independent checks tied to explicit requirements. Different tools establish different facts: a type checker rejects some invalid programs, a test observes selected behavior, a proof establishes a stated property within its assumptions, and a receipt records an execution. None is a substitute for all the others.

Last reviewed: 2026-10-19. Canonical page: https://kujolang.ai/compare/ai-code-verification-tools/

## Match the check to the claim.

Types, tests, proofs and receipts answer different questions.

What failure would make the deliverable unacceptable?

- Before execution: Reject selected invalid programs and unwanted dependencies.
- During evaluation: Observe behavior against independent acceptance criteria.
- After execution: Retain evidence and resolve release conditions.

## Decision lenses

### Static structure: Reject a class of mistakes early

Type diagnostics and configured architecture boundaries catch different structural problems. Fence checks configured import relationships; it is neither a general security audit nor a substitute for running the application.

Put it into practice: Introduce a known type or import-rule violation and require the relevant check to fail.

Sources: https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/type_checker.rs, https://github.com/kujolang/fence/blob/d3173049b5365af975624fddd48e943d39738c75/README.md

### Behavior and proof: Define what the verdict covers

Eval checks selected command, file and data outcomes. Bend’s proof model addresses stated laws within a trusted boundary. Finite observed cases and a quantified proposition can complement each other, but should not share an ambiguous “proven” label.

Put it into practice: State the assertion or law next to the result, including inputs and excluded behavior.

Sources: https://github.com/kujolang/eval/blob/71e66dff780d6930bcbe093c046bf31aa26411df/src/checks.kujo, https://github.com/bendlang/bend/blob/64230dcb96f2da2cc5a44524e42d5eb34771a6ec/guide/GUIDE.md

### Evidence and release: Follow the pass label to its source

RunLedger records supplied outcomes and metadata; execution receipts describe recorded runs. ShipCheck adds release signals. None makes a missing raw test result appear, and a release decision still needs coverage of the actual acceptance criteria.

Put it into practice: Tie each verdict to the command, revision and artifact it describes.

Sources: https://github.com/kujolang/runledger/blob/334ddd4d33c8cb2612c8edab971ee69170824133/src/record.kujo, https://github.com/kujolang/workcell/blob/a276a92c6bac9279a8cb36ace9687ade34d5128f/src/receipts/receipt.kujo, https://github.com/kujolang/shipcheck/blob/ee4cfd052c0522eebedc0eead223cbb22490b357/src/checks.kujo

## A verification stack organized by failure mode.

Layer checks deliberately. Each row names both a useful result and the question it leaves unanswered.

### Type / compiler diagnostics

Can help establish: The program satisfies the selected static rules.

Does not establish: Domain truth or every runtime outcome.

Challenge it with: A deliberately invalid type use that must be rejected.

Sources: https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/type_checker.rs

### Architecture boundaries

Can help establish: Imports or dependencies satisfy configured rules.

Does not establish: Whole-program security or permitted runtime effects.

Challenge it with: An import across a forbidden boundary.

Sources: https://github.com/kujolang/fence/blob/d3173049b5365af975624fddd48e943d39738c75/README.md

### Behavioral evaluation

Can help establish: The tested artifact meets selected assertions under recorded conditions.

Does not establish: Coverage of every input or an unexpressed requirement.

Challenge it with: A plausible artifact with the wrong value or type.

Sources: https://github.com/kujolang/eval/blob/71e66dff780d6930bcbe093c046bf31aa26411df/src/checks.kujo

### Formal proof

Can help establish: The stated property is checked within the proof system’s assumptions.

Does not establish: Correctness of an incomplete specification or excluded external code.

Challenge it with: An invalid proof or unsatisfied law.

Sources: https://github.com/bendlang/bend/blob/64230dcb96f2da2cc5a44524e42d5eb34771a6ec/guide/GUIDE.md, https://github.com/bendlang/bend/blob/64230dcb96f2da2cc5a44524e42d5eb34771a6ec/tests/check/axiom_import_warn.bend

### Run evidence

Can help establish: Commands, artifacts and supplied outcomes can be traced through a record.

Does not establish: Independent truth of every supplied pass verdict.

Challenge it with: A verdict with missing or mismatched underlying evidence.

Sources: https://github.com/kujolang/runledger/blob/334ddd4d33c8cb2612c8edab971ee69170824133/src/record.kujo, https://github.com/kujolang/workcell/blob/a276a92c6bac9279a8cb36ace9687ade34d5128f/src/receipts/receipt.kujo

### Release gate

Can help establish: Configured readiness conditions have an explicit outcome.

Does not establish: That any unconfigured requirement was satisfied.

Challenge it with: A required failed check or missing release artifact.

Sources: https://github.com/kujolang/shipcheck/blob/ee4cfd052c0522eebedc0eead223cbb22490b357/src/checks.kujo

## Put the decision into practice

Proposed evaluation steps; not reported benchmark results.

### 1. Write the failure first

Describe the incorrect behavior you need to catch. A concrete counterexample is easier to evaluate than a generic request for more tests.

### 2. Choose the narrowest useful layer

Use static checks for structural rules, behavioral checks for observed outputs and a suitable proof system for precisely stated invariants. Add layers when the requirement crosses boundaries.

### 3. Validate the verifier

Run a valid case and at least one invalid case against the actual checker. A test command that exits successfully without inspecting the deliverable is not sufficient evidence.

### 4. Connect coverage to release

Map each acceptance criterion to evidence for the current revision. Label missing or inconclusive evidence explicitly before a release decision.

## One JSON field. Several different guarantees.

The linked Kujo/Python exercise requires an integer total of 42. These expected cases explain why process success, parsing and semantic validation are separate checks.

### Producer exits 0

Expected decision: Insufficient on its own

Reason: The process can succeed while producing the wrong artifact.

### {"total": 42}

Expected decision: Accept this criterion

Reason: The parsed field is an integer with the required value.

### {"total": 41}

Expected decision: Reject

Reason: Valid JSON and a valid integer can still violate the requirement.

### {"total": "42"}

Expected decision: Reject

Reason: The representation is a string, not the required integer.

### {"total": true} or {"total": 42.0}

Expected decision: Reject

Reason: The oracle requires an exact integer type; a boolean or floating-point value is insufficient.

### {} or malformed JSON

Expected decision: Reject

Reason: The required field or valid representation is missing.

## Common interpretation mistakes

### File existence as task completion

An existing file may be empty, stale or incorrect. Inspect its required contents and identity.

### Recorded pass as independently checked pass

A stored verdict may be supplied by a caller. Follow it to the actual check output.

### More tests as automatic coverage

Many assertions can repeat the same assumption. Map tests to failure cases and acceptance criteria.

## Static analysis and architecture checks

Use the target language’s compiler and linter before running the program. Add architecture rules where unwanted imports or dependencies matter. Fence is a Kujo ecosystem tool for configured import boundaries; it is not a general security audit or a theorem prover. Static checks cannot establish every runtime outcome.

## Behavioral tests and evaluations

Eval supports checks against command outcomes, files and structured data. Choose assertions from the requirement, not merely from the implementation an agent happened to produce. A test that only checks whether a file exists cannot establish that its contents are correct. Preserve a failing control to detect permissive or disconnected checks.

## Formal verification has a distinct scope

Bend’s current guide describes laws and proof definitions. This is materially different from running a finite test suite. Proof strength depends on the stated proposition, the checker’s trust boundary and any excluded foreign or unsafe behavior. Do not call ordinary successful tests mathematical proof.

## Execution evidence and release gates

Workcell receipts and RunLedger records can support investigation of what ran and what was reported. RunLedger also accepts supplied test results and verdicts, so readers must follow the evidence links. ShipCheck checks release signals and reports blockers; the existence of a test directory is not evidence that all tests passed.

## Select a stack by the failure you need to catch

For malformed output, validate the schema and values. For an unauthorized effect, test the execution boundary. For a regression, run an independent behavioral suite. For a universal mathematical invariant, investigate a suitable proof system. For an incomplete release, use explicit release gates. Keep the original question visible in every report.

## Adoption without a language rewrite

A verification process can surround a repository in its existing language. Establish a baseline before adding tools, then introduce the smallest check that catches a real failure. The workflow guide supplies a runnable positive and negative artifact check without a model provider or paid service.

## Frequently asked questions

### Can a passing test suite prove an agent finished the task?

It establishes that the suite’s assertions passed under the recorded conditions. Completion also requires the suite to cover the acceptance criteria, to execute against the actual deliverable, and to preserve failures rather than hiding them.

## References

- [Kujo type checker](https://github.com/kujolang/kujo/blob/549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1/src/type_checker.rs) — implementation inspected; 549bdb4d5aa8edc60a83c81bf3be4b1c688ad3e1; reviewed 2026-10-19.
- [Eval scope and implementation](https://github.com/kujolang/eval/blob/71e66dff780d6930bcbe093c046bf31aa26411df/src/checks.kujo) — implementation inspected; 71e66dff780d6930bcbe093c046bf31aa26411df; reviewed 2026-10-19.
- [Fence scope and implementation](https://github.com/kujolang/fence/blob/d3173049b5365af975624fddd48e943d39738c75/README.md) — official documentation; d3173049b5365af975624fddd48e943d39738c75; reviewed 2026-10-19.
- [Bend language guide](https://github.com/bendlang/bend/blob/64230dcb96f2da2cc5a44524e42d5eb34771a6ec/guide/GUIDE.md) — official documentation; Bend website v2.0.37; pinned source snapshot; reviewed 2026-10-19.
- [Workcell scope and implementation](https://github.com/kujolang/workcell/blob/a276a92c6bac9279a8cb36ace9687ade34d5128f/src/receipts/receipt.kujo) — implementation inspected; a276a92c6bac9279a8cb36ace9687ade34d5128f; reviewed 2026-10-19.
- [Runledger scope and implementation](https://github.com/kujolang/runledger/blob/334ddd4d33c8cb2612c8edab971ee69170824133/src/record.kujo) — implementation inspected; 334ddd4d33c8cb2612c8edab971ee69170824133; reviewed 2026-10-19.
- [Shipcheck scope and implementation](https://github.com/kujolang/shipcheck/blob/ee4cfd052c0522eebedc0eead223cbb22490b357/src/checks.kujo) — implementation inspected; ee4cfd052c0522eebedc0eead223cbb22490b357; reviewed 2026-10-19.

## Related pages

- [AI-native programming languages: a practical comparison](https://kujolang.ai/compare/ai-native-programming-languages/)
- [Programming languages for AI agents: choosing the host and tools](https://kujolang.ai/compare/programming-languages-for-ai-agents/)
- [Verify agent workflows: contracts, checks and reproducible evidence](https://kujolang.ai/compare/verify-agent-workflows/)

[Editorial policy](https://kujolang.ai/compare/editorial-policy.md) · [Report inaccuracies](https://github.com/kujolang/kujolang.ai/issues/new)
