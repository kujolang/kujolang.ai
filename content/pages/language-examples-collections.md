---
title: Collections
template: language-examples-collections
custom_url: examples/collections
description: "Combine arrays and dictionaries into a report."
seo_title: "Collections | Kujo"
social_image: /assets/images/social/examples-collections.jpg
---

<nav aria-label="Breadcrumb"><a href="/">Home</a> / <a href="/examples/">Examples</a> / Collections</nav>
<article class="example-panel" id="example-collections" data-example="collections" data-category="Data"><p class="eyebrow">Data · Executed offline · Kujo 1.9.0</p><h3>Collections</h3><p>Combine arrays and dictionaries into a report.</p><div class="sample-code"><pre tabindex="0"><code><span class="syntax-token"># Expected output:</span>
<span class="syntax-token"># build total: 42</span>

<span class="syntax-token">let</span> scores := [8, 13, 21]
<span class="syntax-token">let</span> report := {<span class="syntax-token">&quot;name&quot;</span>: <span class="syntax-token">&quot;build&quot;</span>, <span class="syntax-token">&quot;total&quot;</span>: scores[0] + scores[1] + scores[2]}

print(report[<span class="syntax-token">&quot;name&quot;</span>] + <span class="syntax-token">&quot; total: &quot;</span> + to_string(report[<span class="syntax-token">&quot;total&quot;</span>]))
</code></pre><button type="button" class="sk-button" data-copy-code hidden>Copy code</button><span role="status" data-code-status></span></div><p>Save as <a href="/samples/collections.kujo" download>collections.kujo</a>, then:</p><div class="sample-code"><pre tabindex="0"><code>kujo run collections.kujo</code></pre><button type="button" class="sk-button" data-copy-code hidden>Copy code</button><span role="status" data-code-status></span></div><details><summary>Expected output</summary><pre>build total: 42
</pre></details><p><a href="https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/04-data.kujo">Pinned source</a> · <a href="https://docs.kujolang.ai/learn/">Language documentation</a></p></article>
<nav aria-label="Related examples"><a href="/examples/control-flow/">Previous: Control flow</a> · <a href="/examples/structs/">Next: Structs and methods</a></nav>
