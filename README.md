# Kujolang.ai

The official website for the [Kujo programming language](https://github.com/kujolang/kujo) and its local-first tooling ecosystem.

This site is built with the Kujo SSG and the Kujo SiteKit design system. Markdown content is the editable source of truth; generated files are written to `output/` and should not be edited by hand.

Current release: **v1.2.6**

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

The production build disables flat `.html` aliases. GitHub Pages can therefore
redirect extensionless nested paths to the canonical trailing-slash routes
instead of serving duplicate HTML at both URL forms.

## Installer URL

The one-line installer is published from the site root:

```bash
curl -fsSL https://kujolang.ai/install.sh | bash
```

[`public/install.sh`](public/install.sh) is the published copy of Kujo's
canonical [`install.sh`](https://github.com/kujolang/kujo/blob/main/install.sh).
When the installer changes, copy the reviewed canonical script here in the same
change so the website artifact remains self-contained and deployable.

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
- `content/skills/` mirrors the released `kujo-skills` catalog under `/ecosystem/skills/`.
- `content/workflows/` mirrors the released `kujo-workflows` catalog under `/ecosystem/workflows/`.
- `content/posts/` contains Writing articles.
- `templates/` contains shared SiteKit markup and page templates.
- `assets/css/style.css` contains site-specific, token-based composition styles.
- `assets/js/site.js` contains the dither hero and copy controls.

The ecosystem item template reads `install_command`, `github_url`, `launch_story`, and `scope_note` from frontmatter so every project page keeps the same structure.

## Social sharing cards

Every primary page and ecosystem tool has a dedicated 1200×630 JPEG under
`assets/images/social/`. The SSG writes absolute Open Graph and X/Twitter image
URLs plus image type, dimensions, and accessible alt text into each page head.

The cards are reproducible with [Howl](https://github.com/kujolang/howl). The
editable source is `howl-social.json`: each card supplies its route title,
short description, page type, destination URL, matching hero background, and
the local Departure Mono font. Howl embeds those assets into a self-contained
SVG, then Sharp produces the network-ready JPEG.

```bash
npm install
npm run social:cards
kujo run ./build.kujo -- --site-url https://kujolang.ai
npm run social:verify
```

To add a page, tool, skill, workflow, or Writing post, add a card whose `id` matches the route
slug, choose its background image, and run the command again. Set `HOWL_BIN` if
the Howl launcher is not at the default sibling-repository path.

The verification command checks that every generated shareable route has one
manifest card, a matching 1200×630 JPEG copied into the built site, exact
Open Graph and X/Twitter image metadata, accessible alt text, and matching
JSON-LD image data.

## Favicons and device icons

The browser tab, desktop shortcut, pinned-tab, Apple touch, Android, maskable,
and Windows tile icons are generated from the canonical Kujo K logomark at
`assets/images/kujo-logomark.svg`:

```bash
npm install
npm run icons:build
```

Commit the generated files under `assets/icons/`. The SSG copies the complete
suite and `site.webmanifest` to stable root URLs during every build.

## Release policy

Releases are tagged from a clean `main` branch after the production build and verification commands pass. User-facing changes are recorded in [CHANGELOG.md](CHANGELOG.md), and GitHub releases use semantic version tags such as `v1.0.0`.

## Deployment

Pushes to `main` deploy the verified `output/` artifact through GitHub Pages using [`.github/workflows/pages.yml`](.github/workflows/pages.yml). The workflow builds a pinned Kujo runtime from source, runs the production SSG and validation contracts, and publishes only the generated static site.

The production custom domain is declared in [`CNAME`](CNAME). DNS is managed separately and should point the apex `kujolang.ai` records to GitHub Pages while `www.kujolang.ai` aliases `kujolang.github.io`.

## Included licenses

The vendored Kujo SSG and SiteKit assets retain their upstream terms in [SSG-LICENSE.txt](SSG-LICENSE.txt) and [SITEKIT-LICENSE.txt](SITEKIT-LICENSE.txt). The Departure Mono font license is stored beside the font assets.
