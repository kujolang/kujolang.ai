---
title: "Kujo SiteKit Repository"
custom_url: "kujo-site-kit-workflows"
description: "Use this skill when building, validating, consuming, or maintaining SiteKit design-system artifacts in the `site-kit` repository: tokens, component schemas/templates/CSS, generated `dist/sitekit.css`, optional `dist/sitekit.js`, accessibility checks, browser smoke tests, launch checklist, or Workcell evidence."
featured_image: "/assets/images/ecosystem/skill-kujo-site-kit-workflows.webp"
social_image: "/assets/images/social/kujo-site-kit-workflows.jpg"
section: "Agent Skill"
order: "450"
install_command: "mkdir -p ~/.codex/skills && cp -R skills/kujo-site-kit-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-site-kit-workflows/SKILL.md"
launch_story: "One of 83 focused, repository-backed skills in the Kujo Skills 0.2.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.2.0"
last_updated: "2026-08-11"
keywords: "Kujo SiteKit Repository, Kujo Agent Skill, kujo-site-kit-workflows, repository-backed agent guidance"
seo_title: "Kujo SiteKit Repository — Kujo Agent Skill"
seo_description: "Use this skill when building, validating, consuming, or maintaining SiteKit design-system artifacts in the `site-kit` repository: tokens, component schemas/templates/CSS, generated `dist/sitekit.css`, optional `dist/sitekit.js`, accessibility checks, browser smoke tests, launch checklist, or Workcell evidence."
---

## What it covers

Use this skill when building, validating, consuming, or maintaining SiteKit design-system artifacts in the `site-kit` repository: tokens, component schemas/templates/CSS, generated `dist/sitekit.css`, optional `dist/sitekit.js`, accessibility checks, browser smoke tests, launch checklist, or Workcell evidence.

## Released guidance

- SiteKit is private/internal at `0.1.0`; do not imply npm publication or hosted design-system deployment.
- Browser/accessibility proof is local and representative unless a broader device/browser matrix is actually run; release-candidate scope still requires broader representative visual/accessibility evidence.
- Preserve token, schema, semantic HTML, focus, and reduced-motion contracts.
- Do not hand-edit generated output when source generators own the change.
- Preserve the consumer distribution relationship: `dist/sitekit.css`, optional `dist/sitekit.js`, and sibling `dist/fonts/*`.

## Release boundary

This page reflects the 0.2.0 technical preview on 2026-08-11. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-site-kit-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-site-kit-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/main/SKILLS_INDEX.md)
