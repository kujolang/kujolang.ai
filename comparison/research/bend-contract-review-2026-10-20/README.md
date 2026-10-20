# Bend proof and JavaScript boundary review

Verified 2026-10-20 against Bend 2.0.37, release commit `4ff8545f19b09b7d2b8ca2303668100eac8efd66`. This is the current bendlang/bend project, not an inference from the older HVM implementation.

## Evidence and reproduction

The final suite records 76 command observations on macOS x86_64 and 83 on Linux x86_64. The Linux run adds seven `--verdict` cases using Lean 4.34.0. A separate 12-case kernel control suite also passed, including direct acceptance of the exported proof and rejection of its corrupted body. Counts include builds and controls; they are not counts of independent guarantees.

[Successful Linux workflow](https://github.com/kujolang/kujolang.ai/actions/runs/39447902948). See environment and provenance JSON for versions, archive hashes and pinned official source. Run `python3 verify-evidence.py` to check the retained receipts. To repeat the execution, install the pinned release and run `python3 reproduce.py --bend /absolute/path/bin/bend --bend-home /absolute/path/bend --output /tmp/bend-review`; add `--kernel` with the kernel toolchain installed.

## What the tests establish

- Valid proofs and a filled imported law passed. Broken proofs, an unfilled law and a PROOF file missing its LAWS import failed. `--check-only` is distinct from the independent kernel verdict. Some invalid inputs fail before reaching the kernel.
- Unsafe and foreign dependencies were rejected by the proof gate, including the unsafe function's transitive callers. Ordinary evaluation, JavaScript and native execution still returned 42 for these fixtures. This is the documented assurance boundary, not a runtime ban on foreign code. Base effects are not all rejected as foreign dependencies.
- Nondecreasing recursion and reuse of an affine U32 failed checking. Explicit copy permission accepted the same reuse and produced 42 on all three execution paths.
- Exported JavaScript Nat arguments rejected negative, fractional, BigInt, string, null, NaN, infinite and above-limit values. Identity accepted zero, 42 and 2**53. The generic error mentions the internal 2**48-1 immediate limit; that is not the exported input guard's bound. An accepted identity input does not establish that every Nat operation supports it. Curried calls received the same guard.
- Exported U32 identity returned -1, 2**32 and the string "42" unchanged. Official `js_lib` generation applies the Nat input guard specifically; the official U32 marshaling fixture describes trusted host numbers. Callers must validate their U32 inputs. This is not presented as a newly discovered bug.
- U32 overflow returned zero, underflow returned 4294967295, and the fork-join fixture returned 4096 through evaluation, JavaScript and native CPU execution on both systems. These finite fixtures do not prove backend equivalence or measure parallel speedup.
- Compiled JavaScript and native IO.exit fixtures returned statuses 0, 7 and 255. Input 256 failed with status 1 and the documented range diagnostic.

## Official source and limits

Pinned `bend2/comp.ts` defines `nat_in` and the export wrappers; `bend2/main.ts` defines the proof gate and dependency checks. Official tests `tests/io/nat_host_export.*` and `tests/io/marshal_u32_integer.*` support the host-boundary interpretation. The README documents possible backend differences and that translation into the small kernel is not proven. Source URLs and hashes are retained in provenance.json.

GPU execution, performance, all IO effects, exhaustive arithmetic and a proof of compiler or kernel translation were not tested. No Kujo–Bend adapter was tested. Initial fixture authoring failures are retained separately in setup-attempts.json and excluded from the final counts. The first native foreign fixture omitted its C import; adding both C and JavaScript imports resolved the build failure before the final runs.
