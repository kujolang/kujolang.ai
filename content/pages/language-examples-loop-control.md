---
title: Break and continue
template: language-examples-loop-control
custom_url: examples/loop-control
description: "Stop a loop early and skip even numbers."
seo_title: "Break and continue | Kujo"
social_image: /assets/images/social/examples-loop-control.jpg
---

<script type="application/ld+json">{"@context":"https://schema.org","@type":"SoftwareSourceCode","@id":"https://kujolang.ai/examples/loop-control/#source","name":"Break and continue","description":"Stop a loop early and skip even numbers.","codeRepository":"https://github.com/kujolang/kujo","programmingLanguage":"Kujo","codeSampleType":"code snippet","url":"https://kujolang.ai/examples/loop-control/","text":"print(\"=== Break in While Loop ===\")\nx := 0\nwhile true {\n    print(x)\n    x := x + 1\n    if x >= 5 {\n        break\n    }\n}\nprint(\"Broke out of loop\")\n\nprint(\"\")\nprint(\"=== Continue in While Loop ===\")\ny := 0\nwhile y \u003c 10 {\n    y := y + 1\n    if y % 2 == 0 {\n        continue\n    }\n    print(y)\n}\n","isBasedOn":"https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/loop_control_simple.kujo#L4-L24"}</script>
 <nav class="examples-breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a><span aria-hidden="true">/</span><a href="/examples/">Examples</a><span aria-hidden="true">/</span><span aria-current="page">Break and continue</span></nav>
 <header class="examples-hero example-detail-hero"><div><p class="eyebrow">37 / Basics</p><h1>Break and continue</h1><p>Stop a loop early and skip even numbers.</p></div><div class="example-hero-meta"><span class="example-badge">Executed offline</span><a href="/examples/#category-Basics">More in Basics ↗</a></div></header>
 <div class="example-workbench">
 <section class="example-source" aria-labelledby="source-title"><header class="example-file-bar"><h2 id="source-title">loop-control.kujo</h2><a href="/samples/loop-control.kujo" download>Download ↓</a></header><div class="sample-code"><pre tabindex="0"><code>print(<span class="syntax-token syntax-string">&quot;=== Break in While Loop ===&quot;</span>)
x := <span class="syntax-token syntax-number">0</span>
while <span class="syntax-token syntax-literal">true</span> {
    print(x)
    x := x + <span class="syntax-token syntax-number">1</span>
    <span class="syntax-token syntax-keyword">if</span> x &gt;= <span class="syntax-token syntax-number">5</span> {
        break
    }
}
print(<span class="syntax-token syntax-string">&quot;Broke out of loop&quot;</span>)

print(<span class="syntax-token syntax-string">&quot;&quot;</span>)
print(<span class="syntax-token syntax-string">&quot;=== Continue in While Loop ===&quot;</span>)
y := <span class="syntax-token syntax-number">0</span>
while y &lt; <span class="syntax-token syntax-number">10</span> {
    y := y + <span class="syntax-token syntax-number">1</span>
    <span class="syntax-token syntax-keyword">if</span> y % <span class="syntax-token syntax-number">2</span> == <span class="syntax-token syntax-number">0</span> {
        continue
    }
    print(y)
}
</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></section>
 <aside class="example-runbook" aria-labelledby="run-title"><p class="eyebrow">Run it locally</p><h2 id="run-title">Try this example.</h2><ol><li><strong>Set up Kujo</strong><p><a href="/language/">Install the runtime</a> before running the command below.</p></li><li><strong>Save the sample</strong><p>Download <a href="/samples/loop-control.kujo" download>loop-control.kujo</a> or copy the code into a file with that name.</p></li><li><strong>Run the command</strong><div class="sample-code"><pre tabindex="0"><code>kujo run loop-control.kujo</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></li></ol><a class="example-bundle-link" href="/samples/kujo-examples.tar.gz">Download all samples + fixtures ↓</a></aside>
 </div>
 <section class="example-result" aria-labelledby="result-title"><header><p class="eyebrow">Check the result</p><h2 id="result-title">Expected output</h2><p>Your terminal should show this output.</p></header><div><div class="sample-code"><pre tabindex="0"><code>=== Break in While Loop ===
0
1
2
3
4
Broke out of loop

=== Continue in While Loop ===
1
3
5
7
9
</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></div></section>
 <details class="example-provenance"><summary>Source &amp; verification details</summary><div><p>Verified against <a href="https://github.com/kujolang/kujo/tree/2cfaf185ad03059c89ef4f72fb061074255d00fc">Kujo 1.9.0</a>. Executed offline.</p><p><a href="https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/loop_control_simple.kujo#L4-L24">Pinned source</a> · <a href="https://docs.kujolang.ai/learn/">Language documentation</a></p><p class="example-checksum">SHA-256 <code>fe54c89dc1fe3fe34fe8ecd1bc35664590753264698c43a341c71c5b34988e6d</code></p></div></details>
 <nav class="example-pagination" aria-label="Related examples"><a href="/examples/result-errors/"><span>← Previous example</span><strong>Return errors as values</strong></a><a href="/examples/recursion/"><span>Next example →</span><strong>Calculate a factorial</strong></a></nav>
