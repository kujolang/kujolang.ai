---
title: Combine arrays
template: language-examples-array-spread
custom_url: examples/array-spread
description: "Combine arrays, insert values and copy a list with spread syntax."
seo_title: "Combine arrays | Kujo"
social_image: /assets/images/social/examples-array-spread.jpg
---

<script type="application/ld+json">{"@context":"https://schema.org","@type":"SoftwareSourceCode","@id":"https://kujolang.ai/examples/array-spread/#source","name":"Combine arrays","description":"Combine arrays, insert values and copy a list with spread syntax.","codeRepository":"https://github.com/kujolang/kujo","programmingLanguage":"Kujo","codeSampleType":"code snippet","url":"https://kujolang.ai/examples/array-spread/","text":"# Combine arrays\nfruits := [\"apple\", \"banana\"]\nvegetables := [\"carrot\", \"broccoli\"]\nfood := [...fruits, ...vegetables]\nprint(\"All food: \" + to_string(food))\n\n# Add elements while spreading\nnumbers := [2, 3, 4]\nextended := [1, ...numbers, 5, 6]\nprint(\"Extended numbers: \" + to_string(extended))\n\n# Clone an array\noriginal := [10, 20, 30]\nclone := [...original]\nprint(\"Clone: \" + to_string(clone))\n","isBasedOn":"https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/spread_operator_demo.kujo#L6-L20"}</script>
 <nav class="examples-breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a><span aria-hidden="true">/</span><a href="/examples/">Examples</a><span aria-hidden="true">/</span><span aria-current="page">Combine arrays</span></nav>
 <header class="examples-hero example-detail-hero"><div><p class="eyebrow">28 / Data</p><h1>Combine arrays</h1><p>Combine arrays, insert values and copy a list with spread syntax.</p></div><div class="example-hero-meta"><span class="example-badge">Executed offline</span><a href="/examples/#category-Data">More in Data ↗</a></div></header>
 <div class="example-workbench">
 <section class="example-source" aria-labelledby="source-title"><header class="example-file-bar"><h2 id="source-title">array-spread.kujo</h2><a href="/samples/array-spread.kujo" download>Download ↓</a></header><div class="sample-code"><pre tabindex="0"><code><span class="syntax-token syntax-comment"># Combine arrays</span>
fruits := [<span class="syntax-token syntax-string">&quot;apple&quot;</span>, <span class="syntax-token syntax-string">&quot;banana&quot;</span>]
vegetables := [<span class="syntax-token syntax-string">&quot;carrot&quot;</span>, <span class="syntax-token syntax-string">&quot;broccoli&quot;</span>]
food := [...fruits, ...vegetables]
print(<span class="syntax-token syntax-string">&quot;All food: &quot;</span> + to_string(food))

<span class="syntax-token syntax-comment"># Add elements while spreading</span>
numbers := [<span class="syntax-token syntax-number">2</span>, <span class="syntax-token syntax-number">3</span>, <span class="syntax-token syntax-number">4</span>]
extended := [<span class="syntax-token syntax-number">1</span>, ...numbers, <span class="syntax-token syntax-number">5</span>, <span class="syntax-token syntax-number">6</span>]
print(<span class="syntax-token syntax-string">&quot;Extended numbers: &quot;</span> + to_string(extended))

<span class="syntax-token syntax-comment"># Clone an array</span>
original := [<span class="syntax-token syntax-number">10</span>, <span class="syntax-token syntax-number">20</span>, <span class="syntax-token syntax-number">30</span>]
clone := [...original]
print(<span class="syntax-token syntax-string">&quot;Clone: &quot;</span> + to_string(clone))
</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></section>
 <aside class="example-runbook" aria-labelledby="run-title"><p class="eyebrow">Run it locally</p><h2 id="run-title">Try this example.</h2><ol><li><strong>Set up Kujo</strong><p><a href="/language/">Install the runtime</a> before running the command below.</p></li><li><strong>Save the sample</strong><p>Download <a href="/samples/array-spread.kujo" download>array-spread.kujo</a> or copy the code into a file with that name.</p></li><li><strong>Run the command</strong><div class="sample-code"><pre tabindex="0"><code>kujo run array-spread.kujo</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></li></ol><a class="example-bundle-link" href="/samples/kujo-examples.tar.gz">Download all samples + fixtures ↓</a></aside>
 </div>
 <section class="example-result" aria-labelledby="result-title"><header><p class="eyebrow">Check the result</p><h2 id="result-title">Expected output</h2><p>Your terminal should show this output.</p></header><div><div class="sample-code"><pre tabindex="0"><code>All food: [apple, banana, carrot, broccoli]
Extended numbers: [1, 2, 3, 4, 5, 6]
Clone: [10, 20, 30]
</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></div></section>
 <details class="example-provenance"><summary>Source &amp; verification details</summary><div><p>Verified against <a href="https://github.com/kujolang/kujo/tree/2cfaf185ad03059c89ef4f72fb061074255d00fc">Kujo 1.9.0</a>. Executed offline.</p><p><a href="https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/spread_operator_demo.kujo#L6-L20">Pinned source</a> · <a href="https://docs.kujolang.ai/learn/">Language documentation</a></p><p class="example-checksum">SHA-256 <code>e4ac25f54e85d0fa50e72b44f1cb564ad688c0914ba462aa9ab757b4e8a51268</code></p></div></details>
 <nav class="example-pagination" aria-label="Related examples"><a href="/examples/data-access/"><span>← Previous example</span><strong>Read nested data</strong></a><a href="/examples/map-and-filter/"><span>Next example →</span><strong>Map and filter arrays</strong></a></nav>
