---
title: "TotalRecall"
custom_url: totalrecall
description: "A local-first ingestion showcase that turns meetings, transcripts, chat exports, Slack threads, and GitHub activity into durable local knowledge."
featured_image: "/assets/images/ecosystem/totalrecall-global-memory.webp"
section: "Showcase"
tags: [Showcase, Knowledge]
order: 440
install_command: "git clone https://github.com/robertdevore/totalrecall.git"
github_url: "https://github.com/robertdevore/totalrecall"
launch_story: "Preserve working context through an explicit provider-to-artifact-to-destination pipeline."
scope_note: "Live providers and destinations require their own credentials and policies; local export sources remain the safest default path."
keywords: "TotalRecall, Kujo ecosystem, local knowledge, ingestion"
seo_title: "TotalRecall — Kujo Ecosystem"
---

## What it does

TotalRecall normalizes artifacts from live providers and local exports, deduplicates them, and writes them to Strata, Markdown, static HTML, or a local JSON index.

## Why it belongs in Kujo

It is a complete example of local-first ingestion with deterministic reruns, checkpoints, structured reports, audit logging, and explicit provider boundaries.

## Operating boundary

Live integrations are opt-in and credentialed. Operators should validate retention, redaction, destination access, and source-system policy before importing sensitive context.

## Learn more

The repository contains setup guides, provider and destination contracts, reliability notes, configuration examples, and verification commands.
