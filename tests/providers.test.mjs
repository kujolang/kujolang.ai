import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';

const registry = JSON.parse(await readFile(new URL('../assets/data/providers.json', import.meta.url), 'utf8'));

test('provider registry contains each requested integration exactly once', () => {
  assert.equal(registry.length, 35);
  assert.equal(new Set(registry.map((provider) => provider.id)).size, 35);
  for (const provider of registry) {
    assert.match(provider.repo, /^https:\/\/github\.com\/kujolang\//);
    if (provider.logo) assert.match(provider.logo, /^\/assets\/images\/providers\//);
    assert.ok(provider.docs && provider.code && provider.install);
    assert.match(provider.certificationRevision, /^[a-f0-9]{40}$/);
    assert.ok(['verified', 'partial', 'not_tested'].includes(provider.verification));
    assert.equal(!!provider.verifiedDate, provider.verification !== 'not_tested');
  }
});

test('every registered local logo exists', async () => {
  for (const provider of registry) {
    if (!provider.logo) continue;
    const path = new URL(`..${provider.logo}`, import.meta.url);
    const logo = await readFile(path);
    assert.ok(logo.length > 32, provider.id);
  }
});
