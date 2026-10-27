---
title: A composable development workflow
custom_url: development-workflow
description: "Define scope, retrieve context, implement a change, run tests and inspect evidence in an existing repository."
seo_title: "An inspectable development workflow | Kujo"
social_image: /assets/images/social/development-workflow.jpg
---

## Keep your language. Make the work inspectable.

Scenario: an agent is asked to add a customer API endpoint to an existing Python or TypeScript repository. These are composable stages, not a claim that all the tools are automatically connected. You choose the commands, execution environment and review boundary.

1. **Define scope:** describe the endpoint, expected behavior and excluded changes. [Spec](/ecosystem/spec/) can express a task contract.
2. **Retrieve context:** inspect relevant routes and tests. [Scout](/ecosystem/scout/) analyzes repositories; [Scent](/ecosystem/scent/) creates bounded context packs.
3. **Execute:** implement in your checkout or a separately configured [Workcell](/ecosystem/workcell/) environment. Isolation depends on the selected backend and policy.
4. **Evaluate:** run the repository’s real tests. [Eval](/ecosystem/eval/) and [Lens](/ecosystem/lens/) can provide configured evaluation and browser checks.
5. **Inspect evidence:** review the Git diff. [PatchBrief](/ecosystem/patchbrief/) summarizes changes; [ChangeBucket](/ecosystem/changebucket/) measures their footprint.
6. **Assess readiness:** [ShipCheck](/ecosystem/shipcheck/) evaluates declared release conditions. Deployment still belongs to the project’s authorized pipeline.

These repository-oriented tools can support non-Kujo code. They require their own installation and configuration; they are not language keywords or bundled guarantees.

## Reproduce the local gate-and-evidence stage

Prerequisites: Git, Bash and the target project’s existing test command. Clone the [Loop Engineering source](https://github.com/kujolang/kujo-workflows/tree/main/loop-engineering) beside a disposable test repository:

```sh
git clone https://github.com/kujolang/kujo-workflows.git
cd your-existing-project
../kujo-workflows/loop-engineering/scripts/init-repo-loop.sh
```

Inspect any existing `.loop-engineering/` before initialization. Set the objective and real commands in `.loop-engineering/loop.yml`; the following is a minimal example for a project that already has a working `npm test` script:

```yaml
objective: "Implement and verify the customer endpoint within the agreed scope"
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
  push: false
```

After implementing the endpoint and its tests:

```sh
../kujo-workflows/loop-engineering/scripts/run-workflow.sh --config .loop-engineering/loop.yml
```

Inspect `.loop-engineering/SUMMARY.md`, `ledger.tsv` and `iterations/001/`. Each iteration records context, action, diff, evaluation logs and verdict. The Bash runner gates and records work; it does not implement an endpoint or invoke an AI agent on its own. Inspect the verdict file: the process exit alone does not establish that gates passed. A passing test command only proves the assertions it actually ran.

This website uses the same runner. Its [committed workflow state](https://github.com/kujolang/kujolang.ai/tree/main/.loop-engineering) provides a concrete example of scoped changes and recorded checks.
