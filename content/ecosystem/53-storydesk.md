---
title: "StoryDesk"
custom_url: storydesk
description: "A local-first editorial control desk for ideas, campaigns, commissions, assignments, dependencies, packets, handoffs, and human review queues."
featured_image: "/assets/images/ecosystem/storydesk-editorial-control.webp"
section: "Tooling"
tags: [Tool, Publishing]
order: 530
install_command: "git clone https://github.com/kujolang/storydesk.git"
github_url: "https://github.com/kujolang/storydesk"
launch_story: "Operate the editorial queue from idea and commission through assignment, handoff, packet creation, and human review."
scope_note: "StoryDesk 0.1.0 coordinates local editorial work; it does not grant publication authority or claim hosted identity and distributed multi-host coordination."
keywords: "StoryDesk, Kujo ecosystem, editorial operations, commissions, assignments, publishing workflow, human review"
seo_title: "StoryDesk — Kujo Ecosystem"
---

## What it does

StoryDesk is the editorial control surface for ideas, campaigns, commissions, assignments, dependencies, status, blockers, handoffs, daily or ranged packets, and work awaiting human review. Every mutation requires an actor and becomes immutable, append-only operational evidence.

## Durable editorial operations

Atomic writes, per-record locks, bounded pagination, deterministic fixtures, explicit schemas, and structured failures support serious standalone workflows. Operators can move work through a clear queue while retaining ownership, dependency, and next-action history.

## Why it belongs in Kujo

Publishing agents need coordination without hidden autonomy. StoryDesk makes the assignment graph and human review boundary inspectable, giving the house a shared desk instead of a collection of disconnected prompts and transient chats.

## Operating boundary

StoryDesk records and coordinates work. It does not approve content, publish artifacts, provide hostile-code isolation, or claim authority beyond the explicit local records and actor identities supplied by the operator.

## Learn more

The repository documents the 0.1.0 editorial commands, state model, schemas, security posture, deterministic fixtures, and production validation gate.
