---
title: Redact secret values
template: language-examples-secret-redaction
custom_url: examples/secret-redaction
description: "Check how secret values appear in printed text and JSON."
seo_title: "Redact secret values | Kujo"
social_image: /assets/images/social/examples-secret-redaction.jpg
---

<script type="application/ld+json">{"@context":"https://schema.org","@type":"SoftwareSourceCode","@id":"https://kujolang.ai/examples/secret-redaction/#source","name":"Redact secret values","description":"Check how secret values appear in printed text and JSON.","codeRepository":"https://github.com/kujolang/kujo","programmingLanguage":"Kujo","codeSampleType":"code snippet","url":"https://kujolang.ai/examples/secret-redaction/","text":"# Secret values redact automatically at output boundaries.\n\napi_key := secret(\"sk-local-demo\")\n\nprint(api_key)\nprint(to_json({\"api_key\": api_key, \"label\": \"demo\"}))\nprint(type(api_key))\nprint(is_secret(api_key))\nprint(reveal(api_key) == \"sk-local-demo\")\n","isBasedOn":"https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/secrets_redaction.kujo"}</script>
 <nav class="examples-breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a><span aria-hidden="true">/</span><a href="/examples/">Examples</a><span aria-hidden="true">/</span><span aria-current="page">Redact secret values</span></nav>
 <header class="examples-hero example-detail-hero"><div><p class="eyebrow">46 / Systems</p><h1>Redact secret values</h1><p>Check how secret values appear in printed text and JSON.</p></div><div class="example-hero-meta"><span class="example-badge">Executed offline</span><a href="/examples/#category-Systems">More in Systems ↗</a></div></header>
 <div class="example-workbench">
 <section class="example-source" aria-labelledby="source-title"><header class="example-file-bar"><h2 id="source-title">secret-redaction.kujo</h2><a href="/samples/secret-redaction.kujo" download>Download ↓</a></header><div class="sample-code"><pre tabindex="0"><code><span class="syntax-token syntax-comment"># Secret values redact automatically at output boundaries.</span>

api_key := secret(<span class="syntax-token syntax-string">&quot;sk-local-demo&quot;</span>)

print(api_key)
print(to_json({<span class="syntax-token syntax-string">&quot;api_key&quot;</span>: api_key, <span class="syntax-token syntax-string">&quot;label&quot;</span>: <span class="syntax-token syntax-string">&quot;demo&quot;</span>}))
print(type(api_key))
print(is_secret(api_key))
print(reveal(api_key) == <span class="syntax-token syntax-string">&quot;sk-local-demo&quot;</span>)
</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></section>
 <aside class="example-runbook" aria-labelledby="run-title"><p class="eyebrow">Run it locally</p><h2 id="run-title">Try this example.</h2><ol><li><strong>Set up Kujo</strong><p><a href="/language/">Install the runtime</a> before running the command below.</p></li><li><strong>Save the sample</strong><p>Download <a href="/samples/secret-redaction.kujo" download>secret-redaction.kujo</a> or copy the code into a file with that name.</p></li><li><strong>Run the command</strong><div class="sample-code"><pre tabindex="0"><code>kujo run secret-redaction.kujo</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></li></ol><div class="example-note"><strong>Before you run</strong><p>The credentials in this sample are dummy values.</p></div><a class="example-bundle-link" href="/samples/kujo-examples.tar.gz">Download all samples + fixtures ↓</a></aside>
 </div>
 <section class="example-result" aria-labelledby="result-title"><header><p class="eyebrow">Check the result</p><h2 id="result-title">Expected output</h2><p>Your terminal should show this output.</p></header><div><div class="sample-code"><pre tabindex="0"><code>***
{&quot;api_key&quot;:&quot;***&quot;,&quot;label&quot;:&quot;demo&quot;}
secret
true
true
</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></div></section>
 <details class="example-provenance"><summary>Source &amp; verification details</summary><div><p>Verified against <a href="https://github.com/kujolang/kujo/tree/2cfaf185ad03059c89ef4f72fb061074255d00fc">Kujo 1.9.0</a>. Executed offline.</p><p><a href="https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/secrets_redaction.kujo">Pinned source</a> · <a href="https://docs.kujolang.ai/learn/">Language documentation</a></p><p class="example-checksum">SHA-256 <code>2bca47c7a5c55abebaabdd9489598f3831896c6247bcba75fc5ae0b8b313b33f</code></p></div></details>
 <nav class="example-pagination" aria-label="Related examples"><a href="/examples/log-timestamps/"><span>← Previous example</span><strong>Extract log timestamps</strong></a><a href="/examples/password-verification/"><span>Next example →</span><strong>Verify a password</strong></a></nav>
