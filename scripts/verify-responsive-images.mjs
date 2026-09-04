#!/usr/bin/env node

import { access, readFile, readdir } from "node:fs/promises";
import path from "node:path";
import process from "node:process";

async function filesWithExtension(directory, extension) {
  const entries = await readdir(directory, { withFileTypes: true });
  const files = [];
  for (const entry of entries) {
    const target = path.join(directory, entry.name);
    if (entry.isDirectory()) {
      files.push(...await filesWithExtension(target, extension));
    } else if (entry.isFile() && entry.name.endsWith(extension)) {
      files.push(target);
    }
  }
  return files.sort();
}

function attribute(tag, name) {
  return tag.match(new RegExp(`\\b${name}="([^"]*)"`))?.[1] ?? "";
}

function localPathForUrl(outputRoot, htmlFile, url) {
  const clean = url.split(/[?#]/, 1)[0];
  return clean.startsWith("/")
    ? path.join(outputRoot, clean.slice(1))
    : path.resolve(path.dirname(htmlFile), clean);
}

export async function verifyResponsiveImages(outputDirectory = "output") {
  const outputRoot = path.resolve(outputDirectory);
  const failures = [];
  let checked = 0;

  for (const htmlFile of await filesWithExtension(outputRoot, ".html")) {
    const html = await readFile(htmlFile, "utf8");
    const imageTags = html.match(/<img\b[^>]*>/g) ?? [];
    for (const tag of imageTags) {
      const className = attribute(tag, "class");
      if (!className.split(/\s+/).some((name) => name === "featured-image" || name === "listing-card-image")) {
        continue;
      }
      const source = attribute(tag, "src");
      if (!source.toLowerCase().split(/[?#]/, 1)[0].endsWith(".webp") || /^(?:https?:)?\/\//i.test(source)) {
        continue;
      }

      checked += 1;
      const srcset = attribute(tag, "srcset");
      const sizes = attribute(tag, "sizes");
      const responsiveUrls = [640, 960, 1280].map((width) => [width, source.replace(/\.webp(?=([?#]|$))/i, `-${width}.webp`)]);
      if (!responsiveUrls.every(([width, url]) => srcset.includes(`${url} ${width}w`)) || !srcset.includes(source) || !sizes) {
        failures.push(`${path.relative(outputRoot, htmlFile)}: missing responsive srcset/sizes for ${source}`);
        continue;
      }
      for (const [, responsiveUrl] of responsiveUrls) {
        try {
          await access(localPathForUrl(outputRoot, htmlFile, responsiveUrl));
        } catch {
          failures.push(`${path.relative(outputRoot, htmlFile)}: missing generated file for ${responsiveUrl}`);
        }
      }
    }
  }

  if (checked === 0) {
    failures.push("no local featured or listing WebP images were found");
  }
  if (failures.length > 0) {
    throw new Error(failures.join("\n"));
  }
  return { checked, outputRoot };
}

if (import.meta.url === `file://${process.argv[1]}`) {
  const result = await verifyResponsiveImages(process.argv[2] ?? "output");
  process.stdout.write(`Responsive image contract passed for ${result.checked} rendered images.\n`);
}
