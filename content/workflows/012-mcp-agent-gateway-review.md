---
title: "MCP Agent Gateway Review"
custom_url: "mcp-agent-gateway-review"
description: "Generate and validate a constrained MCP server scaffold and safety packet for a repository."
featured_image: "/assets/images/ecosystem/workflow-mcp-agent-gateway-review.webp"
social_image: "/assets/images/social/mcp-agent-gateway-review.jpg"
section: "production capable with limitations"
order: "120"
install_command: "git clone https://github.com/kujolang/kujo-workflows.git && cd kujo-workflows && mcp-agent-gateway-review/scripts/run-workflow.sh"
github_url: "https://github.com/kujolang/kujo-workflows/tree/main/mcp-agent-gateway-review"
launch_story: "A local-first workflow kit with explicit inputs, outputs, evidence, recovery, and approval boundaries."
scope_note: "Current readiness: production capable with limitations. Review the workflow README before live-provider or host-affecting use."
version: "0.3.0"
last_updated: "2026-08-22"
keywords: "MCP Agent Gateway Review, Kujo workflow, mcp-agent-gateway-review, local-first agent workflow"
seo_title: "MCP Agent Gateway Review — Kujo Workflow"
seo_description: "Generate and validate a constrained MCP server scaffold and safety packet for a repository."
---

## Outcome

Generate and validate a constrained MCP server scaffold and safety packet for a repository.

## Inputs

- fixture or TARGET_REPO
- no-AI validation mode

## Evidence and outputs

- mcp.manifest.json
- repo-profile.json
- safety-review.md
- validation-report.md
- agent-handoff.md

The workflow's evidence contract is: generated manifest, reports and log.

## Approval boundaries

- generated gateway exposure and deployment

## State and recovery

timestamped generated scaffold; no deployment action

## Release boundary

Readiness is **production capable with limitations** in the 0.3.0 local technical preview. Hosted runners, broad live-provider coverage, and enterprise readiness are not implied.

## Source

- [Open the complete mcp-agent-gateway-review workflow kit on GitHub](https://github.com/kujolang/kujo-workflows/tree/main/mcp-agent-gateway-review)
- [Browse the released workflow catalog](https://github.com/kujolang/kujo-workflows/blob/main/docs/audit/workflow-catalog.json)
