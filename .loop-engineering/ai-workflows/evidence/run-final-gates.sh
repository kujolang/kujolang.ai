#!/bin/bash
set -euo pipefail
export PATH="$PWD/tmp/runtime:$PATH"
export KUJO_BIN="$PWD/tmp/runtime/kujo" KUJO="$PWD/tmp/runtime/kujo"
export PLAYWRIGHT_MODULE=/Users/robertdevore/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright
export CHROME_BIN=/Users/robertdevore/Library/Caches/ms-playwright/chromium_headless_shell-1243/chrome-headless-shell-mac-x64/chrome-headless-shell
export AXE_SCRIPT="$PWD/tmp/qa/node_modules/axe-core/axe.min.js"
export SITE_URL=http://127.0.0.1:4178
export BROWSER_EVIDENCE_DIR=.loop-engineering/ai-workflows/evidence/browser-home
export EXAMPLES_EVIDENCE_DIR=.loop-engineering/ai-workflows/evidence/browser-examples
export GUIDE_EVIDENCE_DIR=.loop-engineering/ai-workflows/evidence/browser-guides
export WORKFLOW_EVIDENCE_DIR=.loop-engineering/ai-workflows/evidence/browser-workflows
../kujo-workflows/loop-engineering/scripts/run-workflow.sh --config .loop-engineering/ai-workflows/final/loop.yml
