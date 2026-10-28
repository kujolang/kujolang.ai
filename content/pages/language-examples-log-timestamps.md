---
title: Extract log timestamps
template: language-examples-log-timestamps
custom_url: examples/log-timestamps
description: "Find timestamps in sample log lines with a regular expression."
seo_title: "Extract log timestamps | Kujo"
social_image: /assets/images/social/examples-log-timestamps.jpg
---

<script type="application/ld+json">{"@context":"https://schema.org","@type":"SoftwareSourceCode","@id":"https://kujolang.ai/examples/log-timestamps/#source","name":"Extract log timestamps","description":"Find timestamps in sample log lines with a regular expression.","codeRepository":"https://github.com/kujolang/kujo","programmingLanguage":"Kujo","codeSampleType":"code snippet","url":"https://kujolang.ai/examples/log-timestamps/","text":"// Sample log entries\nlogs := [\n    \"[2026-01-23 10:15:30] INFO: Application started successfully\",\n    \"[2026-01-23 10:15:31] DEBUG: Loading configuration from config.json\",\n    \"[2026-01-23 10:15:32] INFO: Connected to database\",\n    \"[2026-01-23 10:16:45] WARNING: High memory usage detected: 85%\",\n    \"[2026-01-23 10:17:12] ERROR: Failed to connect to API endpoint\",\n    \"[2026-01-23 10:17:15] INFO: Retrying connection...\",\n    \"[2026-01-23 10:17:18] ERROR: Connection timeout after 3 attempts\",\n    \"[2026-01-23 10:18:00] INFO: Fallback mode activated\"\n]\n\nprint(\"Sample Logs:\")\nfor log in logs {\n    print(\"  \" + log)\n}\nprint(\"\")\n\n// Extract timestamps\nprint(\"1. Extracting Timestamps:\")\ntimestamp_pattern := \"\\\\d{4}-\\\\d{2}-\\\\d{2} \\\\d{2}:\\\\d{2}:\\\\d{2}\"\nfor log in logs {\n    timestamps := regex_find_all(log, timestamp_pattern)\n    if len(timestamps) > 0 {\n        print(\"  \" + timestamps[0])\n    }\n}\n","isBasedOn":"https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/log_parser_regex.kujo#L7-L33"}</script>
 <nav class="examples-breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a><span aria-hidden="true">/</span><a href="/examples/">Examples</a><span aria-hidden="true">/</span><span aria-current="page">Extract log timestamps</span></nav>
 <header class="examples-hero example-detail-hero"><div><p class="eyebrow">45 / Text</p><h1>Extract log timestamps</h1><p>Find timestamps in sample log lines with a regular expression.</p></div><div class="example-hero-meta"><span class="example-badge">Executed offline</span><a href="/examples/#category-Text">More in Text ↗</a></div></header>
 <div class="example-workbench">
 <section class="example-source" aria-labelledby="source-title"><header class="example-file-bar"><h2 id="source-title">log-timestamps.kujo</h2><a href="/samples/log-timestamps.kujo" download>Download ↓</a></header><div class="sample-code"><pre tabindex="0"><code><span class="syntax-token syntax-comment">// Sample log entries</span>
logs := [
    <span class="syntax-token syntax-string">&quot;[2026-01-23 10:15:30] INFO: Application started successfully&quot;</span>,
    <span class="syntax-token syntax-string">&quot;[2026-01-23 10:15:31] DEBUG: Loading configuration from config.json&quot;</span>,
    <span class="syntax-token syntax-string">&quot;[2026-01-23 10:15:32] INFO: Connected to database&quot;</span>,
    <span class="syntax-token syntax-string">&quot;[2026-01-23 10:16:45] WARNING: High memory usage detected: 85%&quot;</span>,
    <span class="syntax-token syntax-string">&quot;[2026-01-23 10:17:12] ERROR: Failed to connect to API endpoint&quot;</span>,
    <span class="syntax-token syntax-string">&quot;[2026-01-23 10:17:15] INFO: Retrying connection...&quot;</span>,
    <span class="syntax-token syntax-string">&quot;[2026-01-23 10:17:18] ERROR: Connection timeout after 3 attempts&quot;</span>,
    <span class="syntax-token syntax-string">&quot;[2026-01-23 10:18:00] INFO: Fallback mode activated&quot;</span>
]

