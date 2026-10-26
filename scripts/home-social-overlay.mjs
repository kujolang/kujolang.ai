// Adapt Howl's social layout for the homepage brand lockup before rasterization.
// Keep the background, embedded font, and typography supplied by Howl.
export function homeSocialOverlay(svg, card, logo) {
	svg = svg.replace('<rect x="78" y="570" width="84" height="4" fill="#111"/>', '');
	const escape = (text) => text.replaceAll('&', '&amp;').replaceAll('<', '&lt;')
		.replaceAll('>', '&gt;').replaceAll('"', '&quot;').replaceAll("'", '&apos;');
	for (const className of ['label', 'social-title', 'social-tag']) {
		const pattern = new RegExp(`<text\\b[^>]*class="mono ${className}"[^>]*>[\\s\\S]*?</text>`, 'g');
		if (!pattern.test(svg)) throw new Error(`Howl homepage layout missing ${className}`);
		svg = svg.replace(pattern, '');
	}
	const lines = [];
	for (const word of card.tagline.split(/\s+/)) {
		const last = lines.length - 1;
		if (last < 0 || `${lines[last]} ${word}`.length > 43) lines.push(word);
		else lines[last] += ` ${word}`;
	}
	if (lines.length > 5) throw new Error('Homepage description exceeds the social card layout');
	const lockup = `<image href="data:image/svg+xml;base64,${logo.toString('base64')}" x="78" y="154" width="82" height="82"/>\n`
		+ `<text x="184" y="232" class="mono social-title">${escape(card.title)}</text>\n`
		+ lines.map((line, index) => `<text x="78" y="342" class="mono social-tag" transform="translate(0 ${index * 34})">${escape(line)}</text>`).join('\n');
	return svg.replace('</svg>', `${lockup}\n</svg>`);
}
