# Verification

- Official Kujo 1.9.0 macOS x64 archive passed its published SHA-256 check. Final site, docs, course and native MCP checks used this runtime.
- Marketing: Node tests passed; 50 real language examples and 28 AI workflow tests passed. Production SSG build, 1,179 responsive variants, site contract, 326-file HTML validation, 325-route social coverage, language and comparison checks passed.
- Docs: official-runtime complete site contract passed (110 HTML files, 109 canonical pages). Source commit fac6448; verified generated gh-pages commit 1f6ad0d. CI and Pages publication passed.
- Course: full npm verification passed, including 54 pages, 2,985 internal references and 40 complete lessons. Source 8841cfa. Cloudflare production version cad9c1b2-199c-453c-8d7f-3c187b8b1242. CI passed.
- Public MCP: five native assertion files and Worker contracts passed. Production compared all 239 catalog entries and six installation profiles against the reviewed Worker. Source a53deec, production version 1acbf67a-71fc-4ac6-8d9f-921a45450412. CI passed.
- Kennel: source 0002823 records external installation only. No version, archive, package count or registry routing changed.
- Full Howl validation/render completed. New 1200×630 card inspected visually; unrelated pre-existing rasterizer drift reverted. Docs/course retain their matching shared Howl cards.
- Browser inspection: marketing page's hero loaded; title settled correctly after the existing text animation; no horizontal overflow at the observed 652px viewport. This is not a claimed full accessibility or cross-device audit.
- Main-site first deployment failed because Python serialization escaped existing non-ASCII text in the generated Howl manifest. The canonical generator restored its Unicode format in c7d6c43; required example/workflow gates then passed. No check was weakened.
- Production metadata/asset receipts and deployment URLs are separate JSON artifacts. Search outcomes remain unmeasured.

The corrected main-site Linux CI build passed every required check; deployment status is recorded separately in deployment.json.

GitHub Pages timed out twice at its default 600000ms window (first syncing_files, then finished_file_sync). Source 46e8ae4 sets the supported deployment timeout to 1200000ms within a 25-minute job; build/security gates are unchanged. This is a hosting-time allowance, not a claim that a build timeout was fixed. Final production status is recorded in deployment.json.

Final production: https://github.com/kujolang/kujolang.ai/actions/runs/42821985759 passed. verify-live.py passed for all three live pages, canonical URLs, one H1 per page, sitemap entries, exact hero/social bytes and homepage/ecosystem/tooling/WebMCP discovery. Public MCP parity passed all 239 entries and six installer profiles. Both earlier Pages timeouts are resolved; no remaining publication blocker.
