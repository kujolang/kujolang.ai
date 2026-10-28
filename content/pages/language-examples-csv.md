---
title: Read and write CSV
template: language-examples-csv
custom_url: examples/csv
description: "Parse rows, read named fields and check a CSV round trip."
seo_title: "Read and write CSV | Kujo"
social_image: /assets/images/social/examples-csv.jpg
---

<script type="application/ld+json">{"@context":"https://schema.org","@type":"SoftwareSourceCode","@id":"https://kujolang.ai/examples/csv/#source","name":"Read and write CSV","description":"Parse rows, read named fields and check a CSV round trip.","codeRepository":"https://github.com/kujolang/kujo","programmingLanguage":"Kujo","codeSampleType":"code snippet","url":"https://kujolang.ai/examples/csv/","text":"# CSV parsing and generation\n\nlet csv_text := \"name,age,active\\nAlice,28,true\\nBob,35,false\"\nlet rows := parse_csv(csv_text)\n\nassert_equal(len(rows), 2)\nassert_equal(rows[0][\"name\"], \"Alice\")\nassert_equal(rows[1][\"age\"], 35)\n\nlet generated := to_csv(rows)\nlet round_trip := parse_csv(generated)\n\nassert_equal(len(round_trip), 2)\nassert_equal(round_trip[0][\"name\"], \"Alice\")\nprint(\"parsed rows:\", rows)\nprint(\"generated CSV:\\n\" + generated)\n","isBasedOn":"https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/csv_demo.kujo"}</script>
 <nav class="examples-breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a><span aria-hidden="true">/</span><a href="/examples/">Examples</a><span aria-hidden="true">/</span><span aria-current="page">Read and write CSV</span></nav>
 <header class="examples-hero example-detail-hero"><div><p class="eyebrow">41 / Data</p><h1>Read and write CSV</h1><p>Parse rows, read named fields and check a CSV round trip.</p></div><div class="example-hero-meta"><span class="example-badge">Executed offline</span><a href="/examples/#category-Data">More in Data ↗</a></div></header>
 <div class="example-workbench">
 <section class="example-source" aria-labelledby="source-title"><header class="example-file-bar"><h2 id="source-title">csv.kujo</h2><a href="/samples/csv.kujo" download>Download ↓</a></header><div class="sample-code"><pre tabindex="0"><code><span class="syntax-token syntax-comment"># CSV parsing and generation</span>

<span class="syntax-token syntax-keyword">let</span> csv_text := <span class="syntax-token syntax-string">&quot;name,age,active\nAlice,28,true\nBob,35,false&quot;</span>
<span class="syntax-token syntax-keyword">let</span> rows := parse_csv(csv_text)

assert_equal(len(rows), <span class="syntax-token syntax-number">2</span>)
assert_equal(rows[<span class="syntax-token syntax-number">0</span>][<span class="syntax-token syntax-string">&quot;name&quot;</span>], <span class="syntax-token syntax-string">&quot;Alice&quot;</span>)
assert_equal(rows[<span class="syntax-token syntax-number">1</span>][<span class="syntax-token syntax-string">&quot;age&quot;</span>], <span class="syntax-token syntax-number">35</span>)

<span class="syntax-token syntax-keyword">let</span> generated := to_csv(rows)
<span class="syntax-token syntax-keyword">let</span> round_trip := parse_csv(generated)

assert_equal(len(round_trip), <span class="syntax-token syntax-number">2</span>)
assert_equal(round_trip[<span class="syntax-token syntax-number">0</span>][<span class="syntax-token syntax-string">&quot;name&quot;</span>], <span class="syntax-token syntax-string">&quot;Alice&quot;</span>)
print(<span class="syntax-token syntax-string">&quot;parsed rows:&quot;</span>, rows)
print(<span class="syntax-token syntax-string">&quot;generated CSV:\n&quot;</span> + generated)
</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></section>
 <aside class="example-runbook" aria-labelledby="run-title"><p class="eyebrow">Run it locally</p><h2 id="run-title">Try this example.</h2><ol><li><strong>Set up Kujo</strong><p><a href="/language/">Install the runtime</a> before running the command below.</p></li><li><strong>Save the sample</strong><p>Download <a href="/samples/csv.kujo" download>csv.kujo</a> or copy the code into a file with that name.</p></li><li><strong>Run the command</strong><div class="sample-code"><pre tabindex="0"><code>kujo run csv.kujo</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></li></ol><a class="example-bundle-link" href="/samples/kujo-examples.tar.gz">Download all samples + fixtures ↓</a></aside>
 </div>
 <section class="example-result" aria-labelledby="result-title"><header><p class="eyebrow">Check the result</p><h2 id="result-title">Expected output</h2><p>Your terminal should show this output.</p></header><div><div class="sample-code"><pre tabindex="0"><code>parsed rows: [{&quot;active&quot;: true, &quot;age&quot;: 28, &quot;name&quot;: Alice}, {&quot;active&quot;: false, &quot;age&quot;: 35, &quot;name&quot;: Bob}]
generated CSV:
active,age,name
true,28,Alice
false,35,Bob

</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></div></section>
 <details class="example-provenance"><summary>Source &amp; verification details</summary><div><p>Verified against <a href="https://github.com/kujolang/kujo/tree/2cfaf185ad03059c89ef4f72fb061074255d00fc">Kujo 1.9.0</a>. Executed offline.</p><p><a href="https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/csv_demo.kujo">Pinned source</a> · <a href="https://docs.kujolang.ai/learn/">Language documentation</a></p><p class="example-checksum">SHA-256 <code>bfd5e914e4db86f310b7a673ed0bbd98bbd6c536e5593f7b2e7004418c3fd36f</code></p></div></details>
 <nav class="example-pagination" aria-label="Related examples"><a href="/examples/canonical-json/"><span>← Previous example</span><strong>Canonical JSON</strong></a><a href="/examples/yaml/"><span>Next example →</span><strong>Read and write YAML</strong></a></nav>
