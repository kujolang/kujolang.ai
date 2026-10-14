# Verification receipt

Reviewed website content: `4e7110308b9815c254a2fd4bfbc872af0749641b`.
GitHub run `38597461622` passed build and Pages deployment; artifact `11911223490`.

## Website

Baseline runtime: checksum-verified Kujo 1.8.0. Baseline source: `000b0fb168abb7e58166b36b84eb498687517df3`.

```sh
kujo run ./build.kujo -- --site-url https://kujolang.ai
npm run images:responsive
npm test
bash scripts/verify-site-contract.sh output
bash scripts/validate-generated-output.sh output
node --check output/assets/js/site.js
```

Final CI passed the commands above, including responsive image checks, 246 Howl social cards covering every shareable route, and Source's exact title, release link, installation and image contracts. Baseline contract checks ran from a detached original-source worktree against the preserved baseline output; its three Node tests passed with the locked dependencies installed. Local post-change Node tests also passed.

```sh
HOWL_BIN=/path/to/howl/bin/howl KUJO=/path/to/kujo-1.8.0 npm run social:cards
python3 capture.py raw/baseline-site https://kujolang.ai raw/baseline-inventory.json
python3 capture.py raw/after-site https://kujolang.ai raw/after-inventory.json
python3 probe.py after
python3 finalize.py
```

The complete Howl manifest was rendered; one unrelated JPEG changed during rasterization and was restored to its original bytes. Live original hero/social bytes match the reviewed hashes in assets.json. Chrome checked ecosystem and docs at 1440×1000 and 390×844, using reduced motion for deterministic screenshots: HTTP 200, loaded images and no document overflow. The public Source title matches the exact CI contract. See browser-receipt.json and production-receipt.json.

Raw logs include initial source/output mismatch checks, the corrected card-count gate, and the superseded pre-title build. These are not counted as passing final checks; methodology.md explains them.

## Related release surfaces

- Source release CI `38591218086` and main CI `38595618121`: passed. Fresh tagged clone: `npm ci`, `npm run demo:contest -- --trace`, `npm run demo:hybrid` passed. The hybrid rehearsal is emulated, not a new live Cloudflare test.
- Docs CI `38592510754`, then generated Pages deployment `38593824506` attempt 2: passed. Receipt-only docs CI `38595806349` passed. The public Source guide is accurate; all 107 generated routes remain.
- MCP final pinned-source CI `38597555221`: passed. Commands: `sync_catalog --check`, `tests/run_all.kujo`, `server --self-check`, Worker generation/syntax/parity, native HTTP tests. Wrangler 4.130.0 dry-run and deploy passed. `node tests/production_catalog_test.mjs` matched 235 items and six installation profiles against the reviewed Worker. Exact Source lookup is included. Production revision is recorded in the MCP evidence receipt.
- Kennel: not applicable; no unsupported package or installation contract was added.

No runtime or SEO performance improvement is inferred by comparing different build machines. Search/traffic/citation outcome data remains unavailable.
