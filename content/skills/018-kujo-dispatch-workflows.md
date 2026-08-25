---
title: "Kujo Dispatch"
custom_url: "kujo-dispatch-workflows"
description: "Use this skill when running, inspecting, extending, or maintaining Dispatch reliable AI workflow orchestration: `dispatch.kujo`, `kujo run dispatch.kujo`, `demo`, `resume`, `templates`, `runs`, `show`, `inspect`, `doctor`, `cleanup`, `export-run`, `import-run`, workflow templates, declarative workflow files, plugins, approval gates, trace/report/state artifacts, tool policy profiles, bundle signing, offline fixture runs, SDK bridge integration, or Dispatch CLI/tests/source changes."
excerpt: "Use this skill when running, inspecting, extending, or maintaining Dispatch reliable AI workflow orchestration."
featured_image: "/assets/images/ecosystem/skill-kujo-dispatch-workflows.webp"
social_image: "/assets/images/social/kujo-dispatch-workflows.jpg"
section: "Agent Skill"
order: "180"
install_command: "mkdir -p ~/.codex/skills && cp -R skills/kujo-dispatch-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-dispatch-workflows/SKILL.md"
launch_story: "One of 96 focused, repository-backed skills in the Kujo Skills 0.4.1 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.4.1"
last_updated: "2026-08-25"
keywords: "Kujo Dispatch, Kujo Agent Skill, kujo-dispatch-workflows, repository-backed agent guidance"
seo_title: "Kujo Dispatch — Kujo Agent Skill"
seo_description: "Use this skill when running, inspecting, extending, or maintaining Dispatch reliable AI workflow orchestration: `dispatch.kujo`, `kujo run dispatch.kujo`, `demo`, `resume`, `templates`, `runs`, `show`, `inspect`, `doctor`, `cleanup`, `export-run`, `import-run`, workflow templates, declarative workflow files, plugins, approval gates, trace/report/state artifacts, tool policy profiles, bundle signing, offline fixture runs, SDK bridge integration, or Dispatch CLI/tests/source changes."
---

## What it covers

Use this skill when running, inspecting, extending, or maintaining Dispatch reliable AI workflow orchestration: `dispatch.kujo`, `kujo run dispatch.kujo`, `demo`, `resume`, `templates`, `runs`, `show`, `inspect`, `doctor`, `cleanup`, `export-run`, `import-run`, workflow templates, declarative workflow files, plugins, approval gates, trace/report/state artifacts, tool policy profiles, bundle signing, offline fixture runs, SDK bridge integration, or Dispatch CLI/tests/source changes.

## Released guidance

- Read `README.md` first, then `AGENTS.md`. For release, deployment, extension, or backlog work, read the specific doc named in the request.
- Prefer safe local fixture runs first. Dispatch defaults to `DISPATCH_OFFLINE_FIXTURE=true`, so normal demo/test paths do not need provider credentials.
- Run commands from the Dispatch repo root so relative paths, output roots, fixtures, and bridge scripts resolve consistently.
- Use the VM path `kujo run dispatch.kujo ...` for Dispatch CLI commands unless a task explicitly targets interpreter fallback or parity.
- Treat `outputs/`, `tests/tmp/`, `target/`, and `.ci/` as generated or bulk output unless the task explicitly targets them.

## Release boundary

This page reflects the 0.4.1 technical preview on 2026-08-25. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-dispatch-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-dispatch-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/main/SKILLS_INDEX.md)
