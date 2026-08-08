---
title: "Ward"
custom_url: ward
description: "A local Dependabot security command center for collecting alerts, planning remediation, preparing safe fixes, verifying changes, and generating reports."
featured_image: "/assets/images/ecosystem/ward-security-command-center.webp"
section: "Tooling"
tags: [Tool, Security]
order: 290
install_command: "git clone https://github.com/robertdevore/ward.git"
github_url: "https://github.com/robertdevore/ward"
launch_story: "Turn dependency alerts across many repositories into a local, reviewable remediation workflow."
scope_note: "Ward is read-only by default; code changes require explicit apply mode, and operators remain responsible for credentials and review."
keywords: "Ward, Kujo ecosystem, Dependabot, dependency security"
seo_title: "Ward — Kujo Ecosystem"
---

## What it does

Ward collects and normalizes Dependabot alerts, applies deterministic planning policy, prepares ecosystem-specific remediation commands, and produces Markdown, JSON, and static dashboard reports.

## Why it belongs in Kujo

It demonstrates how security operations can stay local, explicit, and inspectable across a portfolio of repositories.

## Operating boundary

Ward never auto-merges, dismisses alerts, or pushes protected branches. Applying changes is opt-in and every proposed fix still requires repository-aware review.

## Learn more

The repository documents authentication, supported ecosystems, policy configuration, commands, tests, and known limitations.
