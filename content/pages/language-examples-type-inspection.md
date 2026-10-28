---
title: Inspect value types
template: language-examples-type-inspection
custom_url: examples/type-inspection
description: "Inspect runtime types and check whether a value is a number or string."
seo_title: "Inspect value types | Kujo"
social_image: /assets/images/social/examples-type-inspection.jpg
---

<script type="application/ld+json">{"@context":"https://schema.org","@type":"SoftwareSourceCode","@id":"https://kujolang.ai/examples/type-inspection/#source","name":"Inspect value types","description":"Inspect runtime types and check whether a value is a number or string.","codeRepository":"https://github.com/kujolang/kujo","programmingLanguage":"Kujo","codeSampleType":"code snippet","url":"https://kujolang.ai/examples/type-inspection/","text":"func section(title) {\n    print(\"\")\n    print(\"== \" + title + \" ==\")\n}\n\nfunc kv(label, value) {\n    print(\"  \" + label + \": \" + to_string(value))\n}\n\nsection(\"Type Introspection Demo\")\n\n# 1. Basic Type Inspection\nsection(\"1. Basic Type Inspection\")\nkv(\"type(42)\", type(42))\nkv(\"type(3.14)\", type(3.14))\nkv(\"type(\\\"hello\\\")\", type(\"hello\"))\nkv(\"type(true)\", type(true))\nkv(\"type(0)\", type(0))\nkv(\"type([1, 2, 3])\", type([1, 2, 3]))\nkv(\"type({\\\"a\\\": 1})\", type({\"a\": 1}))\n\n# 2. Type Predicates\nsection(\"2. Type Predicates\")\nx := 42\nkv(\"x\", x)\nkv(\"is_int(x)\", is_int(x))\nkv(\"is_float(x)\", is_float(x))\nkv(\"is_string(x)\", is_string(x))\n","isBasedOn":"https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/type_introspection_demo.kujo#L4-L31"}</script>
 <nav class="examples-breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a><span aria-hidden="true">/</span><a href="/examples/">Examples</a><span aria-hidden="true">/</span><span aria-current="page">Inspect value types</span></nav>
 <header class="examples-hero example-detail-hero"><div><p class="eyebrow">34 / Basics</p><h1>Inspect value types</h1><p>Inspect runtime types and check whether a value is a number or string.</p></div><div class="example-hero-meta"><span class="example-badge">Executed offline</span><a href="/examples/#category-Basics">More in Basics ↗</a></div></header>
 <div class="example-workbench">
 <section class="example-source" aria-labelledby="source-title"><header class="example-file-bar"><h2 id="source-title">type-inspection.kujo</h2><a href="/samples/type-inspection.kujo" download>Download ↓</a></header><div class="sample-code"><pre tabindex="0"><code><span class="syntax-token syntax-keyword">func</span> section(title) {
    print(<span class="syntax-token syntax-string">&quot;&quot;</span>)
    print(<span class="syntax-token syntax-string">&quot;== &quot;</span> + title + <span class="syntax-token syntax-string">&quot; ==&quot;</span>)
}

<span class="syntax-token syntax-keyword">func</span> kv(label, value) {
    print(<span class="syntax-token syntax-string">&quot;  &quot;</span> + label + <span class="syntax-token syntax-string">&quot;: &quot;</span> + to_string(value))
}

section(<span class="syntax-token syntax-string">&quot;Type Introspection Demo&quot;</span>)

