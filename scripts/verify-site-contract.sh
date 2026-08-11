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

require_social_meta() {
	local html_file="$1"
	local card_id="$2"
	local expected="https://kujolang.ai/assets/images/social/${card_id}.jpg"
	local og_image
	local twitter_image
	og_image=$(sed -n 's/.*<meta property="og:image" content="\([^"]*\)">.*/\1/p' "$html_file")
	twitter_image=$(sed -n 's/.*<meta name="twitter:image" content="\([^"]*\)">.*/\1/p' "$html_file")
	[[ "$og_image" == "$expected" ]] || fail "unexpected og:image in ${html_file}: ${og_image}"
	[[ "$twitter_image" == "$expected" ]] || fail "unexpected twitter:image in ${html_file}: ${twitter_image}"
	require_text "$html_file" '<meta property="og:image:type" content="image/jpeg">'
	require_text "$html_file" '<meta property="og:image:width" content="1200">'
	require_text "$html_file" '<meta property="og:image:height" content="630">'
	require_text "$html_file" '<meta property="og:image:alt" content="'
	require_text "$html_file" '<meta name="twitter:site" content="@kujolang">'
	require_text "$html_file" '<meta name="twitter:image:alt" content="'
}

require_file "${output_dir}/index.html"
require_file "${output_dir}/ecosystem/index.html"
require_file "${output_dir}/ethos/index.html"
require_file "${output_dir}/contact/index.html"
require_file "${output_dir}/writing/index.html"
require_file "${output_dir}/assets/js/vendor/scramble-decode.js"
require_file "${output_dir}/assets/prompts/kujo-agent-onboarding.txt"
require_file "${output_dir}/favicon.ico"
require_file "${output_dir}/favicon.svg"
require_file "${output_dir}/favicon-16x16.png"
require_file "${output_dir}/favicon-32x32.png"
require_file "${output_dir}/favicon-48x48.png"
require_file "${output_dir}/apple-touch-icon.png"
require_file "${output_dir}/android-chrome-192x192.png"
require_file "${output_dir}/android-chrome-512x512.png"
require_file "${output_dir}/maskable-icon-512x512.png"
require_file "${output_dir}/mstile-150x150.png"
require_file "${output_dir}/safari-pinned-tab.svg"
require_file "${output_dir}/site.webmanifest"
require_file "${output_dir}/browserconfig.xml"
require_file "${repo_root}/CNAME"
require_file "${repo_root}/.github/workflows/pages.yml"

require_text "${repo_root}/CNAME" 'kujolang.ai'
require_text "${repo_root}/.github/workflows/pages.yml" 'uses: actions/deploy-pages@v4'
require_text "${repo_root}/.github/workflows/pages.yml" 'kujo run ./build.kujo -- --site-url https://kujolang.ai'

if find "${output_dir}" -type f -name '*.html' ! -name 'index.html' ! -name '404.html' | grep -q .; then
	fail 'flat HTML aliases should be disabled so GitHub Pages canonicalizes trailing slashes'
fi

