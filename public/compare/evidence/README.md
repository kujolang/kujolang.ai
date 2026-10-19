# Artifact verification exercise

Reviewed 2026-10-19. This is a reproducibility exercise, not a cross-language benchmark.

## Workload and conditions

Kujo 1.8.2 computes 6 × 7 and writes a JSON object to stdout. Python 3 independently parses that artifact and requires an integer `total` equal to 42. A wrong-value control plus malformed, missing-field and wrong-type controls must fail. No model, provider credentials, network or additional dependencies are used.

Download `produce.kujo` and `verify.py` into one directory, then run:

```sh
KUJO_BIN=/absolute/path/to/kujo python3 verify.py
```

The runner requires `kujo --version` to report `kujo 1.8.2`. Expected overall exit: 0. A failed producer or incorrectly accepted negative control makes the exercise fail. `evidence.json` records actual environment, commands, exit codes, output and SHA-256 hashes. Each invocation is one repetition. Do not publish timing conclusions from this exercise.

## Interpretation

This demonstrates an independent artifact oracle and its negative controls. It does not evaluate a coding agent, exercise all Kujo ecosystem tools, prove an arbitrary program correct, or establish that a competitor cannot implement the same workflow. A malicious producer and sandbox escape are outside this fixture's threat model. Run untrusted programs under a separately reviewed execution boundary.

Compare evidence.json only after checking the runtime, source hash and workload. The repository's internal validation report records the launch verification; repeat locally before relying on the result in another environment.
