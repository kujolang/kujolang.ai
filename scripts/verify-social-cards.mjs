import { readdir, readFile, stat } from 'node:fs/promises';
import path from 'node:path';
import process from 'node:process';
import { fileURLToPath } from 'node:url';

const repoRoot = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const manifestPath = path.join(repoRoot, 'howl-social.json');
const sourceImageDir = path.join(repoRoot, 'assets/images/social');
const outputDir = path.join(repoRoot, 'output');
const outputImageDir = path.join(outputDir, 'assets/images/social');
const manifest = JSON.parse(await readFile(manifestPath, 'utf8'));
const failures = [];

function fail(message) {
	failures.push(message);
}

function routeFromUrl(rawUrl) {
	const parsed = new URL(rawUrl.includes('://') ? rawUrl : `https://${rawUrl}`);
	return parsed.pathname === '/' ? '/' : `/${parsed.pathname.replace(/^\/+|\/+$/g, '')}/`;
}

function htmlPathForRoute(route) {
	return route === '/'
		? path.join(outputDir, 'index.html')
		: path.join(outputDir, route.slice(1), 'index.html');
}

function metaValues(html, attribute, value) {
	const pattern = new RegExp(`<meta ${attribute}="${value}" content="([^"]*)">`, 'g');
	return [...html.matchAll(pattern)].map((match) => match[1]);
}

function jpegDimensions(bytes) {
	if (bytes[0] !== 0xff || bytes[1] !== 0xd8) throw new Error('not a JPEG');
	const startOfFrameMarkers = new Set([0xc0, 0xc1, 0xc2, 0xc3, 0xc5, 0xc6, 0xc7, 0xc9, 0xca, 0xcb, 0xcd, 0xce, 0xcf]);
	let offset = 2;
	while (offset + 8 < bytes.length) {
		if (bytes[offset] !== 0xff) {
			offset += 1;
			continue;
		}
		const marker = bytes[offset + 1];
		if (startOfFrameMarkers.has(marker)) {
			return { height: bytes.readUInt16BE(offset + 5), width: bytes.readUInt16BE(offset + 7) };
		}
		if (marker === 0xd8 || marker === 0xd9) {
			offset += 2;
			continue;
		}
		const segmentLength = bytes.readUInt16BE(offset + 2);
		if (segmentLength < 2) throw new Error('invalid JPEG segment');
		offset += segmentLength + 2;
	}
	throw new Error('JPEG dimensions not found');
}

async function indexRoutes(dir, relative = '') {
	const routes = [];
	for (const entry of await readdir(dir, { withFileTypes: true })) {
		const nextRelative = path.join(relative, entry.name);
		if (entry.isDirectory()) {
			routes.push(...await indexRoutes(path.join(dir, entry.name), nextRelative));
		} else if (entry.name === 'index.html') {
			const parent = path.dirname(nextRelative);
			routes.push(parent === '.' ? '/' : `/${parent.split(path.sep).join('/')}/`);
		}
	}
	return routes;
}

const cards = manifest.cards ?? [];
const ids = new Set();
const routes = new Set();