<span class="syntax-token syntax-comment"># 1. Basic Type Inspection</span>
section(<span class="syntax-token syntax-string">&quot;1. Basic Type Inspection&quot;</span>)
kv(<span class="syntax-token syntax-string">&quot;type(42)&quot;</span>, type(<span class="syntax-token syntax-number">42</span>))
kv(<span class="syntax-token syntax-string">&quot;type(3.14)&quot;</span>, type(<span class="syntax-token syntax-number">3.14</span>))
kv(<span class="syntax-token syntax-string">&quot;type(\&quot;hello\&quot;)&quot;</span>, type(<span class="syntax-token syntax-string">&quot;hello&quot;</span>))
kv(<span class="syntax-token syntax-string">&quot;type(true)&quot;</span>, type(<span class="syntax-token syntax-literal">true</span>))
kv(<span class="syntax-token syntax-string">&quot;type(0)&quot;</span>, type(<span class="syntax-token syntax-number">0</span>))
kv(<span class="syntax-token syntax-string">&quot;type([1, 2, 3])&quot;</span>, type([<span class="syntax-token syntax-number">1</span>, <span class="syntax-token syntax-number">2</span>, <span class="syntax-token syntax-number">3</span>]))
kv(<span class="syntax-token syntax-string">&quot;type({\&quot;a\&quot;: 1})&quot;</span>, type({<span class="syntax-token syntax-string">&quot;a&quot;</span>: <span class="syntax-token syntax-number">1</span>}))

<span class="syntax-token syntax-comment"># 2. Type Predicates</span>
section(<span class="syntax-token syntax-string">&quot;2. Type Predicates&quot;</span>)
x := <span class="syntax-token syntax-number">42</span>
kv(<span class="syntax-token syntax-string">&quot;x&quot;</span>, x)
kv(<span class="syntax-token syntax-string">&quot;is_int(x)&quot;</span>, is_int(x))
kv(<span class="syntax-token syntax-string">&quot;is_float(x)&quot;</span>, is_float(x))
kv(<span class="syntax-token syntax-string">&quot;is_string(x)&quot;</span>, is_string(x))
</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></section>
 <aside class="example-runbook" aria-labelledby="run-title"><p class="eyebrow">Run it locally</p><h2 id="run-title">Try this example.</h2><ol><li><strong>Set up Kujo</strong><p><a href="/language/">Install the runtime</a> before running the command below.</p></li><li><strong>Save the sample</strong><p>Download <a href="/samples/type-inspection.kujo" download>type-inspection.kujo</a> or copy the code into a file with that name.</p></li><li><strong>Run the command</strong><div class="sample-code"><pre tabindex="0"><code>kujo run type-inspection.kujo</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></li></ol><a class="example-bundle-link" href="/samples/kujo-examples.tar.gz">Download all samples + fixtures ↓</a></aside>
 </div>
 <section class="example-result" aria-labelledby="result-title"><header><p class="eyebrow">Check the result</p><h2 id="result-title">Expected output</h2><p>Your terminal should show this output.</p></header><div><div class="sample-code"><pre tabindex="0"><code>
== Type Introspection Demo ==

== 1. Basic Type Inspection ==
  type(42): int
  type(3.14): float
  type(&quot;hello&quot;): string
  type(true): bool
  type(0): int
  type([1, 2, 3]): array
  type({&quot;a&quot;: 1}): dict

== 2. Type Predicates ==
  x: 42
  is_int(x): true
  is_float(x): false
  is_string(x): false
</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></div></section>
 <details class="example-provenance"><summary>Source &amp; verification details</summary><div><p>Verified against <a href="https://github.com/kujolang/kujo/tree/2cfaf185ad03059c89ef4f72fb061074255d00fc">Kujo 1.9.0</a>. Executed offline.</p><p><a href="https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/type_introspection_demo.kujo#L4-L31">Pinned source</a> · <a href="https://docs.kujolang.ai/learn/">Language documentation</a></p><p class="example-checksum">SHA-256 <code>cb085aa0bcb44a962acf646ff38332df56e9e7d6a9e18b6e46f5e04ee9a5350d</code></p></div></details>
 <nav class="example-pagination" aria-label="Related examples"><a href="/examples/partial-application/"><span>← Previous example</span><strong>Capture function arguments</strong></a><a href="/examples/function-composition/"><span>Next example →</span><strong>Compose functions</strong></a></nav>
