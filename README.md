# Kujolang.ai

The official website for the [Kujo programming language](https://github.com/kujolang/kujo) and its local-first tooling ecosystem.

This site is built with the Kujo SSG and the Kujo SiteKit design system. Markdown content is the editable source of truth; generated files are written to `output/` and should not be edited by hand.

Current release: **v1.0.0**

- Website: [kujolang.ai](https://kujolang.ai)
- Documentation: [docs.kujolang.ai](https://docs.kujolang.ai)
- Community: [Discord](https://discord.gg/RqDgyb3BX)

## Build

Install [Kujo](https://github.com/kujolang/kujo), then run:

```bash
kujo run ./build.kujo -- --site-url https://kujolang.ai
bash scripts/validate-generated-output.sh output
```

Build, validate, and start Kujo's local HTTP server in one command:

```bash
bash scripts/dev.sh
```

Then open [http://127.0.0.1:8080](http://127.0.0.1:8080). Pass a different port when needed:

```bash
bash scripts/dev.sh 4178
```

The equivalent manual preview command is `kujo serve output --host 127.0.0.1 --port 8080`. This repository does not require a third-party hosting runtime.

## Verification

Run the production build and both site contracts before publishing:

```bash
kujo run ./build.kujo -- --site-url https://kujolang.ai
bash scripts/verify-site-contract.sh output
bash scripts/validate-generated-output.sh output
node --check assets/js/site.js
npm audit --omit=dev
```

## Content model

- `content/pages/` contains the Ethos and Contact pages.
- `content/ecosystem/` contains one editable page per Kujo project or showcase.
- `content/posts/` contains Writing articles.
- `templates/` contains shared SiteKit markup and page templates.
- `assets/css/style.css` contains site-specific, token-based composition styles.
- `assets/js/site.js` contains the dither hero and copy controls.

The ecosystem item template reads `install_command`, `github_url`, `launch_story`, and `scope_note` from frontmatter so every project page keeps the same structure.

## Release policy

Releases are tagged from a clean `main` branch after the production build and verification commands pass. User-facing changes are recorded in [CHANGELOG.md](CHANGELOG.md), and GitHub releases use semantic version tags such as `v1.0.0`.

## Included licenses

The vendored Kujo SSG and SiteKit assets retain their upstream terms in [SSG-LICENSE.txt](SSG-LICENSE.txt) and [SITEKIT-LICENSE.txt](SITEKIT-LICENSE.txt). The Departure Mono font license is stored beside the font assets.
