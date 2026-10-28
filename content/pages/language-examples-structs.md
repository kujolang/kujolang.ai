---
title: Structs and methods
template: language-examples-structs
custom_url: examples/structs
description: "Return a new counter from an instance method."
seo_title: "Structs and methods | Kujo"
social_image: /assets/images/social/examples-structs.jpg
---

<script type="application/ld+json">{"@context":"https://schema.org","@type":"SoftwareSourceCode","@id":"https://kujolang.ai/examples/structs/#source","name":"Structs and methods","description":"Return a new counter from an instance method.","codeRepository":"https://github.com/kujolang/kujo","programmingLanguage":"Kujo","codeSampleType":"code snippet","url":"https://kujolang.ai/examples/structs/","text":"# Struct methods with an explicit self parameter\n\nstruct Counter {\n    value: int,\n\n    func increment(self) {\n        return Counter { value: self.value + 1 }\n    }\n\n    func add(self, amount) {\n        return Counter { value: self.value + amount }\n    }\n\n    func describe(self) {\n        return \"Counter(\" + to_string(self.value) + \")\"\n    }\n}\n\nlet initial := Counter { value: 1 }\nlet incremented := initial.increment()\nlet advanced := incremented.add(8)\n\nassert_equal(initial.value, 1)\nassert_equal(incremented.value, 2)\nassert_equal(advanced.value, 10)\nprint(advanced.describe())\n","isBasedOn":"https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/struct_self_methods.kujo"}</script>
 <nav class="examples-breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a><span aria-hidden="true">/</span><a href="/examples/">Examples</a><span aria-hidden="true">/</span><span aria-current="page">Structs and methods</span></nav>
 <header class="examples-hero example-detail-hero"><div><p class="eyebrow">06 / Data</p><h1>Structs and methods</h1><p>Return a new counter from an instance method.</p></div><div class="example-hero-meta"><span class="example-badge">Executed offline</span><a href="/examples/#category-Data">More in Data ↗</a></div></header>
 <div class="example-workbench">
 <section class="example-source" aria-labelledby="source-title"><header class="example-file-bar"><h2 id="source-title">structs.kujo</h2><a href="/samples/structs.kujo" download>Download ↓</a></header><div class="sample-code"><pre tabindex="0"><code><span class="syntax-token syntax-comment"># Struct methods with an explicit self parameter</span>

<span class="syntax-token syntax-keyword">struct</span> Counter {
    value: int,

    <span class="syntax-token syntax-keyword">func</span> increment(self) {
        <span class="syntax-token syntax-keyword">return</span> Counter { value: self.value + <span class="syntax-token syntax-number">1</span> }
    }

    <span class="syntax-token syntax-keyword">func</span> add(self, amount) {
        <span class="syntax-token syntax-keyword">return</span> Counter { value: self.value + amount }
    }

    <span class="syntax-token syntax-keyword">func</span> describe(self) {
        <span class="syntax-token syntax-keyword">return</span> <span class="syntax-token syntax-string">&quot;Counter(&quot;</span> + to_string(self.value) + <span class="syntax-token syntax-string">&quot;)&quot;</span>
    }
}

<span class="syntax-token syntax-keyword">let</span> initial := Counter { value: <span class="syntax-token syntax-number">1</span> }
<span class="syntax-token syntax-keyword">let</span> incremented := initial.increment()
<span class="syntax-token syntax-keyword">let</span> advanced := incremented.add(<span class="syntax-token syntax-number">8</span>)

assert_equal(initial.value, <span class="syntax-token syntax-number">1</span>)
assert_equal(incremented.value, <span class="syntax-token syntax-number">2</span>)
assert_equal(advanced.value, <span class="syntax-token syntax-number">10</span>)
print(advanced.describe())
</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></section>
 <aside class="example-runbook" aria-labelledby="run-title"><p class="eyebrow">Run it locally</p><h2 id="run-title">Try this example.</h2><ol><li><strong>Set up Kujo</strong><p><a href="/language/">Install the runtime</a> before running the command below.</p></li><li><strong>Save the sample</strong><p>Download <a href="/samples/structs.kujo" download>structs.kujo</a> or copy the code into a file with that name.</p></li><li><strong>Run the command</strong><div class="sample-code"><pre tabindex="0"><code>kujo run structs.kujo</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></li></ol><a class="example-bundle-link" href="/samples/kujo-examples.tar.gz">Download all samples + fixtures ↓</a></aside>
 </div>
 <section class="example-result" aria-labelledby="result-title"><header><p class="eyebrow">Check the result</p><h2 id="result-title">Expected output</h2><p>Your terminal should show this output.</p></header><div><div class="sample-code"><pre tabindex="0"><code>Counter(10)
</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></div></section>
 <details class="example-provenance"><summary>Source &amp; verification details</summary><div><p>Verified against <a href="https://github.com/kujolang/kujo/tree/2cfaf185ad03059c89ef4f72fb061074255d00fc">Kujo 1.9.0</a>. Executed offline.</p><p><a href="https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/struct_self_methods.kujo">Pinned source</a> · <a href="https://docs.kujolang.ai/learn/">Language documentation</a></p><p class="example-checksum">SHA-256 <code>fa2c4c4c75bf6cc56f772fbd954de6bdbe5d1ab80fe0a271408f9b419dc985ad</code></p></div></details>
 <nav class="example-pagination" aria-label="Related examples"><a href="/examples/collections/"><span>← Previous example</span><strong>Collections</strong></a><a href="/examples/pattern-matching/"><span>Next example →</span><strong>Enums and pattern matching</strong></a></nav>
