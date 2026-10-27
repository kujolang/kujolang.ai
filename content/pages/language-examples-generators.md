---
title: Generators
template: language-examples-generators
custom_url: examples/generators
description: "Yield values lazily and iterate over them."
seo_title: "Generators | Kujo"
social_image: /assets/images/social/examples-generators.jpg
---

<nav aria-label="Breadcrumb"><a href="/">Home</a> / <a href="/examples/">Examples</a> / Generators</nav>
<article class="example-panel" id="example-generators" data-example="generators" data-category="Concurrency"><p class="eyebrow">Concurrency · Executed offline · Kujo 1.9.0</p><h3>Generators</h3><p>Yield values lazily and iterate over them.</p><div class="sample-code"><pre tabindex="0"><code><span class="syntax-token"># Test: Generator Functions</span>
<span class="syntax-token"># Tests generator creation, yielding, and iteration</span>
<span class="syntax-token"># Both runtimes resume loops lazily and preserve state across every yield.</span>

print(<span class="syntax-token">&quot;=== Test 1: Simple Generator ===&quot;</span>)
<span class="syntax-token">func</span>* count() {
    <span class="syntax-token">yield</span> 1
    <span class="syntax-token">yield</span> 2
    <span class="syntax-token">yield</span> 3
}

gen := count()
print(<span class="syntax-token">&quot;Generator created, type:&quot;</span>)
print(type(gen))

print(<span class="syntax-token">&quot;&quot;</span>)
print(<span class="syntax-token">&quot;=== Test 2: Generator Iteration ===&quot;</span>)
<span class="syntax-token">for</span> n <span class="syntax-token">in</span> count() {
    print(<span class="syntax-token">&quot;Value:&quot;</span>)
    print(n)
}

print(<span class="syntax-token">&quot;&quot;</span>)
print(<span class="syntax-token">&quot;=== Test 3: Generator with State ===&quot;</span>)
</code></pre><button type="button" class="sk-button" data-copy-code hidden>Copy code</button><span role="status" data-code-status></span></div><p>Save as <a href="/samples/generators.kujo" download>generators.kujo</a>, then:</p><div class="sample-code"><pre tabindex="0"><code>kujo run generators.kujo</code></pre><button type="button" class="sk-button" data-copy-code hidden>Copy code</button><span role="status" data-code-status></span></div><details><summary>Expected output</summary><pre>=== Test 1: Simple Generator ===
Generator created, type:
generator

=== Test 2: Generator Iteration ===
Value:
1
Value:
2
Value:
3

=== Test 3: Generator with State ===
</pre></details><p><a href="https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/tests/test_generators.kujo#L1-L24">Pinned source</a> · <a href="https://docs.kujolang.ai/learn/">Language documentation</a></p></article>
<nav aria-label="Related examples"><a href="/examples/channels/">Previous: Channels</a> · <a href="/examples/json/">Next: JSON data</a></nav>
