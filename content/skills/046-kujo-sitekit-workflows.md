---
title: "Kujo SiteKit"
custom_url: "kujo-sitekit-workflows"
description: "Use this skill when building, validating, consuming, or maintaining SiteKit design-system artifacts: tokens, component schemas/templates/CSS, layout recipes, generated `dist/sitekit.css`, optional `dist/sitekit.js`, `DESIGN.md`, accessibility/semantic standards, examples, snapshots, smoke tests, or SiteKit source/docs changes."
excerpt: "Use this skill when building, validating, consuming, or maintaining SiteKit design-system artifacts."
featured_image: "/assets/images/ecosystem/skill-kujo-sitekit-workflows.webp"
social_image: "/assets/images/social/kujo-sitekit-workflows.jpg"
section: "Agent Skill"
order: "460"
install_command: "mkdir -p ~/.codex/skills && cp -R skills/kujo-sitekit-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-sitekit-workflows/SKILL.md"
launch_story: "One of 83 focused, repository-backed skills in the Kujo Skills 0.2.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.2.0"
last_updated: "2026-08-11"
keywords: "Kujo SiteKit, Kujo Agent Skill, kujo-sitekit-workflows, repository-backed agent guidance"
seo_title: "Kujo SiteKit — Kujo Agent Skill"
seo_description: "Use this skill when building, validating, consuming, or maintaining SiteKit design-system artifacts: tokens, component schemas/templates/CSS, layout recipes, generated `dist/sitekit.css`, optional `dist/sitekit.js`, `DESIGN.md`, accessibility/semantic standards, examples, snapshots, smoke tests, or SiteKit source/docs changes."
---

## What it covers

Use this skill when building, validating, consuming, or maintaining SiteKit design-system artifacts: tokens, component schemas/templates/CSS, layout recipes, generated `dist/sitekit.css`, optional `dist/sitekit.js`, `DESIGN.md`, accessibility/semantic standards, examples, snapshots, smoke tests, or SiteKit source/docs changes.

## Released guidance

- The package is private/internal at `0.1.0`; consumers copy or vendor `dist/`, or use the repo as a local dependency. Do not imply npm publication.
- `npm run build` regenerates reset, primitive and semantic tokens, theme overrides, base styles, components, utilities, `dist/sitekit.css`, optional behavior JS, and font assets.
- `dist/sitekit.js` is optional progressive behavior for documented hooks: dropdowns, popovers, drawers, dialogs, tooltips, theme controls, and focus behavior.
- `css/generated/*` is useful for source inspection; consumers should not manually assemble generated CSS.
- Browser/accessibility testing is a separate pre-launch requirement for representative consuming layouts; package release checks alone are not proof for every site.

## Release boundary

This page reflects the 0.2.0 technical preview on 2026-08-11. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-sitekit-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-sitekit-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/main/SKILLS_INDEX.md)
