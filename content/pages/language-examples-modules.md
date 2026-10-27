---
title: Modules and imports
template: language-examples-modules
custom_url: examples/modules
description: "Inspect dotted imports and named imports."
seo_title: "Modules and imports | Kujo"
social_image: /assets/images/social/examples-modules.jpg
---

<nav aria-label="Breadcrumb"><a href="/">Home</a> / <a href="/examples/">Examples</a> / Modules and imports</nav>
<article class="example-panel" id="example-modules" data-example="modules" data-category="Tooling"><p class="eyebrow">Tooling · Checked only · Kujo 1.9.0</p><h3>Modules and imports</h3><p>Inspect dotted imports and named imports.</p><p class="example-note">Parse-only upstream tour. The imported modules are intentionally not supplied; this is not a standalone runnable program.</p><div class="sample-code"><pre tabindex="0"><code><span class="syntax-token"># Parse-only module import tour.</span>
<span class="syntax-token"># To run this pattern, create the imported files beside your script or inside a package root.</span>

<span class="syntax-token">import</span> math_helpers
<span class="syntax-token">from</span> metrics <span class="syntax-token">import</span> average, total
<span class="syntax-token">from</span> src.util <span class="syntax-token">import</span> value
<span class="syntax-token">from</span> src.core.math <span class="syntax-token">import</span> add
</code></pre><button type="button" class="sk-button" data-copy-code hidden>Copy code</button><span role="status" data-code-status></span></div><p>Save as <a href="/samples/modules.kujo" download>modules.kujo</a>, then:</p><div class="sample-code"><pre tabindex="0"><code>kujo check modules.kujo</code></pre><button type="button" class="sk-button" data-copy-code hidden>Copy code</button><span role="status" data-code-status></span></div><p><a href="https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/05-modules.kujo">Pinned source</a> · <a href="https://docs.kujolang.ai/learn/">Language documentation</a></p></article>
<nav aria-label="Related examples"><a href="/examples/tests/">Previous: Tests</a> · <a href="/examples/files/">Next: File operations</a></nav>
