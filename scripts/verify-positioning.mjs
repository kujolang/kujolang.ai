import fs from 'node:fs';
import { createHash } from 'node:crypto';
import assert from 'node:assert/strict';
import path from 'node:path';
const root = process.argv[2] || 'output';
for (const route of ['integrations', 'agent-accountability', 'providers', 'ecosystem/muzzle']) {
  const html = fs.readFileSync(path.join(root, route, 'index.html'), 'utf8');
  assert.equal((html.match(/<h1(?:\s|>)/g) || []).length, 1, `${route}: one H1`);
  assert(html.includes(`rel="canonical" href="https://kujolang.ai/${route}/"`), `${route}: canonical`);
  for (const [, href] of html.matchAll(/href="(\/[^"#?]*)/g)) {
    if (href.startsWith('//')) continue;
    assert(fs.existsSync(path.join(root, href, href.endsWith('/') ? 'index.html' : '')), `${route}: broken local link ${href}`);
  }
}
const providers = JSON.parse(fs.readFileSync('assets/data/providers.json', 'utf8'));
const html = fs.readFileSync(path.join(root, 'providers/index.html'), 'utf8');
const scriptVersion = createHash('md5').update(fs.readFileSync('assets/js/providers.js')).digest('hex').slice(0, 12);
assert(html.includes(`src="/assets/js/providers.js?v=${scriptVersion}"`), 'Provider enhancement must use its content hash to invalidate stale scripts');
for (const provider of providers) assert(html.includes(`href="${provider.repo}"`), `Missing static package ${provider.id}`);
console.log('Positioning routes: single H1, canonicals, local links and static provider coverage passed.');
