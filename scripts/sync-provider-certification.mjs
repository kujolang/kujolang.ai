import { readFileSync, writeFileSync } from 'node:fs';

const [, , manifestPath, revision, mode] = process.argv;
if (!manifestPath || !/^[a-f0-9]{40}$/.test(revision ?? '')) {
  throw Error('Usage: node scripts/sync-provider-certification.mjs <certification.json> <AI SDK commit> [--check]');
}
const manifest = JSON.parse(readFileSync(manifestPath, 'utf8'));
if (manifest.schema_version !== 1) throw Error('Unsupported provider certification schema');
const target = 'assets/data/providers.json';
const original = readFileSync(target, 'utf8');
const existing = new Map(JSON.parse(original).filter(row => row.package !== 'ai-sdk').map(row => [row.id, row]));
const seen = new Set();
const repo = 'https://github.com/kujolang/ai-sdk';
const records = manifest.providers.map(provider => {
  if (seen.has(provider.id)) throw Error('Duplicate provider ' + provider.id);
  seen.add(provider.id);
  const prior = existing.get(provider.id);
  if (!provider.base_url && !prior) throw Error('Missing base provider starter ' + provider.id);
  const script = provider.capabilities.chat === 'unsupported' ? 'embed' : 'chat';
  const starter = {
    id: provider.id,
    package: 'ai-sdk',
    repo: repo + '/tree/' + revision,
    setup: repo + '/blob/' + revision + '/docs/PROVIDER_SETUP.md',
    protocol: provider.integration_type === 'native' ? 'Native retrieval' : 'OpenAI-compatible',
    install: 'git clone ' + repo + '.git\ncd ai-sdk\ngit checkout ' + revision,
    code: 'KUJO_MODULE_PATH="$PWD/src" kujo run examples/provider_quickstart.kujo -- ' + provider.id + ' ' + script + ' YOUR_MODEL_ID',
    description: provider.limitations,
  };
  return {
    ...(prior ?? starter),
    name: provider.name,
    category: provider.category,
    docs: provider.documentation_url,
    integration: provider.integration_type,
    verification: provider.live_status,
    verifiedDate: provider.verification_date,
    capabilities: Object.keys(provider.capabilities).filter(key => ['verified', 'experimental'].includes(provider.capabilities[key])),
    certificationRevision: revision,
  };
});
for (const id of existing.keys()) {
  if (!seen.has(id)) throw Error('Provider absent from certification manifest ' + id);
}
const output = '[\n' + records.map(record => '  ' + JSON.stringify(record)).join(',\n') + '\n]\n';
if (mode === '--check') {
  if (output !== original) throw Error('Provider directory differs from the supplied certification manifest');
} else {
  writeFileSync(target, output);
}
