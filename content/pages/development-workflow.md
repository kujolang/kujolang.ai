---
template: guide-development-workflow
title: A composable development workflow
custom_url: development-workflow
description: "Define scope, retrieve context, implement a change, run tests and inspect evidence in an existing repository."
seo_title: "An inspectable development workflow | Kujo"
social_image: /assets/images/social/development-workflow.jpg
---

<div class="guide-intro"><h2>A change you can trace.</h2>
<p>Take one change from a clear scope to reviewed evidence. Use your existing repository and its real test commands.</p>
</div>
<div class="guide-overview"><article><span>Scope</span><h2>A customer endpoint</h2>
<p>Define the response, validation rules and excluded changes.</p>
</article>
<article><span>Check</span><h2>Your project’s tests</h2>
<p>Use commands that exercise the behavior you changed.</p>
</article>
<article><span>Review</span><h2>A recorded result</h2>
<p>Read the diff, gate logs and verdict before shipping.</p>
</article>
</div>
<nav class="guide-nav" aria-label="On this page"><a href="#step-1">Keep your language. Make the work inspectable. <span aria-hidden="true">↗</span></a><a href="#step-2">Reproduce the local gate-and-evidence stage <span aria-hidden="true">↗</span></a></nav>
<div class="guide-sections kujo-content"><section class="guide-section"><h2 id="step-1">Keep your language. Make the work inspectable.</h2>
<p>Suppose an agent needs to add a customer API endpoint to a Python or TypeScript repository. Choose the tools you need for each stage. You configure their commands, environment and review rules; they do not connect automatically.</p>
<ol><li><strong>Define scope:</strong> describe the endpoint, expected behavior and excluded changes. <a href="/ecosystem/spec/">Spec</a> can express a task contract.</li>
<li><strong>Retrieve context:</strong> inspect relevant routes and tests. <a href="/ecosystem/scout/">Scout</a> analyzes repositories; <a href="/ecosystem/scent/">Scent</a> creates bounded context packs.</li>
<li><strong>Execute:</strong> implement in your checkout or a separately configured <a href="/ecosystem/workcell/">Workcell</a> environment. Isolation depends on the selected backend and policy.</li>
<li><strong>Evaluate:</strong> run the repository’s real tests. <a href="/ecosystem/eval/">Eval</a> and <a href="/ecosystem/lens/">Lens</a> can provide configured evaluation and browser checks.</li>
<li><strong>Inspect evidence:</strong> review the Git diff. <a href="/ecosystem/patchbrief/">PatchBrief</a> summarizes changes; <a href="/ecosystem/changebucket/">ChangeBucket</a> measures their footprint.</li>
<li><strong>Assess readiness:</strong> <a href="/ecosystem/shipcheck/">ShipCheck</a> evaluates declared release conditions. Deployment still belongs to the project’s authorized pipeline.</li>
</ol>
<p>These tools also work with non-Kujo code. Install and configure each one separately.</p>
</section>
<section class="guide-section"><h2 id="step-2">Reproduce the local gate-and-evidence stage</h2>
<p>Prerequisites: Git, Bash and the target project’s existing test command. Clone the <a href="https://github.com/kujolang/kujo-workflows/tree/main/loop-engineering">Loop Engineering source</a> beside a disposable test repository:</p>
<pre><code class="language-sh">git clone https://github.com/kujolang/kujo-workflows.git
cd your-existing-project
../kujo-workflows/loop-engineering/scripts/init-repo-loop.sh</code></pre>
<p>Inspect any existing <code>.loop-engineering/</code> before initialization. Set the objective and real commands in <code>.loop-engineering/loop.yml</code>; the following is a minimal example for a project that already has a working <code>npm test</code> script:</p>
<pre><code class="language-yaml">objective: "Implement and verify the customer endpoint within the agreed scope"
max_iterations: 2
max_no_progress: 1
max_consecutive_failures: 2
eval_gates:
  - id: project_tests
    command: "npm test"
    required: true
  - id: diff_check
    command: "git diff --check"
    required: true
commit:
  enabled: false
  push: false</code></pre>
<p>After implementing the endpoint and its tests:</p>
<pre><code class="language-sh">../kujo-workflows/loop-engineering/scripts/run-workflow.sh --config .loop-engineering/loop.yml</code></pre>
<p>Inspect <code>.loop-engineering/SUMMARY.md</code>, <code>ledger.tsv</code> and <code>iterations/001/</code>. Each iteration records context, action, diff, evaluation logs and verdict. The Bash runner gates and records work; it does not implement an endpoint or invoke an AI agent on its own. Inspect the verdict file: the process exit alone does not establish that gates passed. A passing test command only proves the assertions it actually ran.</p>
<p>This website uses the same runner. Its <a href="https://github.com/kujolang/kujolang.ai/tree/main/.loop-engineering">committed workflow state</a> provides a concrete example of scoped changes and recorded checks.</p>
</section>
</div>
