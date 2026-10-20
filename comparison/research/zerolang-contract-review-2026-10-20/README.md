# Zerolang graph-editing contracts — 2026-10-20

This review tests Vercel's Zerolang, not the unrelated zero-lang.com preview. The latest published release checked on this date was **v0.3.4**, commit `5b3a90a7756e48ab449eb16e688044b8decec7a9`. We used the official macOS x86_64 binary and verified its SHA-256 against the release checksum file.

The tested workflows behaved as documented. We found no new defect in this bounded review. That is not a claim that the compiler is defect-free.

## What we tested

The baseline has a `main` function that prints `baseline` and an `add(i32, i32)` function. Each scenario starts from a fresh copy. Receipts record command arguments, exit status, stdout, stderr and before/after SHA-256 hashes of `zero.graph`, `zero.toml` and the source projection. These hashes establish file preservation for the named files, not the absence of cache writes.

| Contract | Observed result | Limit |
|---|---|---|
| Clean state | Status and projection verification succeeded without changing tracked fixture files; execution printed `baseline`. | One package and source file. |
| Source-only edit | Status and verify-projection did not write. Verification rejected drift; `check` refreshed the graph, and execution printed `human-edit`. | Tested a string edit preserving the function set. |
| Strict stale policy | `ZERO_STALE=fail` returned `RGP008` without changing the graph or projection. Explicit import then succeeded and ran the edited program. | Strict mode was tested through `check`. |
| Graph-only edit | Runtime used the patched graph and printed both lines; it reported that the graph was newer. Export synchronized the projection and verification passed. | A checked append operation. |
| Conflicting source and graph edits | `check` and `run` returned `RGP006`, preserving both files. | Sequentially constructed conflict, not simultaneous writers. |
| Explicit conflict resolution | Export selected the graph edit; import selected the source edit. Each ran the selected program and passed projection verification. | These commands choose an authority; they do not combine conflicting intent. |
| Invalid source | Both automatic refresh and explicit import rejected a Bool return in an i32 function with `TYP003`, leaving graph and edited source unchanged. | One return-type mismatch. |
| Content rather than timestamps | An edited projection with an old timestamp still refreshed correctly despite a newer graph timestamp. Execution printed the edited text. | One deliberately reversed timestamp pair. |
| Patch rollback | A valid first operation followed by an ill-typed operation or an unknown operation failed without persisting the earlier edit. | Tested two failure paths, not crash/power-loss atomicity. |
| Stale-hash guard | A wrong expected graph hash returned `GPH002` and preserved the files. | No concurrent-writer test. |
| Dry run | A valid `--check-only` patch succeeded without saving; runtime still printed the baseline. | One valid append operation. |
| Three-way independent merge | Edits to separate functions merged. Runtime printed the left-side text; the exported projection also contained the right-side arithmetic change. | The arithmetic change was checked in the merged projection, not separately executed. |
| Three-way conflicting merge | Competing text edits produced `RGM003`, left the destination unchanged, and the destination still ran the baseline. | One same-value conflict. |
| Checks versus tests | One assertion passed. Adding an incorrect expected result left `check` successful but made `test` fail. | Structural/type checks do not prove intended behavior. |

There are **53 command observations** in `results.json`. The self-contained runner repeated all 53 in a fresh temporary directory; `portable-results.json` records that second run. These counts include setup operations within each scenario, status queries and positive/negative controls; they are not 53 independent language guarantees. The initial baseline's three commands are recorded separately in `setup-results.json`.

## Official sources inspected

All source links are pinned to the tested release. `provenance.json` records their SHA-256 hashes.

- [Release and assets](https://github.com/vercel-labs/zerolang/releases/tag/v0.3.4).
- [Projection workflow](https://github.com/vercel-labs/zerolang/blob/5b3a90a7756e48ab449eb16e688044b8decec7a9/docs/articles/concepts/projections.md): content-based state detection, refresh, conflict handling and `ZERO_STALE=fail`.
- [Compiler input diagnostics](https://github.com/vercel-labs/zerolang/blob/5b3a90a7756e48ab449eb16e688044b8decec7a9/native/zero-c/src/program_graph_repository_input.c): `RGP006` and `RGP008` match observed conflict and strict-stale failures.
- [Repository projection commands](https://github.com/vercel-labs/zerolang/blob/5b3a90a7756e48ab449eb16e688044b8decec7a9/native/zero-c/src/program_graph_repository.c): verification and explicit import/export paths.
- [Merge implementation](https://github.com/vercel-labs/zerolang/blob/5b3a90a7756e48ab449eb16e688044b8decec7a9/native/zero-c/src/program_graph_repository_merge.c): durable node matching and the observed `RGM003` conflicting-node rejection.
- [Patch parser and shape validation](https://github.com/vercel-labs/zerolang/blob/5b3a90a7756e48ab449eb16e688044b8decec7a9/native/zero-c/src/program_graph_patch.c). The runtime receipts, rather than parser inspection alone, establish the tested rollback behavior.

## Reproduce

Download `zero-darwin-x64` from the pinned release and check its digest against `CHECKSUMS.txt`. Run:

```sh
python3 reproduce.py --binary /absolute/path/to/zero-darwin-x64 --output /absolute/path/to/results
python3 verify-evidence.py
```

The runner creates its own temporary fixture directory and removes it after a successful run. It retains JSON receipts and source projections in the requested output directory. `verify-evidence.py` checks the committed evidence bundle, including its hash manifest; it does not itself run Zerolang. No API keys or model services are required.

An initial attempt to export inside the macOS Documents workspace returned `Operation not permitted`. The same fixture succeeded in a temporary directory. We recorded this as an environment restriction, not a language defect; completed runs used temporary directories.

## Remaining limits

No simultaneous-writer race, interrupted filesystem write, complex multi-file merge, exhaustive patch-operation suite, dependency integration, cross-platform execution or performance benchmark was tested. Runtime capability metadata was not assessed as a security sandbox. This review concerns editing and validation contracts, not exploitability or a security audit. We did not file an upstream issue because the completed scenarios did not establish a new defect.
