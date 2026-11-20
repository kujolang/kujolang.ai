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
const lobeIcons = 'https://raw.githubusercontent.com/lobehub/lobe-icons/9752d967494e48d8f83f2808feb2b0207bf70997/packages/static-svg/icons/';
const logos = {
  'lm-studio': lobeIcons + 'lmstudio.svg',
  vllm: lobeIcons + 'vllm-color.svg',
  'llama-cpp': 'https://raw.githubusercontent.com/ggml-org/llama.brand/9e91eb167731ae69a3f2108b3b577b6baf32dede/logo/svg/icon/icon-light.svg',
  sglang: 'https://raw.githubusercontent.com/sgl-project/sglang/d675c98bc76df951eec83196063cf2e546e0753d/assets/logo_square.svg',
  moonshot: lobeIcons + 'kimi-color.svg',
  minimax: lobeIcons + 'minimax-color.svg',
  siliconflow: lobeIcons + 'siliconcloud-color.svg',
  novita: lobeIcons + 'novita-color.svg',
  voyage: lobeIcons + 'voyage-color.svg',
  jina: lobeIcons + 'jina.svg',
};

const descriptions = {
  'llama-cpp': 'Run GGUF models locally with llama-server. Tool calling depends on the model and chat template. Embeddings require a pooling mode.',
  jina: 'Generate embeddings, rerank documents, or extract text from a URL with Jina Reader. Set a Jina API key for authenticated requests.',
};
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
    description: descriptions[provider.id] ?? provider.limitations,
    ...(logos[provider.id] && {
      logo: '/assets/images/providers/' + provider.id + '.svg',
      logo_source: logos[provider.id],
    }),
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
