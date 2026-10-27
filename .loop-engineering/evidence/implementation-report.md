# Language-first website implementation

## Product changes

Before: a full-viewport hero, ecosystem CTA and introductory video. After: a
shorter language hero, Get Started and View Examples, visible executable code,
practical language capabilities, runtime AI mechanisms, installation, six
job-oriented ecosystem goals, proof and three onboarding paths. Monochrome
SiteKit typography, dither imagery and the video remain. No frontend framework
or visitor-side dependency was added.

The native select explorer supports keyboard input and exact-code copy with
live feedback. Static HTML contains all six featured samples without JavaScript.
The collection supports search and categories; deep pages have breadcrumbs,
commands, expected output, pinned sources, download links and previous/next.

## Routes

Modified: `/`, `/ecosystem/`, and global navigation on every page.
New: `/language/`, `/examples/`, `/development-workflow/`, `/performance/`.
New example routes under `/examples/`: hello-world, variables, functions,
control-flow, collections, structs, pattern-matching, errors, async, channels,
generators, json, structured-output, request-hash, replay, streaming,
capabilities, tests, modules, files, http (all canonical trailing slash URLs).
Existing comparison, ecosystem, skills, workflows, Writing and utility routes
remain available. 25 new Howl cards bring the total to 281 shareable routes.

## Source and verification

21 samples derive verbatim or by exact line range from Kujo v1.9.0 commit
2cfaf185ad03059c89ef4f72fb061074255d00fc. SHA-256 and output assertions are in
examples/catalog.json. The official macOS x64 runtime archive was checked
against its published SHA-256. 17 scripts execute offline, one test fixture runs
through test-run, and three are explicitly check-only. AI replay and streaming
use bundled synthetic cassettes. AI calls are denied without the capability
and succeed with the explicit grant. Nested route tests reject traversal,
empty segments, absolute paths and noncanonical segments.

Packages and SDK integration are separate linked guides. Check-only examples
are not claimed to have run; live provider calls are not claimed to be tested.
The benchmark measures ten process starts plus a tiny function script, records
hardware/software and exact source hash, and makes no cross-language claim.

## Evaluation commands

Native harness: ../kujo-workflows/loop-engineering/scripts/run-workflow.sh
--config .loop-engineering/loop.yml. One evaluation per bounded run; archive
before the runner reuses iterations/001. Prior project state was preserved.

Gates: examples:check, examples:verify, npm test, production Kujo SSG build,
images:responsive, verify-site-contract.sh, validate-generated-output.sh,
language:verify, social:verify, compare:verify, JavaScript and shell syntax,
npm audit --omit=dev, browser suite with axe-core, and git diff --check.
Baseline npm ci and 26 Node tests passed. Baseline build passed; its later
social check overlapped new card generation and is explicitly not a passing
unchanged-baseline receipt. Run 01 caught route and stale-navigation failures.
Run 02 passed all configured gates. Run 03 passed all 14 non-browser gates on the final application, but its
new macOS native-select keyboard test used the wrong popup interaction. A
focused native browser-correction run uses native type-to-select plus Tab,
passes browser/accessibility checks, and requires all prior gate receipts and
SHA-256 equality of application source and generated output. No application
change or acceptance gate was dropped during that retry.
See the final native eval.log and verdict.yml for authoritative results.

## Browser and visual evidence

Desktop 1440×1000, tablet 768×1024, mobile 390×844. The browser suite checks native
keyboard selection, exact clipboard content, filtering and empty results,
mobile menu/Escape, page overflow, console errors and no-JavaScript fallback.
Axe checks WCAG 2 A/AA and 2.1 AA on six key page types. Baseline and resulting
screenshots are in evidence/browser/. The tighter hero and calmer text backdrop
keep the category, primary actions and code entry near the beginning.

JavaScript increases from 23,217 to 25,892 bytes (6,278 bytes gzipped total).
CSS increases from 58,321 to 61,699 bytes (10,036 bytes gzipped total).
No new runtime dependency. Existing responsive image processing is retained.

## Release

Push to main invokes the unchanged authorized GitHub Pages deployment mechanism;
the build now additionally checks sample integrity/runtime behavior, language
routes and exhaustive social metadata before uploading. Publication confirmation
and exact commit/run identifiers are recorded in the release receipt and Strata
handoff after deployment succeeds. No DNS, secrets or branch protection changes.

## Confirmed publication

GitHub Pages run https://github.com/kujolang/kujolang.ai/actions/runs/40599173462
succeeded for commit 7573955c618e05b3b1ec3612c750c3bea935b03f. The native release
loop verified 28 live routes, canonical URLs, social metadata and new example
content. See release/evidence/production.json. The final follow-up commit only
records evidence and its verifier; it does not alter the deployed application.

Verbatim upstream samples, raw command logs and archived baseline HTML retain
their original whitespace. Git attributes exempt those artifacts from whitespace
formatting checks; source SHA-256 and executable/output assertions remain strict.

Strata saved the pinned-example maintenance procedure as
244d3612-0f46-477e-a04c-72d3ccc93319. Exact ID and scoped title retrieval pass.
A broad semantic paraphrase missed the note even after a focused-tag update; use
the exact title/ID or the linked release handoff. No duplicate memory was written.
SignalBox: no captures warranted.
