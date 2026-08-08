#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
howl_bin="${HOWL_BIN:-${repo_root}/../kujo-repos/howl/bin/howl}"
output_dir="${repo_root}/assets/images/social"
render_dir="${repo_root}/.howl-social-render"

cleanup() {
	rm -rf -- "$render_dir"
}
trap cleanup EXIT

if [[ ! -x "$howl_bin" ]]; then
	printf 'Howl executable not found: %s\n' "$howl_bin" >&2
	printf 'Set HOWL_BIN to your Howl launcher path.\n' >&2
	exit 1
fi

rm -rf -- "$render_dir"
"$howl_bin" validate --manifest "${repo_root}/howl-social.json"
"$howl_bin" render --manifest "${repo_root}/howl-social.json" --out "$render_dir" --format svg
mkdir -p "$output_dir"

if command -v node >/dev/null 2>&1 && [[ -d "${repo_root}/node_modules/sharp" ]]; then
	node "${repo_root}/scripts/rasterize-social-cards.mjs" "$render_dir" "$output_dir" "${repo_root}/howl-social.json"
else
	printf 'Node.js and project dependencies are required to rasterize Howl SVG cards. Run npm install first.\n' >&2
	exit 1
fi

printf 'Rendered %s social cards to %s\n' "$(find "$output_dir" -maxdepth 1 -type f -name '*.jpg' | wc -l | tr -d ' ')" "$output_dir"
