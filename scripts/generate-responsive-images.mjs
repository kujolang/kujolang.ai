#!/usr/bin/env node

import { readdir, rename, stat, unlink } from "node:fs/promises";
import path from "node:path";
import process from "node:process";
import sharp from "sharp";

export const RESPONSIVE_WIDTHS = [640, 960, 1280];

export function responsivePathFor(sourcePath, width = RESPONSIVE_WIDTHS[0]) {
  const extension = path.extname(sourcePath);
  return `${sourcePath.slice(0, -extension.length)}-${width}${extension}`;
}

async function webpFiles(directory) {
  const entries = await readdir(directory, { withFileTypes: true });
  const files = [];
  for (const entry of entries) {
    const target = path.join(directory, entry.name);
    if (entry.isDirectory()) {
      files.push(...await webpFiles(target));
    } else if (entry.isFile() && entry.name.endsWith(".webp") && !RESPONSIVE_WIDTHS.some((width) => entry.name.endsWith(`-${width}.webp`))) {
      files.push(target);
    }
  }
  return files.sort();
}

export async function generateResponsiveImages(outputDirectory = "output") {
  const root = path.resolve(outputDirectory);
  const rootStats = await stat(root);
  if (!rootStats.isDirectory()) {
    throw new Error(`Responsive image root is not a directory: ${root}`);
  }

  let generated = 0;
  let skipped = 0;
  for (const source of await webpFiles(root)) {
    const metadata = await sharp(source).metadata();
    for (const width of RESPONSIVE_WIDTHS) {
      if (!metadata.width || metadata.width <= width) {
        skipped += 1;
        continue;
      }

      const destination = responsivePathFor(source, width);
      const temporary = `${destination}.tmp`;
      try {
        await sharp(source)
          .resize({ width, withoutEnlargement: true })
          .webp({ quality: 80, effort: 6 })
          .toFile(temporary);
        await rename(temporary, destination);
      } catch (error) {
        await unlink(temporary).catch(() => {});
        throw error;
      }
      generated += 1;
    }
  }

  return { generated, skipped, widths: RESPONSIVE_WIDTHS, root };
}

if (import.meta.url === `file://${process.argv[1]}`) {
  const outputDirectory = process.argv[2] ?? "output";
  const result = await generateResponsiveImages(outputDirectory);
  process.stdout.write(`Generated ${result.generated} responsive images at ${result.widths.join("/")}px; skipped ${result.skipped}.\n`);
}
