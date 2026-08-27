import { readFile } from 'node:fs/promises';
import path from 'node:path';
import sharp from 'sharp';

const repoRoot = path.resolve(new URL('..', import.meta.url).pathname);
const providers = JSON.parse(await readFile(path.join(repoRoot, 'assets/data/providers.json'), 'utf8'));

const dataUri = async (file, mime) => `data:${mime};base64,${(await readFile(path.join(repoRoot, file))).toString('base64')}`;
const kujoMark = await dataUri('assets/images/kujo-logomark.svg', 'image/svg+xml');
const font = await dataUri('assets/css/fonts/DepartureMono-Regular.woff2', 'font/woff2');

const logo = async (provider) => dataUri(provider.logo.replace(/^\//, ''), provider.logo.endsWith('.jpg') ? 'image/jpeg' : 'image/png');
const columns = 5;
const cardWidth = 205;
const cardHeight = 62;
const gap = 10;
const startX = 67;
const startY = 208;

const cards = await Promise.all(providers.map(async (provider, index) => {
	const x = startX + (index % columns) * (cardWidth + gap);
	const y = startY + Math.floor(index / columns) * (cardHeight + gap);
	const image = await logo(provider);
	return `<g transform="translate(${x} ${y})"><rect width="${cardWidth}" height="${cardHeight}" rx="3" fill="#fff" fill-opacity=".92" stroke="#111" stroke-opacity=".2"/><image href="${image}" x="77" y="6" width="50" height="50" preserveAspectRatio="xMidYMid meet"/></g>`;
}));

const svg = `<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1200" height="630" viewBox="0 0 1200 630"><style>@font-face{font-family:DepartureMono;src:url(${font})}text{font-family:DepartureMono,monospace}</style><rect width="1200" height="630" fill="#0d0d0d" fill-opacity=".18"/><rect x="52" y="36" width="1096" height="132" rx="4" fill="#fff" fill-opacity=".94"/><rect x="407" y="54" width="90" height="90" fill="#fff" stroke="#111" stroke-width="2"/><image href="${kujoMark}" x="422" y="69" width="60" height="60" preserveAspectRatio="xMidYMid meet"/><text x="524" y="103" fill="#111" font-size="39" letter-spacing="-.08em">Kujo</text><text x="524" y="132" fill="#555" font-size="13" letter-spacing=".08em">NATIVE PROVIDERS</text><text x="1120" y="96" text-anchor="end" fill="#111" font-size="18">25 integrations</text><text x="1120" y="127" text-anchor="end" fill="#555" font-size="12">one readable interface</text><text x="600" y="193" text-anchor="middle" fill="#fff" font-size="14" letter-spacing=".12em">LOCAL · HOSTED · CLOUD · MEDIA</text>${cards.join('')}</svg>`;

await sharp(path.join(repoRoot, 'assets/images/ecosystem/ai-sdk-provider-network.webp'))
	.resize(1200, 630, { fit: 'cover', position: 'center' })
	.composite([{ input: Buffer.from(svg), blend: 'over' }])
	.flatten({ background: '#fff' })
	.jpeg({ quality: 92, chromaSubsampling: '4:4:4', progressive: true })
	.toFile(path.join(repoRoot, 'assets/images/social/providers.jpg'));
console.log('Rendered provider social promo with 25 official local logos.');
