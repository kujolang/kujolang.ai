# Methodology

Audit date: 2026-10-19. Scope: the comparison hub and seven populated comparison/guide pages. The entire 255-page canonical site was crawled for inbound links, duplicates and depth; editorial conclusions apply only to the eight comparison pages.

Delivery chain: comparison/catalog.json and render-comparisons.mjs produce Markdown and HTML partials; Kujo SSG build.kujo combines these with shared templates, navigation and metadata. howl-social.json supplies social-card copy; Howl embeds the local image and Departure Mono font in SVG, then sharp rasterizes JPEG. GitHub Actions builds with pinned Kujo 1.8.2 and publishes through GitHub Pages.

Baseline: source commit 8551554, untouched focused build exit 0 (99.507394655 seconds), raw live HTML and cited-source receipts collected before edits. The full successful pinned CI baseline is run 39320862640, artifact 12219798730; downloaded ZIP SHA-256 matched GitHub's digest. Its complete extracted output remains in work/comparison-ci-baseline, outside rebuild directories. See baseline-provenance.json. A redundant slow local full build was stopped after this complete CI artifact was recovered. Disk exhaustion interrupted an initial extraction; only this audit's redundant temporary copies were removed and extraction was rerun successfully.

After: focused pinned rebuild includes authors.yml so author IDs resolve exactly as in the full build. Its eight comparison HTML files were placed in a separate hard-linked copy of the immutable full baseline, with each changed file unlinked before replacement. This graph fixture supports like-for-like context crawling; it is explicitly not a newly built full artifact. The successful deployed full CI build at 3fea597 (run 39328814874) provides independent whole-site build validation. Source changes outside these eight pages affect audit tooling only. No factual assertions, review dates, crawler policies or navigation placement were changed.

Commands (from repository root; set KUJO and HOWL_BIN to the official runtime and launcher):

```sh
npm test
python3 -m unittest discover -s tests -p 'test_probe_site.py'
npm run compare:check
"$KUJO" check build.kujo
"$KUJO" run build.kujo -- --content tmp/compare-content --output tmp/audit-after --site-url https://kujolang.ai
python3 scripts/seo_audit.py --output tmp/audit-graph-after --audit-dir seo-audit/comparison-quality/2026-10-19 --phase after
python3 seo-audit/comparison-quality/2026-10-19/scope-audit.py after
python3 scripts/verify-comparisons.py --output tmp/audit-graph-after
bash scripts/validate-generated-output.sh tmp/audit-graph-after
bash scripts/verify-site-contract.sh tmp/audit-graph-after
python3 scripts/probe_site.py --audit-dir seo-audit/comparison-quality/2026-10-19 --phase after --key-path /compare/ --skip-external
python3 seo-audit/comparison-quality/2026-10-19/probe-comparison-pages.py after
```

The focused content fixture must contain content/compare plus content/authors.yml. The full production build uses all content. The scope helper filters the full crawl to the eight pages while retaining full-graph depth and inbound counts. Manual content and source-probe annotations are retained in the committed CSVs; running the generic crawler alone resets those annotations.

Howl: help, validate, list, show, default caption and X caption were run for every card, followed by render --format all, SVG XML parsing, complete-title/tagline checks, image dimension checks, and visual inspection of all eight cards. The temporary eight-card manifest is derived from the committed howl-social.json. Default title wrapping had truncated five titles and seven descriptions. Revised SVGs include each complete title and tagline with no truncation; font and background are embedded. Howl does not run the producer example. No external sharing or posting occurred.

Browser checks used the live site at 1280px and rebuilt pages in 375px frames. Both sets have one H1, correct tables, Departure Mono headings and no page overflow. Horizontal table scrolling is intentional. Static source bytes are reported separately from browser performance; no Lighthouse, field CWV or transfer measurements are claimed. User-agent probes originate from this machine, not authenticated crawler IPs. No numeric SEO score is assigned.
