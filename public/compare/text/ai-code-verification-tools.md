# AI code verification tools: what each check can establish

Verify AI-generated code with independent checks tied to explicit requirements. Different tools establish different facts: a type checker rejects some invalid programs, a test observes selected behavior, a proof establishes a stated property within its assumptions, and a receipt records an execution. None is a substitute for all the others.

Last reviewed: 2026-10-19. Canonical page: https://kujolang.ai/compare/ai-code-verification-tools/

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
