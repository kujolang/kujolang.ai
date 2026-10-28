---
title: Fit a token budget
template: language-examples-token-budget
custom_url: examples/token-budget
description: "Estimate token counts and trim a conversation to fit a budget."
seo_title: "Fit a token budget | Kujo"
social_image: /assets/images/social/examples-token-budget.jpg
---

<script type="application/ld+json">{"@context":"https://schema.org","@type":"SoftwareSourceCode","@id":"https://kujolang.ai/examples/token-budget/#source","name":"Fit a token budget","description":"Estimate token counts and trim a conversation to fit a budget.","codeRepository":"https://github.com/kujolang/kujo","programmingLanguage":"Kujo","codeSampleType":"code snippet","url":"https://kujolang.ai/examples/token-budget/","text":"func kv(label, value) {\n    print(label + \": \" + to_string(value))\n}\n\nlet messages := [\n    {\n        \"role\": \"system\",\n        \"content\": \"Answer briefly and cite constraints.\"\n    },\n    {\n        \"role\": \"user\",\n        \"content\": \"Summarize the previous research notes and all implementation details.\"\n    },\n    {\n        \"role\": \"assistant\",\n        \"content\": \"The previous answer was intentionally long and should be dropped first.\"\n    },\n    {\n        \"role\": \"user\",\n        \"content\": \"Give me the short version.\"\n    }\n]\n\nlet options := {\n    \"model\": \"gpt-4o\"\n}\n\nlet text_tokens := ai_count_tokens(\"Kujo estimates tokens deterministically.\", options)\nlet message_tokens := ai_count_tokens(messages, options)\nlet fitted := ai_fit_context(messages, 28, options)\n\nkv(\"text_tokens\", text_tokens)\nkv(\"message_tokens\", message_tokens)\nkv(\"dropped\", fitted[\"dropped\"])\nkv(\"est_tokens\", fitted[\"est_tokens\"])\nkv(\"fits\", fitted[\"fits\"])\nkv(\"messages\", fitted[\"messages\"])\n","isBasedOn":"https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/ai_token_budget.kujo"}</script>
 <nav class="examples-breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a><span aria-hidden="true">/</span><a href="/examples/">Examples</a><span aria-hidden="true">/</span><span aria-current="page">Fit a token budget</span></nav>
 <header class="examples-hero example-detail-hero"><div><p class="eyebrow">50 / AI runtime</p><h1>Fit a token budget</h1><p>Estimate token counts and trim a conversation to fit a budget.</p></div><div class="example-hero-meta"><span class="example-badge">Executed offline</span><a href="/examples/#category-AI-runtime">More in AI runtime ↗</a></div></header>
 <div class="example-workbench">
 <section class="example-source" aria-labelledby="source-title"><header class="example-file-bar"><h2 id="source-title">token-budget.kujo</h2><a href="/samples/token-budget.kujo" download>Download ↓</a></header><div class="sample-code"><pre tabindex="0"><code><span class="syntax-token syntax-keyword">func</span> kv(label, value) {
    print(label + <span class="syntax-token syntax-string">&quot;: &quot;</span> + to_string(value))
}

<span class="syntax-token syntax-keyword">let</span> messages := [
    {
        <span class="syntax-token syntax-string">&quot;role&quot;</span>: <span class="syntax-token syntax-string">&quot;system&quot;</span>,
        <span class="syntax-token syntax-string">&quot;content&quot;</span>: <span class="syntax-token syntax-string">&quot;Answer briefly and cite constraints.&quot;</span>
    },
    {
        <span class="syntax-token syntax-string">&quot;role&quot;</span>: <span class="syntax-token syntax-string">&quot;user&quot;</span>,
        <span class="syntax-token syntax-string">&quot;content&quot;</span>: <span class="syntax-token syntax-string">&quot;Summarize the previous research notes and all implementation details.&quot;</span>
    },
    {
        <span class="syntax-token syntax-string">&quot;role&quot;</span>: <span class="syntax-token syntax-string">&quot;assistant&quot;</span>,
        <span class="syntax-token syntax-string">&quot;content&quot;</span>: <span class="syntax-token syntax-string">&quot;The previous answer was intentionally long and should be dropped first.&quot;</span>
    },
    {
        <span class="syntax-token syntax-string">&quot;role&quot;</span>: <span class="syntax-token syntax-string">&quot;user&quot;</span>,
        <span class="syntax-token syntax-string">&quot;content&quot;</span>: <span class="syntax-token syntax-string">&quot;Give me the short version.&quot;</span>
    }
]

