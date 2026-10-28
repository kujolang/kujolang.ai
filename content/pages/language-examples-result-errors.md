---
title: Return errors as values
template: language-examples-result-errors
custom_url: examples/result-errors
description: "Return Ok or Err from division and handle each result."
seo_title: "Return errors as values | Kujo"
social_image: /assets/images/social/examples-result-errors.jpg
---

<script type="application/ld+json">{"@context":"https://schema.org","@type":"SoftwareSourceCode","@id":"https://kujolang.ai/examples/result-errors/#source","name":"Return errors as values","description":"Return Ok or Err from division and handle each result.","codeRepository":"https://github.com/kujolang/kujo","programmingLanguage":"Kujo","codeSampleType":"code snippet","url":"https://kujolang.ai/examples/result-errors/","text":"# Example 1: Division with error handling\nfunc divide(a, b) {\n    if b == 0 {\n        return Err(\"Cannot divide by zero\")\n    }\n    return Ok(a / b)\n}\n\nprint(\"Example 1: Safe Division\")\nlet result1 := divide(10, 2)\nmatch result1 {\n    case Ok(value): {\n        print(\"10 / 2 = \" + to_string(value))\n    }\n    case Err(error): {\n        print(\"Error: \" + error)\n    }\n}\n\nlet result2 := divide(10, 0)\nmatch result2 {\n    case Ok(value): {\n        print(\"10 / 0 = \" + to_string(value))\n    }\n    case Err(error): {\n        print(\"Error: \" + error)\n    }\n}\n","isBasedOn":"https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/result_option_demo.kujo#L7-L34"}</script>
 <nav class="examples-breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a><span aria-hidden="true">/</span><a href="/examples/">Examples</a><span aria-hidden="true">/</span><span aria-current="page">Return errors as values</span></nav>
 <header class="examples-hero example-detail-hero"><div><p class="eyebrow">36 / Basics</p><h1>Return errors as values</h1><p>Return Ok or Err from division and handle each result.</p></div><div class="example-hero-meta"><span class="example-badge">Executed offline</span><a href="/examples/#category-Basics">More in Basics ↗</a></div></header>
 <div class="example-workbench">
 <section class="example-source" aria-labelledby="source-title"><header class="example-file-bar"><h2 id="source-title">result-errors.kujo</h2><a href="/samples/result-errors.kujo" download>Download ↓</a></header><div class="sample-code"><pre tabindex="0"><code><span class="syntax-token syntax-comment"># Example 1: Division with error handling</span>
<span class="syntax-token syntax-keyword">func</span> divide(a, b) {
    <span class="syntax-token syntax-keyword">if</span> b == <span class="syntax-token syntax-number">0</span> {
        <span class="syntax-token syntax-keyword">return</span> Err(<span class="syntax-token syntax-string">&quot;Cannot divide by zero&quot;</span>)
    }
    <span class="syntax-token syntax-keyword">return</span> Ok(a / b)
}

print(<span class="syntax-token syntax-string">&quot;Example 1: Safe Division&quot;</span>)
<span class="syntax-token syntax-keyword">let</span> result1 := divide(<span class="syntax-token syntax-number">10</span>, <span class="syntax-token syntax-number">2</span>)
<span class="syntax-token syntax-keyword">match</span> result1 {
    <span class="syntax-token syntax-keyword">case</span> Ok(value): {
        print(<span class="syntax-token syntax-string">&quot;10 / 2 = &quot;</span> + to_string(value))
    }
    <span class="syntax-token syntax-keyword">case</span> Err(error): {
        print(<span class="syntax-token syntax-string">&quot;Error: &quot;</span> + error)
    }
}

<span class="syntax-token syntax-keyword">let</span> result2 := divide(<span class="syntax-token syntax-number">10</span>, <span class="syntax-token syntax-number">0</span>)
<span class="syntax-token syntax-keyword">match</span> result2 {
    <span class="syntax-token syntax-keyword">case</span> Ok(value): {
        print(<span class="syntax-token syntax-string">&quot;10 / 0 = &quot;</span> + to_string(value))
    }
    <span class="syntax-token syntax-keyword">case</span> Err(error): {
        print(<span class="syntax-token syntax-string">&quot;Error: &quot;</span> + error)
    }
}
</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></section>
 <aside class="example-runbook" aria-labelledby="run-title"><p class="eyebrow">Run it locally</p><h2 id="run-title">Try this example.</h2><ol><li><strong>Set up Kujo</strong><p><a href="/language/">Install the runtime</a> before running the command below.</p></li><li><strong>Save the sample</strong><p>Download <a href="/samples/result-errors.kujo" download>result-errors.kujo</a> or copy the code into a file with that name.</p></li><li><strong>Run the command</strong><div class="sample-code"><pre tabindex="0"><code>kujo run result-errors.kujo</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></li></ol><a class="example-bundle-link" href="/samples/kujo-examples.tar.gz">Download all samples + fixtures ↓</a></aside>
 </div>
 <section class="example-result" aria-labelledby="result-title"><header><p class="eyebrow">Check the result</p><h2 id="result-title">Expected output</h2><p>Your terminal should show this output.</p></header><div><div class="sample-code"><pre tabindex="0"><code>Example 1: Safe Division
10 / 2 = 5
Error: Cannot divide by zero
</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></div></section>
 <details class="example-provenance"><summary>Source &amp; verification details</summary><div><p>Verified against <a href="https://github.com/kujolang/kujo/tree/2cfaf185ad03059c89ef4f72fb061074255d00fc">Kujo 1.9.0</a>. Executed offline.</p><p><a href="https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/result_option_demo.kujo#L7-L34">Pinned source</a> · <a href="https://docs.kujolang.ai/learn/">Language documentation</a></p><p class="example-checksum">SHA-256 <code>d3bc848d5589f64f410b2ad55d107ac3b8709a4a6225682c182b78097eb4e2df</code></p></div></details>
 <nav class="example-pagination" aria-label="Related examples"><a href="/examples/function-composition/"><span>← Previous example</span><strong>Compose functions</strong></a><a href="/examples/loop-control/"><span>Next example →</span><strong>Break and continue</strong></a></nav>
