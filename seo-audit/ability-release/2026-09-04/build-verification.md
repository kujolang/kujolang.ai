# Build and deployment verification

Production source: 025bad2dc7990889796fd0b63f7c78866ec05915. GitHub Actions run 33929513049 passed its full SSG build, asset generation, contracts and deployment. Its pinned runtime commit is 7df293865ae7d342b669789d011f607449808b02 (CLI reports 1.0.0), identical to the baseline pipeline.

Downloaded Pages artifact 9958285900 matched the recorded SHA-256 in after-provenance.json. Both scripts/verify-site-contract.sh output and scripts/validate-generated-output.sh output passed on that exact artifact. The final local contract moves its result check after the existing final assertions; this test-only change was validated locally and does not alter site output. Subsequent test/audit-only commits skip CI deliberately.

Node tests passed. npm audit --omit=dev reported zero vulnerabilities. Raw logs are preserved locally under raw/; output hashes are committed in after-manifest.json. All 194 canonical production routes return HTTP 200. Changed-page visible text and private-source boundaries were verified against preserved production HTML. A separate default Python urllib probe received HTTP 403; the browser-like full crawl and ten named crawler-profile checks succeeded, as recorded in crawler-access.csv. No blanket claim about all arbitrary clients is made.
