---
title: AI capability restrictions
template: language-examples-capabilities
custom_url: examples/capabilities
description: "Use replay with the AI egress example; pair it with the documented capability policy."
seo_title: "AI capability restrictions | Kujo"
social_image: /assets/images/social/examples-capabilities.jpg
---

<nav aria-label="Breadcrumb"><a href="/">Home</a> / <a href="/examples/">Examples</a> / AI capability restrictions</nav>
<article class="example-panel" id="example-capabilities" data-example="capabilities" data-category="AI runtime"><p class="eyebrow">AI runtime · Executed offline · Kujo 1.9.0</p><h3>AI capability restrictions</h3><p>Use replay with the AI egress example; pair it with the documented capability policy.</p><p class="example-note">Run from the samples bundle directory with --untrusted --allow-ai. Without --allow-ai this call is denied. Replay uses bundled fixtures; this is not a claim of process isolation.</p><div class="sample-code"><pre tabindex="0"><code><span class="syntax-token">func</span> kv(label, value) {
    print(label + <span class="syntax-token">&quot;: &quot;</span> + value)
}

<span class="syntax-token">let</span> options := {
    <span class="syntax-token">&quot;endpoint&quot;</span>: <span class="syntax-token">&quot;http://127.0.0.1:1/v1/chat/completions&quot;</span>,
    <span class="syntax-token">&quot;model&quot;</span>: <span class="syntax-token">&quot;gpt-replay&quot;</span>,
    <span class="syntax-token">&quot;structured_errors&quot;</span>: true,
    <span class="syntax-token">&quot;cassette&quot;</span>: {
        <span class="syntax-token">&quot;mode&quot;</span>: <span class="syntax-token">&quot;replay&quot;</span>,
        <span class="syntax-token">&quot;dir&quot;</span>: <span class="syntax-token">&quot;tests/fixtures/ai_cassettes&quot;</span>
    }
}

<span class="syntax-token">let</span> result := ai_chat(<span class="syntax-token">&quot;Hello model&quot;</span>, options)

kv(<span class="syntax-token">&quot;allowlisted_replay&quot;</span>, to_string(result))
</code></pre><button type="button" class="sk-button" data-copy-code hidden>Copy code</button><span role="status" data-code-status></span></div><p>Save as <a href="/samples/capabilities.kujo" download>capabilities.kujo</a>, then:</p><div class="sample-code"><pre tabindex="0"><code>kujo run --untrusted --allow-ai capabilities.kujo</code></pre><button type="button" class="sk-button" data-copy-code hidden>Copy code</button><span role="status" data-code-status></span></div><details><summary>Expected output</summary><pre>allowlisted_replay: Ok({&quot;finish_reason&quot;: tool_calls, &quot;headers&quot;: {&quot;content-type&quot;: application/json}, &quot;json&quot;: {&quot;choices&quot;: [{&quot;finish_reason&quot;: tool_calls, &quot;message&quot;: {&quot;content&quot;: hello from cassette, &quot;tool_calls&quot;: [{&quot;function&quot;: {&quot;arguments&quot;: {&quot;query&quot;:&quot;kujo&quot;}, &quot;name&quot;: lookup}, &quot;id&quot;: call_1}]}}], &quot;usage&quot;: {&quot;completion_tokens&quot;: 5, &quot;prompt_tokens&quot;: 7, &quot;total_tokens&quot;: 12}}, &quot;message&quot;: hello from cassette, &quot;model&quot;: gpt-replay, &quot;provider&quot;: , &quot;status&quot;: 200, &quot;text&quot;: {&quot;choices&quot;:[{&quot;finish_reason&quot;:&quot;tool_calls&quot;,&quot;message&quot;:{&quot;content&quot;:&quot;hello from cassette&quot;,&quot;tool_calls&quot;:[{&quot;id&quot;:&quot;call_1&quot;,&quot;function&quot;:{&quot;name&quot;:&quot;lookup&quot;,&quot;arguments&quot;:&quot;{\&quot;query\&quot;:\&quot;kujo\&quot;}&quot;}}]}}],&quot;usage&quot;:{&quot;prompt_tokens&quot;:7,&quot;completion_tokens&quot;:5,&quot;total_tokens&quot;:12}}, &quot;tool_calls&quot;: [{&quot;arguments_json&quot;: {&quot;query&quot;:&quot;kujo&quot;}, &quot;id&quot;: call_1, &quot;name&quot;: lookup}], &quot;usage&quot;: {&quot;completion_tokens&quot;: 5, &quot;prompt_tokens&quot;: 7, &quot;total_tokens&quot;: 12}})
</pre></details><p><a href="https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/ai_egress_allowlist.kujo">Pinned source</a> · <a href="https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/docs/AI_RUNTIME.md#egress-controls">Language documentation</a></p></article>
<nav aria-label="Related examples"><a href="/examples/streaming/">Previous: AI streaming</a> · <a href="/examples/tests/">Next: Tests</a></nav>
