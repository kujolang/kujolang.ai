---
title: File operations
template: language-examples-files
custom_url: examples/files
description: "Read the upstream filesystem demonstration."
seo_title: "File operations | Kujo"
social_image: /assets/images/social/examples-files.jpg
---

<nav aria-label="Breadcrumb"><a href="/">Home</a> / <a href="/examples/">Examples</a> / File operations</nav>
<article class="example-panel" id="example-files" data-example="files" data-category="Systems"><p class="eyebrow">Systems · Checked only · Kujo 1.9.0</p><h3>File operations</h3><p>Read the upstream filesystem demonstration.</p><p class="example-note">Checked only. Execution creates and modifies files; use a disposable working directory.</p><div class="sample-code"><pre tabindex="0"><code><span class="syntax-token"># File Operations Demo</span>
<span class="syntax-token"># Demonstrates file operation helpers with local output helpers.</span>

<span class="syntax-token">func</span> section(title) {
    print(<span class="syntax-token">&quot;&quot;</span>)
    print(<span class="syntax-token">&quot;== &quot;</span> + title + <span class="syntax-token">&quot; ==&quot;</span>)
}

<span class="syntax-token">func</span> kv(label, value) {
    print(<span class="syntax-token">&quot;  &quot;</span> + label + <span class="syntax-token">&quot;: &quot;</span> + to_string(value))
}

<span class="syntax-token">func</span> ok(message) {
    print(<span class="syntax-token">&quot;  ✓ &quot;</span> + message)
}

section(<span class="syntax-token">&quot;File Operations Demo&quot;</span>)

<span class="syntax-token"># Create a test file</span>
section(<span class="syntax-token">&quot;1. Creating test file&quot;</span>)
write_file(<span class="syntax-token">&quot;demo_test.txt&quot;</span>, <span class="syntax-token">&quot;Hello, Kujo!\nThis is a test file.\n&quot;</span>)
ok(<span class="syntax-token">&quot;Created demo_test.txt&quot;</span>)

<span class="syntax-token"># Check file size</span>
section(<span class="syntax-token">&quot;2. Checking file size&quot;</span>)
size := file_size(<span class="syntax-token">&quot;demo_test.txt&quot;</span>)
kv(<span class="syntax-token">&quot;File size&quot;</span>, <span class="syntax-token">&quot;${size} bytes&quot;</span>)

<span class="syntax-token"># Copy the file</span>
section(<span class="syntax-token">&quot;3. Copying file&quot;</span>)
copy_file(<span class="syntax-token">&quot;demo_test.txt&quot;</span>, <span class="syntax-token">&quot;demo_test_copy.txt&quot;</span>)
ok(<span class="syntax-token">&quot;Copied to demo_test_copy.txt&quot;</span>)

<span class="syntax-token"># Verify both files exist</span>
section(<span class="syntax-token">&quot;4. Verifying both files exist&quot;</span>)
exists1 := file_exists(<span class="syntax-token">&quot;demo_test.txt&quot;</span>)
exists2 := file_exists(<span class="syntax-token">&quot;demo_test_copy.txt&quot;</span>)
kv(<span class="syntax-token">&quot;Original exists&quot;</span>, exists1)
kv(<span class="syntax-token">&quot;Copy exists&quot;</span>, exists2)

<span class="syntax-token"># Check sizes match</span>
section(<span class="syntax-token">&quot;5. Comparing file sizes&quot;</span>)
size1 := file_size(<span class="syntax-token">&quot;demo_test.txt&quot;</span>)
size2 := file_size(<span class="syntax-token">&quot;demo_test_copy.txt&quot;</span>)
<span class="syntax-token">if</span> size1 == size2 {
    ok(<span class="syntax-token">&quot;Sizes match: ${size1} bytes&quot;</span>)
} <span class="syntax-token">else</span> {
    print(<span class="syntax-token">&quot;   ✗ Size mismatch!&quot;</span>)
}

<span class="syntax-token"># Rename the original</span>
section(<span class="syntax-token">&quot;6. Renaming original file&quot;</span>)
rename_file(<span class="syntax-token">&quot;demo_test.txt&quot;</span>, <span class="syntax-token">&quot;demo_renamed.txt&quot;</span>)
ok(<span class="syntax-token">&quot;Renamed to demo_renamed.txt&quot;</span>)

