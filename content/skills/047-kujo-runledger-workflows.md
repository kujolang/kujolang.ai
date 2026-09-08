---
title: "Kujo RunLedger"
custom_url: "kujo-runledger-workflows"
description: "Use this skill when recording, comparing, reporting, correlating, or maintaining RunLedger receipts for AI-agent build runs: `runledger start`, `finish`, `usage`, `cost`, `correlate`, `note`, `followup`, `list`, `show`, `compare`, `report`, `.runledger/` JSON files, run verdicts, token/cost capture, Watchdog/Dispatch/Relay/Eval links, read-only git metadata receipts, RunLedger reports, or RunLedger CLI/tests/source changes."
excerpt: "Use this skill when recording, comparing, reporting, correlating, or maintaining RunLedger receipts for AI-agent build runs."
featured_image: "/assets/images/ecosystem/skill-kujo-runledger-workflows.webp"
social_image: "/assets/images/social/kujo-runledger-workflows.jpg"
section: "Agent Skill"
order: "470"
install_command: "git clone --branch v0.7.0 --depth 1 https://github.com/kujolang/kujo-skills.git && mkdir -p ~/.codex/skills && cp -R kujo-skills/skills/kujo-runledger-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/v0.7.0/skills/kujo-runledger-workflows/SKILL.md"
launch_story: "One of 135 focused, repository-backed skills in the Kujo Skills 0.7.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.7.0"
last_updated: "tag v0.7.0 Tagger: Robert DeVore <deviodigital@gmail.com> Kujo Skills v0.7.0: reusable video styles 2026-09-08"
keywords: "Kujo RunLedger, Kujo Agent Skill, kujo-runledger-workflows, repository-backed agent guidance"
seo_title: "Kujo RunLedger — Kujo Agent Skill"
seo_description: "Use this skill when recording, comparing, reporting, correlating, or maintaining RunLedger receipts for AI-agent build runs: `runledger start`, `finish`, `usage`, `cost`, `correlate`, `note`, `followup`, `list`, `show`, `compare`, `report`, `.runledger/` JSON files, run verdicts, token/cost capture, Watchdog/Dispatch/Relay/Eval links, read-only git metadata receipts, RunLedger reports, or RunLedger CLI/tests/source changes."
---

## What it covers

Use this skill when recording, comparing, reporting, correlating, or maintaining RunLedger receipts for AI-agent build runs: `runledger start`, `finish`, `usage`, `cost`, `correlate`, `note`, `followup`, `list`, `show`, `compare`, `report`, `.runledger/` JSON files, run verdicts, token/cost capture, Watchdog/Dispatch/Relay/Eval links, read-only git metadata receipts, RunLedger reports, or RunLedger CLI/tests/source changes.

Run the install command from a new working directory. If you already have the released checkout, copy the complete skill folder from it instead of cloning again.

## Released guidance

- Default storage is `./.runledger/runs/<run-id>.json` relative to the current
- Override with `--ledger <dir>` on commands or `RUNLEDGER_DIR`.
- A ledger can track runs across many repos; `--repo` only identifies the target repo for git metadata.
- Run ids are human-readable and sortable: `YYYY-MM-DD-<model>-<task>-NNN`.
- Treat `.runledger/`, temp ledgers, and generated report outputs as

## Release boundary

This page reflects the 0.7.0 technical preview on tag v0.7.0
Tagger: Robert DeVore <deviodigital@gmail.com>

Kujo Skills v0.7.0: reusable video styles
2026-09-08. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-runledger-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/v0.7.0/skills/kujo-runledger-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/v0.7.0/SKILLS_INDEX.md)
