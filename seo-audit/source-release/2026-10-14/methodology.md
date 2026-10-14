# Scope and method — 2026-10-14

This is a release-scoped SEO and AI-search readiness audit of Source's new ecosystem page and existing documentation page, plus their listing, sitemap and MCP discovery paths. It is not a new full-site SEO audit or an authority/ranking study of every Kujo property.

Preserve the untouched generated sites and live responses under ignored `raw/`. `capture.py` inventories every generated HTML route before and after to detect missing metadata, broken internal routes, invalid JSON-LD and unintended removal. Inspect the affected pages in depth; surrounding unrelated content stays unchanged. Record source revisions, exact runtime pins, source-to-output hashes and production receipts.

Site: Kujo SSG source → generated output → GitHub Pages Actions deployment → Cloudflare → kujolang.ai. Docs: section SSG builds → output → gh-pages branch → GitHub Pages → Cloudflare. MCP: reviewed website content → catalog snapshot → generated Worker → Cloudflare endpoint. Kennel only enrolls suitable Kujo packages; Source is a Node application and remains outside that package protocol.

Python urllib received 403 responses across hosts; independent curl requests reached the live sites. Those 403s are recorded as client-specific access failures, not missing pages or proof that search bots are blocked. Crawler UA probes do not establish access from verified crawler IPs. No DNS, WAF or training-crawler policy changes are authorized or needed for this content release.

The untouched build completed before content edits; responsive generation and the immutable output copy finished independently. An initial baseline contract invocation used the edited source tree and therefore reported expected source/output mismatches; it is not counted as a baseline regression. The same baseline artifact is checked from a detached original-source worktree instead. Final checks use matching new source and CI output.

Complete Howl regeneration changed one unrelated workflow JPEG by 41 bytes; its original tracked bytes were restored. Source is the only added social image. Local social verification against the old baseline output reports expected new-page absence; the new build CI must pass the complete social gate before publication.

The detached baseline contract passed. Its first npm test invocation lacked installed Sharp; rerunning with the existing locked dependencies passed all three tests. These environmental/setup failures are preserved separately from the successful matching-artifact checks.

First new-site CI run `38594568677` passed the build, responsive-image verification and exhaustive social checks, then rejected the old expected social-card count (245 versus 246). Commit `898f7e2` updates that count for the added Source card; no check was removed. Docs Pages attempt 1 timed out in GitHub's `updating_pages` state after its artifact build succeeded; retry uses the same verified artifact and unchanged timeout. GitHub's status API reported no active incident at the check time; no cause is inferred.

Artifact review found that Source supplied its own brand suffix while the template already appends Kujolang.ai. Commit 4e71103 removes the duplicated suffix and locks the final title in the site gate. The catalog record and Worker bytes are unchanged by this metadata-only correction. Image table paths resolve relative URLs against the page URL. Audit CSV writers emit LF so git whitespace validation remains useful.

The pre-title artifact from run 38595494300 passed all build gates and was preserved for inspection. Its pending deployment was canceled because final title revision 4e71103 superseded it; the final revision must independently pass the full build and deployment. Desktop (1440px) and mobile (390px) artifact previews passed with all images loaded and no document overflow. Deterministic final screenshots use the site's supported reduced-motion mode to avoid capturing transient scramble text.