<span class="syntax-token"># List current directory to see files</span>
section(<span class="syntax-token">&quot;7. Files in current directory&quot;</span>)
files := list_dir(<span class="syntax-token">&quot;.&quot;</span>)
<span class="syntax-token">for</span> file <span class="syntax-token">in</span> files {
    <span class="syntax-token">if</span> contains(file, <span class="syntax-token">&quot;demo_&quot;</span>) {
        print(<span class="syntax-token">&quot;   - ${file}&quot;</span>)
    }
}

<span class="syntax-token"># Clean up</span>
section(<span class="syntax-token">&quot;8. Cleaning up&quot;</span>)
delete_file(<span class="syntax-token">&quot;demo_renamed.txt&quot;</span>)
delete_file(<span class="syntax-token">&quot;demo_test_copy.txt&quot;</span>)
ok(<span class="syntax-token">&quot;Deleted all test files&quot;</span>)

<span class="syntax-token"># Verify cleanup</span>
section(<span class="syntax-token">&quot;9. Verification&quot;</span>)
check1 := file_exists(<span class="syntax-token">&quot;demo_test.txt&quot;</span>)
check2 := file_exists(<span class="syntax-token">&quot;demo_test_copy.txt&quot;</span>)
check3 := file_exists(<span class="syntax-token">&quot;demo_renamed.txt&quot;</span>)

<span class="syntax-token">if</span> !check1 &amp;&amp; !check2 &amp;&amp; !check3 {
    ok(<span class="syntax-token">&quot;All files successfully removed&quot;</span>)
} <span class="syntax-token">else</span> {
    print(<span class="syntax-token">&quot;   ✗ Some files still exist&quot;</span>)
}

section(<span class="syntax-token">&quot;Demo Complete&quot;</span>)

<span class="syntax-token"># Practical example: Backup system</span>
section(<span class="syntax-token">&quot;Practical Example: Simple Backup&quot;</span>)

<span class="syntax-token"># Create a config file</span>
config := <span class="syntax-token">&quot;database_host=localhost\ndatabase_port=5432\n&quot;</span>
write_file(<span class="syntax-token">&quot;app_config.txt&quot;</span>, config)
ok(<span class="syntax-token">&quot;Created app_config.txt (${len(config)} bytes)&quot;</span>)

<span class="syntax-token"># Create backup</span>
<span class="syntax-token">if</span> file_exists(<span class="syntax-token">&quot;app_config.txt&quot;</span>) {
    copy_file(<span class="syntax-token">&quot;app_config.txt&quot;</span>, <span class="syntax-token">&quot;app_config.backup.txt&quot;</span>)
    size := file_size(<span class="syntax-token">&quot;app_config.backup.txt&quot;</span>)
    ok(<span class="syntax-token">&quot;Backup created: app_config.backup.txt (${size} bytes)&quot;</span>)
}

<span class="syntax-token"># Modify the config</span>
new_config := <span class="syntax-token">&quot;database_host=prod-server\ndatabase_port=5432\n&quot;</span>
write_file(<span class="syntax-token">&quot;app_config.txt&quot;</span>, new_config)
ok(<span class="syntax-token">&quot;Modified app_config.txt&quot;</span>)

<span class="syntax-token"># Compare sizes</span>
original_size := file_size(<span class="syntax-token">&quot;app_config.txt&quot;</span>)
backup_size := file_size(<span class="syntax-token">&quot;app_config.backup.txt&quot;</span>)
kv(<span class="syntax-token">&quot;Original bytes&quot;</span>, original_size)
kv(<span class="syntax-token">&quot;Backup bytes&quot;</span>, backup_size)

<span class="syntax-token"># Cleanup</span>
delete_file(<span class="syntax-token">&quot;app_config.txt&quot;</span>)
delete_file(<span class="syntax-token">&quot;app_config.backup.txt&quot;</span>)
ok(<span class="syntax-token">&quot;Cleanup complete&quot;</span>)
</code></pre><button type="button" class="sk-button" data-copy-code hidden>Copy code</button><span role="status" data-code-status></span></div><p>Save as <a href="/samples/files.kujo" download>files.kujo</a>, then:</p><div class="sample-code"><pre tabindex="0"><code>kujo check files.kujo</code></pre><button type="button" class="sk-button" data-copy-code hidden>Copy code</button><span role="status" data-code-status></span></div><p><a href="https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/file_operations_demo.kujo">Pinned source</a> · <a href="https://docs.kujolang.ai/learn/">Language documentation</a></p></article>
<nav aria-label="Related examples"><a href="/examples/modules/">Previous: Modules and imports</a> · <a href="/examples/http/">Next: HTTP and networking</a></nav>
