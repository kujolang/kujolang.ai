---
title: "Kujo video styles"
custom_url: "kujo-video-styles"
description: "Create Kujo launch and release videos in ten reusable styles, from kinetic drops and polished micro interactions to changelog films, product proof reels, PR explainers, integrations and cinematic launches. Use to choose a style or automate a family of HyperFrames videos from source evidence."
excerpt: "Create Kujo launch and release videos in ten reusable styles, from kinetic drops and polished micro interactions to changelog films, product proof reels, PR…"
featured_image: "/assets/images/ecosystem/skills-agent-guidance-library.webp"
social_image: "/assets/images/social/kujo-video-styles.jpg"
section: "Agent Skill"
order: "660"
install_command: "git clone --branch v0.7.0 --depth 1 https://github.com/kujolang/kujo-skills.git && mkdir -p ~/.codex/skills && cp -R kujo-skills/skills/kujo-video-styles ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/v0.7.0/skills/kujo-video-styles/SKILL.md"
launch_story: "One of 135 focused, repository-backed skills in the Kujo Skills 0.7.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.7.0"
last_updated: "2026-09-08"
keywords: "Kujo video styles, Kujo Agent Skill, kujo-video-styles, repository-backed agent guidance"
seo_title: "Kujo video styles — Kujo Agent Skill"
seo_description: "Create Kujo launch and release videos in ten reusable styles, from kinetic drops and polished micro interactions to changelog films, product proof reels, PR explainers, integrations and cinematic launches. Use to choose a style or automate a family of HyperFrames videos from source evidence."
---

## What it covers

Create Kujo launch and release videos in ten reusable styles, from kinetic drops and polished micro interactions to changelog films, product proof reels, PR explainers, integrations and cinematic launches. Use to choose a style or automate a family of HyperFrames videos from source evidence.

Run the install command from a new working directory. If you already have the released checkout, copy the complete skill folder from it instead of cloning again.

## Released guidance

The released skill file defines the authoritative workflow, boundaries, sources, and validation guidance.

## Make more than release videos

Choose from ten HyperFrames styles for product demos, launches, feature reveals, integrations, engineering explainers, editorial arguments, and release announcements. Give your agent source material, choose a style, and refine an editable composition before rendering.

```text
Use $kujo-video-styles to make a 25-second feature-reveal for [feature]
from [source]. Show the real before and after. Use an American ElevenLabs
voice, and verify the voice before generation.
```

The styles are `cinematic-hero-launch`, `apple-style-micro-launch`, `release-notes-changelog`, `real-product-proof-reel`, `editorial-thesis-launch`, `feature-reveal`, `integration-partnership-launch`, `engineering-pr-to-video`, `short-product-launch`, and `kinetic-release-drop`.

Each has an ElevenLabs narrator default. You can choose another name or voice ID, or make a silent video. The style guides the story; native HyperFrames skills handle the composition, preview, and render. Provider access and generation authorization are separate from installing a skill.

[See every style, narrator, installation step, and example prompt in the video skills guide](https://docs.kujolang.ai/collections/video-skills/).

For the fixed 15-second monochrome announcement, choose [Kujo Release Video](/ecosystem/skills/kujo-release-video/). For a full production team, use [Kujo VideoOps](/ecosystem/skills/kujo-videoops-workflows/).

## Release boundary

This page reflects the 0.7.0 technical preview on 2026-09-08. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-video-styles skill on GitHub](https://github.com/kujolang/kujo-skills/blob/v0.7.0/skills/kujo-video-styles/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/v0.7.0/SKILLS_INDEX.md)
