---
title: Structs and methods
template: language-examples-structs
custom_url: examples/structs
description: "Return a new counter from an instance method."
seo_title: "Structs and methods | Kujo"
social_image: /assets/images/social/examples-structs.jpg
---

<nav aria-label="Breadcrumb"><a href="/">Home</a> / <a href="/examples/">Examples</a> / Structs and methods</nav>
<article class="example-panel" id="example-structs" data-example="structs" data-category="Data"><p class="eyebrow">Data · Executed offline · Kujo 1.9.0</p><h3>Structs and methods</h3><p>Return a new counter from an instance method.</p><div class="sample-code"><pre tabindex="0"><code><span class="syntax-token"># Struct methods with an explicit self parameter</span>

<span class="syntax-token">struct</span> Counter {
    value: int,

    <span class="syntax-token">func</span> increment(self) {
        <span class="syntax-token">return</span> Counter { value: self.value + 1 }
    }

    <span class="syntax-token">func</span> add(self, amount) {
        <span class="syntax-token">return</span> Counter { value: self.value + amount }
    }

    <span class="syntax-token">func</span> describe(self) {
        <span class="syntax-token">return</span> <span class="syntax-token">&quot;Counter(&quot;</span> + to_string(self.value) + <span class="syntax-token">&quot;)&quot;</span>
    }
}

<span class="syntax-token">let</span> initial := Counter { value: 1 }
<span class="syntax-token">let</span> incremented := initial.increment()
<span class="syntax-token">let</span> advanced := incremented.add(8)

assert_equal(initial.value, 1)
assert_equal(incremented.value, 2)
assert_equal(advanced.value, 10)
print(advanced.describe())
</code></pre><button type="button" class="sk-button" data-copy-code hidden>Copy code</button><span role="status" data-code-status></span></div><p>Save as <a href="/samples/structs.kujo" download>structs.kujo</a>, then:</p><div class="sample-code"><pre tabindex="0"><code>kujo run structs.kujo</code></pre><button type="button" class="sk-button" data-copy-code hidden>Copy code</button><span role="status" data-code-status></span></div><details><summary>Expected output</summary><pre>Counter(10)
</pre></details><p><a href="https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/struct_self_methods.kujo">Pinned source</a> · <a href="https://docs.kujolang.ai/learn/">Language documentation</a></p></article>
<nav aria-label="Related examples"><a href="/examples/collections/">Previous: Collections</a> · <a href="/examples/pattern-matching/">Next: Enums and pattern matching</a></nav>
