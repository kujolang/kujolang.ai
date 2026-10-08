# Repeat the production checks

Run from the parent workspace containing `agent-city-sites-web`, `agent-city-sites-docs`, and `agent-city-sites-registry`, or set `AUDIT_WORKSPACE` to it. Build or extract verified site output first. Set `AUDIT_DATE` to a new date. The scripts create its raw directory and refuse to overwrite existing receipts.

```sh
export AUDIT_DATE=YYYY-MM-DD
node agent-city-sites-web/seo-audit/agent-city/2026-10-08/reproduce/live.mjs web docs registry
PLAYWRIGHT_PACKAGE=agent-city/package.json CHROMIUM_PATH="/path/to/chromium" node agent-city-sites-web/seo-audit/agent-city/2026-10-08/reproduce/browser.mjs web docs registry
```

These are read-only HTTP and browser probes. They write local receipts and screenshots. The scripts use the installed Playwright package; they do not install a browser or submit tasks.

Generated-output auditing uses `scripts/seo_audit.py` from this repository with `--repo`, `--output`, `--audit-dir`, `--phase`, and `--origin`. Build commands and pinned revisions are recorded in each audit’s build/verification receipts. MCP uses `tests/production_catalog_test.mjs`, with `RECEIPT_PATH` set to a fresh local JSON path.
