---
title: "Docsgen Repo Contract Runner"
custom_url: "docsgen-repo-contract-runner"
description: "Generate a reviewable DocsGen contract packet for a chosen repository."
featured_image: "/assets/images/ecosystem/workflow-docsgen-repo-contract-runner.webp"
social_image: "/assets/images/social/docsgen-repo-contract-runner.jpg"
section: "production capable with limitations"
order: "60"
install_command: "git clone https://github.com/kujolang/kujo-workflows.git && cd kujo-workflows && docsgen-repo-contract-runner/scripts/run-workflow.sh"
github_url: "https://github.com/kujolang/kujo-workflows/tree/main/docsgen-repo-contract-runner"
launch_story: "A local-first workflow kit with explicit inputs, outputs, evidence, recovery, and approval boundaries."
scope_note: "Current readiness: production capable with limitations. Review the workflow README before live-provider or host-affecting use."
version: "0.2.0"
last_updated: "2026-08-11"
keywords: "Docsgen Repo Contract Runner, Kujo workflow, docsgen-repo-contract-runner, local-first agent workflow"
seo_title: "Docsgen Repo Contract Runner — Kujo Workflow"
seo_description: "Generate a reviewable DocsGen contract packet for a chosen repository."
---

## Outcome

Generate a reviewable DocsGen contract packet for a chosen repository.

## Inputs

- optional TARGET_REPO
- optional DOCGEN_STRICT

## Evidence and outputs

- docgen.md
- docgen.json
- docgen-gaps.json
- agent-handoff.md

The workflow's evidence contract is: CLI JSON, gap files, logs, handoff.

## Approval boundaries

- publication and source-repository writes are outside scope

## State and recovery

timestamped output packet; rerun creates a new packet

## Release boundary

Readiness is **production capable with limitations** in the 0.2.0 local technical preview. Hosted runners, broad live-provider coverage, and enterprise readiness are not implied.

## Source

- [Open the complete docsgen-repo-contract-runner workflow kit on GitHub](https://github.com/kujolang/kujo-workflows/tree/main/docsgen-repo-contract-runner)
- [Browse the released workflow catalog](https://github.com/kujolang/kujo-workflows/blob/main/docs/audit/workflow-catalog.json)
