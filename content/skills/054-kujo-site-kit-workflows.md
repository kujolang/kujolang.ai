---
title: "Kujo SiteKit Repository"
custom_url: "kujo-site-kit-workflows"
description: "Use this skill when building, validating, consuming, or maintaining SiteKit 1.0 design-system artifacts in the `site-kit` repository: tokens, component schemas/templates/CSS, generated `dist/sitekit.css`, `dist/sitekit.js`, theme behavior, Tabler icon assets, accessibility checks, browser/release smoke tests, or Workcell evidence."
excerpt: "Use this skill when building, validating, consuming, or maintaining SiteKit 1.0 design-system artifacts in the `site-kit` repository."
featured_image: "/assets/images/ecosystem/skill-kujo-site-kit-workflows.webp"
social_image: "/assets/images/social/kujo-site-kit-workflows.jpg"
section: "Agent Skill"
order: "540"
install_command: "git clone --branch v0.7.1 --depth 1 https://github.com/kujolang/kujo-skills.git && mkdir -p ~/.codex/skills && cp -R kujo-skills/skills/kujo-site-kit-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/v0.7.1/skills/kujo-site-kit-workflows/SKILL.md"
launch_story: "One of 135 focused, repository-backed skills in the Kujo Skills 0.7.1 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.7.1"
last_updated: "2026-10-22"
keywords: "Kujo SiteKit Repository, Kujo Agent Skill, kujo-site-kit-workflows, repository-backed agent guidance"
seo_title: "Kujo SiteKit Repository — Kujo Agent Skill"
seo_description: "Use this skill when building, validating, consuming, or maintaining SiteKit 1.0 design-system artifacts in the `site-kit` repository: tokens, component schemas/templates/CSS, generated `dist/sitekit.css`, `dist/sitekit.js`, theme behavior, Tabler icon assets, accessibility checks, browser/release smoke tests, or Workcell evidence."
---

## What it covers

Use this skill when building, validating, consuming, or maintaining SiteKit 1.0 design-system artifacts in the `site-kit` repository: tokens, component schemas/templates/CSS, generated `dist/sitekit.css`, `dist/sitekit.js`, theme behavior, Tabler icon assets, accessibility checks, browser/release smoke tests, or Workcell evidence.

Run the install command from a new working directory. If you already have the released checkout, copy the complete skill folder from it instead of cloning again.

## Released guidance

- SiteKit is stable at `1.0.0`, but still `private: true`; it ships as a source/dist release and not as an npm publication or hosted design-system deployment.
- The stable v1 contract covers tokens, themes, schemas, semantic templates, generated CSS/JS, layout recipes, documented progressive hooks, and representative static consumers.
- Browser/accessibility proof is representative unless the current Playwright Chromium, Firefox, and WebKit desktop/tablet/mobile release matrix is actually run.
- Preserve token, schema, semantic HTML, focus, and reduced-motion contracts.
- Do not hand-edit generated output when source generators own the change.

## Release boundary

This page reflects the 0.7.1 technical preview on 2026-10-22. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-site-kit-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/v0.7.1/skills/kujo-site-kit-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/v0.7.1/SKILLS_INDEX.md)
