---
title: "GalleyPack"
custom_url: galleypack
description: "A Kujo-native production packager that binds editorial artifacts, lineage, evidence, reviews, and package versions to exact checksums."
featured_image: "/assets/images/ecosystem/galleypack-production-package.webp"
section: "Tooling"
tags: [Tool, Publishing]
order: 500
install_command: "git clone https://github.com/kujolang/galleypack.git"
github_url: "https://github.com/kujolang/galleypack"
launch_story: "Freeze reproducible editorial packages whose artifacts, lineage, evidence, reviews, and versions can be verified offline."
scope_note: "GalleyPack packages and verifies exact artifacts; it does not modify source work, interpret review as approval, or publish."
keywords: "GalleyPack, Kujo ecosystem, editorial packaging, artifact lineage, checksum verification, production workflow"
seo_title: "GalleyPack — Kujo Ecosystem"
---

## What it does

GalleyPack replaces mutable “latest” folders with deterministic production records. It binds editorial artifacts, source and derivative relationships, upstream evidence, completed reviews, manifests, and package versions to exact SHA-256 checksums.

## Reproducible packages

Operators can build and freeze package versions, compare claims and artifacts, and re-hash every bound file to detect missing content or byte drift. Immutable records, atomic writes, locks, bounded queries, and fail-closed validation keep the package evidence trustworthy.

## Why it belongs in Kujo

Publishing handoffs need an exact answer to “which version?” GalleyPack gives production editors, agents, and downstream systems the same verifiable bundle without requiring a hosted service or sibling tool.

## Operating boundary

Packaging is not publication or approval. GalleyPack preserves review references and file identity without editing source artifacts, filling missing evidence, or assigning authority to a package.

## Learn more

The repository documents the artifact and package contracts, lineage model, comparison commands, security controls, and full validation gate.
