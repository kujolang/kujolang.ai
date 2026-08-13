---
title: "Kujo RunLedger Workflows"
custom_url: "kujo-runledger-workflows"
description: "Use this skill when recording, comparing, reporting, or maintaining RunLedger receipts for AI-agent build runs: `runledger start`, `finish`, `usage`, `cost`, `note`, `followup`, `list`, `show`, `compare`, `report`, `.runledger/` JSON files, run verdicts, token/cost capture, read-only git metadata receipts, RunLedger reports, or RunLedger CLI/tests/source changes."
featured_image: "/assets/images/ecosystem/skill-kujo-runledger-workflows.webp"
social_image: "/assets/images/social/kujo-runledger-workflows.jpg"
section: "Agent Skill"
order: "380"
install_command: "mkdir -p ~/.codex/skills && cp -R skills/kujo-runledger-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-runledger-workflows/SKILL.md"
launch_story: "One of 83 focused, repository-backed skills in the Kujo Skills 0.2.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.2.0"
last_updated: "2026-08-11"
keywords: "Kujo RunLedger Workflows, Kujo Agent Skill, kujo-runledger-workflows, repository-backed agent guidance"
seo_title: "Kujo RunLedger Workflows — Kujo Agent Skill"
seo_description: "Use this skill when recording, comparing, reporting, or maintaining RunLedger receipts for AI-agent build runs: `runledger start`, `finish`, `usage`, `cost`, `note`, `followup`, `list`, `show`, `compare`, `report`, `.runledger/` JSON files, run verdicts, token/cost capture, read-only git metadata receipts, RunLedger reports, or RunLedger CLI/tests/source changes."
---

## What it covers

Use this skill when recording, comparing, reporting, or maintaining RunLedger receipts for AI-agent build runs: `runledger start`, `finish`, `usage`, `cost`, `note`, `followup`, `list`, `show`, `compare`, `report`, `.runledger/` JSON files, run verdicts, token/cost capture, read-only git metadata receipts, RunLedger reports, or RunLedger CLI/tests/source changes.

## Released guidance

- Default storage is `./.runledger/runs/<run-id>.json` relative to the current
- Override with `--ledger <dir>` on commands or `RUNLEDGER_DIR`.
- A ledger can track runs across many repos; `--repo` only identifies the target repo for git metadata.
- Run ids are human-readable and sortable: `YYYY-MM-DD-<model>-<task>-NNN`.
- Treat `.runledger/`, temp ledgers, and generated report outputs as

## Release boundary

This page reflects the 0.2.0 technical preview on 2026-08-11. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-runledger-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-runledger-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/main/SKILLS_INDEX.md)
