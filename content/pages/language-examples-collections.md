---
title: Collections
template: language-examples-collections
custom_url: examples/collections
description: "Combine arrays and dictionaries into a report."
seo_title: "Collections | Kujo"
social_image: /assets/images/social/examples-collections.jpg
---


 <nav class="examples-breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a><span aria-hidden="true">/</span><a href="/examples/">Examples</a><span aria-hidden="true">/</span><span aria-current="page">Collections</span></nav>
 <header class="examples-hero example-detail-hero"><div><p class="eyebrow">05 / Data</p><h1>Collections</h1><p>Combine arrays and dictionaries into a report.</p></div><div class="example-hero-meta"><span class="example-badge">Executed offline</span><a href="/examples/#category-Data">More in Data ↗</a></div></header>
 <div class="example-workbench">
 <section class="example-source" aria-labelledby="source-title"><header class="example-file-bar"><h2 id="source-title">collections.kujo</h2><a href="/samples/collections.kujo" download>Download ↓</a></header><div class="sample-code"><pre tabindex="0"><code><span class="syntax-token syntax-comment"># Expected output:</span>
<span class="syntax-token syntax-comment"># build total: 42</span>

<span class="syntax-token syntax-keyword">let</span> scores := [<span class="syntax-token syntax-number">8</span>, <span class="syntax-token syntax-number">13</span>, <span class="syntax-token syntax-number">21</span>]
<span class="syntax-token syntax-keyword">let</span> report := {<span class="syntax-token syntax-string">&quot;name&quot;</span>: <span class="syntax-token syntax-string">&quot;build&quot;</span>, <span class="syntax-token syntax-string">&quot;total&quot;</span>: scores[<span class="syntax-token syntax-number">0</span>] + scores[<span class="syntax-token syntax-number">1</span>] + scores[<span class="syntax-token syntax-number">2</span>]}

print(report[<span class="syntax-token syntax-string">&quot;name&quot;</span>] + <span class="syntax-token syntax-string">&quot; total: &quot;</span> + to_string(report[<span class="syntax-token syntax-string">&quot;total&quot;</span>]))
</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></section>
 <aside class="example-runbook" aria-labelledby="run-title"><p class="eyebrow">Run it locally</p><h2 id="run-title">Try this example.</h2><ol><li><strong>Set up Kujo</strong><p><a href="/language/">Install the runtime</a> if this is your first program.</p></li><li><strong>Save the sample</strong><p>Download <a href="/samples/collections.kujo" download>collections.kujo</a> or copy the code into a file.</p></li><li><strong>Run the command</strong><div class="sample-code"><pre tabindex="0"><code>kujo run collections.kujo</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></li></ol><a class="example-bundle-link" href="/samples/kujo-examples.tar.gz">Download all samples + fixtures ↓</a></aside>
 </div>
 <section class="example-result" aria-labelledby="result-title"><header><p class="eyebrow">Check the result</p><h2 id="result-title">Expected output</h2><p>Compare your terminal output with this recorded result.</p></header><div><div class="sample-code"><pre tabindex="0"><code>build total: 42
</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></div></section>
 <details class="example-provenance"><summary>Source &amp; verification details</summary><div><p>Verified against <a href="https://github.com/kujolang/kujo/tree/2cfaf185ad03059c89ef4f72fb061074255d00fc">Kujo 1.9.0</a>. Executed offline.</p><p><a href="https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/04-data.kujo">Pinned source</a> · <a href="https://docs.kujolang.ai/learn/">Language documentation</a></p><p class="example-checksum">SHA-256 <code>26a0903e6d03a26b989c32f43b6cac81492518a6f250dc725fabc3de3f17055a</code></p></div></details>
 <nav class="example-pagination" aria-label="Related examples"><a href="/examples/control-flow/"><span>← Previous example</span><strong>Control flow</strong></a><a href="/examples/structs/"><span>Next example →</span><strong>Structs and methods</strong></a></nav>
