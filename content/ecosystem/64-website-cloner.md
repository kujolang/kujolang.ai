---
title: "Website Cloner"
custom_url: "website-cloner"
description: "Turn a public WordPress site into an editable static website on your own computer. Keep the design, review the result, and take the files with you."
featured_image: "/assets/images/ecosystem/website-cloner-page-duplication.webp"
social_image: "/assets/images/social/website-cloner.jpg"
section: "Showcase"
tags: ["Showcase", "WordPress", "Publishing", "Static sites"]
order: 630
install_command: "curl -fsSL https://raw.githubusercontent.com/kujolang/website-cloner/main/install.sh | bash"
github_url: "https://github.com/kujolang/website-cloner"
launch_story: "Move a client site off WordPress, make a local working copy, or start a migration with content and templates you can maintain. No AI or API key is required."
scope_note: "Version 0.1.1 is a local, single-user public preview. The installer handles dependencies on macOS and Linux. Review every export: checkout, accounts, form delivery, and other server features need their own services."
version: "0.1.1"
latest_release_url: "https://github.com/kujolang/website-cloner/releases/tag/v0.1.1"
release_status: "Public preview. macOS installation and release checks verified; clean Linux installation acceptance remains open."
last_updated: "2026-11-09"
keywords: "Website Cloner, WordPress to static site, Kujo SSG, local website migration, editable Markdown"
seo_title: "Website Cloner — Move WordPress to an Editable Static Site"
seo_description: "Clone a public WordPress site locally with no AI required. Export Markdown, shared templates and assets, then review and publish your Kujo static site."
---

## See the cloner in use

Watch the local app capture a site, then compare a live homepage with its clone as both scroll from top to bottom. The walkthrough also shows editable project files and publishing options.

WEBSITE_CLONER_DEMO

## Three steps to a local clone

1. **Install.** Download the [release archive](https://github.com/kujolang/website-cloner/releases/tag/v0.1.1). On macOS, double-click `Install.command`. On Linux, run `bash install.sh`. You can also use the terminal command above. Setup installs the required runtime and browser dependencies, then opens the app.
2. **Clone.** Paste a public WordPress URL and click **Clone**. Preserve Source Without AI is the default. The builder discovers pages, downloads assets, creates the project, and runs its checks. Set a page limit when you want a sample first.
3. **Review and keep it.** Open the local preview, inspect the reports, and download the ZIP. Edit the source files or connect your own GitHub Pages or Cloudflare Pages account to publish.

You do not need a running Kujo service, AI Chat, Codex, agent skills, or an API key. Setup provides Kujo for the build. You need an internet connection, Bash, curl and tar, plus disk space for setup and the sites you capture. Some Linux browser dependencies require administrator access. Read the [setup requirements](https://github.com/kujolang/website-cloner#readme) before installing.

## Files you can maintain

Each export includes the static frontend and the source project for [Kujo SSG](/ecosystem/ssg/). Posts and other suitable content use Markdown and frontmatter. Shared templates, content types and taxonomy relationships keep recurring layouts and content organized while preserving captured URLs.

Complex page-builder sections may still need HTML components or structured layout data. The goal is useful source you can edit, not a claim that every design can become plain Markdown.

Local assets, search, feeds, a sitemap, `llms.txt`, and read-only WebMCP discovery come with the export. Reports show what was captured, what was checked, and what still needs attention. You can rebuild from saved downloads instead of fetching the whole site again.

## Use AI only when you choose it

The default path makes no model calls. If you want design review, connect [AI Chat](/ecosystem/ai-chat/) and choose an available model. Review is bounded to CSS adjustments, with quality checks and rollback. It does not rewrite your posts or recreate a missing backend.

The builder reports input, output and cached token usage when the provider supplies it. AI review can help with styling, but it may accept no changes; it is not a promise of a better result.

## Know what you are moving

A static clone preserves captured pages and supported browser interactions. It does not transfer WordPress administration, customer accounts, checkout processing, comment submission or form delivery. Connect those features to suitable services before launching.

Review mobile layouts, navigation, images and accessibility reports. Missing source files, protected pages, unusual scripts and third-party embeds can limit a capture. The builder respects crawl restrictions and does not bypass access protections. Clone sites you own or have permission to migrate.

Version 0.1.1 is ready for public testing. [Report a reproducible issue](https://github.com/kujolang/website-cloner/issues) with the affected behavior and safe diagnostic details—never credentials or private client data.

## Video transcript

Your website shouldn't be trapped on one platform. Website Cloner runs on your own computer. Download it, run the installer, and the app opens in your browser.

Paste the site's address and click Clone. No AI is needed. The builder captures the site, gathers its assets, and checks the result.

Here's the original beside a real clone. Scroll from the first section to the footer. Compare the images, the spacing, and the details. You can see what carried across, and what still needs a closer look.

And you get files you can work with. Markdown content, frontmatter, and shared templates, built for the Kujo static site generator.

Download the project, or connect your own GitHub Pages or Cloudflare Pages account to publish it.

Your website. Your next move. Try Website Cloner.