require_text "${output_dir}/index.html" 'Trust at the speed of AI'
require_text "${output_dir}/index.html" '<title>Kujo — AI-Native Programming Language | Kujolang.ai</title>'
require_text "${output_dir}/index.html" '"name":"Kujo","alternateName":["Kujolang.ai","Kujolang"]'
require_text "${output_dir}/index.html" '<meta name="author" content="Kujo Team">'
require_text "${output_dir}/index.html" 'Kujo is an AI-native programming language and toolchain built to make agent-driven software development clear, controlled, and verifiable.'
require_text "${output_dir}/index.html" '<button class="sk-button" data-variant="secondary" type="button" data-quick-install-open>Quick Install</button>'
reject_text "${output_dir}/index.html" 'Read the docs'
reject_text "${output_dir}/index.html" '&rarr;'
require_text "${output_dir}/index.html" 'assets/images/home-agent-workflow.webp'
require_text "${output_dir}/index.html" 'width="1672" height="941" fetchpriority="high"'
require_text "${output_dir}/index.html" 'data-hero-dither'
require_text "${output_dir}/index.html" 'data-quick-install-modal hidden'
require_text "${output_dir}/index.html" 'data-agent-prompt-modal hidden'
require_text "${output_dir}/index.html" 'data-agent-prompt-open'
require_text "${output_dir}/index.html" 'data-agent-prompt-text'
require_text "${output_dir}/index.html" 'data-copy-agent-prompt'
require_text "${output_dir}/index.html" 'curl -fsSL https://raw.githubusercontent.com/kujolang/kujo/main/install.sh | bash'
require_text "${output_dir}/index.html" 'Install Kujo &amp; the local-first ecosystem (or <a href="assets/prompts/kujo-agent-onboarding.txt"'
require_text "${output_dir}/index.html" 'data-copy-status data-scramble-skip'
require_text "${output_dir}/index.html" 'assets/images/kujo-logomark.svg'
require_text "${output_dir}/index.html" 'assets/js/vendor/scramble-decode.js'
require_text "${output_dir}/index.html" '<link rel="icon" href="favicon.ico" sizes="16x16 32x32 48x48">'
require_text "${output_dir}/index.html" '<link rel="icon" type="image/svg+xml" sizes="any" href="favicon.svg?v=kujo-k-1">'
require_text "${output_dir}/index.html" '<link rel="icon" type="image/png" sizes="48x48" href="favicon-48x48.png">'
require_text "${output_dir}/index.html" '<link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">'
require_text "${output_dir}/index.html" '<link rel="mask-icon" href="safari-pinned-tab.svg" color="#000000">'
require_text "${output_dir}/index.html" '<link rel="manifest" href="site.webmanifest">'
require_text "${output_dir}/index.html" '<meta name="apple-mobile-web-app-title" content="Kujo">'
require_text "${output_dir}/index.html" '<meta name="mobile-web-app-capable" content="yes">'
require_text "${output_dir}/index.html" '<meta name="msapplication-TileImage" content="mstile-150x150.png">'
require_text "${output_dir}/ecosystem/shipcheck/index.html" 'href="../../favicon.svg?v=kujo-k-1"'
require_text "${output_dir}/ecosystem/shipcheck/index.html" 'href="../../site.webmanifest"'
require_text "${output_dir}/index.html" '>Home</a></li><li><a href="/ecosystem/"'
require_text "${output_dir}/index.html" '>Ecosystem</a></li><li><a href="/ethos/"'
require_text "${output_dir}/index.html" '>Ethos</a></li><li><a href="/writing/"'
require_text "${output_dir}/index.html" '>Writing</a></li><li><a href="https://docs.kujolang.ai"'
require_text "${output_dir}/index.html" '>Docs</a></li><li><a href="/contact/"'
require_text "${output_dir}/index.html" '<nav aria-label="Footer"><a href="ecosystem/">Ecosystem</a>'
reject_text "${output_dir}/index.html" '<nav aria-label="Footer"><a href="index.html">Home</a>'
reject_text "${output_dir}/index.html" 'Programming language for AI-native software'
reject_text "${output_dir}/index.html" 'data-dither-canvas'

require_text "${output_dir}/ethos/index.html" 'ethos-human-agent-trust'
require_text "${output_dir}/contact/index.html" 'contact-conversation'
require_text "${output_dir}/writing/index.html" 'writing-technical-documents.webp'
require_text "${output_dir}/writing/index.html" 'Content coming soon.'
require_text "${output_dir}/writing/index.html" 'Launch notes, ecosystem deep dives, tutorials, and field reports are on the way. Follow on <a href="https://x.com/kujolang">X</a> for updates'
reject_text "${output_dir}/writing/index.html" 'From the Kujo ecosystem.'
reject_text "${output_dir}/writing/index.html" 'Welcome to Kujo'
reject_text "${output_dir}/writing/index.html" 'Local-first agent workflows'
reject_text "${output_dir}/writing/index.html" 'Mapping the Kujo ecosystem'
require_text "${output_dir}/ecosystem/index.html" 'ecosystem-distributed-tools.webp'
require_text "${output_dir}/ecosystem/index.html" '<meta name="description" content="Explore the Kujo ecosystem of language primitives, local-first tools, and inspectable AI-native application showcases.">'
require_text "${output_dir}/ecosystem/index.html" '"@type":"CollectionPage"'
require_text "${output_dir}/ecosystem/index.html" '<h2 id="primitives-title">Primitives</h2>'
require_text "${output_dir}/ecosystem/index.html" '<h2 id="tooling-title">Tooling</h2>'
require_text "${output_dir}/ecosystem/index.html" '<h2 id="showcase-title">Showcase</h2>'
require_text "${output_dir}/ecosystem/workcell/index.html" 'href="https://github.com/kujolang/workcell"'
require_text "${output_dir}/ecosystem/redact/index.html" 'href="https://github.com/kujolang/redact"'
require_text "${output_dir}/ecosystem/sitekit/index.html" 'href="https://github.com/kujolang/site-kit"'

