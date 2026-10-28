# Linked-page refinement

## Scope and decisions

Follow-up to the homepage/Examples release at e4a7415. Preserve prior Loop state; use a new bounded run with the installed native runner. Root loop.yml is unchanged. Implementation is agent-directed; the native harness records context, evaluates real gates and writes the verdict. Explicit user authorization covers commits, push and the existing Pages deployment after verification.

- Remove the homepage hero eyebrow. Center the explorer heading with space below it; use white panels instead of tan.
- Default to Deterministic AI request IDs. Keep a native select as the underlying value and provide a themed disclosure/listbox with mouse, keyboard, focus, Escape, outside-click and type-ahead handling. Without JavaScript, all sample panels remain available.
- Center plain copy feedback vertically with its 44px icon and keep the 1.5-second timeout. Extend absolute icons, side gutters and readable highlighted code to content pages and tool installation panels. Scope the shared handler to sample-code wrappers so existing tool controls do not trigger a second handler with a null root.
- Give Language/Get Started, Development Workflow and Performance dedicated guide layouts: overview cards, section navigation, clear sections and a shared next step. Apply Orwell editing guidance while retaining installation versions, platform constraints, reproducibility and measured/unmeasured boundaries.
- Performance exposes the existing receipt's median, range, environment and all ten observations. No new benchmark or comparative speed claim is introduced.

## Rendering correction

The former generic Markdown rendering converted YAML sequence entries into HTML lists inside a code block and stripped indentation. The dedicated guide templates preserve authored code bytes. Source lives in content/pages/{language,development-workflow,performance}.md; run npm run guides:generate after editing. npm run guides:check and the Node test prevent stale projections. Browser checks assert the YAML indentation and absence of list markup inside code, as well as exact clipboard content.

## Review and verification

Desktop guide screenshots were visually reviewed. The native gates cover the build, 21 pinned runtime examples, content contracts, comparisons, source synchronization, responsive images and all browser suites. The guide browser suite checks desktop/tablet/mobile layouts, receipt details, accessibility, no-JavaScript content and every internal page destination linked from the homepage. The first run precedes a final small list-card styling refinement; acceptance will bind the final source and build separately.

No unresolved future action or SignalBox-worthy finding is introduced.

## Iteration result

The initial browser run caught transient misalignment when the live-region text changed: computed typography/transform could still be at their initial values on the first rendered frame. The final fix keeps status geometry unconditional, uses a 44px flex alignment area matching the icon, and disables transitions/animations for feedback. The first run is historical, not release acceptance. Final acceptance is under acceptance/iterations/001/ and includes the final list-card styles, performance explanation and all 28 Node tests.
