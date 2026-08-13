---
title: "Kujo Kennel"
custom_url: "kujo-kennel-workflows"
description: "Use this skill when inspecting, using, validating, or maintaining Kennel package/dependency workflows: `kennel.kujo`, package manifests, lockfiles, file dependencies, static indexes and mirrors, trust policy, source policy, semver range resolution, local hosted-registry lifecycle, install/update/validate behavior, release gates, or `kennel` source/test changes."
featured_image: "/assets/images/ecosystem/skill-kujo-kennel-workflows.webp"
social_image: "/assets/images/social/kujo-kennel-workflows.jpg"
section: "Agent Skill"
order: "240"
install_command: "mkdir -p ~/.codex/skills && cp -R skills/kujo-kennel-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-kennel-workflows/SKILL.md"
launch_story: "One of 83 focused, repository-backed skills in the Kujo Skills 0.2.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.2.0"
last_updated: "2026-08-11"
keywords: "Kujo Kennel, Kujo Agent Skill, kujo-kennel-workflows, repository-backed agent guidance"
seo_title: "Kujo Kennel — Kujo Agent Skill"
seo_description: "Use this skill when inspecting, using, validating, or maintaining Kennel package/dependency workflows: `kennel.kujo`, package manifests, lockfiles, file dependencies, static indexes and mirrors, trust policy, source policy, semver range resolution, local hosted-registry lifecycle, install/update/validate behavior, release gates, or `kennel` source/test changes."
---

## What it covers

Use this skill when inspecting, using, validating, or maintaining Kennel package/dependency workflows: `kennel.kujo`, package manifests, lockfiles, file dependencies, static indexes and mirrors, trust policy, source policy, semver range resolution, local hosted-registry lifecycle, install/update/validate behavior, release gates, or `kennel` source/test changes.

## Released guidance

- Package manifests, lockfiles, static indexes/mirrors, trust policy, source policy, and local hosted-registry artifacts are contract surfaces.
- Root-level module files such as `commands_shared.kujo`, `installer.kujo`, `lockfile.kujo`, and `utils.kujo` are compatibility shims that re-export `src/` implementations; keep them aligned until downstream root-module imports are retired.
- Local hosted-registry lifecycle, auth, publish/access/visibility/search/metadata APIs, and hosted install against local artifacts are in the launch-safe scope. Operated public registry service, public discovery, hosted moderation, malware scanning, and public trust scoring remain deferred.
- Generated package directories and `.kennel_tmp/` are bulk/runtime surfaces.
- Preserve CLI output byte-for-byte unless changing user-facing wording intentionally.

## Release boundary

This page reflects the 0.2.0 technical preview on 2026-08-11. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-kennel-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-kennel-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/main/SKILLS_INDEX.md)
