---
title: Control flow
template: language-examples-control-flow
custom_url: examples/control-flow
description: "Choose which code runs with a comparison."
seo_title: "Control flow | Kujo"
social_image: /assets/images/social/examples-control-flow.jpg
---

<script type="application/ld+json">{"@context":"https://schema.org","@type":"SoftwareSourceCode","@id":"https://kujolang.ai/examples/control-flow/#source","name":"Control flow","description":"Choose which code runs with a comparison.","codeRepository":"https://github.com/kujolang/kujo","programmingLanguage":"Kujo","codeSampleType":"code snippet","url":"https://kujolang.ai/examples/control-flow/","text":"# Expected output:\n# pass: build score\n\nlet score := 42\n\nif score >= 40 {\n    print(\"pass: build score\")\n} else {\n    print(\"retry: build score\")\n}\n","isBasedOn":"https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/03-control-flow.kujo"}</script>
 <nav class="examples-breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a><span aria-hidden="true">/</span><a href="/examples/">Examples</a><span aria-hidden="true">/</span><span aria-current="page">Control flow</span></nav>
 <header class="examples-hero example-detail-hero"><div><p class="eyebrow">04 / Basics</p><h1>Control flow</h1><p>Choose which code runs with a comparison.</p></div><div class="example-hero-meta"><span class="example-badge">Executed offline</span><a href="/examples/#category-Basics">More in Basics ↗</a></div></header>
 <div class="example-workbench">
 <section class="example-source" aria-labelledby="source-title"><header class="example-file-bar"><h2 id="source-title">control-flow.kujo</h2><a href="/samples/control-flow.kujo" download>Download ↓</a></header><div class="sample-code"><pre tabindex="0"><code><span class="syntax-token syntax-comment"># Expected output:</span>
<span class="syntax-token syntax-comment"># pass: build score</span>

<span class="syntax-token syntax-keyword">let</span> score := <span class="syntax-token syntax-number">42</span>

<span class="syntax-token syntax-keyword">if</span> score &gt;= <span class="syntax-token syntax-number">40</span> {
    print(<span class="syntax-token syntax-string">&quot;pass: build score&quot;</span>)
} <span class="syntax-token syntax-keyword">else</span> {
    print(<span class="syntax-token syntax-string">&quot;retry: build score&quot;</span>)
}
</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></section>
 <aside class="example-runbook" aria-labelledby="run-title"><p class="eyebrow">Run it locally</p><h2 id="run-title">Try this example.</h2><ol><li><strong>Set up Kujo</strong><p><a href="/language/">Install the runtime</a> before running the command below.</p></li><li><strong>Save the sample</strong><p>Download <a href="/samples/control-flow.kujo" download>control-flow.kujo</a> or copy the code into a file with that name.</p></li><li><strong>Run the command</strong><div class="sample-code"><pre tabindex="0"><code>kujo run control-flow.kujo</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></li></ol><a class="example-bundle-link" href="/samples/kujo-examples.tar.gz">Download all samples + fixtures ↓</a></aside>
 </div>
 <section class="example-result" aria-labelledby="result-title"><header><p class="eyebrow">Check the result</p><h2 id="result-title">Expected output</h2><p>Your terminal should show this output.</p></header><div><div class="sample-code"><pre tabindex="0"><code>pass: build score
</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></div></section>
 <details class="example-provenance"><summary>Source &amp; verification details</summary><div><p>Verified against <a href="https://github.com/kujolang/kujo/tree/2cfaf185ad03059c89ef4f72fb061074255d00fc">Kujo 1.9.0</a>. Executed offline.</p><p><a href="https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/03-control-flow.kujo">Pinned source</a> · <a href="https://docs.kujolang.ai/learn/">Language documentation</a></p><p class="example-checksum">SHA-256 <code>98b756da1a9e20a74c0b55fe4bc1645d2aae425f64f0e0f6bfaff2096d57a35d</code></p></div></details>
 <nav class="example-pagination" aria-label="Related examples"><a href="/examples/functions/"><span>← Previous example</span><strong>Functions and operators</strong></a><a href="/examples/collections/"><span>Next example →</span><strong>Collections</strong></a></nav>
