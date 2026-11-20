import fs from 'node:fs';
const records = JSON.parse(fs.readFileSync('assets/data/providers.json', 'utf8'));
const escape = value => String(value).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const statuses = {verified: 'Live verified', partial: 'Partly live verified', not_tested: 'Live testing pending'};
const cards = records.map(p => {
  const logo = p.logo ? `<img src="${escape(p.logo)}" alt="" width="56" height="56" loading="lazy">` : '';
  const setup = p.setup ? `<a href="${escape(p.setup)}">Setup</a>` : '';
  const date = p.verifiedDate ? ` · <time datetime="${escape(p.verifiedDate)}">${escape(p.verifiedDate)}</time>` : '';
  return `<article class="provider-card" data-provider-record="${escape(p.id)}"><div class="provider-card__top"><span class="provider-logo">${logo}</span><span class="sk-badge">${escape(p.category)}</span></div><h3>${escape(p.name)}</h3><p class="provider-card__description">${escape(p.description)}</p><p><code>${escape(p.package)}</code> · ${escape(p.protocol)}</p><p>${escape(statuses[p.verification] ?? p.verification)}${date}</p><div class="provider-card__footer"><a href="${escape(p.repo)}">Package source</a><a href="${escape(p.docs)}">Provider docs</a>${setup}</div><button type="button" class="sk-button" data-provider-id="${escape(p.id)}" hidden>Open ${escape(p.name)} starter</button></article>`;
}).join('\n');
const target = 'templates/page-providers.html';
const original = fs.readFileSync(target, 'utf8');
const rendered = original.replace(/data-provider-count>[^<]*</, `data-provider-count>${records.length} integrations<`).replace(/<!-- PROVIDERS START -->[\s\S]*?<!-- PROVIDERS END -->/, `<!-- PROVIDERS START -->\n${cards}\n<!-- PROVIDERS END -->`);
if (process.argv.includes('--check')) {
  if (original !== rendered) throw Error('Stale static provider directory; run npm run providers:generate');
} else fs.writeFileSync(target, rendered);
