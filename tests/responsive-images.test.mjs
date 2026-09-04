import assert from "node:assert/strict";
import { mkdtemp, readFile, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import path from "node:path";
import { afterEach, test } from "node:test";
import sharp from "sharp";
import { generateResponsiveImages, responsivePathFor } from "../scripts/generate-responsive-images.mjs";

const temporaryDirectories = [];

afterEach(async () => {
  await Promise.all(temporaryDirectories.splice(0).map((directory) => rm(directory, { recursive: true, force: true })));
});

test("creates deterministic responsive WebP variants without enlarging small images", async () => {
  const directory = await mkdtemp(path.join(tmpdir(), "kujo-responsive-images-"));
  temporaryDirectories.push(directory);
  const large = path.join(directory, "large.webp");
  const small = path.join(directory, "small.webp");
  await sharp({ create: { width: 1600, height: 800, channels: 3, background: "#111111" } }).webp().toFile(large);
  await sharp({ create: { width: 320, height: 180, channels: 3, background: "#eeeeee" } }).webp().toFile(small);

  const first = await generateResponsiveImages(directory);
  assert.equal(first.generated, 3);
  assert.equal(first.skipped, 3);
  const destination = responsivePathFor(large);
  assert.equal((await sharp(destination).metadata()).width, 640);
  assert.equal((await sharp(responsivePathFor(large, 960)).metadata()).width, 960);
  assert.equal((await sharp(responsivePathFor(large, 1280)).metadata()).width, 1280);
  const firstBytes = await readFile(destination);

  const second = await generateResponsiveImages(directory);
  assert.equal(second.generated, 3);
  assert.deepEqual(await readFile(destination), firstBytes);
  await assert.rejects(readFile(responsivePathFor(small)), { code: "ENOENT" });
});
