---
title: "Redact"
custom_url: redact
description: "Deterministic, local-first redaction for Markdown and text files using explicit policies, pattern detectors, transformations, leakage checks, and audit artifacts."
featured_image: "/assets/images/ecosystem/redact-document-sanitization.webp"
section: "Tooling"
tags: [Tool, Privacy]
order: 320
install_command: "git clone https://github.com/kujolang/redact.git"
github_url: "https://github.com/kujolang/redact"
launch_story: "Prepare reviewable sharing copies without sending source material to an AI provider or network service."
scope_note: "Redact does not guarantee complete PII detection or compliance; domain-specific privacy and security review is required before sensitive production use."
keywords: "Redact, Kujo ecosystem, local redaction, privacy, audit"
seo_title: "Redact — Kujo Ecosystem"
---

## What it does

Redact 1.0 scans, sanitizes, and verifies local `.txt` and `.md` files against a strict `redact-policy/v1` contract. Deterministic detectors cover documented email, phone, URL, payment-card, token, date, money, and configured-term patterns, then apply remove, placeholder, role-preserving, generalization, range, or date-generalization strategies.

## Reviewable output

Post-transformation leakage verification checks the result before sharing. Local audit runs record classifications, spans, decisions, hashes, warnings, and output manifests without storing raw matches by default; deterministic non-recursive folder packs support repeatable batch preparation.

## Why it belongs in Kujo

Redact keeps a sensitive-data workflow local, explicit, and inspectable. It makes policy, transformations, residual risk, and evidence available to people and agents without relying on an AI provider or network call.

## Operating boundary

Pattern matching cannot discover every sensitive value, semantic relationship, Unicode confusable, or domain-specific risk. Sanitized files and audit metadata still require human review, protected storage, and organization-specific signoff.

## Learn more

The repository contains the policy contract, detector and transformation boundaries, synthetic examples, CLI and JSON schemas, security guidance, domain-signoff evidence, and verification gates.
