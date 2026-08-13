---
title: "Kujo Language Implementation"
custom_url: "kujo-language-implementation"
description: "Use this skill when contributing to Kujo's Rust implementation: lexer, parser, AST, diagnostics, compiler, VM, interpreter, module loader, native functions, CLI, LSP, DocGen, JIT, or runtime security boundaries."
excerpt: "Use this skill when contributing to Kujo's Rust implementation."
featured_image: "/assets/images/ecosystem/skill-kujo-language-implementation.webp"
social_image: "/assets/images/social/kujo-language-implementation.jpg"
section: "Agent Skill"
order: "250"
install_command: "mkdir -p ~/.codex/skills && cp -R skills/kujo-language-implementation ~/.codex/skills/"
github_url: "https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-language-implementation/SKILL.md"
launch_story: "One of 83 focused, repository-backed skills in the Kujo Skills 0.2.0 technical preview."
scope_note: "Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries."
version: "0.2.0"
last_updated: "2026-08-11"
keywords: "Kujo Language Implementation, Kujo Agent Skill, kujo-language-implementation, repository-backed agent guidance"
seo_title: "Kujo Language Implementation — Kujo Agent Skill"
seo_description: "Use this skill when contributing to Kujo's Rust implementation: lexer, parser, AST, diagnostics, compiler, VM, interpreter, module loader, native functions, CLI, LSP, DocGen, JIT, or runtime security boundaries."
---

## What it covers

Use this skill when contributing to Kujo's Rust implementation: lexer, parser, AST, diagnostics, compiler, VM, interpreter, module loader, native functions, CLI, LSP, DocGen, JIT, or runtime security boundaries.

## Released guidance

- Lexer/parser/AST/diagnostics: `src/lexer.rs`, `src/parser.rs`, `src/ast.rs`, `src/errors.rs`.
- Compiler/VM/bytecode: `src/compiler.rs`, `src/vm.rs`, `src/bytecode.rs`.
- Interpreter: `src/interpreter/mod.rs`, `environment.rs`, `value.rs`.
- Native functions: `src/interpreter/native_functions/*`.
- Capabilities: `src/interpreter/capabilities.rs`.

## Release boundary

This page reflects the 0.2.0 technical preview on 2026-08-11. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.

## Source

- [Read the complete kujo-language-implementation skill on GitHub](https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-language-implementation/SKILL.md)
- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/main/SKILLS_INDEX.md)
