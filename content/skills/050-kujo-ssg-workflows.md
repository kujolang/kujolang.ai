---
title: "Kujo SSG Workflows"
custom_url: "kujo-ssg-workflows"
description: "Use this skill when building, validating, configuring, testing, or maintaining the Kujo SSG static-site showcase: `build.kujo`, starter content, templates, assets, `kujo-ssg.yml`, feeds, sitemap, robots, `llms.txt`, generated `output/`, CLI flags, parallel shard builds, DocGen docs bridge, reusable docs starter, validation scripts, release gates, or `ssg` source/docs changes."
featured_image: "/assets/images/ecosystem/skill-kujo-ssg-workflows.webp"
social_image: "/assets/images/social/kujo-ssg-workflows.jpg"
section: "Agent Skill"
order: "500"
install_command: "mkdir -p ~/.codex/skills && cp -R skills/kujo-ssg-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-ssg-workflows/SKILL.md"
launch_story: "One of 83 focused, repository-backed skills in the Kujo Skills 0.2.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.2.0"
last_updated: "2026-08-11"
keywords: "Kujo SSG Workflows, Kujo Agent Skill, kujo-ssg-workflows, repository-backed agent guidance"
seo_title: "Kujo SSG Workflows — Kujo Agent Skill"
seo_description: "Use this skill when building, validating, configuring, testing, or maintaining the Kujo SSG static-site showcase: `build.kujo`, starter content, templates, assets, `kujo-ssg.yml`, feeds, sitemap, robots, `llms.txt`, generated `output/`, CLI flags, parallel shard builds, DocGen docs bridge, reusable docs starter, validation scripts, release gates, or `ssg` source/docs changes."
---

## What it covers

Use this skill when building, validating, configuring, testing, or maintaining the Kujo SSG static-site showcase: `build.kujo`, starter content, templates, assets, `kujo-ssg.yml`, feeds, sitemap, robots, `llms.txt`, generated `output/`, CLI flags, parallel shard builds, DocGen docs bridge, reusable docs starter, validation scripts, release gates, or `ssg` source/docs changes.

## Released guidance

- Generated site output goes under `output/`; do not hand-edit it.
- `build.kujo`, `kujo-ssg.yml`, `templates/`, and `content/` are canonical implementation/example surfaces.
- Validation checks generated routes, feeds, metadata, docs contracts, and release contract behavior.
- Config discovery prefers `kujo-ssg.yml`, then `kujo-ssg.yaml`, then `kujo-ssg.json`; CLI flags override config values.
- Draft content is excluded by default. Use `--drafts` only for preview/staging builds, and `--no-aliases` to skip flat `.html` redirect aliases for lower large-site write I/O.

## Release boundary

This page reflects the 0.2.0 technical preview on 2026-08-11. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-ssg-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-ssg-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/main/SKILLS_INDEX.md)