print(<span class="syntax-token syntax-string">&quot;Sample Logs:&quot;</span>)
<span class="syntax-token syntax-keyword">for</span> log <span class="syntax-token syntax-keyword">in</span> logs {
    print(<span class="syntax-token syntax-string">&quot;  &quot;</span> + log)
}
print(<span class="syntax-token syntax-string">&quot;&quot;</span>)

<span class="syntax-token syntax-comment">// Extract timestamps</span>
print(<span class="syntax-token syntax-string">&quot;1. Extracting Timestamps:&quot;</span>)
timestamp_pattern := <span class="syntax-token syntax-string">&quot;\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2}&quot;</span>
<span class="syntax-token syntax-keyword">for</span> log <span class="syntax-token syntax-keyword">in</span> logs {
    timestamps := regex_find_all(log, timestamp_pattern)
    <span class="syntax-token syntax-keyword">if</span> len(timestamps) &gt; <span class="syntax-token syntax-number">0</span> {
        print(<span class="syntax-token syntax-string">&quot;  &quot;</span> + timestamps[<span class="syntax-token syntax-number">0</span>])
    }
}
</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></section>
 <aside class="example-runbook" aria-labelledby="run-title"><p class="eyebrow">Run it locally</p><h2 id="run-title">Try this example.</h2><ol><li><strong>Set up Kujo</strong><p><a href="/language/">Install the runtime</a> before running the command below.</p></li><li><strong>Save the sample</strong><p>Download <a href="/samples/log-timestamps.kujo" download>log-timestamps.kujo</a> or copy the code into a file with that name.</p></li><li><strong>Run the command</strong><div class="sample-code"><pre tabindex="0"><code>kujo run log-timestamps.kujo</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></li></ol><a class="example-bundle-link" href="/samples/kujo-examples.tar.gz">Download all samples + fixtures ↓</a></aside>
 </div>
 <section class="example-result" aria-labelledby="result-title"><header><p class="eyebrow">Check the result</p><h2 id="result-title">Expected output</h2><p>Your terminal should show this output.</p></header><div><div class="sample-code"><pre tabindex="0"><code>Sample Logs:
  [2026-01-23 10:15:30] INFO: Application started successfully
  [2026-01-23 10:15:31] DEBUG: Loading configuration from config.json
  [2026-01-23 10:15:32] INFO: Connected to database
  [2026-01-23 10:16:45] WARNING: High memory usage detected: 85%
  [2026-01-23 10:17:12] ERROR: Failed to connect to API endpoint
  [2026-01-23 10:17:15] INFO: Retrying connection...
  [2026-01-23 10:17:18] ERROR: Connection timeout after 3 attempts
  [2026-01-23 10:18:00] INFO: Fallback mode activated

1. Extracting Timestamps:
  2026-01-23 10:15:30
  2026-01-23 10:15:31
  2026-01-23 10:15:32
  2026-01-23 10:16:45
  2026-01-23 10:17:12
  2026-01-23 10:17:15
  2026-01-23 10:17:18
  2026-01-23 10:18:00
</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div></div></section>
 <details class="example-provenance"><summary>Source &amp; verification details</summary><div><p>Verified against <a href="https://github.com/kujolang/kujo/tree/2cfaf185ad03059c89ef4f72fb061074255d00fc">Kujo 1.9.0</a>. Executed offline.</p><p><a href="https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/log_parser_regex.kujo#L7-L33">Pinned source</a> · <a href="https://docs.kujolang.ai/learn/">Language documentation</a></p><p class="example-checksum">SHA-256 <code>56b6173fecffdc2073987f79937c88355aac865a7afc6e51f7d067ec79d3308b</code></p></div></details>
 <nav class="example-pagination" aria-label="Related examples"><a href="/examples/path-components/"><span>← Previous example</span><strong>Build file paths</strong></a><a href="/examples/secret-redaction/"><span>Next example →</span><strong>Redact secret values</strong></a></nav>
