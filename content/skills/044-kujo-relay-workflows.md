---
title: "Kujo Relay"
custom_url: "kujo-relay-workflows"
description: "Use this skill when running, validating, inspecting, repairing, or maintaining Relay bounded agent mission workflows: `bin/relay`, `doctor`, `chat`, `models`, `agents`, `missions`, `runs`, fixture/live provider paths, PackWrite/RunLedger/ChangeBucket/Eval evidence, event bundles, tool-result bundles, run indexes, Watchdog route posture, or Relay source/docs changes."
excerpt: "Use this skill when running, validating, inspecting, repairing, or maintaining Relay bounded agent mission workflows."
featured_image: "/assets/images/ecosystem/skill-kujo-relay-workflows.webp"
social_image: "/assets/images/social/kujo-relay-workflows.jpg"
section: "Agent Skill"
order: "440"
install_command: "mkdir -p ~/.codex/skills && cp -R skills/kujo-relay-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-relay-workflows/SKILL.md"
launch_story: "One of 96 focused, repository-backed skills in the Kujo Skills 0.4.1 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.4.1"
last_updated: "2026-08-25"
keywords: "Kujo Relay, Kujo Agent Skill, kujo-relay-workflows, repository-backed agent guidance"
seo_title: "Kujo Relay — Kujo Agent Skill"
seo_description: "Use this skill when running, validating, inspecting, repairing, or maintaining Relay bounded agent mission workflows: `bin/relay`, `doctor`, `chat`, `models`, `agents`, `missions`, `runs`, fixture/live provider paths, PackWrite/RunLedger/ChangeBucket/Eval evidence, event bundles, tool-result bundles, run indexes, Watchdog route posture, or Relay source/docs changes."
---

## What it covers

Use this skill when running, validating, inspecting, repairing, or maintaining Relay bounded agent mission workflows: `bin/relay`, `doctor`, `chat`, `models`, `agents`, `missions`, `runs`, fixture/live provider paths, PackWrite/RunLedger/ChangeBucket/Eval evidence, event bundles, tool-result bundles, run indexes, Watchdog route posture, or Relay source/docs changes.

## Released guidance

- Fixture mode is default for safe local operation and records `direct_ai_sdk` as the deterministic no-network route. Live calls require configured Watchdog/AI SDK posture and must not silently bypass Watchdog.
- `missions run` writes PackWrite packets and manifest, AgentEvent-compatible JSONL, sealed RelayReceipt index, RunLedger receipt, ChangeBucket result, Eval result, optional provider tool-result bundle, resumable state, and Markdown/JSON reports under `.relay/runs/<run-id>/`.
- Provider-generated tool planning is opt-in with `agent_tool_mode: "provider"` plus `agent_tool_allowlist`; Relay still executes normalized `relay.write_file` and `relay.run_command` calls through the same Agents SDK policy worker and persists typed tool results.
- Mission budgets include step, repair, token, output, write, tool-call, and tool-turn ceilings. Aggregate mission tokens cap at 65,536 and individual provider requests cap at 16,384.
- Write-enabled missions require `allow_writes: true` and `approval.approved: true`; paths must stay inside the real workspace and cannot traverse `.git`, `.env`, or symlinked parents.

## Release boundary

This page reflects the 0.4.1 technical preview on 2026-08-25. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-relay-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-relay-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/main/SKILLS_INDEX.md)
