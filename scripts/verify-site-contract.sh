#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
output_dir="${1:-${repo_root}/output}"
failures=0

fail() {
	printf 'FAIL: %s\n' "$1" >&2
	failures=$((failures + 1))
}

require_file() {
	[[ -f "$1" ]] || fail "missing file: $1"
}

require_text() {
	local file="$1"
	local text="$2"
	grep -Fq -- "$text" "$file" || fail "missing text in ${file}: ${text}"
}

reject_text() {
	local file="$1"
	local text="$2"
	if grep -Fq -- "$text" "$file"; then
		fail "unexpected text in ${file}: ${text}"
	fi
}

require_file "${output_dir}/index.html"
require_file "${output_dir}/ecosystem/index.html"
require_file "${output_dir}/ethos/index.html"
require_file "${output_dir}/contact/index.html"
require_file "${output_dir}/writing/index.html"
require_file "${output_dir}/assets/js/vendor/scramble-decode.js"

require_text "${output_dir}/index.html" 'Trust at the speed of AI'
require_text "${output_dir}/index.html" 'Kujo is an AI-native programming language and toolchain built to make agent-driven software development clear, controlled, and verifiable.'
require_text "${output_dir}/index.html" 'href="https://docs.kujolang.ai">Read the docs'
require_text "${output_dir}/index.html" 'assets/images/home-agent-workflow.webp'
require_text "${output_dir}/index.html" 'data-quick-install-modal hidden'
require_text "${output_dir}/index.html" 'curl -fsSL https://raw.githubusercontent.com/kujolang/kujo/main/install.sh | bash'
require_text "${output_dir}/index.html" 'assets/images/kujo-logomark.svg'
require_text "${output_dir}/index.html" 'assets/js/vendor/scramble-decode.js'
require_text "${output_dir}/index.html" '>Home</a></li><li><a href="/ecosystem/"'
require_text "${output_dir}/index.html" '>Ecosystem</a></li><li><a href="/ethos/"'
require_text "${output_dir}/index.html" '>Ethos</a></li><li><a href="/writing/"'
require_text "${output_dir}/index.html" '>Writing</a></li><li><a href="/contact/"'
reject_text "${output_dir}/index.html" 'Programming language for AI-native software'
reject_text "${output_dir}/index.html" 'data-dither-canvas'

require_text "${output_dir}/ethos/index.html" 'ethos-human-agent-trust'
require_text "${output_dir}/contact/index.html" 'contact-conversation'
require_text "${output_dir}/writing/index.html" 'writing-technical-documents.webp'
require_text "${output_dir}/ecosystem/index.html" 'ecosystem-distributed-tools.webp'
require_text "${output_dir}/ecosystem/index.html" '<h2 id="primitives-title">Primitives</h2>'
require_text "${output_dir}/ecosystem/index.html" '<h2 id="tooling-title">Tooling</h2>'
require_text "${output_dir}/ecosystem/index.html" '<h2 id="showcase-title">Showcase</h2>'

ecosystem_sources=$(find "${repo_root}/content/ecosystem" -maxdepth 1 -type f -name '*.md' | wc -l | tr -d ' ')
ecosystem_outputs=$(find "${output_dir}/ecosystem" -mindepth 1 -maxdepth 1 -type d | wc -l | tr -d ' ')
primitive_count=$(grep -l '^section: "Primitives"$' "${repo_root}"/content/ecosystem/*.md | wc -l | tr -d ' ')
tooling_count=$(grep -l '^section: "Tooling"$' "${repo_root}"/content/ecosystem/*.md | wc -l | tr -d ' ')
showcase_count=$(grep -l '^section: "Showcase"$' "${repo_root}"/content/ecosystem/*.md | wc -l | tr -d ' ')
[[ "$ecosystem_sources" == 30 ]] || fail "expected 30 ecosystem sources, found ${ecosystem_sources}"
[[ "$ecosystem_outputs" == 30 ]] || fail "expected 30 ecosystem output routes, found ${ecosystem_outputs}"
[[ "$primitive_count" == 14 ]] || fail "expected 14 primitive cards, found ${primitive_count}"
[[ "$tooling_count" == 11 ]] || fail "expected 11 tooling cards, found ${tooling_count}"
[[ "$showcase_count" == 5 ]] || fail "expected 5 showcase cards, found ${showcase_count}"

for source_file in "${repo_root}"/content/ecosystem/*.md; do
	image_path=$(sed -n 's/^featured_image: "\(.*\.webp\)"$/\1/p' "$source_file")
	[[ -n "$image_path" ]] || fail "missing WebP featured_image: ${source_file}"
	[[ -f "${repo_root}${image_path}" ]] || fail "missing featured image asset: ${image_path}"
done

for tool_page in "${output_dir}"/ecosystem/*/index.html; do
	require_text "$tool_page" 'class="copy-icon copy-icon--copy"'
	require_text "$tool_page" '>View ecosystem</a>'
	reject_text "$tool_page" 'Back to ecosystem'
done

require_text "${output_dir}/assets/css/style.css" 'position: fixed;'
require_text "${output_dir}/assets/css/style.css" 'font-size: 96px;'
require_text "${output_dir}/assets/css/style.css" 'body:has(.home-hero) .site-footer'
require_text "${output_dir}/assets/css/style.css" '.ethos-page .kujo-content > h2:first-child'
require_text "${output_dir}/assets/css/style.css" 'margin-block-start: auto;'
reject_text "${output_dir}/assets/css/style.css" '@keyframes grid-drift'
reject_text "${output_dir}/assets/js/site.js" 'enhanceDitherHero'
require_text "${output_dir}/assets/js/site.js" 'function enhanceMonoScramble()'
require_text "${output_dir}/assets/js/site.js" "indexOf('departure mono')"
require_text "${output_dir}/assets/js/site.js" "duration: 680 + Math.min(420, original.length * 12)"

require_text "${output_dir}/contact/index.html" 'href="https://x.com/kujolang"'
require_text "${output_dir}/contact/index.html" 'href="https://github.com/kujolang"'
require_text "${output_dir}/contact/index.html" 'href="https://discord.gg/kujolang"'

if rg -n 'K[-–—]U[-–—]J[-–—]O|\bKUJO\b|Security network|Intake' \
	"${repo_root}/templates" "${repo_root}/content" "${output_dir}" \
	--glob '*.html' --glob '*.md' --glob '*.txt'; then
	fail "found obsolete product naming or removed ecosystem entries"
fi

if rg -n -F '{{' "$output_dir" --glob '*.html'; then
	fail "found unresolved template placeholders"
fi

if (( failures > 0 )); then
	printf 'Site contract failed with %d issue(s).\n' "$failures" >&2
	exit 1
fi

printf 'Site contract passed: 30 ecosystem projects, static WebP heroes, navigation, modal, footer, and content requirements verified.\n'
