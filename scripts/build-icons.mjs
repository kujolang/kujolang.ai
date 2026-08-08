import { mkdir, readFile, writeFile } from 'node:fs/promises';
import path from 'node:path';
import process from 'node:process';
import pngToIco from 'png-to-ico';
import sharp from 'sharp';

const repoRoot = path.resolve(import.meta.dirname, '..');
const sourcePath = path.join(repoRoot, 'assets/images/kujo-logomark.svg');
const iconDir = path.join(repoRoot, 'assets/icons');
const sourceSvg = await readFile(sourcePath, 'utf8');
const pathData = sourceSvg.match(/\bd="([\s\S]*?)"\s*\/>/)?.[1];

if (!pathData) {
	throw new Error('Could not read the Kujo logomark path.');
}

await mkdir(iconDir, { recursive: true });

const faviconSvg = sourceSvg.replace(
	/(<svg\b[^>]*>)/,
	'$1\n  <rect width="1527" height="1536" fill="#ffffff"/>',
);

if (faviconSvg === sourceSvg) {
	throw new Error('Could not add the favicon contrast layer to the Kujo logomark SVG.');
}

await writeFile(path.join(iconDir, 'favicon.svg'), faviconSvg);
await writeFile(path.join(iconDir, 'safari-pinned-tab.svg'), sourceSvg);

const renderSquare = async (size, filename) => {
	await sharp(Buffer.from(faviconSvg), { density: 512 })
		.resize(size, size, { fit: 'fill' })
		.png({ compressionLevel: 9, adaptiveFiltering: true, palette: true })
		.toFile(path.join(iconDir, filename));
};

await Promise.all([
	renderSquare(16, 'favicon-16x16.png'),
	renderSquare(32, 'favicon-32x32.png'),
	renderSquare(48, 'favicon-48x48.png'),
	renderSquare(150, 'mstile-150x150.png'),
	renderSquare(180, 'apple-touch-icon.png'),
	renderSquare(192, 'android-chrome-192x192.png'),
	renderSquare(512, 'android-chrome-512x512.png'),
]);

const maskableSvg = `
<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512">
  <defs>
    <mask id="kujo-k" maskUnits="userSpaceOnUse" x="0" y="0" width="512" height="512">
      <rect width="512" height="512" fill="#000000"/>
      <g transform="translate(51 51) scale(0.2685 0.2669)">
        <rect width="1527" height="1536" fill="#ffffff"/>
        <path fill="#000000" fill-rule="evenodd" d="${pathData}"/>
      </g>
    </mask>
  </defs>
  <rect width="512" height="512" fill="#000000"/>
  <rect width="512" height="512" fill="#ffffff" mask="url(#kujo-k)"/>
</svg>`;

await sharp(Buffer.from(maskableSvg), { density: 512 })
	.resize(512, 512, { fit: 'fill' })
	.png({ compressionLevel: 9, adaptiveFiltering: true, palette: true })
	.toFile(path.join(iconDir, 'maskable-icon-512x512.png'));

const ico = await pngToIco([
	path.join(iconDir, 'favicon-16x16.png'),
	path.join(iconDir, 'favicon-32x32.png'),
	path.join(iconDir, 'favicon-48x48.png'),
]);
await writeFile(path.join(iconDir, 'favicon.ico'), ico);

process.stdout.write(`Built Kujo favicon assets in ${iconDir}\n`);
