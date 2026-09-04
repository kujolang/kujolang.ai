#!/usr/bin/env bash
set -euo pipefail

port="${1:-8080}"
site_url="${KUJO_SITE_URL:-http://127.0.0.1:${port}}"

kujo run ./build.kujo -- --site-url "$site_url"
npm run images:responsive
bash scripts/validate-generated-output.sh output

printf 'Kujolang.ai is available at http://127.0.0.1:%s\n' "$port"
exec kujo serve output --host 127.0.0.1 --port "$port"
