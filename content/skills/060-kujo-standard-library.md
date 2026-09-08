---
title: "Kujo Standard Library"
custom_url: "kujo-standard-library"
description: "Use this skill when using, adding, or reviewing Kujo native standard library functions, including arity, return types, capability gates, JSON/JSONL conversion, filesystem, process, network, database, crypto, strings, URI encoding, arrays, dictionaries, rendering helpers, AI helpers, and collection helper behavior."
excerpt: "Use this skill when using, adding, or reviewing Kujo native standard library functions, including arity, return types, capability gates, JSON/JSONL conversion, filesystem, process, network,…"
featured_image: "/assets/images/ecosystem/skill-kujo-standard-library.webp"
social_image: "/assets/images/social/kujo-standard-library.jpg"
section: "Agent Skill"
order: "600"
install_command: "git clone --branch v0.7.0 --depth 1 https://github.com/kujolang/kujo-skills.git && mkdir -p ~/.codex/skills && cp -R kujo-skills/skills/kujo-standard-library ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/v0.7.0/skills/kujo-standard-library/SKILL.md"
launch_story: "One of 135 focused, repository-backed skills in the Kujo Skills 0.7.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.7.0"
last_updated: "tag v0.7.0 Tagger: Robert DeVore <deviodigital@gmail.com> Kujo Skills v0.7.0: reusable video styles 2026-09-08"
keywords: "Kujo Standard Library, Kujo Agent Skill, kujo-standard-library, repository-backed agent guidance"
seo_title: "Kujo Standard Library — Kujo Agent Skill"
seo_description: "Use this skill when using, adding, or reviewing Kujo native standard library functions, including arity, return types, capability gates, JSON/JSONL conversion, filesystem, process, network, database, crypto, strings, URI encoding, arrays, dictionaries, rendering helpers, AI helpers, and collection helper behavior."
---

## What it covers

Use this skill when using, adding, or reviewing Kujo native standard library functions, including arity, return types, capability gates, JSON/JSONL conversion, filesystem, process, network, database, crypto, strings, URI encoding, arrays, dictionaries, rendering helpers, AI helpers, and collection helper behavior.

Run the install command from a new working directory. If you already have the released checkout, copy the complete skill folder from it instead of cloning again.

## Released guidance

- `docs/STANDARD_LIBRARY.md`: full inventory, arity, return type, errors, capability.
- `docs/STANDARD_LIBRARY_REFERENCE.md`: practical category reference and tier labels.
- `docs/AI_RUNTIME.md`: AI helper contracts, replay, message builders, structured errors, egress policy, token budgeting.
- `src/interpreter/mod.rs`: runtime registration and `get_builtin_names()`.
- `src/interpreter/capabilities.rs`: native capability metadata.

## Release boundary

This page reflects the 0.7.0 technical preview on tag v0.7.0
Tagger: Robert DeVore <deviodigital@gmail.com>

Kujo Skills v0.7.0: reusable video styles
2026-09-08. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-standard-library skill on GitHub](https://github.com/kujolang/kujo-skills/blob/v0.7.0/skills/kujo-standard-library/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/v0.7.0/SKILLS_INDEX.md)
