---
title: HTTP and networking
template: language-examples-http
custom_url: examples/http
description: "Inspect a local HTTP server."
seo_title: "HTTP and networking | Kujo"
social_image: /assets/images/social/examples-http.jpg
---

<nav aria-label="Breadcrumb"><a href="/">Home</a> / <a href="/examples/">Examples</a> / HTTP and networking</nav>
<article class="example-panel" id="example-http" data-example="http" data-category="Systems"><p class="eyebrow">Systems · Checked only · Kujo 1.9.0</p><h3>HTTP and networking</h3><p>Inspect a local HTTP server.</p><p class="example-note">Checked only. Running starts a long-lived listener; follow source instructions and choose a free local port.</p><div class="sample-code"><pre tabindex="0"><code><span class="syntax-token"># Simple HTTP Server Example - Hello World</span>
<span class="syntax-token"># Demonstrates basic HTTP server usage with a single route</span>

print(<span class="syntax-token">&quot;http_server_simple: long-running server example skipped in VM auto-run mode&quot;</span>)
exit(0)

<span class="syntax-token"># Create HTTP server on port 8080</span>
server := http_server(8080)

<span class="syntax-token"># Add a simple GET route</span>
server := server.route(<span class="syntax-token">&quot;GET&quot;</span>, <span class="syntax-token">&quot;/&quot;</span>, <span class="syntax-token">func</span>(req) {
    <span class="syntax-token">return</span> http_response(200, <span class="syntax-token">&quot;Hello, World!&quot;</span>)
})

<span class="syntax-token"># Add another route</span>
server := server.route(<span class="syntax-token">&quot;GET&quot;</span>, <span class="syntax-token">&quot;/hello&quot;</span>, <span class="syntax-token">func</span>(req) {
    <span class="syntax-token">return</span> http_response(200, <span class="syntax-token">&quot;Hello from Kujo!&quot;</span>)
})

<span class="syntax-token"># Start the server (blocking - will run until Ctrl+C)</span>
server.listen()
</code></pre><button type="button" class="sk-button" data-copy-code hidden>Copy code</button><span role="status" data-code-status></span></div><p>Save as <a href="/samples/http.kujo" download>http.kujo</a>, then:</p><div class="sample-code"><pre tabindex="0"><code>kujo check http.kujo</code></pre><button type="button" class="sk-button" data-copy-code hidden>Copy code</button><span role="status" data-code-status></span></div><p><a href="https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/http_server_simple.kujo">Pinned source</a> · <a href="https://docs.kujolang.ai/learn/">Language documentation</a></p></article>
<nav aria-label="Related examples"><a href="/examples/files/">Previous: File operations</a> · <a href="/examples/hello-world/">Next: Hello World</a></nav>
