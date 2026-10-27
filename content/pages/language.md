---
title: Learn the Kujo language
custom_url: language
description: "Install Kujo, check and run your first program, then explore language and AI runtime examples."
seo_title: "Get started with Kujo | Install and run"
social_image: /assets/images/social/language.jpg
---

## Install the runtime

Kujo is a programming language with a Rust-based runtime. Start with the runtime alone; independent ecosystem packages can come later.

With Node.js 18 or newer, the runtime-only npm package supports macOS x64/arm64, Linux x64/arm64 and Windows x64:

```sh
npm install --global @kujolang/kujo-runtime@1.9.0
kujo --version
```

Expected version: `kujo 1.9.0`. On Windows, use PowerShell or a terminal with Node.js on PATH. Native Windows archives and checksum instructions are in the [official installation guide](https://github.com/kujolang/kujo/blob/v1.9.0/INSTALLATION.md).

For the runtime and core toolset on macOS/Linux:

```sh
curl -fsSL https://kujolang.ai/install.sh | KUJO_RELEASE_VERSION=v1.9.0 bash
export PATH="$HOME/.local/bin:$PATH"
kujo --version
```

This second option also installs separately versioned ecosystem tools. The runtime version does not pin those tool snapshots. Review the official installer and release-manifest options when reproducibility matters.

## Create hello.kujo

Open a text editor and save this code as `hello.kujo`:

```kujo
print("Hello, Kujo!")
```

In the same directory:

```sh
kujo check hello.kujo
kujo run hello.kujo
```

The check validates source without executing it. The run prints:

```text
Hello, Kujo!
```

## Where to go next

- [Browse verified examples](/examples/): functions, collections, async and AI replay.
- [Follow the language tutorial](https://docs.kujolang.ai/learn/).
- [Learn packages with Kennel](https://docs.kujolang.ai/learn/packages/).
- [Read the runtime source](https://github.com/kujolang/kujo/tree/v1.9.0).

## Troubleshooting

If `kujo` is not found, reopen your terminal and check the installer’s PATH instructions. If your operating system or architecture is not listed above, consult the [source-build instructions](https://github.com/kujolang/kujo/blob/v1.9.0/INSTALLATION.md). Use the [issue tracker](https://github.com/kujolang/kujo/issues) with your runtime version, operating system and a minimal sample.
