---
title: Functions and operators
template: language-examples-functions
custom_url: examples/functions
description: "Sum a collection with a reusable function."
seo_title: "Functions and operators | Kujo"
social_image: /assets/images/social/examples-functions.jpg
---

<nav aria-label="Breadcrumb"><a href="/">Home</a> / <a href="/examples/">Examples</a> / Functions and operators</nav>
<article class="example-panel" id="example-functions" data-example="functions" data-category="Basics"><p class="eyebrow">Basics · Executed offline · Kujo 1.9.0</p><h3>Functions and operators</h3><p>Sum a collection with a reusable function.</p><div class="sample-code"><pre tabindex="0"><code><span class="syntax-token"># Expected output:</span>
<span class="syntax-token"># total: 42</span>

<span class="syntax-token">func</span> total(values) {
    <span class="syntax-token">mut</span> sum := 0
    <span class="syntax-token">for</span> value <span class="syntax-token">in</span> values {
        sum = sum + value
    }
    <span class="syntax-token">return</span> sum
}

<span class="syntax-token">let</span> scores := [8, 13, 21]
print(<span class="syntax-token">&quot;total: &quot;</span> + to_string(total(scores)))
</code></pre><button type="button" class="sk-button" data-copy-code hidden>Copy code</button><span role="status" data-code-status></span></div><p>Save as <a href="/samples/functions.kujo" download>functions.kujo</a>, then:</p><div class="sample-code"><pre tabindex="0"><code>kujo run functions.kujo</code></pre><button type="button" class="sk-button" data-copy-code hidden>Copy code</button><span role="status" data-code-status></span></div><details><summary>Expected output</summary><pre>total: 42
</pre></details><p><a href="https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/02-functions.kujo">Pinned source</a> · <a href="https://docs.kujolang.ai/learn/">Language documentation</a></p></article>
<nav aria-label="Related examples"><a href="/examples/variables/">Previous: Variables and types</a> · <a href="/examples/control-flow/">Next: Control flow</a></nav>
