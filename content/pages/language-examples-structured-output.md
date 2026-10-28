---
title: Structured output validation
template: language-examples-structured-output
custom_url: examples/structured-output
description: "Check local data against a schema without calling a model."
seo_title: "Structured output validation | Kujo"
social_image: /assets/images/social/examples-structured-output.jpg
---

<script type="application/ld+json">{"@context":"https://schema.org","@type":"SoftwareSourceCode","@id":"https://kujolang.ai/examples/structured-output/#source","name":"Structured output validation","description":"Check local data against a schema without calling a model.","codeRepository":"https://github.com/kujolang/kujo","programmingLanguage":"Kujo","codeSampleType":"code snippet","url":"https://kujolang.ai/examples/structured-output/","text":"func kv(label, value) {\n    print(label + \": \" + to_string(value))\n}\n\nlet schema := {\n    \"type\": \"object\",\n    \"required\": [\"name\", \"scores\"],\n    \"properties\": {\n        \"name\": {\n            \"type\": \"string\",\n            \"minLength\": 2\n        },\n        \"scores\": {\n            \"type\": \"array\",\n            \"minItems\": 1,\n            \"items\": {\n                \"type\": \"number\",\n                \"minimum\": 0,\n                \"maximum\": 100\n            }\n        }\n    },\n    \"additionalProperties\": false\n}\n\nlet valid_report := json_schema_validate({\n    \"name\": \"Kujo\",\n    \"scores\": [95, 88]\n}, schema)\n\nlet invalid_report := json_schema_validate({\n    \"name\": \"K\",\n    \"scores\": [101],\n    \"debug\": true\n}, schema)\n\nkv(\"valid\", valid_report[\"valid\"])\nkv(\"invalid\", invalid_report[\"valid\"])\nkv(\"errors\", invalid_report[\"errors\"])\n","isBasedOn":"https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/json_schema_validate.kujo"}</script>
 <nav class="examples-breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a><span aria-hidden="true">/</span><a href="/examples/">Examples</a><span aria-hidden="true">/</span><span aria-current="page">Structured output validation</span></nav>
 <header class="examples-hero example-detail-hero"><div><p class="eyebrow">13 / AI runtime</p><h1>Structured output validation</h1><p>Check local data against a schema without calling a model.</p></div><div class="example-hero-meta"><span class="example-badge">Executed offline</span><a href="/examples/#category-AI-runtime">More in AI runtime ↗</a></div></header>
 <div class="example-workbench">
 <section class="example-source" aria-labelledby="source-title"><header class="example-file-bar"><h2 id="source-title">structured-output.kujo</h2><a href="/samples/structured-output.kujo" download>Download ↓</a></header><div class="sample-code"><pre tabindex="0"><code><span class="syntax-token syntax-keyword">func</span> kv(label, value) {
    print(label + <span class="syntax-token syntax-string">&quot;: &quot;</span> + to_string(value))
}

<span class="syntax-token syntax-keyword">let</span> schema := {
    <span class="syntax-token syntax-string">&quot;type&quot;</span>: <span class="syntax-token syntax-string">&quot;object&quot;</span>,
    <span class="syntax-token syntax-string">&quot;required&quot;</span>: [<span class="syntax-token syntax-string">&quot;name&quot;</span>, <span class="syntax-token syntax-string">&quot;scores&quot;</span>],
    <span class="syntax-token syntax-string">&quot;properties&quot;</span>: {
        <span class="syntax-token syntax-string">&quot;name&quot;</span>: {
            <span class="syntax-token syntax-string">&quot;type&quot;</span>: <span class="syntax-token syntax-string">&quot;string&quot;</span>,
            <span class="syntax-token syntax-string">&quot;minLength&quot;</span>: <span class="syntax-token syntax-number">2</span>
        },
        <span class="syntax-token syntax-string">&quot;scores&quot;</span>: {
            <span class="syntax-token syntax-string">&quot;type&quot;</span>: <span class="syntax-token syntax-string">&quot;array&quot;</span>,
            <span class="syntax-token syntax-string">&quot;minItems&quot;</span>: <span class="syntax-token syntax-number">1</span>,
            <span class="syntax-token syntax-string">&quot;items&quot;</span>: {
                <span class="syntax-token syntax-string">&quot;type&quot;</span>: <span class="syntax-token syntax-string">&quot;number&quot;</span>,
                <span class="syntax-token syntax-string">&quot;minimum&quot;</span>: <span class="syntax-token syntax-number">0</span>,
                <span class="syntax-token syntax-string">&quot;maximum&quot;</span>: <span class="syntax-token syntax-number">100</span>
            }
        }
    },
    <span class="syntax-token syntax-string">&quot;additionalProperties&quot;</span>: <span class="syntax-token syntax-literal">false</span>
}

