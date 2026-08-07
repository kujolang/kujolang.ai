#!/usr/bin/env bash
set -euo pipefail

site_url="${1:-https://kujolang.ai}"

kujo run ./build.kujo -- --site-url "$site_url"
bash scripts/validate-generated-output.sh output

mkdir -p dist/client dist/server
rsync -a --delete output/ dist/client/
cp hosting/worker.js dist/server/index.js

printf 'Sites bundle ready: %s\n' "$PWD/dist"
