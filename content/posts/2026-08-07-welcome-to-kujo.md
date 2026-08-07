---
title: Welcome to Kujo
author: 1
date: 2026-08-07
description: A first orientation to the Kujo language, its local-first posture, and the ecosystem growing around it.
keywords: Kujo programming language, AI-native software, local-first automation
seo_title: Welcome to the Kujo Programming Language
tags: [Launch, Language]
---

## A language for the work around AI

Kujo is a programming language for AI-native software, built in Rust. It is designed for local-first automation, agentic workflows, and application scripting where deterministic behavior, strong native capabilities, and practical ergonomics matter.

The phrase *AI-native* is not a promise that every program needs a model call. It means the language and its tools account for the operational realities that appear when software collaborates with agents: structured inputs, tool boundaries, replayable interactions, approvals, context budgets, durable artifacts, and machine-readable outcomes.

## Start with a normal program

```kujo
func greet(name) {
    print("Hello, " + name + "!")
}

greet("Kujo")
```

Run it with `kujo run hello.kujo`. From there you can use modules, package manifests, filesystem and process APIs, networking, databases, async work, cryptography, and the AI-oriented runtime helpers when the job calls for them.

## Explore by problem, not by product count

The ecosystem is intentionally composable. Start with the language. Add Kennel when you need deterministic package workflows. Reach for Spec and Eval when work needs an explicit contract and acceptance gates. Use Scent, Scout, PackWrite, or the proof tools when an agent workflow needs stronger context and handoff discipline.

That is the path this site will document: concrete problems, focused tools, accurate boundaries, and examples you can inspect.