require_social_meta "${output_dir}/index.html" 'home'
require_social_meta "${output_dir}/ecosystem/index.html" 'ecosystem'
require_social_meta "${output_dir}/ethos/index.html" 'ethos'
require_social_meta "${output_dir}/writing/index.html" 'writing'
require_social_meta "${output_dir}/contact/index.html" 'contact'

social_card_count=$(find "${repo_root}/assets/images/social" -maxdepth 1 -type f -name '*.jpg' | wc -l | tr -d ' ')
[[ "$social_card_count" == 38 ]] || fail "expected 38 social cards, found ${social_card_count}"

for social_card in "${repo_root}"/assets/images/social/*.jpg; do
	file "$social_card" | grep -Fq '1200x630' || fail "social card is not 1200x630: ${social_card}"
	card_bytes=$(wc -c < "$social_card" | tr -d ' ')
	(( card_bytes < 5242880 )) || fail "social card exceeds 5 MB: ${social_card}"
done
file "${repo_root}/assets/images/og.png" | grep -Fq '1200 x 630' || fail 'legacy og.png is not 1200x630'

file "${output_dir}/favicon.ico" | grep -Fq '3 icons' || fail 'favicon.ico does not contain 16, 32, and 48px entries'
file "${output_dir}/favicon-16x16.png" | grep -Fq '16 x 16' || fail 'favicon-16x16.png has the wrong size'
file "${output_dir}/favicon-32x32.png" | grep -Fq '32 x 32' || fail 'favicon-32x32.png has the wrong size'
file "${output_dir}/favicon-48x48.png" | grep -Fq '48 x 48' || fail 'favicon-48x48.png has the wrong size'
file "${output_dir}/apple-touch-icon.png" | grep -Fq '180 x 180' || fail 'apple-touch-icon.png has the wrong size'
file "${output_dir}/android-chrome-192x192.png" | grep -Fq '192 x 192' || fail 'android-chrome-192x192.png has the wrong size'
file "${output_dir}/android-chrome-512x512.png" | grep -Fq '512 x 512' || fail 'android-chrome-512x512.png has the wrong size'
file "${output_dir}/maskable-icon-512x512.png" | grep -Fq '512 x 512' || fail 'maskable-icon-512x512.png has the wrong size'
file "${output_dir}/mstile-150x150.png" | grep -Fq '150 x 150' || fail 'mstile-150x150.png has the wrong size'
reject_text "${output_dir}/favicon.svg" '<text'
require_text "${output_dir}/favicon.svg" 'M178 234 L593 234'
cmp -s "${repo_root}/assets/icons/favicon.svg" "${output_dir}/favicon.svg" || fail 'root favicon.svg drifted from the generated icon asset'
node -e 'const fs=require("fs"); const m=JSON.parse(fs.readFileSync(process.argv[1], "utf8")); if (m.short_name !== "Kujo" || !m.icons.some((i) => i.sizes === "512x512" && i.purpose === "maskable")) process.exit(1)' "${output_dir}/site.webmanifest" || fail 'site.webmanifest is missing the Kujo maskable icon contract'

ecosystem_sources=$(find "${repo_root}/content/ecosystem" -maxdepth 1 -type f -name '*.md' | wc -l | tr -d ' ')
ecosystem_outputs=$(find "${output_dir}/ecosystem" -mindepth 1 -maxdepth 1 -type d | wc -l | tr -d ' ')
primitive_count=$(grep -l '^section: "Primitives"$' "${repo_root}"/content/ecosystem/*.md | wc -l | tr -d ' ')
tooling_count=$(grep -l '^section: "Tooling"$' "${repo_root}"/content/ecosystem/*.md | wc -l | tr -d ' ')
showcase_count=$(grep -l '^section: "Showcase"$' "${repo_root}"/content/ecosystem/*.md | wc -l | tr -d ' ')
[[ "$ecosystem_sources" == 33 ]] || fail "expected 33 ecosystem sources, found ${ecosystem_sources}"
[[ "$ecosystem_outputs" == 33 ]] || fail "expected 33 ecosystem output routes, found ${ecosystem_outputs}"
[[ "$primitive_count" == 14 ]] || fail "expected 14 primitive cards, found ${primitive_count}"
[[ "$tooling_count" == 14 ]] || fail "expected 14 tooling cards, found ${tooling_count}"
[[ "$showcase_count" == 5 ]] || fail "expected 5 showcase cards, found ${showcase_count}"

for source_file in "${repo_root}"/content/ecosystem/*.md; do
	image_path=$(sed -n 's/^featured_image: "\(.*\.webp\)"$/\1/p' "$source_file")
	[[ -n "$image_path" ]] || fail "missing WebP featured_image: ${source_file}"
	[[ -f "${repo_root}${image_path}" ]] || fail "missing featured image asset: ${image_path}"
done

for tool_page in "${output_dir}"/ecosystem/*/index.html; do
	tool_slug=$(basename "$(dirname "$tool_page")")
	require_social_meta "$tool_page" "$tool_slug"
	require_text "$tool_page" 'class="copy-icon copy-icon--copy"'
	require_text "$tool_page" 'data-copy-status data-scramble-skip></span><button'
	require_text "$tool_page" 'target="_blank" rel="noopener">View on GitHub</a>'
	require_text "$tool_page" '>View ecosystem</a>'
	require_text "$tool_page" '"@type":"SoftwareSourceCode"'
	require_text "$tool_page" '"codeRepository":"https://github.com/'
	require_text "$tool_page" 'fetchpriority="high"'
	reject_text "$tool_page" 'Back to ecosystem'