<span class="syntax-token syntax-keyword">let</span> options := {
    <span class="syntax-token syntax-string">&quot;model&quot;</span>: <span class="syntax-token syntax-string">&quot;gpt-4o&quot;</span>
}

<span class="syntax-token syntax-keyword">let</span> text_tokens := ai_count_tokens(<span class="syntax-token syntax-string">&quot;Kujo estimates tokens deterministically.&quot;</span>, options)
<span class="syntax-token syntax-keyword">let</span> message_tokens := ai_count_tokens(messages, options)
<span class="syntax-token syntax-keyword">let</span> fitted := ai_fit_context(messages, <span class="syntax-token syntax-number">28</span>, options)

kv(<span class="syntax-token syntax-string">&quot;text_tokens&quot;</span>, text_tokens)
kv(<span class="syntax-token syntax-string">&quot;message_tokens&quot;</span>, message_tokens)
kv(<span class="syntax-token syntax-string">&quot;dropped&quot;</span>, fitted[<span class="syntax-token syntax-string">&quot;dropped&quot;</span>])
kv(<span class="syntax-token syntax-string">&quot;est_tokens&quot;</span>, fitted[<span class="syntax-token syntax-string">&quot;est_tokens&quot;</span>])
kv(<span class="syntax-token syntax-string">&quot;fits&quot;</span>, fitted[<span class="syntax-token syntax-string">&quot;fits&quot;</span>])
kv(<span class="syntax-token syntax-string">&quot;messages&quot;</span>, fitted[<span class="syntax-token syntax-string">&quot;messages&quot;</span>])
</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></section>
 <aside class="example-runbook" aria-labelledby="run-title"><p class="eyebrow">Run it locally</p><h2 id="run-title">Try this example.</h2><ol><li><strong>Set up Kujo</strong><p><a href="/language/">Install the runtime</a> before running the command below.</p></li><li><strong>Save the sample</strong><p>Download <a href="/samples/token-budget.kujo" download>token-budget.kujo</a> or copy the code into a file with that name.</p></li><li><strong>Run the command</strong><div class="sample-code"><pre tabindex="0"><code>kujo run token-budget.kujo</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></li></ol><div class="example-note"><strong>Before you run</strong><p>Token counts are local estimates, not provider billing records.</p></div><a class="example-bundle-link" href="/samples/kujo-examples.tar.gz">Download all samples + fixtures ↓</a></aside>
 </div>
 <section class="example-result" aria-labelledby="result-title"><header><p class="eyebrow">Check the result</p><h2 id="result-title">Expected output</h2><p>Your terminal should show this output.</p></header><div><div class="sample-code"><pre tabindex="0"><code>text_tokens: 10
message_tokens: 75
dropped: 2
est_tokens: 27
fits: true
messages: [{&quot;content&quot;: Answer briefly and cite constraints., &quot;role&quot;: system}, {&quot;content&quot;: Give me the short version., &quot;role&quot;: user}]
</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></div></section>
 <details class="example-provenance"><summary>Source &amp; verification details</summary><div><p>Verified against <a href="https://github.com/kujolang/kujo/tree/2cfaf185ad03059c89ef4f72fb061074255d00fc">Kujo 1.9.0</a>. Executed offline.</p><p><a href="https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/ai_token_budget.kujo">Pinned source</a> · <a href="https://docs.kujolang.ai/learn/">Language documentation</a></p><p class="example-checksum">SHA-256 <code>52e80c56ee87218923995593eeb1c41d59b8c0cffe297283d16cf6cb7d615ac9</code></p></div></details>
 <nav class="example-pagination" aria-label="Related examples"><a href="/examples/response-envelope/"><span>← Previous example</span><strong>Inspect AI responses</strong></a><a href="/examples/hello-world/"><span>Next example →</span><strong>Hello World</strong></a></nav>
