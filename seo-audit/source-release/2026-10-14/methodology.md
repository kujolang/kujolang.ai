# Scope and method — 2026-10-14

This is a release-scoped SEO and AI-search readiness audit of Source's new ecosystem page and existing documentation page, plus their listing, sitemap and MCP discovery paths. It is not a new full-site SEO audit or an authority/ranking study of every Kujo property.

Preserve the untouched generated sites and live responses under ignored `raw/`. `capture.py` inventories every generated HTML route before and after to detect missing metadata, broken internal routes, invalid JSON-LD and unintended removal. Inspect the affected pages in depth; surrounding unrelated content stays unchanged. Record source revisions, exact runtime pins, source-to-output hashes and production receipts.

Site: Kujo SSG source → generated output → GitHub Pages Actions deployment → Cloudflare → kujolang.ai. Docs: section SSG builds → output → gh-pages branch → GitHub Pages → Cloudflare. MCP: reviewed website content → catalog snapshot → generated Worker → Cloudflare endpoint. Kennel only enrolls suitable Kujo packages; Source is a Node application and remains outside that package protocol.

Python urllib received 403 responses across hosts; independent curl requests reached the live sites. Those 403s are recorded as client-specific access failures, not missing pages or proof that search bots are blocked. Crawler UA probes do not establish access from verified crawler IPs. No DNS, WAF or training-crawler policy changes are authorized or needed for this content release.

The untouched build completed before content edits; responsive generation and the immutable output copy finished independently. An initial baseline contract invocation used the edited source tree and therefore reported expected source/output mismatches; it is not counted as a baseline regression. The same baseline artifact is checked from a detached original-source worktree instead. Final checks use matching new source and CI output.

Complete Howl regeneration changed one unrelated workflow JPEG by 41 bytes; its original tracked bytes were restored. Source is the only added social image. Local social verification against the old baseline output reports expected new-page absence; the new build CI must pass the complete social gate before publication.
