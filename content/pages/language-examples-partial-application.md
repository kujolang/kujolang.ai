---
title: Capture function arguments
template: language-examples-partial-application
custom_url: examples/partial-application
description: "Make a reusable adder by capturing a value in a closure."
seo_title: "Capture function arguments | Kujo"
social_image: /assets/images/social/examples-partial-application.jpg
---

<script type="application/ld+json">{"@context":"https://schema.org","@type":"SoftwareSourceCode","@id":"https://kujolang.ai/examples/partial-application/#source","name":"Capture function arguments","description":"Make a reusable adder by capturing a value in a closure.","codeRepository":"https://github.com/kujolang/kujo","programmingLanguage":"Kujo","codeSampleType":"code snippet","url":"https://kujolang.ai/examples/partial-application/","text":"func make_adder(x) {\n    return func(y) {\n        return x + y\n    }\n}\n\nadd5 := make_adder(5)\nprint(add5(3))  # Should print 8\nprint(add5(10)) # Should print 15\n","isBasedOn":"https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/test_closure_simple.kujo"}</script>
 <nav class="examples-breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a><span aria-hidden="true">/</span><a href="/examples/">Examples</a><span aria-hidden="true">/</span><span aria-current="page">Capture function arguments</span></nav>
 <header class="examples-hero example-detail-hero"><div><p class="eyebrow">33 / Basics</p><h1>Capture function arguments</h1><p>Make a reusable adder by capturing a value in a closure.</p></div><div class="example-hero-meta"><span class="example-badge">Executed offline</span><a href="/examples/#category-Basics">More in Basics ↗</a></div></header>
 <div class="example-workbench">
 <section class="example-source" aria-labelledby="source-title"><header class="example-file-bar"><h2 id="source-title">partial-application.kujo</h2><a href="/samples/partial-application.kujo" download>Download ↓</a></header><div class="sample-code"><pre tabindex="0"><code><span class="syntax-token syntax-keyword">func</span> make_adder(x) {
    <span class="syntax-token syntax-keyword">return</span> <span class="syntax-token syntax-keyword">func</span>(y) {
        <span class="syntax-token syntax-keyword">return</span> x + y
    }
}

add5 := make_adder(<span class="syntax-token syntax-number">5</span>)
print(add5(<span class="syntax-token syntax-number">3</span>))  <span class="syntax-token syntax-comment"># Should print 8</span>
print(add5(<span class="syntax-token syntax-number">10</span>)) <span class="syntax-token syntax-comment"># Should print 15</span>
</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></section>
 <aside class="example-runbook" aria-labelledby="run-title"><p class="eyebrow">Run it locally</p><h2 id="run-title">Try this example.</h2><ol><li><strong>Set up Kujo</strong><p><a href="/language/">Install the runtime</a> before running the command below.</p></li><li><strong>Save the sample</strong><p>Download <a href="/samples/partial-application.kujo" download>partial-application.kujo</a> or copy the code into a file with that name.</p></li><li><strong>Run the command</strong><div class="sample-code"><pre tabindex="0"><code>kujo run partial-application.kujo</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></li></ol><a class="example-bundle-link" href="/samples/kujo-examples.tar.gz">Download all samples + fixtures ↓</a></aside>
 </div>
 <section class="example-result" aria-labelledby="result-title"><header><p class="eyebrow">Check the result</p><h2 id="result-title">Expected output</h2><p>Your terminal should show this output.</p></header><div><div class="sample-code"><pre tabindex="0"><code>8
15
</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></div></section>
 <details class="example-provenance"><summary>Source &amp; verification details</summary><div><p>Verified against <a href="https://github.com/kujolang/kujo/tree/2cfaf185ad03059c89ef4f72fb061074255d00fc">Kujo 1.9.0</a>. Executed offline.</p><p><a href="https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/test_closure_simple.kujo">Pinned source</a> · <a href="https://docs.kujolang.ai/learn/">Language documentation</a></p><p class="example-checksum">SHA-256 <code>385fbef0bd64b69801a4de19f4c485dc62911bdab14487b29fdccfe6ba161b54</code></p></div></details>
 <nav class="example-pagination" aria-label="Related examples"><a href="/examples/optional-values/"><span>← Previous example</span><strong>Handle missing values</strong></a><a href="/examples/type-inspection/"><span>Next example →</span><strong>Inspect value types</strong></a></nav>
