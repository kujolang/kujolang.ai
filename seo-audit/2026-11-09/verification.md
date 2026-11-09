# Verification

- Website source commit: `99865ad87943d8001dc2a5c8eadcca6fc866e0ed`.
- Public MCP commit: `8bb7af7`.
- Kujo 1.9.0 official macOS x64 archive: release SHA-256 verified before use. The shell default was an older runtime; final checks used the CI-pinned version.
- Node tests: passed. Example/workflow generated-file checks: passed.
- Production SSG build: passed. Responsive image generation: 1,173 variants. Site contract: 58 projects, three catalogs, 135 skills and 45 workflow records. HTML validation: 325 files passed.
- Language-site and comparison verification: passed. Sharing cards: 324 routes covered. Only the new sharing card is changed; unrelated rerender drift was discarded.
- Desktop (1440px) and mobile (390px): page and video inspected; no horizontal overflow. Browser played the 66-second video past 20 seconds without a media error. Final hero image loaded successfully.
- Public MCP: native assertions, Worker parity, native HTTP and self-check passed. Deployed with the existing authorized Wrangler session. Production comparison passed for all 238 records and six installation profiles; see mcp-production.json.
- No Kennel package was added: standalone application installer, not a native package. No builder behavior, site builds, client captures or account credentials were published by this change.

Production website deployment: https://github.com/kujolang/kujolang.ai/actions/runs/42657438576 passed. Live page: https://kujolang.ai/ecosystem/website-cloner/. All 13 scoped production probes returned 200; video, captions, poster, hero, responsive hero and social card match local bytes.

MCP CI: https://github.com/kujolang/kujolang-mcp/actions/runs/42657493471 passed on attempt 2. Attempt 1 hit a native HTTP admission timing failure (503 instead of 429); the unchanged rerun passed. Local native HTTP and live full-catalog parity also passed. No runtime behavior or test assertion was weakened.
