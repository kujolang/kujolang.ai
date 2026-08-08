import { readFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import process from 'node:process';
import sharp from 'sharp';

const [inputDir, outputDir, manifestPath] = process.argv.slice(2);

if (!inputDir || !outputDir || !manifestPath) {
	console.error('Usage: node scripts/rasterize-social-cards.mjs INPUT_DIR OUTPUT_DIR MANIFEST');
	process.exit(1);
}

const manifest = JSON.parse(await readFile(manifestPath, 'utf8'));
const manifestDir = path.dirname(manifestPath);
const cards = new Map(manifest.cards.map((card) => [card.id, card]));
const files = (await readdir(inputDir)).filter((file) => file.endsWith('.svg')).sort();

for (const file of files) {
	const id = path.basename(file, '.svg');
	const card = cards.get(id);
	if (!card?.background_image) {
		throw new Error(`Missing background_image for social card: ${id}`);
	}
	const backgroundPath = path.resolve(manifestDir, card.background_image);
	const overlay = await sharp(path.join(inputDir, file), { density: 144 })
		.resize(1200, 630, { fit: 'fill' })
		.png()
		.toBuffer();
	await sharp(backgroundPath)
		.resize(1200, 630, { fit: 'cover', position: 'center' })
		.composite([{ input: overlay, blend: 'over' }])
		.flatten({ background: '#ffffff' })
		.jpeg({ quality: 90, chromaSubsampling: '4:4:4', progressive: true })
		.toFile(path.join(outputDir, `${id}.jpg`));
}

await sharp(path.join(outputDir, 'home.jpg'))
	.png({ compressionLevel: 9 })
	.toFile(path.join(manifestDir, 'assets/images/og.png'));

console.log(`Rasterized ${files.length} Howl SVG cards.`);
