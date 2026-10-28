---
title: AI capability restrictions
template: language-examples-capabilities
custom_url: examples/capabilities
description: "Replay an AI call with explicit permissions."
seo_title: "AI capability restrictions | Kujo"
social_image: /assets/images/social/examples-capabilities.jpg
---


 <nav class="examples-breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a><span aria-hidden="true">/</span><a href="/examples/">Examples</a><span aria-hidden="true">/</span><span aria-current="page">AI capability restrictions</span></nav>
 <header class="examples-hero example-detail-hero"><div><p class="eyebrow">17 / AI runtime</p><h1>AI capability restrictions</h1><p>Replay an AI call with explicit permissions.</p></div><div class="example-hero-meta"><span class="example-badge">Executed offline</span><a href="/examples/#category-AI-runtime">More in AI runtime ↗</a></div></header>
 <div class="example-workbench">
 <section class="example-source" aria-labelledby="source-title"><header class="example-file-bar"><h2 id="source-title">capabilities.kujo</h2><a href="/samples/capabilities.kujo" download>Download ↓</a></header><div class="sample-code"><pre tabindex="0"><code><span class="syntax-token syntax-keyword">func</span> kv(label, value) {
    print(label + <span class="syntax-token syntax-string">&quot;: &quot;</span> + value)
}

<span class="syntax-token syntax-keyword">let</span> options := {
    <span class="syntax-token syntax-string">&quot;endpoint&quot;</span>: <span class="syntax-token syntax-string">&quot;http://127.0.0.1:1/v1/chat/completions&quot;</span>,
    <span class="syntax-token syntax-string">&quot;model&quot;</span>: <span class="syntax-token syntax-string">&quot;gpt-replay&quot;</span>,
    <span class="syntax-token syntax-string">&quot;structured_errors&quot;</span>: <span class="syntax-token syntax-literal">true</span>,
    <span class="syntax-token syntax-string">&quot;cassette&quot;</span>: {
        <span class="syntax-token syntax-string">&quot;mode&quot;</span>: <span class="syntax-token syntax-string">&quot;replay&quot;</span>,
        <span class="syntax-token syntax-string">&quot;dir&quot;</span>: <span class="syntax-token syntax-string">&quot;tests/fixtures/ai_cassettes&quot;</span>
    }
}

<span class="syntax-token syntax-keyword">let</span> result := ai_chat(<span class="syntax-token syntax-string">&quot;Hello model&quot;</span>, options)

kv(<span class="syntax-token syntax-string">&quot;allowlisted_replay&quot;</span>, to_string(result))
</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></section>
 <aside class="example-runbook" aria-labelledby="run-title"><p class="eyebrow">Run it locally</p><h2 id="run-title">Try this example.</h2><ol><li><strong>Set up Kujo</strong><p><a href="/language/">Install the runtime</a> before running the command below.</p></li><li><strong>Save the sample</strong><p>Download <a href="/samples/capabilities.kujo" download>capabilities.kujo</a> or copy the code into a file with that name.</p></li><li><strong>Run the command</strong><div class="sample-code"><pre tabindex="0"><code>kujo run --untrusted --allow-ai capabilities.kujo</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></li></ol><div class="example-note"><strong>Before you run</strong><p>Run from the samples bundle directory with --untrusted --allow-ai. Without --allow-ai, the call is denied. Replay uses bundled fixtures; it does not provide process isolation.</p></div><a class="example-bundle-link" href="/samples/kujo-examples.tar.gz">Download all samples + fixtures ↓</a></aside>
 </div>
 <section class="example-result" aria-labelledby="result-title"><header><p class="eyebrow">Check the result</p><h2 id="result-title">Expected output</h2><p>Your terminal should show this output.</p></header><div><div class="sample-code"><pre tabindex="0"><code>allowlisted_replay: Ok({&quot;finish_reason&quot;: tool_calls, &quot;headers&quot;: {&quot;content-type&quot;: application/json}, &quot;json&quot;: {&quot;choices&quot;: [{&quot;finish_reason&quot;: tool_calls, &quot;message&quot;: {&quot;content&quot;: hello from cassette, &quot;tool_calls&quot;: [{&quot;function&quot;: {&quot;arguments&quot;: {&quot;query&quot;:&quot;kujo&quot;}, &quot;name&quot;: lookup}, &quot;id&quot;: call_1}]}}], &quot;usage&quot;: {&quot;completion_tokens&quot;: 5, &quot;prompt_tokens&quot;: 7, &quot;total_tokens&quot;: 12}}, &quot;message&quot;: hello from cassette, &quot;model&quot;: gpt-replay, &quot;provider&quot;: , &quot;status&quot;: 200, &quot;text&quot;: {&quot;choices&quot;:[{&quot;finish_reason&quot;:&quot;tool_calls&quot;,&quot;message&quot;:{&quot;content&quot;:&quot;hello from cassette&quot;,&quot;tool_calls&quot;:[{&quot;id&quot;:&quot;call_1&quot;,&quot;function&quot;:{&quot;name&quot;:&quot;lookup&quot;,&quot;arguments&quot;:&quot;{\&quot;query\&quot;:\&quot;kujo\&quot;}&quot;}}]}}],&quot;usage&quot;:{&quot;prompt_tokens&quot;:7,&quot;completion_tokens&quot;:5,&quot;total_tokens&quot;:12}}, &quot;tool_calls&quot;: [{&quot;arguments_json&quot;: {&quot;query&quot;:&quot;kujo&quot;}, &quot;id&quot;: call_1, &quot;name&quot;: lookup}], &quot;usage&quot;: {&quot;completion_tokens&quot;: 5, &quot;prompt_tokens&quot;: 7, &quot;total_tokens&quot;: 12}})
</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></div></section>
 <details class="example-provenance"><summary>Source &amp; verification details</summary><div><p>Verified against <a href="https://github.com/kujolang/kujo/tree/2cfaf185ad03059c89ef4f72fb061074255d00fc">Kujo 1.9.0</a>. Executed offline.</p><p><a href="https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/ai_egress_allowlist.kujo">Pinned source</a> · <a href="https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/docs/AI_RUNTIME.md#egress-controls">Language documentation</a></p><p class="example-checksum">SHA-256 <code>92100f287fe31daa2074f75526514551ee6b0920ac3313883bb6c994d8729d16</code></p></div></details>
 <nav class="example-pagination" aria-label="Related examples"><a href="/examples/streaming/"><span>← Previous example</span><strong>AI streaming</strong></a><a href="/examples/tests/"><span>Next example →</span><strong>Tests</strong></a></nav>
