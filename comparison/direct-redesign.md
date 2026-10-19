# Direct comparison technical field guides

The Bend, BAML and Zero pages now extend the hub's visual language with an asymmetric hero, explicit review baseline, adoption cards, three architecture lenses, a sourced capability matrix, a separate decision-scenario table, four-step evaluation plan, independent artifact-check panel, integration boundaries and native FAQ/source disclosures.

`catalog.json` owns `deepDive` content. Architecture claims require registered source IDs; scenario rows and evaluation steps describe proposed trials, not executed competitor results. Existing pinned facts and research dates remain unchanged. Zero's repository/release identity is still explicitly unverified. No performance ranking or untested adapter is implied.

`render-comparison-direct.mjs` generates the HTML and matching public Markdown additions. Frontmatter selects `post-comparison-direct.html` through the SSG's existing template mechanism. Discovery and workflow-guide layouts remain unchanged. Shared SiteKit cards, tables and accordions were inspected in `assets/css/sitekit.css`; the extension adds scoped CSS and no browser JavaScript.

Validation includes 19 Node tests, generator parity, focused SSG output, two semantic tables and section anchors per direct page, desktop/mobile browser review, then full-site CI and live-route verification. Local focused builds resolve unchanged destinations against the prior full output; deployment CI builds and validates the complete site.
