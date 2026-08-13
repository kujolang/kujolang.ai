---
title: "Kujo RAG"
custom_url: "kujo-rag-workflows"
description: "Use this skill when setting up, running, extending, testing, or maintaining the Kujo RAG Starter Kit: `kujo run main.kujo --interpreter ingest|query|serve|demo|bootstrap`, local/offline RAG indexes, namespace isolation, parser/chunking/embedding/retrieval changes, API ingest/query endpoints, OpenAPI/SDK parity, release-evaluation gates, large-corpus benchmarks, index maintenance, bootstrap templates, or RAG security/operations docs."
featured_image: "/assets/images/ecosystem/skill-kujo-rag-workflows.webp"
social_image: "/assets/images/social/kujo-rag-workflows.jpg"
section: "Agent Skill"
order: "330"
install_command: "mkdir -p ~/.codex/skills && cp -R skills/kujo-rag-workflows ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-rag-workflows/SKILL.md"
launch_story: "One of 83 focused, repository-backed skills in the Kujo Skills 0.2.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.2.0"
last_updated: "2026-08-11"
keywords: "Kujo RAG, Kujo Agent Skill, kujo-rag-workflows, repository-backed agent guidance"
seo_title: "Kujo RAG — Kujo Agent Skill"
seo_description: "Use this skill when setting up, running, extending, testing, or maintaining the Kujo RAG Starter Kit: `kujo run main.kujo --interpreter ingest|query|serve|demo|bootstrap`, local/offline RAG indexes, namespace isolation, parser/chunking/embedding/retrieval changes, API ingest/query endpoints, OpenAPI/SDK parity, release-evaluation gates, large-corpus benchmarks, index maintenance, bootstrap templates, or RAG security/operations docs."
---

## What it covers

Use this skill when setting up, running, extending, testing, or maintaining the Kujo RAG Starter Kit: `kujo run main.kujo --interpreter ingest|query|serve|demo|bootstrap`, local/offline RAG indexes, namespace isolation, parser/chunking/embedding/retrieval changes, API ingest/query endpoints, OpenAPI/SDK parity, release-evaluation gates, large-corpus benchmarks, index maintenance, bootstrap templates, or RAG security/operations docs.

## Released guidance

- CLI/config: `main.kujo`, `src/cli_args.kujo`, `src/config.kujo`, `src/env_loader.kujo`.
- Ingestion/parsing/chunking: `src/ingestion.kujo`, `src/parsers.kujo`, `src/chunking.kujo`.
- Retrieval/indexing: `src/embeddings.kujo`, `src/vector_store.kujo`, `src/vector_backend.kujo`, `src/retrieval.kujo`, `src/rag_engine.kujo`.
- API/ops: `src/query_api.kujo`, `src/privacy_workflows.kujo`, `src/retention_policy.kujo`, `src/audit_log.kujo`.
- Release/evaluation: `src/release_eval.kujo`, `scripts/run_*.kujo`, `config/*.json`, `openapi/`, `sdk/javascript/`.

## Release boundary

This page reflects the 0.2.0 technical preview on 2026-08-11. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-rag-workflows skill on GitHub](https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-rag-workflows/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/main/SKILLS_INDEX.md)
