---
title: Enums and pattern matching
template: language-examples-pattern-matching
custom_url: examples/pattern-matching
description: "Handle tagged values and Result variants explicitly."
seo_title: "Enums and pattern matching | Kujo"
social_image: /assets/images/social/examples-pattern-matching.jpg
---

<nav aria-label="Breadcrumb"><a href="/">Home</a> / <a href="/examples/">Examples</a> / Enums and pattern matching</nav>
<article class="example-panel" id="example-pattern-matching" data-example="pattern-matching" data-category="Data"><p class="eyebrow">Data · Executed offline · Kujo 1.9.0</p><h3>Enums and pattern matching</h3><p>Handle tagged values and Result variants explicitly.</p><div class="sample-code"><pre tabindex="0"><code><span class="syntax-token"># Pattern matching examples using current Kujo match syntax.</span>

<span class="syntax-token">enum</span> Status {
    Success,
    Failure
}

<span class="syntax-token">func</span> status_for(code) {
    <span class="syntax-token">if</span> code == 200 {
        <span class="syntax-token">return</span> Status::Success(<span class="syntax-token">&quot;ok&quot;</span>)
    }
    <span class="syntax-token">return</span> Status::Failure(<span class="syntax-token">&quot;not ok&quot;</span>)
}

<span class="syntax-token">let</span> result := status_for(200)

<span class="syntax-token">match</span> result {
    <span class="syntax-token">case</span> Status::Success(message): {
        print(<span class="syntax-token">&quot;success: &quot;</span> + message)
    }
    <span class="syntax-token">case</span> Status::Failure(error): {
        print(<span class="syntax-token">&quot;failure: &quot;</span> + error)
    }
}

<span class="syntax-token">let</span> maybe_value := Ok(42)

<span class="syntax-token">match</span> maybe_value {
    <span class="syntax-token">case</span> Ok(value): {
        print(<span class="syntax-token">&quot;value: &quot;</span> + to_string(value))
    }
    <span class="syntax-token">case</span> Err(message): {
        print(<span class="syntax-token">&quot;error: &quot;</span> + message)
    }
}
</code></pre><button type="button" class="sk-button" data-copy-code hidden>Copy code</button><span role="status" data-code-status></span></div><p>Save as <a href="/samples/pattern-matching.kujo" download>pattern-matching.kujo</a>, then:</p><div class="sample-code"><pre tabindex="0"><code>kujo run pattern-matching.kujo</code></pre><button type="button" class="sk-button" data-copy-code hidden>Copy code</button><span role="status" data-code-status></span></div><details><summary>Expected output</summary><pre>value: 42
</pre></details><p><a href="https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/pattern_matching.kujo">Pinned source</a> · <a href="https://docs.kujolang.ai/learn/">Language documentation</a></p></article>
<nav aria-label="Related examples"><a href="/examples/structs/">Previous: Structs and methods</a> · <a href="/examples/errors/">Next: Error handling</a></nav>