done

require_text "${output_dir}/assets/css/style.css" 'position: fixed;'
require_text "${output_dir}/assets/css/style.css" 'font-size: 96px;'
require_text "${output_dir}/assets/css/style.css" 'body:has(.home-hero) .site-footer'
require_text "${output_dir}/assets/css/style.css" '.ethos-page .kujo-content > h2:first-child'
require_text "${output_dir}/assets/css/style.css" 'margin-block-start: auto;'
reject_text "${output_dir}/assets/css/style.css" '@keyframes grid-drift'
require_text "${output_dir}/assets/js/site.js" 'function enhanceHeroDither()'
require_text "${output_dir}/assets/js/site.js" ".home-hero__media, .page-hero__media, .tool-hero__media"
require_text "${output_dir}/assets/js/site.js" 'Math.sin(frame * 0.36) * 7'
reject_text "${output_dir}/assets/js/site.js" 'waveAmplitude'
reject_text "${output_dir}/assets/js/site.js" 'secondaryWave'
require_text "${output_dir}/assets/js/site.js" 'function enhanceMonoScramble()'
require_text "${output_dir}/assets/js/site.js" "indexOf('departure mono')"
require_text "${output_dir}/assets/js/site.js" "duration: 680 + Math.min(420, original.length * 12)"
require_text "${output_dir}/assets/css/style.css" 'inset-block-start: var(--site-sticky-offset);'
require_text "${output_dir}/assets/css/style.css" 'grid-template-columns: minmax(0, 1fr) auto auto;'
require_text "${output_dir}/assets/css/style.css" 'grid-template-columns: repeat(2, minmax(0, 1fr));'
require_text "${output_dir}/assets/css/style.css" '.contact-grid .sk-feature-grid'
require_text "${output_dir}/assets/css/style.css" 'scrollbar-color: var(--sk-border-default) var(--sk-surface-card);'
require_text "${output_dir}/assets/css/style.css" '.agent-prompt-copy-field textarea::-webkit-scrollbar-thumb'
require_text "${output_dir}/assets/css/style.css" 'stroke: currentColor;'
require_text "${output_dir}/assets/js/site.js" "label.textContent = open ? 'Close' : 'Menu';"

require_text "${output_dir}/assets/prompts/kujo-agent-onboarding.txt" 'default core and operating profiles'
require_text "${output_dir}/assets/prompts/kujo-agent-onboarding.txt" 'kujo doctor --json'

require_text "${output_dir}/contact/index.html" 'href="https://x.com/kujolang"'
require_text "${output_dir}/contact/index.html" 'href="https://github.com/kujolang"'
require_text "${output_dir}/contact/index.html" 'href="https://discord.gg/RqDgyb3BX"'
reject_text "${output_dir}/contact/index.html" 'href="https://discord.gg/kujolang"'

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

printf 'Site contract passed: 33 ecosystem projects, static WebP heroes, navigation, modal, footer, and content requirements verified.\n'
