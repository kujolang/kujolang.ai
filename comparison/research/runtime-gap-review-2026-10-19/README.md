# Runtime verification follow-up — 2026-10-19

This adds execution evidence to the immutable earlier `runtime-review-2026-10-19` review. It does not replace those receipts. Date uses America/Detroit; some UTC receipts fall on October 20.

## Tested outcomes

| Area | Test | Observed result | Scope |
| --- | --- | --- | --- |
| Bend 2.0.37 | `--verdict` with Lean 4.34.0-built BendTT | Valid Nat add-zero proof accepted | Linux x86_64, official release binary |
| Bend kernel | Run exported proof directly through BendTT | Accepted; replacing the main proof body with `()` rejected with `In main: expected: an enum` | This negative reaches the independent kernel; source negatives can fail earlier |
| Bend diagnostics | Broken proof, return type and affine double-use | Each exited 1 | These exercise the full CLI path, not necessarily the second kernel |
| Bend execution | Fork-join `pow2(12n)` | Native CPU and sequential JavaScript both printed 4096 | Correct result; no measured speedup or thread utilization |
| BAML 0.22.2 + Python bridge 0.22.2 | Generated sync and async calls | Both returned 42 | Python 3.10, macOS x86_64 |
| BAML Python boundary | Correct integer argument; declared thrown error | Integer preserved; `BamlError` propagated | Small host bridge fixtures |
| BAML Python boundary | String passed to `echo(value: int) -> int` | Returned `"wrong"` without rejection | Generated type hints did not enforce this runtime boundary; do not generalize to every type |
| BAML provider adapter | Local HTTP chat-completion fixture | Request URL/model/header verified; response became `Answer(value=42)` | Loopback mock, no hosted inference or real credentials |
| BAML response failures | Invalid integer field; HTTP 401 | `ai.errors.ParseFailed`; `ai.errors.InvalidRequest` | Exact error categories checked |
| BAML tracing | Per-call metadata; following plain call | Metadata reached invocation; next call had empty metadata | Context propagation and isolation |
| BAML local recording | Success and thrown-error CLI runs, then `query --local --verify` | Sealed records; success/error process outcomes; profiler counts 1/0 and 0/1; success span | CLI BTEL recording/query verified, not cloud delivery |
| BAML standalone packaging | `pack total`, then execute from outside project with PATH `/usr/bin:/bin` | Packed executable printed 42, exit 0 | No BAML CLI or Python interpreter on PATH; no network allowed |

The first Python run expected a wrong host type to fail. It did not. `baml-client-initial.json` preserves that result. The final test names this observed boundary explicitly instead of claiming type enforcement. The model response parser separately rejected the invalid integer field.

## Provenance and environment corrections

- Bend source/release: https://github.com/bendlang/bend/tree/4ff8545f19b09b7d2b8ca2303668100eac8efd66
- Passing Linux job: https://github.com/kujolang/kujolang.ai/actions/runs/39349715512 (script commit `7cdf73a`). `ci-final/` contains its raw receipts and exported proof inputs.
- Initial Linux job: https://github.com/kujolang/kujolang.ai/actions/runs/39349536295. Kernel tests passed. Native compilation failed because Lean's bundled clang shadowed the host compiler and lacked the needed standard header path. Setting `CC=/usr/bin/clang` resolved it; `ci-attempt1/` preserves the failure.
- Workflow `.github/workflows/comparison-runtimes.yml` installs fixed Bend/Lean releases and pins archive hashes recorded in the successful job. It can be rerun manually.
- BAML release: https://github.com/BoundaryML/baml/releases/tag/baml-language-0.22.2, commit `01f5c412c73c213846ea8cb6ead89d303b053672`.
- BAML macOS archive SHA-256: `a13b4c004ee011b334bfed31439ba8fb61278e4850b0277774328873deb47ddc`, matched the prior publisher-checksummed archive. `binary-hashes.json` records CLI, pack host and packed output hashes.
- Python bridge distribution: https://pypi.org/project/baml-bridge/0.22.2/. `requirements.txt` pins the installed dependency set.
- Provider fixture design follows the pinned official `baml_language/crates/baml_tests/baml_src/ns_llm_openai_chat/openai_chat.baml`. Trace checks follow `baml_language/crates/baml_cli/tests/telemetry_recording_e2e.rs` and the generated trace API.
- Initial packaging again encountered local disk exhaustion. Once space became available, the same release packed and ran successfully. The environment failure is preserved in `initial-cases.json`; it is not a BAML defect.
- Local executions used a scrubbed environment and macOS sandbox. Network was denied except localhost for the mock provider. `loopback.sb` records the actual profile; adapt its absolute workspace path when reproducing. These are harness restrictions, not claims about BAML isolation. Only the literal `local-fixture-only` placeholder was sent as an API key.

## Reproduce

For Bend, run the repository's **Comparison runtime evidence** workflow, or install the pinned releases and run `python3 run-bend.py` with `bend`, `node`, `lean` and `leanc` on PATH and `CC` pointing to the host clang. `EVIDENCE_DIR` chooses an output directory. The script emits and corrupts the proof for the direct kernel negative.

For BAML, install the official CLI release and create a Python 3.10 environment with `pip install -r requirements.txt`. Use a fresh copy of `baml-project`:

```sh
baml generate
python test-client.py
baml pack total --output ../total-packed
(cd .. && ./total-packed)
BAML_TELEMETRY=medium baml run total
BAML_TELEMETRY=medium baml run fail  # expected exit 1
baml query --local --verify --format json 'select host,status,count(*) as n from processes group by host,status'
baml query --local --verify --format json "select function_name,return_count,error_count from profiler where function_name like '%total%' or function_name like '%fail%'"
```

The captured run used the extracted internal `baml-cli`, which warns that the public launcher is preferred. `test-client.py` starts its own loopback mock and checks specific errors. `btel-recordings/` preserves the original local recordings, while `query-*.json` preserves query outputs. Run `python3 verify-evidence.py` to verify retained hashes and outcome assertions; that command does **not** rerun the languages.

## Remaining limits

No GPU hardware execution, parallel utilization/speed benchmark, full upstream suite, hosted model request, cloud telemetry delivery, exhaustive tracing coverage, or cross-platform BAML packaging test. The independent kernel test does not prove Bend's source-to-kernel translation. Unsafe and foreign-code exclusions remain. The Python type-boundary result means applications should validate host inputs and use static checking; it does not negate the separately tested model-response parser. No new comparison speed, cost, quality or universal-correctness claim is justified.
