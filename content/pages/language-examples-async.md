---
title: Async tasks
template: language-examples-async
custom_url: examples/async
description: "Await a value produced by an async function."
seo_title: "Async tasks | Kujo"
social_image: /assets/images/social/examples-async.jpg
---

<nav aria-label="Breadcrumb"><a href="/">Home</a> / <a href="/examples/">Examples</a> / Async tasks</nav>
<article class="example-panel" id="example-async" data-example="async" data-category="Concurrency"><p class="eyebrow">Concurrency · Executed offline · Kujo 1.9.0</p><h3>Async tasks</h3><p>Await a value produced by an async function.</p><div class="sample-code"><pre tabindex="0"><code><span class="syntax-token">// Simple async test</span>

<span class="syntax-token">async</span> <span class="syntax-token">func</span> get_value() {
    <span class="syntax-token">return</span> 42;
}

<span class="syntax-token">let</span> p = get_value();
println(<span class="syntax-token">&quot;Promise type: &quot;</span>, type(p));
<span class="syntax-token">let</span> result = <span class="syntax-token">await</span> p;
println(<span class="syntax-token">&quot;Result: &quot;</span>, result);
</code></pre><button type="button" class="sk-button" data-copy-code hidden>Copy code</button><span role="status" data-code-status></span></div><p>Save as <a href="/samples/async.kujo" download>async.kujo</a>, then:</p><div class="sample-code"><pre tabindex="0"><code>kujo run <span class="syntax-token">async</span>.kujo</code></pre><button type="button" class="sk-button" data-copy-code hidden>Copy code</button><span role="status" data-code-status></span></div><details><summary>Expected output</summary><pre>Promise type:  promise
Result:  42
</pre></details><p><a href="https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/simple_async_test.kujo">Pinned source</a> · <a href="https://docs.kujolang.ai/learn/">Language documentation</a></p></article>
<nav aria-label="Related examples"><a href="/examples/errors/">Previous: Error handling</a> · <a href="/examples/channels/">Next: Channels</a></nav>
