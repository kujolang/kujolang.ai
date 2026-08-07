---
title: Ethos
custom_url: ethos
nav_title: Ethos
template: ethos
order: 10
description: "The working principles behind Kujo: local-first systems, explicit authority, inspectable artifacts, and tools that help people stay in control."
keywords: Kujo ethos, local-first, agentic software, programming language principles
seo_title: The Kujo Ethos
---

## Software should make its behavior legible

Kujo begins with a simple expectation: people should be able to understand what their software is doing, what it can touch, and what evidence it leaves behind. The language and its ecosystem favor visible files, explicit commands, durable artifacts, and contracts that can be inspected without a hosted control plane.

That does not mean every system must be small. It means complexity should be named and placed where a builder can reason about it.

## Local-first is an operating posture

Local-first does not mean isolated or anti-network. It means useful work should remain possible on infrastructure you control, with remote providers treated as explicit integrations rather than invisible assumptions.

- Source should stay available and editable.
- Offline and replay-backed paths should exist where they materially improve confidence.
- Hosted dependencies should be chosen deliberately.
- Data movement should be visible at the boundary where it occurs.

## Authority should be explicit

Automation is most useful when its authority is clear. Kujo separates trusted execution from capability-minimal execution and makes sensitive host effects visible: filesystem access, process execution, outbound network calls, databases, and AI egress.

The goal is not to pretend that a general-purpose language is a sandbox. The goal is to give operators direct controls and accurate language for the risks they are accepting.

## Determinism earns trust

Repeatable package locks, stable machine-readable outputs, replay fixtures, evaluation gates, and deterministic generation all serve the same purpose: another person or agent should be able to understand how a result was produced and check it again.

> A useful artifact is not only the final answer. It is also the context, decisions, commands, boundaries, and proof that make the answer reviewable.

## Agents are collaborators, not an excuse to remove control

Kujo is built for agentic workflows, but the ecosystem is deliberately proof-oriented. Tools scope work, package context, run bounded workflows, collect evidence, summarize diffs, and preserve handoffs. Approvals and policy checks belong at meaningful boundaries.

The human role may shift from typing every line to shaping intent, reviewing proof, and deciding what happens next. It does not disappear.

## Composable tools beat a mandatory platform

The Kujo ecosystem is a collection of focused projects. A team can use Kujo by itself, add a deterministic evaluator, adopt a context packager, or assemble a full local operating loop. Projects should expose clear contracts and avoid pretending that every user needs the entire stack.

This creates a practical standard for new tools:

1. Solve a specific job.
2. Keep inputs and outputs understandable.
3. State safety and maturity boundaries plainly.
4. Produce artifacts that can survive a handoff.
5. Compose with the rest of the ecosystem without becoming dependent on all of it.

## Clarity, context, and control

These three words are the shortest expression of the Kujo ethos.

**Clarity** means understandable behavior, direct language, and interfaces that show what matters.

**Context** means preserving the source material, constraints, provenance, and evidence needed to make good decisions.

**Control** means explicit authority, local ownership, reversible workflows, and a clear place for human judgment.

The details will evolve. These principles are the test that future details should pass.
