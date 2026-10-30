# Release review

All eight proposed workflows are implemented as Kujo applications, not placeholder cards. Each individual ZIP contains the application, shared request policy, input and schema, authored offline responses and a walkthrough README. The combined ZIP contains all eight directories. Archive freshness checks compare every packaged file; runtime tests execute the actual downloadable archives in isolated temporary directories.

The nineteen runtime tests cover all offline outputs, all eight live adapters against a controlled local HTTP server, two-attempt rejection, invented source locations/invoice amounts/dates/citations, insufficient evidence and recovery, 100-record interrupted/resumed batches, duplicate IDs and changed inputs, wrong/stale editor approvals, prompt-regression failure/recovery, provider exhaustion and a real local HTTP timeout with fallback. No paid provider requests were made. Live model quality is explicitly not claimed.

Reviewed metadata and code/schema alignment for 63 language/application pages and social coverage for 318 routes. New Howl cards use the real sources; the final 25 rendered artifacts are preserved in howl-showcase.zip. Desktop/mobile browser checks cover all eight application pages, every code copy control, exact downloaded ZIP bytes, no-JS behavior and accessibility. The original 50 samples remain separately indexed and verified.

The first full run exposed stale generated output after a final due-date grounding check was added. The final run rebuilt the whole site and passed all 24 gates. Its 1,167 responsive images were reused only after verifying unchanged source image hashes, generator hash and resulting image hashes; see image-reuse.json. The default PATH-based runtime used by CI was separately verified with all nineteen tests after correcting the test runner's local default.

Reviewed the cards and responsive walkthrough layouts. Corrected the dark-panel eyebrow contrast before the final passing run. Download packaging uses an explicit source-file allowlist so local result/checkpoint files do not enter future bundles.

Application boundaries are explicit: review locations do not prove findings; citation quotes do not prove entailment; the editor requires a trusted local directory and is not an OS sandbox; checkpoints are single-writer process recovery, not distributed/power-loss durability; request count and token limits are not dollar budgets. These are documented scope limits, not hidden unresolved defects. SignalBox: no captures warranted.
