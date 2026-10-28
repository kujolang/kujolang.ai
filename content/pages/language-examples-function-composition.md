---
title: Compose functions
template: language-examples-function-composition
custom_url: examples/function-composition
description: "Pass one function result into the next to calculate a value or format text."
seo_title: "Compose functions | Kujo"
social_image: /assets/images/social/examples-function-composition.jpg
---

<script type="application/ld+json">{"@context":"https://schema.org","@type":"SoftwareSourceCode","@id":"https://kujolang.ai/examples/function-composition/#source","name":"Compose functions","description":"Pass one function result into the next to calculate a value or format text.","codeRepository":"https://github.com/kujolang/kujo","programmingLanguage":"Kujo","codeSampleType":"code snippet","url":"https://kujolang.ai/examples/function-composition/","text":"func double(x) { return x * 2 }\nfunc add_five(x) { return x + 5 }\nfunc square(x) { return x * x }\n\nlet result := square(add_five(double(3)))\nprint(result)\n\nfunc exclaim(s) { return s + \"!\" }\nlet greeting := exclaim(to_upper(\"hello\"))\nprint(greeting)\n","isBasedOn":"https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/method_chaining.kujo#L22-L31"}</script>
 <nav class="examples-breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a><span aria-hidden="true">/</span><a href="/examples/">Examples</a><span aria-hidden="true">/</span><span aria-current="page">Compose functions</span></nav>
 <header class="examples-hero example-detail-hero"><div><p class="eyebrow">35 / Basics</p><h1>Compose functions</h1><p>Pass one function result into the next to calculate a value or format text.</p></div><div class="example-hero-meta"><span class="example-badge">Executed offline</span><a href="/examples/#category-Basics">More in Basics ↗</a></div></header>
 <div class="example-workbench">
 <section class="example-source" aria-labelledby="source-title"><header class="example-file-bar"><h2 id="source-title">function-composition.kujo</h2><a href="/samples/function-composition.kujo" download>Download ↓</a></header><div class="sample-code"><pre tabindex="0"><code><span class="syntax-token syntax-keyword">func</span> double(x) { <span class="syntax-token syntax-keyword">return</span> x * <span class="syntax-token syntax-number">2</span> }
<span class="syntax-token syntax-keyword">func</span> add_five(x) { <span class="syntax-token syntax-keyword">return</span> x + <span class="syntax-token syntax-number">5</span> }
<span class="syntax-token syntax-keyword">func</span> square(x) { <span class="syntax-token syntax-keyword">return</span> x * x }

<span class="syntax-token syntax-keyword">let</span> result := square(add_five(double(<span class="syntax-token syntax-number">3</span>)))
print(result)

<span class="syntax-token syntax-keyword">func</span> exclaim(s) { <span class="syntax-token syntax-keyword">return</span> s + <span class="syntax-token syntax-string">&quot;!&quot;</span> }
<span class="syntax-token syntax-keyword">let</span> greeting := exclaim(to_upper(<span class="syntax-token syntax-string">&quot;hello&quot;</span>))
print(greeting)
</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></section>
 <aside class="example-runbook" aria-labelledby="run-title"><p class="eyebrow">Run it locally</p><h2 id="run-title">Try this example.</h2><ol><li><strong>Set up Kujo</strong><p><a href="/language/">Install the runtime</a> before running the command below.</p></li><li><strong>Save the sample</strong><p>Download <a href="/samples/function-composition.kujo" download>function-composition.kujo</a> or copy the code into a file with that name.</p></li><li><strong>Run the command</strong><div class="sample-code"><pre tabindex="0"><code>kujo run function-composition.kujo</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></li></ol><a class="example-bundle-link" href="/samples/kujo-examples.tar.gz">Download all samples + fixtures ↓</a></aside>
 </div>
 <section class="example-result" aria-labelledby="result-title"><header><p class="eyebrow">Check the result</p><h2 id="result-title">Expected output</h2><p>Your terminal should show this output.</p></header><div><div class="sample-code"><pre tabindex="0"><code>121
HELLO!
</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></div></section>
 <details class="example-provenance"><summary>Source &amp; verification details</summary><div><p>Verified against <a href="https://github.com/kujolang/kujo/tree/2cfaf185ad03059c89ef4f72fb061074255d00fc">Kujo 1.9.0</a>. Executed offline.</p><p><a href="https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/method_chaining.kujo#L22-L31">Pinned source</a> · <a href="https://docs.kujolang.ai/learn/">Language documentation</a></p><p class="example-checksum">SHA-256 <code>b7a394ceb404ed5e904cd6418622a5d6569f4e6ecf04cf30aaa0a0ab13dd7214</code></p></div></details>
 <nav class="example-pagination" aria-label="Related examples"><a href="/examples/type-inspection/"><span>← Previous example</span><strong>Inspect value types</strong></a><a href="/examples/result-errors/"><span>Next example →</span><strong>Return errors as values</strong></a></nav>
