---
title: Handle missing values
template: language-examples-optional-values
custom_url: examples/optional-values
description: "Look up users and handle both Some and None."
seo_title: "Handle missing values | Kujo"
social_image: /assets/images/social/examples-optional-values.jpg
---

<script type="application/ld+json">{"@context":"https://schema.org","@type":"SoftwareSourceCode","@id":"https://kujolang.ai/examples/optional-values/#source","name":"Handle missing values","description":"Look up users and handle both Some and None.","codeRepository":"https://github.com/kujolang/kujo","programmingLanguage":"Kujo","codeSampleType":"code snippet","url":"https://kujolang.ai/examples/optional-values/","text":"func find_user_by_id(id) {\n    if id == 1 {\n        return Some(\"Alice\")\n    }\n    if id == 2 {\n        return Some(\"Bob\")\n    }\n    if id == 3 {\n        return Some(\"Charlie\")\n    }\n    return None\n}\n\nlet users := [1, 2, 99, 3]\nfor user_id in users {\n    let user := find_user_by_id(user_id)\n    match user {\n        case Some(name): {\n            print(\"User \" + to_string(user_id) + \": \" + name)\n        }\n        case None: {\n            print(\"User \" + to_string(user_id) + \": Not found\")\n        }\n    }\n}\n","isBasedOn":"https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/result_option_demo.kujo#L88-L112"}</script>
 <nav class="examples-breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a><span aria-hidden="true">/</span><a href="/examples/">Examples</a><span aria-hidden="true">/</span><span aria-current="page">Handle missing values</span></nav>
 <header class="examples-hero example-detail-hero"><div><p class="eyebrow">32 / Basics</p><h1>Handle missing values</h1><p>Look up users and handle both Some and None.</p></div><div class="example-hero-meta"><span class="example-badge">Executed offline</span><a href="/examples/#category-Basics">More in Basics ↗</a></div></header>
 <div class="example-workbench">
 <section class="example-source" aria-labelledby="source-title"><header class="example-file-bar"><h2 id="source-title">optional-values.kujo</h2><a href="/samples/optional-values.kujo" download>Download ↓</a></header><div class="sample-code"><pre tabindex="0"><code><span class="syntax-token syntax-keyword">func</span> find_user_by_id(id) {
    <span class="syntax-token syntax-keyword">if</span> id == <span class="syntax-token syntax-number">1</span> {
        <span class="syntax-token syntax-keyword">return</span> Some(<span class="syntax-token syntax-string">&quot;Alice&quot;</span>)
    }
    <span class="syntax-token syntax-keyword">if</span> id == <span class="syntax-token syntax-number">2</span> {
        <span class="syntax-token syntax-keyword">return</span> Some(<span class="syntax-token syntax-string">&quot;Bob&quot;</span>)
    }
    <span class="syntax-token syntax-keyword">if</span> id == <span class="syntax-token syntax-number">3</span> {
        <span class="syntax-token syntax-keyword">return</span> Some(<span class="syntax-token syntax-string">&quot;Charlie&quot;</span>)
    }
    <span class="syntax-token syntax-keyword">return</span> None
}

<span class="syntax-token syntax-keyword">let</span> users := [<span class="syntax-token syntax-number">1</span>, <span class="syntax-token syntax-number">2</span>, <span class="syntax-token syntax-number">99</span>, <span class="syntax-token syntax-number">3</span>]
<span class="syntax-token syntax-keyword">for</span> user_id <span class="syntax-token syntax-keyword">in</span> users {
    <span class="syntax-token syntax-keyword">let</span> user := find_user_by_id(user_id)
    <span class="syntax-token syntax-keyword">match</span> user {
        <span class="syntax-token syntax-keyword">case</span> Some(name): {
            print(<span class="syntax-token syntax-string">&quot;User &quot;</span> + to_string(user_id) + <span class="syntax-token syntax-string">&quot;: &quot;</span> + name)
        }
        <span class="syntax-token syntax-keyword">case</span> None: {
            print(<span class="syntax-token syntax-string">&quot;User &quot;</span> + to_string(user_id) + <span class="syntax-token syntax-string">&quot;: Not found&quot;</span>)
        }
    }
}
</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></section>
 <aside class="example-runbook" aria-labelledby="run-title"><p class="eyebrow">Run it locally</p><h2 id="run-title">Try this example.</h2><ol><li><strong>Set up Kujo</strong><p><a href="/language/">Install the runtime</a> before running the command below.</p></li><li><strong>Save the sample</strong><p>Download <a href="/samples/optional-values.kujo" download>optional-values.kujo</a> or copy the code into a file with that name.</p></li><li><strong>Run the command</strong><div class="sample-code"><pre tabindex="0"><code>kujo run optional-values.kujo</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></li></ol><a class="example-bundle-link" href="/samples/kujo-examples.tar.gz">Download all samples + fixtures ↓</a></aside>
 </div>
 <section class="example-result" aria-labelledby="result-title"><header><p class="eyebrow">Check the result</p><h2 id="result-title">Expected output</h2><p>Your terminal should show this output.</p></header><div><div class="sample-code"><pre tabindex="0"><code>User 1: Alice
User 2: Bob
User 99: Not found
User 3: Charlie
</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></div></section>
 <details class="example-provenance"><summary>Source &amp; verification details</summary><div><p>Verified against <a href="https://github.com/kujolang/kujo/tree/2cfaf185ad03059c89ef4f72fb061074255d00fc">Kujo 1.9.0</a>. Executed offline.</p><p><a href="https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/result_option_demo.kujo#L88-L112">Pinned source</a> · <a href="https://docs.kujolang.ai/learn/">Language documentation</a></p><p class="example-checksum">SHA-256 <code>a5ace8392985f05f75ad05ad82bf7b1a9d059204960c3267325ba2962a25ae8c</code></p></div></details>
 <nav class="example-pagination" aria-label="Related examples"><a href="/examples/nested-dictionaries/"><span>← Previous example</span><strong>Nested dictionaries</strong></a><a href="/examples/partial-application/"><span>Next example →</span><strong>Capture function arguments</strong></a></nav>
