# Competitive research — 2026-10-19

## Identity and evidence hierarchy

The dated catalog is the public claim registry. Each matrix cell names its layer and sources. Implementation inspection supports narrower claims than vendor positioning. Tests were inspected where linked; they were not executed unless the validation report explicitly says so. No benchmark results from another project are republished as independent measurements.

- **Bend:** bend-lang.org links to bendlang/bend, guide/GUIDE.md, and displays v2.0.37. Its current guide describes affine dependent types, laws and proofs, explicit IO, CPU/GPU execution and a sequential JS target. Source snapshot: 64230dcb96f2da2cc5a44524e42d5eb34771a6ec. The negative proof fixture shows an unfilled law rejected with an expected failure. Do not use old HVM-era descriptions to deny current proof support. Guide limits include unsafe/foreign exclusions and an unproven translation to the secondary kernel.
- **BAML:** boundaryml.com links to BoundaryML/baml. Current source 648ad5ed10f543c129b51789c7d02e29b64f06f7 contains the new language checker and test runner. The release API returned baml-language-0.22.3-nightly.20261018.a; this is an observed nightly identifier, not a tested stable baseline. Current product positioning extends beyond the older structured-output DSL. The site advertises tracing, typed AI functions, bridges and concurrency. No overhead, speed or agent-productivity claim was independently demonstrated.
- **Zero:** the requested domain identifies a developer-preview language with value semantics and documented interpreter/native/C++ execution modes. Homepage and installation links do not establish a canonical source repository or numbered version. Search did not resolve that gap. The page explicitly identifies this domain, avoids a guessed repository, and marks implementation support as partial/documentation-only. No claim of formal verification or AI-native intent is inferred.

## Coverage of requested dimensions

| Dimension | Kujo | Bend | BAML | Zero |
|---|---|---|---|---|
| Goals/audience | Language plus explicit workflow accountability | Laws/proofs and parallel programs | Current agent-oriented language/application integration | Documented systems behavior; preview |
| Syntax/model | CLI/type-checker source and runnable artifact exercise | Affine dependent types; pure with IO per guide | Current checker/test command source; TypeScript-like product description | Website value semantics; not source-verified |
| Compilation/runtime | VM/interpreter and optional JIT paths inspected | Native CPU/GPU and JS documented | Compiler/check/test paths inspected; no full build here | Interpreter/JIT/native/C++ documented only |
| Types/static analysis | Type-checker implementation | Proof-relevant types and termination constraints documented | Diagnostic collection implementation | Static check mode documented |
| Formal verification | General theorem proving unknown | Supported in documented subset; negative source fixture inspected | General theorem proving unknown | Unknown |
| Tests/evaluations | Eval source plus local artifact oracle | Proof fixtures inspected; no runtime run here | Test runner/result tests inspected | Assertion workflow documented only |
| Agent workflow | Separate Spec/Eval/Dispatch/SDK tools | Laws/PROOF convention documented | Agent tooling/AI functions advertised; checker/tests inspected | Agent-specific tooling unknown |
| Determinism | Offline exercise only; external effects not assumed deterministic | Pure model does not certify every effect/replay | External-model determinism not verified | Cleanup/parallel semantics do not establish reproducible provider execution |
| Isolation | Workcell configured boundary; not automatic in core | Process invocation is not a sandbox per guide | Current site advertises sandbox; isolation guarantees not verified | Unknown |
| Observability/evidence | RunLedger, Workcell, Watchdog separately scoped | Proof verdicts; broader run ledger unknown | Tracing advertised; not measured | Unknown |
| Packages/integrations | Ecosystem has separate pins; inspect selected tool | Base and foreign interfaces documented | Bridges described; direct Kujo bridge unknown | Native-library support documented; canonical source unavailable |
| Performance | No comparative claim | Vendor claims not independently reproduced | Vendor claims not independently reproduced | No measured comparison |
| Deployment | Local runtime and tool-specific deployments | Target-specific behavior documented | Standalone/bridged adoption advertised | Native/browser modes documented |
| Maturity/limitations | Varies by tool; no blanket enterprise certification | Young/evolving; proof and target boundaries | Generational documentation drift; pinned version required | Developer preview; identity/release gaps |

Nonapplicable: shared throughput rankings are not applicable because no equivalent workload and environment were established. Unknown is used instead of unsupported whenever documentation or local verification is insufficient.

## Search observations and editorial opportunity

Qualitative research used the available web search tool on 2026-10-19. Queries included Kujo/Bend, “Kujo vs BAML”, Bend/BAML comparisons, zero-lang.com repository, and AI-generated-code verification/coding-agent evaluation. The interface does not provide a controlled Google/Bing country/device ranking export. Separate Google and Bing result positions, commercial keyword metrics and AI-answer citations are **NOT AVAILABLE — DATA ACCESS REQUIRED**. Do not interpret missing surfaced results as proof of no indexed results.

Observed result themes: Vercel's agent-evaluation article emphasizes harnesses and independent checks; OpenAI's verification research discusses the generation/verification gap; search also surfaced community workflow questions about agents changing tests and checking the wrong files. Technical claims in the public pages use primary sources. Community results inform questions, not implementation facts.

Useful gap: explain what a proof, test, trace, receipt and release gate actually establishes. Current language generations also make outdated “Bend has no proofs” or “BAML is only a wrapper” comparisons unsafe. The new pages address those distinctions instead of inventing a winner.

## Inspiration and additional candidates

Boat's comparison hub was inspected for its use of workflow categories, transparent limits and technical references. No copy, markup, benchmarks or design was reused.

Python, TypeScript and Rust are included as established alternatives in decision guidance, with official documentation links; detailed head-to-head pages are deferred until real migration/workload evidence exists. Official Mojo, MoonBit and Unison sites were reviewed as additional candidates. Mojo's hardware focus, MoonBit's language/tooling focus and Unison's programming model deserve separate research rather than thin pages. Aria, Lumen and fastC surfaced in search but did not receive implementation review and are not ranked or described as verified alternatives.

## Primary research links

- https://boat.dev/compare
- https://bend-lang.org/
- https://github.com/bendlang/bend
- https://boundaryml.com/
- https://github.com/BoundaryML/baml
- https://zero-lang.com/
- https://zero-lang.com/download.html
- https://vercel.com/i/evaluating-ai-coding-agents
- https://alignment.openai.com/scaling-code-verification/
- https://mojolang.org/
- https://www.moonbitlang.com/
- https://www.unison-lang.org/

See catalog.json for claim-level pinned sources, source-checks.json for HTTP receipts and ecosystem-inventory.json for local source hashes.
