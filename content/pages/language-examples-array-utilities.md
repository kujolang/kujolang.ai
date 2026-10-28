---
title: Sort and summarize arrays
template: language-examples-array-utilities
custom_url: examples/array-utilities
description: "Sort, reverse, deduplicate and sum a list of numbers."
seo_title: "Sort and summarize arrays | Kujo"
social_image: /assets/images/social/examples-array-utilities.jpg
---

<script type="application/ld+json">{"@context":"https://schema.org","@type":"SoftwareSourceCode","@id":"https://kujolang.ai/examples/array-utilities/#source","name":"Sort and summarize arrays","description":"Sort, reverse, deduplicate and sum a list of numbers.","codeRepository":"https://github.com/kujolang/kujo","programmingLanguage":"Kujo","codeSampleType":"code snippet","url":"https://kujolang.ai/examples/array-utilities/","text":"func print_lines(lines) {\n    for line in lines {\n        print(line)\n    }\n}\n\nfunc section(title) {\n    print(\"\")\n    print(title)\n}\n\nfunc kv(label, value) {\n    print(\"   \" + label + \": \" + to_string(value))\n}\n\nfunc show_result(label, value) {\n    print(\"   \" + label + \" = \" + to_string(value))\n    print()\n}\n\nprint_lines([\n    \"=== Array Utilities Demo ===\",\n    \"\"\n])\n\n# Sample data\nnums := [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]\nkv(\"Original array\", nums)\n\n# 1. Sort - arrange in ascending order\nsection(\"1. SORT - Arrange in ascending order\")\nsorted := sort(nums)\nshow_result(\"sort(nums)\", sorted)\n\n# 2. Reverse - reverse the order\nsection(\"2. REVERSE - Reverse the order\")\nreversed := reverse(nums)\nshow_result(\"reverse(nums)\", reversed)\n\n# 3. Unique - remove duplicates\nsection(\"3. UNIQUE - Remove duplicates (preserves order)\")\nunique_nums := unique(nums)\nshow_result(\"unique(nums)\", unique_nums)\n\n# 4. Sum - calculate total\nsection(\"4. SUM - Calculate total\")\ntotal := sum(nums)\nshow_result(\"sum(nums)\", total)\n","isBasedOn":"https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/array_utilities_demo.kujo#L4-L51"}</script>
 <nav class="examples-breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a><span aria-hidden="true">/</span><a href="/examples/">Examples</a><span aria-hidden="true">/</span><span aria-current="page">Sort and summarize arrays</span></nav>
 <header class="examples-hero example-detail-hero"><div><p class="eyebrow">30 / Data</p><h1>Sort and summarize arrays</h1><p>Sort, reverse, deduplicate and sum a list of numbers.</p></div><div class="example-hero-meta"><span class="example-badge">Executed offline</span><a href="/examples/#category-Data">More in Data ↗</a></div></header>
 <div class="example-workbench">
 <section class="example-source" aria-labelledby="source-title"><header class="example-file-bar"><h2 id="source-title">array-utilities.kujo</h2><a href="/samples/array-utilities.kujo" download>Download ↓</a></header><div class="sample-code"><pre tabindex="0"><code><span class="syntax-token syntax-keyword">func</span> print_lines(lines) {
    <span class="syntax-token syntax-keyword">for</span> line <span class="syntax-token syntax-keyword">in</span> lines {
        print(line)
    }
}

<span class="syntax-token syntax-keyword">func</span> section(title) {
    print(<span class="syntax-token syntax-string">&quot;&quot;</span>)
    print(title)
}

<span class="syntax-token syntax-keyword">func</span> kv(label, value) {
    print(<span class="syntax-token syntax-string">&quot;   &quot;</span> + label + <span class="syntax-token syntax-string">&quot;: &quot;</span> + to_string(value))
}

<span class="syntax-token syntax-keyword">func</span> show_result(label, value) {
    print(<span class="syntax-token syntax-string">&quot;   &quot;</span> + label + <span class="syntax-token syntax-string">&quot; = &quot;</span> + to_string(value))
    print()
}

print_lines([
    <span class="syntax-token syntax-string">&quot;=== Array Utilities Demo ===&quot;</span>,
    <span class="syntax-token syntax-string">&quot;&quot;</span>
])