<span class="syntax-token syntax-keyword">let</span> valid_report := json_schema_validate({
    <span class="syntax-token syntax-string">&quot;name&quot;</span>: <span class="syntax-token syntax-string">&quot;Kujo&quot;</span>,
    <span class="syntax-token syntax-string">&quot;scores&quot;</span>: [<span class="syntax-token syntax-number">95</span>, <span class="syntax-token syntax-number">88</span>]
}, schema)

<span class="syntax-token syntax-keyword">let</span> invalid_report := json_schema_validate({
    <span class="syntax-token syntax-string">&quot;name&quot;</span>: <span class="syntax-token syntax-string">&quot;K&quot;</span>,
    <span class="syntax-token syntax-string">&quot;scores&quot;</span>: [<span class="syntax-token syntax-number">101</span>],
    <span class="syntax-token syntax-string">&quot;debug&quot;</span>: <span class="syntax-token syntax-literal">true</span>
}, schema)

kv(<span class="syntax-token syntax-string">&quot;valid&quot;</span>, valid_report[<span class="syntax-token syntax-string">&quot;valid&quot;</span>])
kv(<span class="syntax-token syntax-string">&quot;invalid&quot;</span>, invalid_report[<span class="syntax-token syntax-string">&quot;valid&quot;</span>])
kv(<span class="syntax-token syntax-string">&quot;errors&quot;</span>, invalid_report[<span class="syntax-token syntax-string">&quot;errors&quot;</span>])
</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></section>
 <aside class="example-runbook" aria-labelledby="run-title"><p class="eyebrow">Run it locally</p><h2 id="run-title">Try this example.</h2><ol><li><strong>Set up Kujo</strong><p><a href="/language/">Install the runtime</a> before running the command below.</p></li><li><strong>Save the sample</strong><p>Download <a href="/samples/structured-output.kujo" download>structured-output.kujo</a> or copy the code into a file with that name.</p></li><li><strong>Run the command</strong><div class="sample-code"><pre tabindex="0"><code>kujo run structured-output.kujo</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></li></ol><a class="example-bundle-link" href="/samples/kujo-examples.tar.gz">Download all samples + fixtures ↓</a></aside>
 </div>
 <section class="example-result" aria-labelledby="result-title"><header><p class="eyebrow">Check the result</p><h2 id="result-title">Expected output</h2><p>Your terminal should show this output.</p></header><div><div class="sample-code"><pre tabindex="0"><code>valid: true
invalid: false
errors: [{&quot;keyword&quot;: minLength, &quot;message&quot;: string length is less than 2, &quot;path&quot;: /name}, {&quot;keyword&quot;: maximum, &quot;message&quot;: number is greater than 100, &quot;path&quot;: /scores/0}, {&quot;keyword&quot;: additionalProperties, &quot;message&quot;: additional property 'debug' is not allowed, &quot;path&quot;: /debug}]
</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></div></section>
 <details class="example-provenance"><summary>Source &amp; verification details</summary><div><p>Verified against <a href="https://github.com/kujolang/kujo/tree/2cfaf185ad03059c89ef4f72fb061074255d00fc">Kujo 1.9.0</a>. Executed offline.</p><p><a href="https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/json_schema_validate.kujo">Pinned source</a> · <a href="https://docs.kujolang.ai/learn/">Language documentation</a></p><p class="example-checksum">SHA-256 <code>62b79648298d6f166b49eae8ec4a5484cc9da33f5b52e92c6ec569eed97db3e9</code></p></div></details>
 <nav class="example-pagination" aria-label="Related examples"><a href="/examples/json/"><span>← Previous example</span><strong>JSON data</strong></a><a href="/examples/request-hash/"><span>Next example →</span><strong>Deterministic AI request IDs</strong></a></nav>
