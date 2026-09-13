---
title: "Kennel"
custom_url: kennel
description: "Deterministic Kujo package and dependency workflows with manifests, lockfiles, source policy, trust policy, indexes, and mirrors."
featured_image: "/assets/images/ecosystem/kennel-package-system.webp"
section: "Primitives"
tags: [Core, Packages]
order: 20
install_command: "curl -fsSL https://kennel.kujolang.ai/install.sh -o /tmp/kennel-install.sh && sh /tmp/kennel-install.sh"
github_url: "https://github.com/kujolang/kennel"
launch_story: "The package foundation for reproducible local and static dependency workflows."
scope_note: "The official first-party static registry is live at https://kennel.kujolang.ai. Kennel 1.1.0 provides native bootstrap and global tool commands on macOS/Linux with Kujo 1.4.0 or newer. Official package installation requires no Git or Python. Accounts and third-party publishing are future work."
keywords: "Kennel, Kujo ecosystem, Core, Packages"
seo_title: "Kennel — Kujo Ecosystem"
version: "1.1.0"
latest_release_url: "https://github.com/kujolang/kennel/releases/tag/v1.1.0"
release_status: "Version identifies the published Kennel release. Install Kujo 1.4.0 or newer first; the public installer selects the latest compatible stable Kennel package."
last_updated: "2026-09-13"
---

## What it does

Deterministic Kujo package and dependency workflows with manifests, lockfiles, source policy, trust policy, indexes, and mirrors.

## Why it belongs in Kujo

The package foundation for reproducible local and static dependency workflows.

## Operating boundary

The official first-party static registry is live at https://kennel.kujolang.ai. Kennel 1.1.0 provides native bootstrap and global tool commands on macOS/Linux with Kujo 1.4.0 or newer. Official package installation requires no Git or Python. Accounts and third-party publishing are future work.

## Learn more

The repository is the source of truth for current setup, commands, examples, security notes, compatibility, and verification evidence.

## Install packages and tools

Install [Kujo 1.4.0 or newer](https://docs.kujolang.ai/install/) first, then use the installer above. Open a new terminal or load the generated environment:

```sh
. "$HOME/.kennel/env"
kennel add changebucket
kennel tool install shipcheck
shipcheck --help
```

Use `kennel self update` to update Kennel and `kennel tool update` to update unpinned global tools. The registry reconciles actual GitHub Releases automatically; scheduled runs may be delayed by GitHub. Browse packages and exact artifact metadata at [kennel.kujolang.ai](https://kennel.kujolang.ai/).
