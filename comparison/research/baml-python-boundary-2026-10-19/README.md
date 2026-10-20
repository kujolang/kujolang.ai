# BAML Python validation boundaries

Reviewed 2026-10-19. Scope: stable BAML language toolchain and `baml-bridge` **0.22.2**, Python 3.10, Pydantic 2.14.1, mypy 2.4.0, macOS x86_64. Upstream release commit: `01f5c412c73c213846ea8cb6ead89d303b053672`. These are small correctness fixtures, not benchmarks or a complete bridge audit.

## Conclusion

Generated Python signatures support static checking. They do not ensure every dynamic Python call has the declared BAML type. Validation differs by layer: call shape, wire representation, optional/union conversion, Pydantic class decoding and model-response parsing each perform checks. Plain integer and list identity functions accepted invalid dynamic values in this release. A string passed to an integer-addition function crashed the Python process twice, with and without the sandbox. That upstream defect remains unresolved; the comparison records it rather than implying a fix.

| Layer | Executed evidence | Result and limit |
| --- | --- | --- |
| BAML source checking | `baml check` in separate valid/invalid fixture projects | `echo(42)` exit 0; `echo("wrong")` exit 4, E0001 expected int. Standard-library unreachable-code warnings also appeared. This checks BAML source. |
| Python static checking | mypy against generated signatures | Valid call passed; string argument rejected as `arg-type`. Only useful when a checker runs and has usable types. |
| Host call shape and encoding | Missing, extra and duplicate arguments; unsupported object; integer beyond i64 | Each rejected. Rejection of these inputs does not establish complete declared-type validation. |
| Plain values | int identity with string, numeric string, bool, float, None and list; async string identity; mixed int list | Incorrect values returned unchanged, including string values through a declared int return. Numeric strings were not coerced here. |
| Optional type | String passed to `int?` | TypeError union mismatch. The plain-int result cannot be generalized to every BAML type. |
| Generated class construction | Valid int, bad string, numeric string, explicit strict model validation | Normal constructor rejects bad string, coerces numeric string to int; strict validation rejects numeric string. |
| Class result decoding | Forged `model_construct` class, invalid BAML-constructed class, mutated class | Returning the full class triggers Pydantic ValidationError. Returning its invalid primitive field passes the string through. An ordinary dict with a valid field can become the declared class. |
| Model-response parsing | `Extract_spec().parse` on JSON with 42, bad string, numeric string and 41 | Valid 42 passes; bad string produces `baml.errors.ParseError`; numeric string becomes int; 41 also passes. Parser/schema acceptance does not establish domain correctness (such as requiring 42). No provider request was made for these cases. |
| Arithmetic on invalid host input | `plus(41)` and `plus("bad")`, where body is `value + 1` | Valid input returns 42. Invalid input terminates the process with SIGSEGV (Python subprocess return code -11), both sandboxed and unsandboxed. This is not a caught validation error. |
| Application validation | `TypeAdapter(int).validate_python(value, strict=True)` before call | Rejects numeric string; valid integer still returns 42. This is an explicit application guard, not a change to the BAML runtime. Domain rules still need separate checks. |

## Official documentation and implementation

The [current bridge documentation](https://developer.boundaryml.com/baml/bridges) describes generated host bindings and runtime dependencies. The [function documentation](https://developer.boundaryml.com/baml/language/functions) describes typed parameters and return values. Neither page should be stretched into a claim that every dynamic Python FFI value is strictly validated.

For the tested generation, the [pinned Python SDK README](https://github.com/BoundaryML/baml/blob/01f5c412c73c213846ea8cb6ead89d303b053672/baml_language/sdks/python/README.md) describes its protobuf bridge. The [function factory](https://github.com/BoundaryML/baml/blob/01f5c412c73c213846ea8cb6ead89d303b053672/baml_language/sdks/python/src/baml_bridge/__init__.py#L367) receives required/optional argument names, encodes the call and decodes its result. The [encoder and decoder](https://github.com/BoundaryML/baml/blob/01f5c412c73c213846ea8cb6ead89d303b053672/baml_language/sdks/python/src/baml_bridge/proto.py) encode actual host values (`encode_call_args`, around line 783), decode primitive wire values (`decode_value`, around line 1368), and use `model_validate(field_dict)` for class results (around line 1088). The installed `proto.py` matched the pinned file byte for byte.

The [engine conversion code](https://github.com/BoundaryML/baml/blob/01f5c412c73c213846ea8cb6ead89d303b053672/baml_language/crates/bex_engine/src/conversion.rs) threads declared types through argument conversion, but `coerce_numeric_to_declared_type` has a final `(v, _) => Ok(v)` fallback. This helps explain the observed primitive pass-through; it is not a completed root-cause analysis of the native crash. No exploitability, unsafe instruction, other operating system or other release was established.

[Pydantic's official strict-mode documentation](https://pydantic.dev/docs/validation/latest/concepts/strict_mode/) explains the difference between default coercion and explicit strict checks. Generated `Answer` configuration has no strict or assignment-validation setting. `model_construct` deliberately bypasses construction checks, and ordinary field assignment can also introduce an invalid value. Return decoding can subsequently reject that value if the full class is returned.

Older `docs.boundaryml.com` Python installation pages describe the `baml-py`/`baml_client` generation. These results concern `baml-bridge`/`baml_sdk` 0.22.2; do not transfer guarantees between generations without testing.

## Evidence and reproduction

`probe-results.json` contains **32 isolated runtime cases**. `followup-results.json` preserves five additional runtime observations and two failed command attempts: `check --file` was unsupported (exit 2), so those attempts are **not** compiler evidence. `compiler-results.json` contains the corrected two project-based compiler checks. `mypy-valid.txt` and `mypy-invalid.txt` retain the static-check output (exit 0 and 1 respectively). A failed initial probe run exhausted disk; `probe-results.json` is the completed rerun, not the partial attempt.

The original `probe.py` and `followup.py` preserve the exact local harness layout. To reproduce elsewhere, create a clean Python 3.10 environment, install `baml-bridge==0.22.2`, `pydantic==2.14.1` and `mypy==2.4.0`, and obtain the official 0.22.2 CLI. Put `main.baml` under `project/baml_src/`, place `baml.toml` in `project/`, then run `baml-cli generate` in that directory. Use `run-probes.py --python /absolute/path/to/python --project /absolute/path/to/project --output /absolute/path/to/results.json` to rerun the 32 cases with bounded, separate processes. **The invalid arithmetic case is expected to crash its child process on the reviewed platform.** This portable runner does not claim sandbox isolation; the original sandboxed receipts and unsandboxed controls are retained separately.

For static checks, put `good.baml` and `bad.baml` separately at `baml_src/main.baml` in projects with the same package manifest, then run `baml-cli check` in each project. Copy the two `typecheck-*.py` files into the generated client project and run `python -m mypy --no-incremental --follow-imports=silent typecheck-valid.py` and its invalid counterpart.

`requirements-observed.txt` records the tested Python environment; `source-provenance.json` records pinned official source hashes. `verify-evidence.py` checks retained observations and file integrity. Success means the evidence matches the recorded outcomes, **including the defect**; it does not mean the runtime passed all validation cases.
