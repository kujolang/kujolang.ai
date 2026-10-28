---
title: AI streaming
template: language-examples-streaming
custom_url: examples/streaming
description: "Read a recorded response through a streaming callback."
seo_title: "AI streaming | Kujo"
social_image: /assets/images/social/examples-streaming.jpg
---


 <nav class="examples-breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a><span aria-hidden="true">/</span><a href="/examples/">Examples</a><span aria-hidden="true">/</span><span aria-current="page">AI streaming</span></nav>
 <header class="examples-hero example-detail-hero"><div><p class="eyebrow">16 / AI runtime</p><h1>AI streaming</h1><p>Read a recorded response through a streaming callback.</p></div><div class="example-hero-meta"><span class="example-badge">Executed offline</span><a href="/examples/#category-AI-runtime">More in AI runtime ↗</a></div></header>
 <div class="example-workbench">
 <section class="example-source" aria-labelledby="source-title"><header class="example-file-bar"><h2 id="source-title">streaming.kujo</h2><a href="/samples/streaming.kujo" download>Download ↓</a></header><div class="sample-code"><pre tabindex="0"><code><span class="syntax-token syntax-keyword">func</span> kv(label, value) {
    print(label + <span class="syntax-token syntax-string">&quot;: &quot;</span> + to_string(value))
}

<span class="syntax-token syntax-keyword">func</span> on_chunk(delta, raw_chunk) {
    kv(<span class="syntax-token syntax-string">&quot;delta&quot;</span>, delta)
    kv(<span class="syntax-token syntax-string">&quot;raw&quot;</span>, raw_chunk)
    <span class="syntax-token syntax-keyword">return</span> <span class="syntax-token syntax-literal">true</span>
}

<span class="syntax-token syntax-keyword">let</span> replay_options := {
    <span class="syntax-token syntax-string">&quot;endpoint&quot;</span>: <span class="syntax-token syntax-string">&quot;http://127.0.0.1:1/v1/chat/completions&quot;</span>,
    <span class="syntax-token syntax-string">&quot;model&quot;</span>: <span class="syntax-token syntax-string">&quot;gpt-replay&quot;</span>,
    <span class="syntax-token syntax-string">&quot;provider&quot;</span>: <span class="syntax-token syntax-string">&quot;mock-provider&quot;</span>,
    <span class="syntax-token syntax-string">&quot;cassette&quot;</span>: {
        <span class="syntax-token syntax-string">&quot;mode&quot;</span>: <span class="syntax-token syntax-string">&quot;replay&quot;</span>,
        <span class="syntax-token syntax-string">&quot;dir&quot;</span>: <span class="syntax-token syntax-string">&quot;tests/fixtures/ai_cassettes&quot;</span>
    }
}

<span class="syntax-token syntax-keyword">let</span> result := ai_stream_chat(<span class="syntax-token syntax-string">&quot;Stream please&quot;</span>, replay_options, on_chunk)
kv(<span class="syntax-token syntax-string">&quot;stream_result&quot;</span>, result)
</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></section>
 <aside class="example-runbook" aria-labelledby="run-title"><p class="eyebrow">Run it locally</p><h2 id="run-title">Try this example.</h2><ol><li><strong>Set up Kujo</strong><p><a href="/language/">Install the runtime</a> before running the command below.</p></li><li><strong>Save the sample</strong><p>Download <a href="/samples/streaming.kujo" download>streaming.kujo</a> or copy the code into a file with that name.</p></li><li><strong>Run the command</strong><div class="sample-code"><pre tabindex="0"><code>kujo run streaming.kujo</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></li></ol><div class="example-note"><strong>Before you run</strong><p>Use the bundled fixtures for offline replay. Live calls require provider credentials and network access and may cost money.</p></div><a class="example-bundle-link" href="/samples/kujo-examples.tar.gz">Download all samples + fixtures ↓</a></aside>
 </div>
 <section class="example-result" aria-labelledby="result-title"><header><p class="eyebrow">Check the result</p><h2 id="result-title">Expected output</h2><p>Your terminal should show this output.</p></header><div><div class="sample-code"><pre tabindex="0"><code>delta: chunk one
raw: {&quot;choices&quot;: [{&quot;delta&quot;: {&quot;content&quot;: chunk one}}]}
delta: chunk two
raw: {&quot;choices&quot;: [{&quot;delta&quot;: {&quot;content&quot;: chunk two}, &quot;finish_reason&quot;: stop}], &quot;usage&quot;: {&quot;completion_tokens&quot;: 3, &quot;prompt_tokens&quot;: 3, &quot;total_tokens&quot;: 6}}
stream_result: Ok({&quot;chunks&quot;: [chunk one, chunk two], &quot;finish_reason&quot;: stop, &quot;headers&quot;: {&quot;content-type&quot;: application/json}, &quot;json&quot;: {&quot;choices&quot;: [{&quot;delta&quot;: {&quot;content&quot;: chunk one}}, {&quot;delta&quot;: {&quot;content&quot;: chunk two}, &quot;finish_reason&quot;: stop}], &quot;usage&quot;: {&quot;completion_tokens&quot;: 3, &quot;prompt_tokens&quot;: 3, &quot;total_tokens&quot;: 6}}, &quot;model&quot;: gpt-replay, &quot;provider&quot;: mock-provider, &quot;status&quot;: 200, &quot;text&quot;: {&quot;choices&quot;:[{&quot;delta&quot;:{&quot;content&quot;:&quot;chunk one&quot;}},{&quot;delta&quot;:{&quot;content&quot;:&quot;chunk two&quot;},&quot;finish_reason&quot;:&quot;stop&quot;}],&quot;usage&quot;:{&quot;prompt_tokens&quot;:3,&quot;completion_tokens&quot;:3,&quot;total_tokens&quot;:6}}, &quot;usage&quot;: {&quot;completion_tokens&quot;: 3, &quot;prompt_tokens&quot;: 3, &quot;total_tokens&quot;: 6}})
</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></div></section>
 <details class="example-provenance"><summary>Source &amp; verification details</summary><div><p>Verified against <a href="https://github.com/kujolang/kujo/tree/2cfaf185ad03059c89ef4f72fb061074255d00fc">Kujo 1.9.0</a>. Executed offline.</p><p><a href="https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/ai_stream_callback.kujo">Pinned source</a> · <a href="https://docs.kujolang.ai/learn/">Language documentation</a></p><p class="example-checksum">SHA-256 <code>6e366b595b6128640059b02d3838658f0a8f28920913c7049327e242fd3e88c3</code></p></div></details>
 <nav class="example-pagination" aria-label="Related examples"><a href="/examples/replay/"><span>← Previous example</span><strong>AI calls and replay</strong></a><a href="/examples/capabilities/"><span>Next example →</span><strong>AI capability restrictions</strong></a></nav>
