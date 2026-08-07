# Kujolang.ai

The public website for the Kujo programming language and its local-first tooling ecosystem.

This site is built with the Kujo SSG and the Kujo SiteKit design system. Markdown content is the editable source of truth; generated files are written to `output/` and should not be edited by hand.

## Build

```bash
kujo run ./build.kujo -- --site-url https://kujolang.ai
bash scripts/validate-generated-output.sh output
```

Preview the generated site locally:

```bash
kujo serve output --port 8080
```

Create the static Sites deployment bundle after a validated SSG build:

```bash
bash scripts/build-sites.sh https://kujolang.ai
```

## Content model

- `content/pages/` contains the Ethos and Contact pages.
- `content/ecosystem/` contains one editable page per Kujo project or showcase.
- `content/posts/` contains Writing articles.
- `templates/` contains shared SiteKit markup and page templates.
- `assets/css/style.css` contains site-specific, token-based composition styles.
- `assets/js/site.js` contains the dither hero and copy controls.

The ecosystem item template reads `install_command`, `github_url`, `launch_story`, and `scope_note` from frontmatter so every project page keeps the same structure.
