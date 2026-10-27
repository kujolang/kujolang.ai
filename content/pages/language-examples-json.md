---
title: JSON data
template: language-examples-json
custom_url: examples/json
description: "Parse configuration and access nested fields."
seo_title: "JSON data | Kujo"
social_image: /assets/images/social/examples-json.jpg
---

<nav aria-label="Breadcrumb"><a href="/">Home</a> / <a href="/examples/">Examples</a> / JSON data</nav>
<article class="example-panel" id="example-json" data-example="json" data-category="Data"><p class="eyebrow">Data · Executed offline · Kujo 1.9.0</p><h3>JSON data</h3><p>Parse configuration and access nested fields.</p><div class="sample-code"><pre tabindex="0"><code><span class="syntax-token"># JSON Support Demo</span>
<span class="syntax-token"># Demonstrates parse_json() and to_json() functions</span>

print(<span class="syntax-token">&quot;=== Kujo JSON Support Demo ===&quot;</span>)
print(<span class="syntax-token">&quot;&quot;</span>)

<span class="syntax-token"># Example 1: Parse a configuration file</span>
print(<span class="syntax-token">&quot;1. Parsing Configuration&quot;</span>)
config_json := <span class="syntax-token">&quot;{\&quot;app_name\&quot;: \&quot;My App\&quot;, \&quot;version\&quot;: \&quot;1.0.0\&quot;, \&quot;settings\&quot;: {\&quot;debug\&quot;: true, \&quot;port\&quot;: 8080}}&quot;</span>
config := parse_json(config_json)
print(<span class="syntax-token">&quot;App name:&quot;</span>, config[<span class="syntax-token">&quot;app_name&quot;</span>])
print(<span class="syntax-token">&quot;Version:&quot;</span>, config[<span class="syntax-token">&quot;version&quot;</span>])
print(<span class="syntax-token">&quot;Debug mode:&quot;</span>, config[<span class="syntax-token">&quot;settings&quot;</span>][<span class="syntax-token">&quot;debug&quot;</span>])
print(<span class="syntax-token">&quot;Port:&quot;</span>, config[<span class="syntax-token">&quot;settings&quot;</span>][<span class="syntax-token">&quot;port&quot;</span>])
print(<span class="syntax-token">&quot;&quot;</span>)

</code></pre><button type="button" class="sk-button" data-copy-code hidden>Copy code</button><span role="status" data-code-status></span></div><p>Save as <a href="/samples/json.kujo" download>json.kujo</a>, then:</p><div class="sample-code"><pre tabindex="0"><code>kujo run json.kujo</code></pre><button type="button" class="sk-button" data-copy-code hidden>Copy code</button><span role="status" data-code-status></span></div><details><summary>Expected output</summary><pre>=== Kujo JSON Support Demo ===

1. Parsing Configuration
App name: My App
Version: 1.0.0
Debug mode: true
Port: 8080

</pre></details><p><a href="https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/json_demo.kujo#L1-L16">Pinned source</a> · <a href="https://docs.kujolang.ai/learn/">Language documentation</a></p></article>
<nav aria-label="Related examples"><a href="/examples/generators/">Previous: Generators</a> · <a href="/examples/structured-output/">Next: Structured output validation</a></nav>
