import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';

const siteRoot = path.resolve(import.meta.dirname, '..');
const reposRoot = path.resolve(siteRoot, '..', 'kujo-repos');
const skillsRepo = path.join(reposRoot, 'kujo-skills');
const workflowsRepo = path.join(reposRoot, 'kujo-workflows');

function git(repo, ...args) {
  return execFileSync('git', ['-C', repo, ...args], { encoding: 'utf8' });
}

function releasedFile(repo, file) {
  return git(repo, 'show', `origin/main:${file}`);
}

function yamlString(value) {
  return JSON.stringify(String(value).replace(/\s+/g, ' ').trim());
}

function frontmatterValue(source, key) {
  const match = source.match(new RegExp(`^${key}:\\s*(.+)$`, 'm'));
  if (!match) return '';
  const raw = match[1].trim();
  if ((raw.startsWith('"') && raw.endsWith('"')) || (raw.startsWith("'") && raw.endsWith("'"))) return raw.slice(1, -1);
  return raw;
}

function titleFromMarkdown(source, fallback) {
  const title = source.match(/^#\s+(.+)$/m)?.[1]?.trim() || fallback;
  return title
    .replace(/\bContentgraph\b/g, 'ContentGraph')
    .replace(/\bWebops\b/g, 'WebOps')
    .replace(/\bSite Kit\b/g, 'SiteKit')
    .replace(/\bSitekit\b/g, 'SiteKit');
}

function usefulBullets(source) {
  return source.split('\n')
    .map((line) => line.trim())
    .filter((line) => /^-\s+/.test(line) && !/^-(?:\s+)?Status:/.test(line))
    .slice(0, 5);
}

function words(value) {
  return value.replace(/^kujo-/, '').replace(/-workflows$/, '').replace(/-/g, ' ');
}

function skillCatalogExcerpt(description) {
  const summary = description.split(/:\s/)[0].replace(/\s+/g, ' ').trim();
  const parts = summary.split(' ');
  if (parts.length <= 24) return /[.!?]$/.test(summary) ? summary : `${summary}.`;
  return `${parts.slice(0, 24).join(' ')}…`;
}

const objectRules = [
  [/assetworks/, 'media production bench with render adapters checksum manifest and accessibility artifact trays'],
  [/bluepencil/, 'editorial review desk with eight calibration gauges and blocker verdict stamps'],
  [/dossier/, 'evidence ledger desk linking claim cards to captured source fragments'],
  [/galleypack/, 'immutable package press binding artifacts evidence records and review seals'],
  [/presswire/, 'guarded publication switchboard with approval seal and destination adapters'],
  [/publishing-house-workflows/, 'editorial lifecycle floor with separated authority desks and receipt handoff trays'],
  [/readersignal/, 'privacy-bounded audience measurement console with uncertainty gauges and feedback cards'],
  [/storydesk/, 'editorial planning desk with campaign queues assignment cards and handoff lanes'],
  [/versionseal/, 'human approval station sealing an exact checksum to a destination action card'],
  [/way-development/, 'engineering workbench with routing map contract cards and verification gates'],
  [/publishing-house-profile/, 'cabinet holding house brand audience and permission-boundary cards'],
  [/publishing-house-quality/, 'blind editorial comparison bench with eight scoring gauges and a blocker seal'],
  [/accessibility/, 'tactile inspection desk with contrast gauges and navigation controls'],
  [/ai-search|visibility/, 'signal observatory with citation lenses and query beacons'],
  [/analytics|search-performance/, 'measurement console with trend reels and evidence meters'],
  [/backlink|mention/, 'link-analysis table with connected citation pins and archive trays'],
  [/cannibalization/, 'two competing signal transmitters converging on one receiver'],
  [/capability-preflight/, 'preflight inspection bench with sealed capability modules'],
  [/competitor/, 'public intelligence map table with comparison lenses'],
  [/content-accuracy/, 'fact-checking desk with source files and calibration instruments'],
  [/content-decay|pruning/, 'archive conservation table with aging documents and review trays'],
  [/content-gap/, 'topic map with one clearly missing structural tile'],
  [/content-portfolio/, 'portfolio sorting table with evidence folders and decision bins'],
  [/distribution/, 'publication routing press with outbound channel trays'],
  [/indexation/, 'search index cabinet with crawl gates and canonical drawers'],
  [/information-architecture/, 'website blueprint table with hierarchical route blocks'],
  [/internal-linking/, 'interconnected document table with contextual bridge lines'],
  [/keyword/, 'query research console with clustered signal tokens'],
  [/link-health/, 'network continuity tester attached to a web of cables'],
  [/longitudinal/, 'timeline evidence bench with aligned historical measurement reels'],
  [/reporting/, 'quiet reporting desk with verified evidence trays and summary press'],
  [/schema|metadata/, 'structured-data drafting table with nested semantic blocks'],
  [/standards-watch/, 'standards observatory with update signals and source archives'],
  [/submission/, 'controlled dispatch gate with approved URL packets'],
  [/site-profile/, 'portable website identity dossier beside a configuration console'],
  [/technical-seo/, 'crawler diagnostics bench with sitemap and canonical instruments'],
  [/web-performance/, 'performance wind tunnel testing a webpage frame'],
  [/security|hardening|dependabot/, 'locked evidence vault with inspection lamp and guarded access panel'],
  [/language|standard-library|runtime-parity/, 'mechanical typesetting bench with modular grammar and runtime blocks'],
  [/implementation|tool-building/, 'language workshop with compiler gears and a code assembly bench'],
  [/cli-contract/, 'command console with separate output channels and exit gates'],
  [/testing|eval|readiness|release-gate/, 'calibration rig with deterministic pass and failure gates'],
  [/maintainer-review|auditor|docs-drift|backlog/, 'maintainer review desk with diff sheets and evidence stamps'],
  [/docgen/, 'documentation press with source pages and generated reference trays'],
  [/enterprise-automation/, 'enterprise automation control room with isolated job cells'],
  [/agent|dispatch|relay/, 'agent orchestration console with bounded handoff trays'],
  [/chat/, 'conversation relay desk with paired communication terminals'],
  [/sdk|mcp/, 'modular provider patch bay with guarded adapter sockets'],
  [/casefile/, 'incident evidence desk with sealed case folders and redaction tools'],
  [/changebucket/, 'change-footprint weighing station with categorized file bins'],
  [/cms/, 'content operations room with delivery shelves and migration controls'],
  [/concord/, 'artifact alignment table with synchronized document frames'],
  [/contentgraph/, 'content relationship map with connected document nodes'],
  [/crud-api/, 'application service bench with database and interface modules'],
  [/fence/, 'architectural boundary model with guarded dependency crossings'],
  [/howl/, 'printmaking station rendering social cards from source artifacts'],
  [/kennel/, 'package registry storeroom with lockboxes and trust checkpoints'],
  [/lens/, 'browser inspection rig with screenshot and accessibility instruments'],
  [/loop-engineering/, 'bounded engineering loop console with evaluation and stop gates'],
  [/muzzle/, 'quiet workflow console with filtered logs and controlled output'],
  [/packwrite/, 'execution-pack assembly desk with prompts and validation seals'],
  [/patchbrief/, 'git diff briefing table with reviewer handoff folders'],
  [/rag/, 'knowledge retrieval archive with citation drawers and namespace gates'],
  [/redact/, 'document sanitization station with blackout tools and audit tray'],
  [/runledger/, 'run receipt ledger desk with usage meters and verdict stamps'],
  [/scent/, 'context packing bench with budget scale and selected file bundles'],
  [/scout/, 'codebase survey table with repository maps and context packets'],
  [/searchbridge/, 'search provider relay console with normalized evidence channels'],
  [/shipcheck/, 'release inspection dock with checklist gates and sealed containers'],
  [/site-?kit/, 'interface component drafting table with accessible control samples'],
  [/siteprobe/, 'website crawler station scanning linked page structures'],
  [/spec/, 'task contract drafting table with acceptance gates and export trays'],
  [/ssg/, 'static site printing press with templates and generated page stacks'],
  [/tribunal/, 'adversarial review chamber with evidence bench and decision seal'],
  [/watchdog/, 'local telemetry watch station with proxy gauges and alert beacon'],
  [/workcell/, 'sealed execution workcell with operator console and artifact bay']
];

function skillObject(slug) {
  const cue = words(slug).split(' ').slice(0, 3).join(' ');
  const prop = objectRules.find(([pattern]) => pattern.test(slug))?.[1] || 'repository guidance desk with source manuals and verification instruments';
  return `${cue} ${prop}`.split(' ').slice(0, 18).join(' ');
}

const workflowObjects = {
  'agency-runner': 'agency mission desk with resumable client task packets and proof trays',
  'agency-verified-fix-loop': 'verified repair loop bench with browser proof and handoff folders',
  'ai-sdk-muzzle-benchmark': 'dual-lane AI benchmark rig comparing raw and filtered output meters',
  'ai-sdk-watchdog-showcase': 'AI traffic proxy station with telemetry gauges and export reels',
  'casefile-incident-evidence-packet': 'incident capture desk with sealed redacted evidence packet',
  'docsgen-repo-contract-runner': 'repository documentation press producing contract pages and review packets',
  'enterprise-dispatch-approval-router': 'enterprise dispatch switchboard with a guarded human approval gate',
  'feature-card-workflow': 'feature task card moving through implementation proof and reviewer handoff stations',
  'howl-content-factory': 'content print factory rendering cards galleries and caption sheets',
  'loop-engineering': 'bounded engineering loop console with context evaluation and stop gates',
  'mcp-agent-gateway-review': 'constrained agent gateway checkpoint with tool manifests and safety inspection',
  'publishing-house-adaptation': 'versioned adaptation drafting bench with source-lineage spool and format trays',
  'publishing-house-format-production': 'multi-format production press feeding newsletter social case-study and media trays',
  'publishing-house-governance': 'portfolio decision table with mandate folder priority tokens and accountable handoff trays',
  'rag-enterprise-knowledge-gate': 'enterprise knowledge archive with namespace gate and citation drawers',
  'relay-lifecycle-handoff': 'mission relay station with pause resume export and delivery receipts',
  'tribunal-decision-gate': 'adversarial decision chamber with review evidence and verified receipt seal',
  'webops-ai-visibility-benchmark': 'AI search observatory running fixed queries across citation surfaces',
  'webops-content-refresh': 'content restoration desk with decay evidence approval gate and updated pages',
  'webops-finding-to-fix': 'website finding moving through proposal approval repair and verification gates',
  'webops-monthly-seo-review': 'monthly search review table consolidating specialist evidence packets',
  'webops-post-publish': 'post-publication control desk checking pages links submissions and receipts',
  'webops-quarterly-content-portfolio': 'quarterly content portfolio board with evidence folders and disposition bins',
  'webops-site-bootstrap': 'website baseline survey station with crawler browser and graph instruments',
  'webops-weekly-content-intelligence': 'weekly content intelligence desk connecting trends gaps accuracy and links',
  'webops-weekly-search-intelligence': 'weekly search measurement console comparing queries trends and decay signals',
  'webops-weekly-site-health': 'weekly website health inspection rig with crawl performance and accessibility gauges',
  'workcell-execution-gate': 'sealed container execution gate with validation console and completion receipt tray'
};

function writePage(dir, order, slug, fields, body) {
  fs.mkdirSync(dir, { recursive: true });
  const name = `${String(order).padStart(3, '0')}-${slug}.md`;
  const lines = ['---'];
  for (const [key, value] of Object.entries(fields)) lines.push(`${key}: ${yamlString(value)}`);
  lines.push('---', '', body.trim(), '');
  fs.writeFileSync(path.join(dir, name), lines.join('\n'));
}

const skillPaths = git(skillsRepo, 'ls-tree', '-r', '--name-only', 'origin/main', 'skills')
  .split('\n').filter((file) => /^skills\/[^/]+\/SKILL\.md$/.test(file)).sort();
const skillVersion = releasedFile(skillsRepo, 'VERSION').trim();
const skillDate = git(skillsRepo, 'show', '-s', '--format=%cs', 'origin/main').trim();
const skillsDir = path.join(siteRoot, 'content', 'skills');
fs.rmSync(skillsDir, { recursive: true, force: true });

const targets = [
  {
    kind: 'skills-index', name: 'Skills', slug: 'skills',
    source_evidence: 'https://github.com/kujolang/kujo-skills/tree/main/skills',
    object_description: 'agent guidance library with modular field manuals and verification instruments',
    hero_path: 'assets/images/ecosystem/skills-agent-guidance-library.webp',
    social_path: 'assets/images/social/skills.jpg'
  }
];

const generatedCards = [{
  id: 'skills', title: 'Skills', tagline: `${skillPaths.length} repository-backed skills for Kujo and WebOps.`,
  file: 'social-card.txt', variant: 'social', label: 'collection', url: 'kujolang.ai/ecosystem/skills/',
  background_image: 'assets/images/ecosystem/skills-agent-guidance-library.webp',
  font_file: 'assets/css/fonts/DepartureMono-Regular.woff2', show_border: false, show_url: false
}];

skillPaths.forEach((skillPath, index) => {
  const source = releasedFile(skillsRepo, skillPath);
  const slug = skillPath.split('/')[1];
  const title = slug === 'kujo-site-kit-workflows'
    ? 'Kujo SiteKit Repository'
    : titleFromMarkdown(source, words(slug)).replace(/\s+Workflows$/i, '');
  const description = frontmatterValue(source, 'description');
  const heroPath = `assets/images/ecosystem/skill-${slug}.webp`;
  const sourceUrl = `https://github.com/kujolang/kujo-skills/blob/main/${skillPath}`;
  const bullets = usefulBullets(source);
  const body = `## What it covers\n\n${description}\n\n## Released guidance\n\n${bullets.length ? bullets.join('\n') : 'The released skill file defines the authoritative workflow, boundaries, sources, and validation guidance.'}\n\n## Release boundary\n\nThis page reflects the ${skillVersion} technical preview on ${skillDate}. The skill provides repository-backed guidance; the agent host remains responsible for permissions and enforcement.\n\n## Source\n\n- [Read the complete ${slug} skill on GitHub](${sourceUrl})\n- [Browse the released Kujo Skills Index](https://github.com/kujolang/kujo-skills/blob/main/SKILLS_INDEX.md)`;
  writePage(skillsDir, index + 1, slug, {
    title, custom_url: slug, description, excerpt: skillCatalogExcerpt(description),
    featured_image: `/${heroPath}`, social_image: `/assets/images/social/${slug}.jpg`,
    section: 'Agent Skill', order: (index + 1) * 10,
    install_command: `mkdir -p ~/.codex/skills && cp -R skills/${slug} ~/.codex/skills/`,
    github_url: sourceUrl,
    launch_story: `One of ${skillPaths.length} focused, repository-backed skills in the Kujo Skills ${skillVersion} technical preview.`,
    scope_note: 'Guidance only. The agent host must enforce permissions, capability limits, and approval boundaries.',
    version: skillVersion, last_updated: skillDate,
    keywords: `${title}, Kujo Agent Skill, ${slug}, repository-backed agent guidance`,
    seo_title: `${title} — Kujo Agent Skill`, seo_description: description
  }, body);
  targets.push({ kind: 'skill', name: title, slug, source_evidence: sourceUrl, object_description: skillObject(slug), hero_path: heroPath, social_path: `assets/images/social/${slug}.jpg` });
  generatedCards.push({
    id: slug, title, tagline: description, file: 'social-card.txt', variant: 'social', label: 'agent skill',
    url: `kujolang.ai/ecosystem/skills/${slug}/`, background_image: heroPath,
    font_file: 'assets/css/fonts/DepartureMono-Regular.woff2', show_border: false, show_url: false
  });
});

const workflowCatalog = JSON.parse(releasedFile(workflowsRepo, 'docs/audit/workflow-catalog.json'));
const workflowVersion = releasedFile(workflowsRepo, 'VERSION').trim();
const workflowDate = git(workflowsRepo, 'show', '-s', '--format=%cs', 'origin/main').trim();
const workflows = workflowCatalog.active_workflows;
const workflowsDir = path.join(siteRoot, 'content', 'workflows');
fs.rmSync(workflowsDir, { recursive: true, force: true });
targets.push({
  kind: 'workflows-index', name: 'Workflows', slug: 'workflows',
  source_evidence: 'https://github.com/kujolang/kujo-workflows',
  object_description: 'workflow evidence routing bench with approval gates and receipt trays',
  hero_path: 'assets/images/ecosystem/workflows-evidence-routing-bench.webp',
  social_path: 'assets/images/social/workflows.jpg'
});
generatedCards.push({
  id: 'workflows', title: 'Workflows', tagline: `${workflows.length} local-first workflow kits with inspectable evidence.`,
  file: 'social-card.txt', variant: 'social', label: 'collection', url: 'kujolang.ai/ecosystem/workflows/',
  background_image: 'assets/images/ecosystem/workflows-evidence-routing-bench.webp',
  font_file: 'assets/css/fonts/DepartureMono-Regular.woff2', show_border: false, show_url: false
});

workflows.forEach((workflow, index) => {
  const slug = workflow.id;
  const sourceUrl = `https://github.com/kujolang/kujo-workflows/tree/main/${workflow.path}`;
  const title = slug.split('-').map((part) => {
    if (part === 'webops') return 'WebOps';
    return /^(ai|sdk|mcp|rag|seo)$/.test(part) ? part.toUpperCase() : part[0].toUpperCase() + part.slice(1);
  }).join(' ');
  const readiness = workflow.production_readiness.replace(/-/g, ' ');
  const list = (items) => items.map((item) => `- ${item}`).join('\n');
  const body = `## Outcome\n\n${workflow.purpose}\n\n## Inputs\n\n${list(workflow.inputs)}\n\n## Evidence and outputs\n\n${list(workflow.outputs)}\n\nThe workflow's evidence contract is: ${workflow.evidence}.\n\n## Approval boundaries\n\n${list(workflow.approval_boundaries)}\n\n## State and recovery\n\n${workflow.state_and_recovery}\n\n## Release boundary\n\nReadiness is **${readiness}** in the ${workflowVersion} local technical preview. Hosted runners, broad live-provider coverage, and enterprise readiness are not implied.\n\n## Source\n\n- [Open the complete ${slug} workflow kit on GitHub](${sourceUrl})\n- [Browse the released workflow catalog](https://github.com/kujolang/kujo-workflows/blob/main/docs/audit/workflow-catalog.json)`;
  const heroPath = `assets/images/ecosystem/workflow-${slug}.webp`;
  writePage(workflowsDir, index + 1, slug, {
    title, custom_url: slug, description: workflow.purpose,
    featured_image: `/${heroPath}`, social_image: `/assets/images/social/${slug}.jpg`,
    section: readiness, order: (index + 1) * 10,
    install_command: `git clone https://github.com/kujolang/kujo-workflows.git && cd kujo-workflows && ${workflow.entry}`,
    github_url: sourceUrl,
    launch_story: `A local-first workflow kit with explicit inputs, outputs, evidence, recovery, and approval boundaries.`,
    scope_note: `Current readiness: ${readiness}. Review the workflow README before live-provider or host-affecting use.`,
    version: workflowVersion, last_updated: workflowDate,
    keywords: `${title}, Kujo workflow, ${slug}, local-first agent workflow`,
    seo_title: `${title} — Kujo Workflow`, seo_description: workflow.purpose
  }, body);
  targets.push({ kind: 'workflow', name: title, slug, source_evidence: sourceUrl, object_description: workflowObjects[slug], hero_path: heroPath, social_path: `assets/images/social/${slug}.jpg` });
  generatedCards.push({
    id: slug, title, tagline: workflow.purpose, file: 'social-card.txt', variant: 'social', label: 'workflow',
    url: `kujolang.ai/ecosystem/workflows/${slug}/`, background_image: heroPath,
    font_file: 'assets/css/fonts/DepartureMono-Regular.woff2', show_border: false, show_url: false
  });
});

const manifestPath = path.join(siteRoot, 'howl-social.json');
const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
manifest.cards = manifest.cards.filter((card) => !/^kujolang\.ai\/ecosystem\/(skills|workflows)\//.test(card.url || ''));
manifest.cards.push(...generatedCards);
fs.writeFileSync(manifestPath, `${JSON.stringify(manifest, null, 2)}\n`);

const targetsPath = path.join(siteRoot, 'assets', 'prompts', 'ecosystem-catalog-heroes.json');
fs.writeFileSync(targetsPath, `${JSON.stringify({
  contract: 'generate-kujo-dither-heroes/references/visual-contract.json',
  generated_with: 'ChatGPT built-in image generation; one call per target',
  dimensions: { width: 1916, height: 821 },
  targets
}, null, 2)}\n`);

console.log(JSON.stringify({ skills: skillPaths.length, workflows: workflows.length, targets: targets.length, cards: generatedCards.length }));
