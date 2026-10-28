---
title: Build file paths
template: language-examples-path-components
custom_url: examples/path-components
description: "Join path segments and extract a directory and filename."
seo_title: "Build file paths | Kujo"
social_image: /assets/images/social/examples-path-components.jpg
---

<script type="application/ld+json">{"@context":"https://schema.org","@type":"SoftwareSourceCode","@id":"https://kujolang.ai/examples/path-components/#source","name":"Build file paths","description":"Join path segments and extract a directory and filename.","codeRepository":"https://github.com/kujolang/kujo","programmingLanguage":"Kujo","codeSampleType":"code snippet","url":"https://kujolang.ai/examples/path-components/","text":"func print_lines(lines) {\n    for line in lines {\n        print(line)\n    }\n}\n\nfunc section(title) {\n    print(\"\")\n    print(title)\n}\n\nfunc kv(label, value) {\n    print(\"  \" + label + \": \" + to_string(value))\n}\n\nprint_lines([\n    \"=== Path Utilities Demo ===\",\n    \"\"\n])\n\n// Build paths\nsection(\"1. Building Paths:\")\nhome_dir := \"/home/user\"\ndocs_path := join_path(home_dir, \"Documents\", \"projects\", \"kujo\")\nkv(\"Home directory\", home_dir)\nkv(\"Documents path\", docs_path)\n\nconfig_path := join_path(home_dir, \".config\", \"kujo\", \"settings.json\")\nkv(\"Config path\", config_path)\n\n// Extract path components\nsection(\"2. Extracting Path Components:\")\nfull_path := \"/home/user/projects/kujo/examples/demo.kujo\"\nkv(\"Full path\", full_path)\nkv(\"Directory\", dirname(full_path))\nkv(\"Filename\", basename(full_path))\n","isBasedOn":"https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/path_utilities.kujo#L4-L39"}</script>
 <nav class="examples-breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a><span aria-hidden="true">/</span><a href="/examples/">Examples</a><span aria-hidden="true">/</span><span aria-current="page">Build file paths</span></nav>
 <header class="examples-hero example-detail-hero"><div><p class="eyebrow">44 / Systems</p><h1>Build file paths</h1><p>Join path segments and extract a directory and filename.</p></div><div class="example-hero-meta"><span class="example-badge">Executed offline</span><a href="/examples/#category-Systems">More in Systems ↗</a></div></header>
 <div class="example-workbench">
 <section class="example-source" aria-labelledby="source-title"><header class="example-file-bar"><h2 id="source-title">path-components.kujo</h2><a href="/samples/path-components.kujo" download>Download ↓</a></header><div class="sample-code"><pre tabindex="0"><code><span class="syntax-token syntax-keyword">func</span> print_lines(lines) {
    <span class="syntax-token syntax-keyword">for</span> line <span class="syntax-token syntax-keyword">in</span> lines {
        print(line)
    }
}

<span class="syntax-token syntax-keyword">func</span> section(title) {
    print(<span class="syntax-token syntax-string">&quot;&quot;</span>)
    print(title)
}

<span class="syntax-token syntax-keyword">func</span> kv(label, value) {
    print(<span class="syntax-token syntax-string">&quot;  &quot;</span> + label + <span class="syntax-token syntax-string">&quot;: &quot;</span> + to_string(value))
}

print_lines([
    <span class="syntax-token syntax-string">&quot;=== Path Utilities Demo ===&quot;</span>,
    <span class="syntax-token syntax-string">&quot;&quot;</span>
])

<span class="syntax-token syntax-comment">// Build paths</span>
section(<span class="syntax-token syntax-string">&quot;1. Building Paths:&quot;</span>)
home_dir := <span class="syntax-token syntax-string">&quot;/home/user&quot;</span>
docs_path := join_path(home_dir, <span class="syntax-token syntax-string">&quot;Documents&quot;</span>, <span class="syntax-token syntax-string">&quot;projects&quot;</span>, <span class="syntax-token syntax-string">&quot;kujo&quot;</span>)
kv(<span class="syntax-token syntax-string">&quot;Home directory&quot;</span>, home_dir)
kv(<span class="syntax-token syntax-string">&quot;Documents path&quot;</span>, docs_path)

config_path := join_path(home_dir, <span class="syntax-token syntax-string">&quot;.config&quot;</span>, <span class="syntax-token syntax-string">&quot;kujo&quot;</span>, <span class="syntax-token syntax-string">&quot;settings.json&quot;</span>)
kv(<span class="syntax-token syntax-string">&quot;Config path&quot;</span>, config_path)

<span class="syntax-token syntax-comment">// Extract path components</span>
section(<span class="syntax-token syntax-string">&quot;2. Extracting Path Components:&quot;</span>)
full_path := <span class="syntax-token syntax-string">&quot;/home/user/projects/kujo/examples/demo.kujo&quot;</span>
kv(<span class="syntax-token syntax-string">&quot;Full path&quot;</span>, full_path)
kv(<span class="syntax-token syntax-string">&quot;Directory&quot;</span>, dirname(full_path))
kv(<span class="syntax-token syntax-string">&quot;Filename&quot;</span>, basename(full_path))
</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></section>
 <aside class="example-runbook" aria-labelledby="run-title"><p class="eyebrow">Run it locally</p><h2 id="run-title">Try this example.</h2><ol><li><strong>Set up Kujo</strong><p><a href="/language/">Install the runtime</a> before running the command below.</p></li><li><strong>Save the sample</strong><p>Download <a href="/samples/path-components.kujo" download>path-components.kujo</a> or copy the code into a file with that name.</p></li><li><strong>Run the command</strong><div class="sample-code"><pre tabindex="0"><code>kujo run path-components.kujo</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></li></ol><a class="example-bundle-link" href="/samples/kujo-examples.tar.gz">Download all samples + fixtures ↓</a></aside>
 </div>
 <section class="example-result" aria-labelledby="result-title"><header><p class="eyebrow">Check the result</p><h2 id="result-title">Expected output</h2><p>Your terminal should show this output.</p></header><div><div class="sample-code"><pre tabindex="0"><code>=== Path Utilities Demo ===


1. Building Paths:
  Home directory: /home/user
  Documents path: /home/user/Documents/projects/kujo
  Config path: /home/user/.config/kujo/settings.json

2. Extracting Path Components:
  Full path: /home/user/projects/kujo/examples/demo.kujo
  Directory: /home/user/projects/kujo/examples
  Filename: demo.kujo
</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></div></section>
 <details class="example-provenance"><summary>Source &amp; verification details</summary><div><p>Verified against <a href="https://github.com/kujolang/kujo/tree/2cfaf185ad03059c89ef4f72fb061074255d00fc">Kujo 1.9.0</a>. Executed offline.</p><p><a href="https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/path_utilities.kujo#L4-L39">Pinned source</a> · <a href="https://docs.kujolang.ai/learn/">Language documentation</a></p><p class="example-checksum">SHA-256 <code>e35c2c291114b43e8bec4a1dd004470f92c3ce35d4c41837238d59b418cffe0f</code></p></div></details>
 <nav class="example-pagination" aria-label="Related examples"><a href="/examples/toml/"><span>← Previous example</span><strong>Read and write TOML</strong></a><a href="/examples/log-timestamps/"><span>Next example →</span><strong>Extract log timestamps</strong></a></nav>
