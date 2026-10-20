# BAML arithmetic crash and nightly retest — 2026-10-20

The latest published nightly checked in this review **still crashes** on `plus("bad")`, where `plus(value: int) -> int { value + 1 }`. Valid `plus(41)` returns 42. This is an isolated Python process failure, not a caught type-validation exception.

## Scope and results

| Toolchain | Python bridge | Boundary cases | Invalid arithmetic |
|---|---|---|---|
| 0.22.2, commit `01f5c412c73c213846ea8cb6ead89d303b053672` | baml-bridge 0.22.2 | Existing 32-case baseline | SIGSEGV, confirmed again without Python's signal handler |
| 0.22.3-nightly.20261018.a, commit `481d074234fce9df31ee0ab0da5f29c5d5fe1e4d` | baml-bridge 0.22.3.dev2026101800 | All 32 exit codes and stdout results match the baseline | SIGSEGV, with and without Python's signal handler |

Both use Python 3.10, Pydantic 2.14.1 and macOS x86_64. The nightly client was regenerated with its own CLI and installed into a separate environment. Parser fixtures are offline; no provider calls or keys were used. The stable baseline is retained from the previous review; the arithmetic crash and three tagged-value controls were rerun on both versions here. Matching outcomes are evidence of persistence, **not passing runtime validation**.

[Official nightly release](https://github.com/BoundaryML/baml/releases/tag/baml-language-0.22.3-nightly.20261018.a). GitHub marks this release `prerelease: false`; its explicit nightly tag determines the channel. `provenance.json` records the release, PyPI wheel, artifact hashes and pinned source hashes.

## Failure mechanism

The source and native crash evidence support a type-invariant violation across the host boundary:

1. Python encodes the actual string. The engine's `coerce_numeric_to_declared_type` fallback returns unmatched values unchanged, so this string reaches an integer parameter.
2. The specialized `AddInt` opcode trusts the compiler's integer types. `Value::tagged_int_add_checked` checks **arithmetic overflow**, but checks operand tags only with a debug assertion. Its release-build arithmetic is `a.bits + (b.bits - 1)`.
3. Integers use `(n << 1) | 1`; an integer 1 has bits 3. Strings use heap pointers. Applying that formula to a string pointer adds **2 bytes**, creating a malformed pointer value rather than rejecting the input.
4. Result conversion inspects the value as an object. Both no-handler crash reports fault in `baml_py.abi3.so` at `movslq (%rcx,%rax,4), %rax`, following a load from `%r12`. In each report `%r12 & 7 == 2`, consistent with a pointer shifted by two bytes. `%rax` is `0x0300000000000000`, an invalid object-discriminant jump-table index. Stable image offset is `0x9d6099`; nightly is `0x9da797`.

Three additional controls distinguish tagged arithmetic from Python arithmetic. Both releases return `False` for `plus(None)`, `True` for `plus(False)`, and an “internal omitted argument escaped” TypeError for `plus(True)`. These match the source's sentinel bit patterns 0, 2, 4 and 6 after adding 2. They are incorrect results for an integer-only boundary.

This identifies a source-supported mechanism with matching machine-level evidence. Live LLDB attachment was denied by macOS. Offline disassembly worked, but the distributed binaries lack source symbols; we have not proved every intermediate instruction with a live trace or verified an upstream patch. The exact source-to-machine mapping is inferred from the source, instruction sequence, registers and controls. We make no claim about exploitability, other operating systems, architectures, bridges or later releases.

## Pinned official source

Use either commit above with these paths:

- [Stable inbound coercion and outbound conversion](https://github.com/BoundaryML/baml/blob/01f5c412c73c213846ea8cb6ead89d303b053672/baml_language/crates/bex_engine/src/conversion.rs): `coerce_numeric_to_declared_type`, `convert_vm_value_to_external_with_type`, `convert_heap_ptr_to_external_with_type`.
- [Stable VM dispatch](https://github.com/BoundaryML/baml/blob/01f5c412c73c213846ea8cb6ead89d303b053672/baml_language/crates/bex_vm/src/vm.rs): `OpCode::AddInt`.
- [Stable tagged values](https://github.com/BoundaryML/baml/blob/01f5c412c73c213846ea8cb6ead89d303b053672/baml_language/crates/bex_vm_types/src/types/value.rs): `tagged_int_add_checked`, `kind`, singleton constants.
- [Nightly tagged values](https://github.com/BoundaryML/baml/blob/481d074234fce9df31ee0ab0da5f29c5d5fe1e4d/baml_language/crates/bex_vm_types/src/types/value.rs): byte-identical to the reviewed stable file.
- [Nightly inbound conversion](https://github.com/BoundaryML/baml/blob/481d074234fce9df31ee0ab0da5f29c5d5fe1e4d/baml_language/crates/bex_engine/src/conversion.rs) and [VM dispatch](https://github.com/BoundaryML/baml/blob/481d074234fce9df31ee0ab0da5f29c5d5fe1e4d/baml_language/crates/bex_vm/src/vm.rs) retain the relevant fallback and tagged-add path.

## Reproduction and limits

Install the exact bridge and dependencies from the corresponding requirements file in separate environments. Verify the CLI archive hash against the official release checksum. Create a project with `baml.toml` and `baml_src/main.baml` from this directory, then run that release's `baml-cli generate` inside it.

```sh
python3 run-probes.py --python /absolute/venv/bin/python --project /absolute/project --output results.json
# Separate child process, without faulthandler:
cd /absolute/project
/absolute/venv/bin/python -c 'import baml_sdk as s; print(s.plus("bad"))'
```

Run invalid cases only in disposable child processes. `tag-controls.json` records the same command with `None`, `False` and `True`. Crash extracts omit unrelated machine/report metadata. `verify-evidence.py` checks retained evidence, not whether BAML is fixed.

Keep static checks and explicit strict input validation. The prior review's class decoding, optional-value checks and model-response parsing results remain valid; this defect does not imply that all BAML validation is absent. No upstream report was submitted, patched runtime built, or security-model assessment performed.
