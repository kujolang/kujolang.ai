import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';

const registry = JSON.parse(await readFile(new URL('../assets/data/providers.json', import.meta.url), 'utf8'));

test('provider registry contains each requested integration exactly once', () => {
  assert.equal(registry.length, 35);
  assert.equal(new Set(registry.map((provider) => provider.id)).size, 35);
  for (const provider of registry) {
    assert.match(provider.repo, /^https:\/\/github\.com\/kujolang\//);
    assert.match(provider.logo, /^\/assets\/images\/providers\//);
    if (provider.package === 'ai-sdk') {
      assert.equal(provider.logo, `/assets/images/providers/${provider.id}.svg`);
      assert.match(provider.logo_source, /^https:\/\/raw\.githubusercontent\.com\//);
    }
    assert.ok(provider.docs && provider.code && provider.install);
    assert.equal(provider.setup, 'https://docs.kujolang.ai/ecosystem/providers/#configure-a-provider');
    if (provider.package !== 'ai-sdk') {
      assert.match(provider.install, /kujo run "\$KENNEL_SCRIPT" -- add github:kujolang\//);
    }
    assert.match(provider.certificationRevision, /^[a-f0-9]{40}$/);
    assert.ok(['verified', 'partial', 'not_tested'].includes(provider.verification));
    assert.equal(!!provider.verifiedDate, provider.verification !== 'not_tested');
  }
});

test('every registered local logo exists', async () => {
  for (const provider of registry) {
    const path = new URL(`..${provider.logo}`, import.meta.url);
    const logo = await readFile(path);
    assert.ok(logo.length > 32, provider.id);
    if (provider.logo.endsWith('.svg')) assert.match(logo.toString(), /<svg\b/);
  }
});

test('public provider directory displays the registry count without verification labels', async () => {
  const template = await readFile(new URL('../templates/page-providers.html', import.meta.url), 'utf8');
  assert.match(template, new RegExp(`data-provider-filter="all"[^>]*>All <span data-provider-total>${registry.length}</span>`));
  assert.match(template, new RegExp(`data-provider-count>${registry.length} integrations`));
  assert.doesNotMatch(template, /data-provider-verification|live verification|(?:partly )?live verified|live testing pending/i);
});
