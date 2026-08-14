---
title: "VersionSeal"
custom_url: versionseal
description: "A local-first approval ledger for exact-version human authorization, explicit scope, revocation, and checksum-backed verification."
featured_image: "/assets/images/ecosystem/versionseal-version-approval.webp"
section: "Tooling"
tags: [Tool, Publishing]
order: 540
install_command: "git clone https://github.com/kujolang/versionseal.git"
github_url: "https://github.com/kujolang/versionseal"
launch_story: "Bind a named human approval to an exact package version and verify that neither scope nor bytes have drifted."
scope_note: "VersionSeal 0.1.0 records explicit local approvals and revocations; checksum integrity does not prove identity, custody, legal authority, or external publication."
keywords: "VersionSeal, Kujo ecosystem, human approval, exact version, revocation, checksum verification, publishing authority"
seo_title: "VersionSeal — Kujo Ecosystem"
---

## What it does

VersionSeal records human approval for an exact version, package checksum, authority scope, approver, and timestamp. Later verification fails when the package drifts, the approval is revoked, or the requested effect falls outside the recorded scope.

## Exact approval evidence

Immutable records, append-only history, atomic writes, locks, bounded inputs, deterministic fixtures, and structured errors make approval evidence portable and inspectable. Revocation remains a first-class event rather than an edit to history.

## Why it belongs in Kujo

“Approved” is unsafe when nobody can tell which bytes or action it covered. VersionSeal gives GalleyPack and PressWire a narrow, verifiable authorization contract while keeping the human decision explicit.

## Operating boundary

A checksum proves byte identity, not human identity, custody, legal rights, or publication success. VersionSeal records supplied authority; it does not create, broaden, or independently authenticate it.

## Learn more

The repository documents the 0.1.0 approval, revocation, validation, export, security, and drift-detection contracts.
