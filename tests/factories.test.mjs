import { createHash } from 'node:crypto';
import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { execFileSync } from 'node:child_process';

const root = path.resolve(import.meta.dirname, '..');
const slugs = ['software-factory', 'videoops-factory', 'publishing-house-factory', 'webops-factory', 'product-launch-factory'];
const read = file => fs.readFileSync(path.join(root, file), 'utf8');
const field = (source, key) => source.match(new RegExp(`^${key}:\\s*["']?([^\\n"']+)`, 'm'))?.[1]?.trim();
const pages = fs.readdirSync(path.join(root, 'content/ecosystem')).filter(file => file.endsWith('.md')).map(file => ({file, source: read(`content/ecosystem/${file}`)}));
const factories = pages.filter(page => field(page.source, 'section') === 'Factories');

test('factory category contains exactly the five intended repositories and unique routes', () => {
  assert.deepEqual(factories.map(page => field(page.source, 'custom_url')).sort(), [...slugs].sort());
  const routes = pages.map(page => field(page.source, 'custom_url'));
  assert.equal(new Set(routes).size, routes.length, 'ecosystem routes must stay unique');
  for (const page of factories) {
    const slug = field(page.source, 'custom_url');
    assert.equal(field(page.source, 'github_url'), `https://github.com/kujolang/${slug}`);
  }
  assert.equal(field(read('content/pages/factories.md'), 'custom_url'), 'ecosystem/factories');
});

