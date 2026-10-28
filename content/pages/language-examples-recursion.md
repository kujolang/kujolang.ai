---
title: Calculate a factorial
template: language-examples-recursion
custom_url: examples/recursion
description: "Call a function recursively until it reaches a base case."
seo_title: "Calculate a factorial | Kujo"
social_image: /assets/images/social/examples-recursion.jpg
---

<script type="application/ld+json">{"@context":"https://schema.org","@type":"SoftwareSourceCode","@id":"https://kujolang.ai/examples/recursion/#source","name":"Calculate a factorial","description":"Call a function recursively until it reaches a base case.","codeRepository":"https://github.com/kujolang/kujo","programmingLanguage":"Kujo","codeSampleType":"code snippet","url":"https://kujolang.ai/examples/recursion/","text":"// Test factorial with VM\nfunc factorial(n) {\n    if n \u003c= 1 {\n        return 1\n    }\n    return n * factorial(n - 1)\n}\n\nresult := factorial(5)\nprint(\"factorial(5) =\", result)\n","isBasedOn":"https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/test_factorial.kujo"}</script>
 <nav class="examples-breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a><span aria-hidden="true">/</span><a href="/examples/">Examples</a><span aria-hidden="true">/</span><span aria-current="page">Calculate a factorial</span></nav>
 <header class="examples-hero example-detail-hero"><div><p class="eyebrow">38 / Basics</p><h1>Calculate a factorial</h1><p>Call a function recursively until it reaches a base case.</p></div><div class="example-hero-meta"><span class="example-badge">Executed offline</span><a href="/examples/#category-Basics">More in Basics ↗</a></div></header>
 <div class="example-workbench">
 <section class="example-source" aria-labelledby="source-title"><header class="example-file-bar"><h2 id="source-title">recursion.kujo</h2><a href="/samples/recursion.kujo" download>Download ↓</a></header><div class="sample-code"><pre tabindex="0"><code><span class="syntax-token syntax-comment">// Test factorial with VM</span>
<span class="syntax-token syntax-keyword">func</span> factorial(n) {
    <span class="syntax-token syntax-keyword">if</span> n &lt;= <span class="syntax-token syntax-number">1</span> {
        <span class="syntax-token syntax-keyword">return</span> <span class="syntax-token syntax-number">1</span>
    }
    <span class="syntax-token syntax-keyword">return</span> n * factorial(n - <span class="syntax-token syntax-number">1</span>)
}

result := factorial(<span class="syntax-token syntax-number">5</span>)
print(<span class="syntax-token syntax-string">&quot;factorial(5) =&quot;</span>, result)
</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></section>
 <aside class="example-runbook" aria-labelledby="run-title"><p class="eyebrow">Run it locally</p><h2 id="run-title">Try this example.</h2><ol><li><strong>Set up Kujo</strong><p><a href="/language/">Install the runtime</a> before running the command below.</p></li><li><strong>Save the sample</strong><p>Download <a href="/samples/recursion.kujo" download>recursion.kujo</a> or copy the code into a file with that name.</p></li><li><strong>Run the command</strong><div class="sample-code"><pre tabindex="0"><code>kujo run recursion.kujo</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></li></ol><a class="example-bundle-link" href="/samples/kujo-examples.tar.gz">Download all samples + fixtures ↓</a></aside>
 </div>
 <section class="example-result" aria-labelledby="result-title"><header><p class="eyebrow">Check the result</p><h2 id="result-title">Expected output</h2><p>Your terminal should show this output.</p></header><div><div class="sample-code"><pre tabindex="0"><code>factorial(5) = 120
</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></div></section>
 <details class="example-provenance"><summary>Source &amp; verification details</summary><div><p>Verified against <a href="https://github.com/kujolang/kujo/tree/2cfaf185ad03059c89ef4f72fb061074255d00fc">Kujo 1.9.0</a>. Executed offline.</p><p><a href="https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/test_factorial.kujo">Pinned source</a> · <a href="https://docs.kujolang.ai/learn/">Language documentation</a></p><p class="example-checksum">SHA-256 <code>2b449eb836ac68b862c5007c7006cb053276021a9eb97addeda6fdf8dda96da3</code></p></div></details>
 <nav class="example-pagination" aria-label="Related examples"><a href="/examples/loop-control/"><span>← Previous example</span><strong>Break and continue</strong></a><a href="/examples/loop-scope/"><span>Next example →</span><strong>Accumulate a total</strong></a></nav>