<span class="syntax-token syntax-comment"># Sample data</span>
nums := [<span class="syntax-token syntax-number">3</span>, <span class="syntax-token syntax-number">1</span>, <span class="syntax-token syntax-number">4</span>, <span class="syntax-token syntax-number">1</span>, <span class="syntax-token syntax-number">5</span>, <span class="syntax-token syntax-number">9</span>, <span class="syntax-token syntax-number">2</span>, <span class="syntax-token syntax-number">6</span>, <span class="syntax-token syntax-number">5</span>, <span class="syntax-token syntax-number">3</span>]
kv(<span class="syntax-token syntax-string">&quot;Original array&quot;</span>, nums)

<span class="syntax-token syntax-comment"># 1. Sort - arrange in ascending order</span>
section(<span class="syntax-token syntax-string">&quot;1. SORT - Arrange in ascending order&quot;</span>)
sorted := sort(nums)
show_result(<span class="syntax-token syntax-string">&quot;sort(nums)&quot;</span>, sorted)

<span class="syntax-token syntax-comment"># 2. Reverse - reverse the order</span>
section(<span class="syntax-token syntax-string">&quot;2. REVERSE - Reverse the order&quot;</span>)
reversed := reverse(nums)
show_result(<span class="syntax-token syntax-string">&quot;reverse(nums)&quot;</span>, reversed)

<span class="syntax-token syntax-comment"># 3. Unique - remove duplicates</span>
section(<span class="syntax-token syntax-string">&quot;3. UNIQUE - Remove duplicates (preserves order)&quot;</span>)
unique_nums := unique(nums)
show_result(<span class="syntax-token syntax-string">&quot;unique(nums)&quot;</span>, unique_nums)

<span class="syntax-token syntax-comment"># 4. Sum - calculate total</span>
section(<span class="syntax-token syntax-string">&quot;4. SUM - Calculate total&quot;</span>)
total := sum(nums)
show_result(<span class="syntax-token syntax-string">&quot;sum(nums)&quot;</span>, total)
</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></section>
 <aside class="example-runbook" aria-labelledby="run-title"><p class="eyebrow">Run it locally</p><h2 id="run-title">Try this example.</h2><ol><li><strong>Set up Kujo</strong><p><a href="/language/">Install the runtime</a> before running the command below.</p></li><li><strong>Save the sample</strong><p>Download <a href="/samples/array-utilities.kujo" download>array-utilities.kujo</a> or copy the code into a file with that name.</p></li><li><strong>Run the command</strong><div class="sample-code"><pre tabindex="0"><code>kujo run array-utilities.kujo</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></li></ol><a class="example-bundle-link" href="/samples/kujo-examples.tar.gz">Download all samples + fixtures ↓</a></aside>
 </div>
 <section class="example-result" aria-labelledby="result-title"><header><p class="eyebrow">Check the result</p><h2 id="result-title">Expected output</h2><p>Your terminal should show this output.</p></header><div><div class="sample-code"><pre tabindex="0"><code>=== Array Utilities Demo ===

   Original array: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

1. SORT - Arrange in ascending order
   sort(nums) = [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]


2. REVERSE - Reverse the order
   reverse(nums) = [3, 5, 6, 2, 9, 5, 1, 4, 1, 3]


3. UNIQUE - Remove duplicates (preserves order)
   unique(nums) = [3, 1, 4, 5, 9, 2, 6]


4. SUM - Calculate total
   sum(nums) = 39

</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></div></section>
 <details class="example-provenance"><summary>Source &amp; verification details</summary><div><p>Verified against <a href="https://github.com/kujolang/kujo/tree/2cfaf185ad03059c89ef4f72fb061074255d00fc">Kujo 1.9.0</a>. Executed offline.</p><p><a href="https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/array_utilities_demo.kujo#L4-L51">Pinned source</a> · <a href="https://docs.kujolang.ai/learn/">Language documentation</a></p><p class="example-checksum">SHA-256 <code>adc41075c346875a9d20e582db49643c4ecac3e0fdbaaa4b3626e82c610ebebb</code></p></div></details>
 <nav class="example-pagination" aria-label="Related examples"><a href="/examples/map-and-filter/"><span>← Previous example</span><strong>Map and filter arrays</strong></a><a href="/examples/nested-dictionaries/"><span>Next example →</span><strong>Nested dictionaries</strong></a></nav>
