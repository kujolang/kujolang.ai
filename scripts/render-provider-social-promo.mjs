import { readFile } from 'node:fs/promises';
import path from 'node:path';
import sharp from 'sharp';

const repoRoot = path.resolve(new URL('..', import.meta.url).pathname);
const providers = JSON.parse(await readFile(path.join(repoRoot, 'assets/data/providers.json'), 'utf8'));

const dataUri = async (file, mime) => `data:${mime};base64,${(await readFile(path.join(repoRoot, file))).toString('base64')}`;
const kujoMark = await dataUri('assets/images/kujo-logomark.svg', 'image/svg+xml');
const font = await dataUri('assets/css/fonts/DepartureMono-Regular.woff2', 'font/woff2');

const logo = async (provider) => {
	let buffer = await readFile(path.join(repoRoot, provider.logo.replace(/^\//, '')));
	if (provider.logo.endsWith('.svg')) {
		buffer = await sharp(buffer).resize({ width: 100, height: 100, fit: 'inside' }).png().toBuffer();
	}
	const mime = buffer[0] === 0xff && buffer[1] === 0xd8 ? 'image/jpeg' : 'image/png';
	return `data:${mime};base64,${buffer.toString('base64')}`;
};
const columns = Math.max(5, Math.ceil(providers.length / 5));
const cardHeight = 62;
const gap = 10;
const startX = 67;
const cardWidth = (1200 - 2 * startX - (columns - 1) * gap) / columns;
const logoSize = 50;

const renderProvider = async (provider, index, startY) => {
	const x = startX + (index % columns) * (cardWidth + gap);
	const y = startY + Math.floor(index / columns) * (cardHeight + gap);
	const image = await logo(provider);
	return `<g transform="translate(${x} ${y})"><rect width="${cardWidth}" height="${cardHeight}" rx="3" fill="#fff" fill-opacity=".92" stroke="#111" stroke-opacity=".2"/><image href="${image}" x="${(cardWidth - logoSize) / 2}" y="6" width="${logoSize}" height="${logoSize}" preserveAspectRatio="xMidYMid meet"/></g>`;
};

const cards = await Promise.all(providers.map((provider, index) => renderProvider(provider, index, 170)));

const svg = `<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1200" height="630" viewBox="0 0 1200 630"><style>@font-face{font-family:DepartureMono;src:url(${font})}text{font-family:DepartureMono,monospace}</style><rect width="1200" height="630" fill="#0d0d0d" fill-opacity=".12"/><rect x="52" y="28" width="1096" height="116" rx="4" fill="#fff" fill-opacity=".95"/><image href="${kujoMark}" x="78" y="49" width="74" height="74" preserveAspectRatio="xMidYMid meet"/><text x="178" y="82" fill="#111" font-size="39" letter-spacing="-.08em">Kujo</text><text x="178" y="111" fill="#555" font-size="13" letter-spacing=".08em">PROVIDERS</text><text x="1120" y="78" text-anchor="end" fill="#111" font-size="17">${providers.length} integrations</text><text x="1120" y="106" text-anchor="end" fill="#555" font-size="11">one readable interface</text><text x="600" y="158" text-anchor="middle" fill="#fff" font-size="12" letter-spacing=".12em">LOCAL · HOSTED · CLOUD · MEDIA</text>${cards.join('')}</svg>`;

await sharp(path.join(repoRoot, 'assets/images/ecosystem/ai-sdk-provider-network.webp'))
	.resize(1200, 630, { fit: 'cover', position: 'center' })
	.composite([{ input: Buffer.from(svg), blend: 'over' }])
	.flatten({ background: '#fff' })
	.jpeg({ quality: 92, chromaSubsampling: '4:4:4', progressive: true })
	.toFile(path.join(repoRoot, 'assets/images/social/providers.jpg'));
console.log(`Rendered provider social promo with ${providers.length} local logos.`);
