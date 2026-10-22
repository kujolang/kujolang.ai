---
title: "Kujo SiteKit"
custom_url: "kujo-sitekit-workflows"
description: "Use this skill when building, validating, consuming, or maintaining SiteKit 1.0 design-system artifacts: tokens, component schemas/templates/CSS, layout recipes, generated `dist/sitekit.css`, `dist/sitekit.js`, `DESIGN.md`, accessibility/semantic standards, examples, snapshots, smoke tests, release checks, or SiteKit source/docs changes."
excerpt: "Use this skill when building, validating, consuming, or maintaining SiteKit 1.0 design-system artifacts."
featured_image: "/assets/images/ecosystem/skill-kujo-sitekit-workflows.webp"
social_image: "/assets/images/social/kujo-sitekit-workflows.jpg"
section: "Agent Skill"
order: "550"
install_command: "git clone --branch v0.7.1 --depth 1 https://github.com/kujolang/kujo-skills.git && mkdir -p ~/.codex/skills && cp -R kujo-skills/skills/kujo-sitekit-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/v0.7.1/skills/kujo-sitekit-workflows/SKILL.md"
launch_story: "One of 135 focused, repository-backed skills in the Kujo Skills 0.7.1 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.7.1"
last_updated: "2026-10-22"
keywords: "Kujo SiteKit, Kujo Agent Skill, kujo-sitekit-workflows, repository-backed agent guidance"
seo_title: "Kujo SiteKit — Kujo Agent Skill"
seo_description: "Use this skill when building, validating, consuming, or maintaining SiteKit 1.0 design-system artifacts: tokens, component schemas/templates/CSS, layout recipes, generated `dist/sitekit.css`, `dist/sitekit.js`, `DESIGN.md`, accessibility/semantic standards, examples, snapshots, smoke tests, release checks, or SiteKit source/docs changes."
---

## What it covers

Use this skill when building, validating, consuming, or maintaining SiteKit 1.0 design-system artifacts: tokens, component schemas/templates/CSS, layout recipes, generated `dist/sitekit.css`, `dist/sitekit.js`, `DESIGN.md`, accessibility/semantic standards, examples, snapshots, smoke tests, release checks, or SiteKit source/docs changes.

Run the install command from a new working directory. If you already have the released checkout, copy the complete skill folder from it instead of cloning again.

## Released guidance

- The package is stable at `1.0.0` but remains `private: true`; consumers copy or vendor `dist/`, or use the repo as a local dependency. Do not imply npm publication.
- `npm run build` regenerates reset, primitive and semantic tokens, theme overrides, base styles, components, utilities, `dist/sitekit.css`, optional behavior JS, and font assets.
- `dist/sitekit.js` is optional progressive behavior for documented hooks: dropdowns, popovers, drawers, dialogs, tooltips, theme controls, mobile navigation, native scrollbar theming, and focus behavior.
- `css/generated/*` is useful for source inspection; consumers should not manually assemble generated CSS.
- Browser/accessibility testing is representative unless the current Playwright Chromium, Firefox, and WebKit desktop/tablet/mobile release matrix is actually run; package release checks are not proof for every site.

## Release boundary

This page reflects the 0.7.1 technical preview on 2026-10-22. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-sitekit-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/v0.7.1/skills/kujo-sitekit-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/v0.7.1/SKILLS_INDEX.md)
