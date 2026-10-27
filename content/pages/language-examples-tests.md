---
title: Tests
template: language-examples-tests
custom_url: examples/tests
description: "Run assertions using the built-in test runner."
seo_title: "Tests | Kujo"
social_image: /assets/images/social/examples-tests.jpg
---

<nav aria-label="Breadcrumb"><a href="/">Home</a> / <a href="/examples/">Examples</a> / Tests</nav>
<article class="example-panel" id="example-tests" data-example="tests" data-category="Tooling"><p class="eyebrow">Tooling · Test runner · Kujo 1.9.0</p><h3>Tests</h3><p>Run assertions using the built-in test runner.</p><div class="sample-code"><pre tabindex="0"><code><span class="syntax-token"># Kujo test framework example</span>
<span class="syntax-token"># Run with: kujo test-run examples/testing_demo.kujo</span>

<span class="syntax-token">test</span> <span class="syntax-token">&quot;arithmetic&quot;</span> {
    assert_equal(2 + 3, 5)
    assert_equal(7 - 4, 3)
}

<span class="syntax-token">test</span> <span class="syntax-token">&quot;booleans&quot;</span> {
    assert_true(8 % 2 == 0)
    assert_false(7 % 2 == 0)
}

<span class="syntax-token">test</span> <span class="syntax-token">&quot;arrays&quot;</span> {
    <span class="syntax-token">let</span> samples := [1, 2, 3]
    assert_equal(len(samples), 3)
    assert_contains(samples, 2)
}

<span class="syntax-token">test</span> <span class="syntax-token">&quot;dictionaries&quot;</span> {
    <span class="syntax-token">let</span> user := {<span class="syntax-token">&quot;name&quot;</span>: <span class="syntax-token">&quot;Ada&quot;</span>, <span class="syntax-token">&quot;active&quot;</span>: true}
    assert_equal(user[<span class="syntax-token">&quot;name&quot;</span>], <span class="syntax-token">&quot;Ada&quot;</span>)
    assert_true(user[<span class="syntax-token">&quot;active&quot;</span>])
}

<span class="syntax-token">test</span> <span class="syntax-token">&quot;strings&quot;</span> {
    assert_equal(to_upper(<span class="syntax-token">&quot;kujo&quot;</span>), <span class="syntax-token">&quot;KUJO&quot;</span>)
    assert_true(contains(<span class="syntax-token">&quot;local-first&quot;</span>, <span class="syntax-token">&quot;local&quot;</span>) == 1)
}
</code></pre><button type="button" class="sk-button" data-copy-code hidden>Copy code</button><span role="status" data-code-status></span></div><p>Save as <a href="/samples/tests.kujo" download>tests.kujo</a>, then:</p><div class="sample-code"><pre tabindex="0"><code>kujo <span class="syntax-token">test</span>-run tests.kujo</code></pre><button type="button" class="sk-button" data-copy-code hidden>Copy code</button><span role="status" data-code-status></span></div><p><a href="https://github.com/kujolang/kujo/blob/2cfaf185ad03059c89ef4f72fb061074255d00fc/examples/testing_demo.kujo">Pinned source</a> · <a href="https://docs.kujolang.ai/learn/">Language documentation</a></p></article>
<nav aria-label="Related examples"><a href="/examples/capabilities/">Previous: AI capability restrictions</a> · <a href="/examples/modules/">Next: Modules and imports</a></nav>
