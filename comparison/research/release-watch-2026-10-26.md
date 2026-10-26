# Release watch — 2026-10-26

This is a version-drift review of the existing full comparison audit. It does not reinterpret or re-run the older executable fixtures.

| Project | Latest stable | Latest preview | Executed evidence still shown | Primary source retrieved |
| --- | --- | --- | --- | --- |
| Kujo | 1.9.0, 2026-10-22 | none identified | 1.8.2 | GitHub Releases API, 2026-10-26T09:01Z |
| Bend | 2.0.39, 2026-10-23 | none identified | 2.0.37 | GitHub Releases API, 2026-10-26T09:01Z |
| BAML | 0.23.0, 2026-10-26 | 0.23.1-nightly.20261025.a, published 2026-10-26 | 0.22.2 and earlier 0.22.3 nightlies | GitHub Releases API, 2026-10-26T09:01Z |
| Vercel Zerolang | 0.3.4, 2026-06-13 | none identified | 0.3.4 | GitHub Releases API, 2026-10-26T09:01Z |

## Correction

The catalog's release metadata now identifies the current stable Kujo, Bend and BAML releases and separately labels BAML's latest nightly. It does not describe those newer versions as tested. All behavior and proof-boundary statements remain tied to their recorded fixture versions.

## Remaining high-impact uncertainty

1. BAML 0.23.0 and 0.23.1 nightly need isolated Python-boundary reruns before the earlier crash result can be generalized.
2. Bend 2.0.39 needs the proof and JavaScript-boundary controls rerun before any behavioral comparison moves from 2.0.37.
3. Kujo 1.9.0 needs the public producer/checker controls rerun before the site changes its 1.8.2 fixture wording.

Recheck on any release above, on a material documentation change, or at the next weekly audit. The standing full claim ledger remains `comparison/research/fact-review-2026-10-19/claim-ledger.csv`.