for (const card of cards) {
	if (ids.has(card.id)) fail(`duplicate card id: ${card.id}`);
	ids.add(card.id);
	if (card.variant !== 'social') fail(`${card.id}: variant must be social`);
	if (card.show_border !== false) fail(`${card.id}: show_border must be false`);
	if (card.show_url !== false) fail(`${card.id}: show_url must be false`);
	if (!card.background_image) fail(`${card.id}: missing background_image`);
	if (!card.font_file) fail(`${card.id}: missing font_file`);

	const route = routeFromUrl(card.url);
	if (routes.has(route)) fail(`duplicate card route: ${route}`);
	routes.add(route);

	const sourceImage = path.join(sourceImageDir, `${card.id}.jpg`);
	const outputImage = path.join(outputImageDir, `${card.id}.jpg`);
	const htmlPath = htmlPathForRoute(route);
	const expectedUrl = `https://kujolang.ai/assets/images/social/${card.id}.jpg`;

	try {
		const [sourceBytes, outputBytes] = await Promise.all([readFile(sourceImage), readFile(outputImage)]);
		const dimensions = jpegDimensions(sourceBytes);
		if (dimensions.width !== 1200 || dimensions.height !== 630) {
			fail(`${card.id}: expected a 1200x630 JPEG, got ${dimensions.width}x${dimensions.height}`);
		}
		if ((await stat(sourceImage)).size >= 5 * 1024 * 1024) fail(`${card.id}: image exceeds 5 MB`);
		if (!sourceBytes.equals(outputBytes)) fail(`${card.id}: generated image copy differs from source`);
	} catch (error) {
		fail(`${card.id}: image verification failed: ${error.message}`);
	}

	try {
		const html = await readFile(htmlPath, 'utf8');
		const ogImages = metaValues(html, 'property', 'og:image');
		const twitterImages = metaValues(html, 'name', 'twitter:image');
		const ogAlts = metaValues(html, 'property', 'og:image:alt');
		const twitterAlts = metaValues(html, 'name', 'twitter:image:alt');
		if (ogImages.length !== 1 || ogImages[0] !== expectedUrl) fail(`${route}: incorrect og:image`);
		if (twitterImages.length !== 1 || twitterImages[0] !== expectedUrl) fail(`${route}: incorrect twitter:image`);
		if (ogAlts.length !== 1 || !ogAlts[0].trim()) fail(`${route}: missing og:image:alt`);
		if (twitterAlts.length !== 1 || !twitterAlts[0].trim()) fail(`${route}: missing twitter:image:alt`);
		if (!html.includes('<meta property="og:image:type" content="image/jpeg">')) fail(`${route}: missing JPEG image type`);
		if (!html.includes('<meta property="og:image:width" content="1200">')) fail(`${route}: missing image width`);
		if (!html.includes('<meta property="og:image:height" content="630">')) fail(`${route}: missing image height`);
		if (!html.includes('<meta name="twitter:card" content="summary_large_image">')) fail(`${route}: missing large Twitter card`);
		if (!html.includes(`"image":"${expectedUrl}"`)) fail(`${route}: JSON-LD image does not match`);
	} catch (error) {
		fail(`${route}: metadata verification failed: ${error.message}`);
	}
}

try {
	const notFoundHtml = await readFile(path.join(outputDir, '404.html'), 'utf8');
	const fallbackUrl = 'https://kujolang.ai/assets/images/social/home.jpg';
	const fallbackOgImages = metaValues(notFoundHtml, 'property', 'og:image');
	const fallbackTwitterImages = metaValues(notFoundHtml, 'name', 'twitter:image');
	if (!notFoundHtml.includes('<meta name="robots" content="noindex,follow">')) fail('/404: missing noindex metadata');
	if (fallbackOgImages.length !== 1 || fallbackOgImages[0] !== fallbackUrl) fail('/404: incorrect og:image fallback');
	if (fallbackTwitterImages.length !== 1 || fallbackTwitterImages[0] !== fallbackUrl) fail('/404: incorrect twitter:image fallback');
} catch (error) {
	fail(`/404: metadata verification failed: ${error.message}`);
}

const generatedRoutes = new Set(await indexRoutes(outputDir));
for (const route of generatedRoutes) {
	if (!routes.has(route)) fail(`${route}: generated page has no Howl social card`);
}
for (const route of routes) {
	if (!generatedRoutes.has(route)) fail(`${route}: Howl card has no generated page`);
}

const imageIds = new Set((await readdir(sourceImageDir))
	.filter((file) => file.endsWith('.jpg'))
	.map((file) => path.basename(file, '.jpg')));
for (const id of imageIds) {
	if (!ids.has(id)) fail(`${id}: social image has no manifest card`);
}
for (const id of ids) {
	if (!imageIds.has(id)) fail(`${id}: manifest card has no social image`);
}

if (failures.length) {
	for (const failure of failures) console.error(`FAIL: ${failure}`);
	console.error(`Social card verification failed: ${failures.length} issue(s)`);
	process.exit(1);
}

console.log(`Social cards verified: ${cards.length} cards cover ${generatedRoutes.size} shareable routes; 404 uses the branded home fallback.`);