test('factory pages explain inputs, execution, evidence, review, setup and limits', () => {
  for (const {file, source} of factories) {
    const headings = source.match(/^## .+$/gm)?.join('\n') || '';
    for (const concept of [/give|inputs/i, /happens|workflow/i, /receive|outputs/i, /factory floor/i, /accountability|verification/i, /demo/i, /installation|first run|setup/i, /release|limitations/i, /related/i]) {
      assert.match(headings, concept, `${file}: missing ${concept}`);
    }
    assert.match(source, /human|your approval|review[^.]*yourself/i, `${file}: review authority`);
    assert.match(source, /github\.com\/kujolang\/[^/]+\/blob\/[a-f0-9]{40}\//, `${file}: immutable source reference`);
  }
});

test('factory image, demo and social references resolve to authored assets', () => {
  const cards = JSON.parse(read('howl-social.json')).cards;
  for (const slug of [...slugs, 'factories']) {
    const card = cards.filter(card => card.id === slug);
    assert.equal(card.length, 1, `${slug}: one social card`);
    assert.ok(fs.existsSync(path.join(root, card[0].background_image)), `${slug}: hero exists`);
    assert.ok(fs.existsSync(path.join(root, `assets/images/social/${slug}.jpg`)), `${slug}: social raster exists`);
  }
  for (const slug of slugs) {
    const media = read(`templates/factory-media/${slug}.html`);
    assert.match(media, /<video\b[^>]*\bcontrols\b/);
    assert.match(media, /preload="none"/);
    assert.doesNotMatch(media, /autoplay/);
    assert.match(media, /poster="[^"]+"/);
    const videos = [...media.matchAll(/(?:src|href)="([^"]+\.mp4(?:\?[^" ]*)?)"/g)].map(match => match[1]);
    assert.ok(videos.length >= 2, `${slug}: playable source and download fallback`);
    const mirror = JSON.parse(read('docs/factories/video-mirrors.json')).find(item => item.factory === slug);
    assert.ok(videos.includes('/' + mirror.local.replace(/^public\//, '')));
    assert.ok(videos.includes(mirror.upstream));
    assert.equal(createHash('sha256').update(fs.readFileSync(path.join(root, mirror.local))).digest('hex'), mirror.sha256);
    for (const match of media.matchAll(/(?:src|poster)="(\/assets\/[^" ]+)"/g)) assert.ok(fs.existsSync(path.join(root, match[1])), match[1]);
    assert.ok(fs.existsSync(path.join(root, `assets/images/factories/${slug}-floor.webp`)), `${slug}: authentic floor visual`);
  }
  assert.match(read('templates/factory-media/product-launch-factory.html'), /releases\/download\/v0\.1\.0\/launch\.mp4/);
});

test('related ecosystem references name existing canonical pages', () => {
  const routes = new Set([...pages.map(page => field(page.source, 'custom_url')), 'factories', 'skills', 'workflows', 'primitives', 'tooling', 'showcase']);
  for (const {file, source} of factories) {
    for (const match of source.matchAll(/\]\(\/ecosystem\/([^/)]+)\/\)/g)) assert.ok(routes.has(match[1]), `${file}: ${match[1]}`);
  }
});

test('release claims match verified publication records and clone commands follow main', () => {
  const matrix = JSON.parse(read('docs/factories/capability-matrix.json'));
  for (const {source} of factories) {
    const slug = field(source, 'custom_url');
    const record = matrix.factories.find(factory => factory.id === slug);
    assert.equal(field(source, 'latest_release_url'), record.release_url);
    assert.equal(field(source, 'release_status'), `Published ${record.release_tag}`);
    assert.doesNotMatch(field(source, 'install_command'), /checkout|--branch/);
    assert.doesNotMatch(source, /no published GitHub Release|Source preview/i);
  }
});

test('normal catalog synchronization preserves factory pages and cards', () => {
  const temporary = fs.mkdtempSync(path.join(os.tmpdir(), 'kujo-factory-sync-'));
  try {
    const site = path.join(temporary, 'site');
    for (const dir of ['scripts', 'content/ecosystem', 'content/pages', 'assets/prompts']) fs.mkdirSync(path.join(site, dir), {recursive: true});
    fs.copyFileSync(path.join(root, 'scripts/sync-ecosystem-catalogs.mjs'), path.join(site, 'scripts/sync-ecosystem-catalogs.mjs'));
    for (const {file, source} of pages) fs.writeFileSync(path.join(site, 'content/ecosystem', file), source);
    fs.copyFileSync(path.join(root, 'content/pages/factories.md'), path.join(site, 'content/pages/factories.md'));
    fs.copyFileSync(path.join(root, 'howl-social.json'), path.join(site, 'howl-social.json'));
    // Minimal real Git catalogs keep this regression deterministic and independent of sibling checkouts.
    for (const repo of ['kujo-skills', 'kujo-workflows']) {
      const dir = path.join(temporary, repo);
      fs.mkdirSync(dir);
      fs.writeFileSync(path.join(dir, 'VERSION'), '0.0.0\n');
      if (repo === 'kujo-skills') {
        fs.mkdirSync(path.join(dir, 'skills/check'), {recursive: true});
        fs.writeFileSync(path.join(dir, 'skills/check/SKILL.md'), '---\ndescription: Fixture catalog guidance.\n---\n# Check\n');
      } else {
        fs.mkdirSync(path.join(dir, 'docs/audit'), {recursive: true});
        fs.writeFileSync(path.join(dir, 'docs/audit/workflow-catalog.json'), JSON.stringify({active_workflows: []}));
      }
      const git = (...args) => execFileSync('git', ['-C', dir, ...args], {stdio: 'pipe'});
      git('init', '-q'); git('add', '.'); git('-c', 'user.name=Fixture', '-c', 'user.email=fixture@example.invalid', '-c', 'commit.gpgsign=false', 'commit', '-qm', 'catalog fixture');
      git('tag', 'fixture');
    }
    execFileSync(process.execPath, [path.join(site, 'scripts/sync-ecosystem-catalogs.mjs')], {env: {...process.env, KUJO_REPOS: temporary, KUJO_SKILLS_REF: 'fixture', KUJO_WORKFLOWS_REF: 'fixture'}, stdio: 'pipe'});
    for (const {file, source} of pages) assert.equal(fs.readFileSync(path.join(site, 'content/ecosystem', file), 'utf8'), source, `${file}: preserved byte-for-byte`);
    assert.equal(fs.readFileSync(path.join(site, 'content/pages/factories.md'), 'utf8'), read('content/pages/factories.md'));
    const originalCards = JSON.parse(read('howl-social.json')).cards;
    const syncedCards = JSON.parse(fs.readFileSync(path.join(site, 'howl-social.json'), 'utf8')).cards;
    for (const slug of [...slugs, 'factories']) assert.deepEqual(syncedCards.find(card => card.id === slug), originalCards.find(card => card.id === slug));
  } finally {
    fs.rmSync(temporary, {recursive: true, force: true});
  }
});

test('built routes retain canonicals, metadata, search and sitemap inclusion', {skip: !process.env.FACTORIES_OUTPUT}, () => {
  const output = path.resolve(root, process.env.FACTORIES_OUTPUT);
  const index = JSON.parse(fs.readFileSync(path.join(output, '.well-known/kujo-site-index.json'), 'utf8'));
  const sitemap = fs.readFileSync(path.join(output, 'sitemap.xml'), 'utf8');
  for (const slug of [...slugs, 'factories']) {
    const route = `https://kujolang.ai/ecosystem/${slug}/`;
    const html = fs.readFileSync(path.join(output, `ecosystem/${slug}/index.html`), 'utf8');
    assert.equal((html.match(/rel="canonical"/g) || []).length, 1);
    assert.ok(html.includes(`href="${route}"`), `${slug}: canonical`);
    for (const property of ['og:title', 'og:description', 'og:image', 'twitter:card']) assert.ok(html.includes(property), `${slug}: ${property}`);
    assert.ok(html.includes(`/assets/images/social/${slug}.jpg`));
    assert.ok(sitemap.includes(`<loc>${route}</loc>`), `${slug}: sitemap`);
    assert.equal(index.items.filter(item => new URL(item.url, "https://kujolang.ai").href === route).length, 1, `${slug}: searchable exactly once`);
  }
  for (const page of pages) assert.ok(fs.existsSync(path.join(output, `ecosystem/${field(page.source, 'custom_url')}/index.html`)), `${page.file}: existing route retained`);
});
