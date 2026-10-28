---
title: Convert text to numbers
template: language-examples-type-conversion
custom_url: examples/type-conversion
description: "Read an age and a balance from strings."
seo_title: "Convert text to numbers | Kujo"
social_image: /assets/images/social/examples-type-conversion.jpg
---

<script type="application/ld+json">{"@context":"https://schema.org","@type":"SoftwareSourceCode","@id":"https://kujolang.ai/examples/type-conversion/#source","name":"Convert text to numbers","description":"Read an age and a balance from strings.","codeRepository":"https://github.com/kujolang/kujo","programmingLanguage":"Kujo","codeSampleType":"code snippet","url":"https://kujolang.ai/examples/type-conversion/","text":"age := to_int(\"25\")\nbalance := to_float(\"150.75\")\nprint(\"Age: \" + to_string(age))\nprint(\"Balance: \" + to_string(balance))\n\nif age >= 18 {\n    print(\"Status: Adult\")\n}\n","isBasedOn":"https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/type_conversion.kujo#L47-L54"}</script>
 <nav class="examples-breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a><span aria-hidden="true">/</span><a href="/examples/">Examples</a><span aria-hidden="true">/</span><span aria-current="page">Convert text to numbers</span></nav>
 <header class="examples-hero example-detail-hero"><div><p class="eyebrow">26 / Basics</p><h1>Convert text to numbers</h1><p>Read an age and a balance from strings.</p></div><div class="example-hero-meta"><span class="example-badge">Executed offline</span><a href="/examples/#category-Basics">More in Basics ↗</a></div></header>
 <div class="example-workbench">
 <section class="example-source" aria-labelledby="source-title"><header class="example-file-bar"><h2 id="source-title">type-conversion.kujo</h2><a href="/samples/type-conversion.kujo" download>Download ↓</a></header><div class="sample-code"><pre tabindex="0"><code>age := to_int(<span class="syntax-token syntax-string">&quot;25&quot;</span>)
balance := to_float(<span class="syntax-token syntax-string">&quot;150.75&quot;</span>)
print(<span class="syntax-token syntax-string">&quot;Age: &quot;</span> + to_string(age))
print(<span class="syntax-token syntax-string">&quot;Balance: &quot;</span> + to_string(balance))

<span class="syntax-token syntax-keyword">if</span> age &gt;= <span class="syntax-token syntax-number">18</span> {
    print(<span class="syntax-token syntax-string">&quot;Status: Adult&quot;</span>)
}
</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></section>
 <aside class="example-runbook" aria-labelledby="run-title"><p class="eyebrow">Run it locally</p><h2 id="run-title">Try this example.</h2><ol><li><strong>Set up Kujo</strong><p><a href="/language/">Install the runtime</a> before running the command below.</p></li><li><strong>Save the sample</strong><p>Download <a href="/samples/type-conversion.kujo" download>type-conversion.kujo</a> or copy the code into a file with that name.</p></li><li><strong>Run the command</strong><div class="sample-code"><pre tabindex="0"><code>kujo run type-conversion.kujo</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></li></ol><a class="example-bundle-link" href="/samples/kujo-examples.tar.gz">Download all samples + fixtures ↓</a></aside>
 </div>
 <section class="example-result" aria-labelledby="result-title"><header><p class="eyebrow">Check the result</p><h2 id="result-title">Expected output</h2><p>Your terminal should show this output.</p></header><div><div class="sample-code"><pre tabindex="0"><code>Age: 25
Balance: 150.75
Status: Adult
</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></div></section>
 <details class="example-provenance"><summary>Source &amp; verification details</summary><div><p>Verified against <a href="https://github.com/kujolang/kujo/tree/2cfaf185ad03059c89ef4f72fb061074255d00fc">Kujo 1.9.0</a>. Executed offline.</p><p><a href="https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/type_conversion.kujo#L47-L54">Pinned source</a> · <a href="https://docs.kujolang.ai/learn/">Language documentation</a></p><p class="example-checksum">SHA-256 <code>cf3a8e81f3c4a0ea9eafafa5e9cbbff7f17ae3e140576881eeffc338697c9895</code></p></div></details>
 <nav class="example-pagination" aria-label="Related examples"><a href="/examples/url-decoding/"><span>← Previous example</span><strong>Decode URL components</strong></a><a href="/examples/data-access/"><span>Next example →</span><strong>Read nested data</strong></a></nav>
