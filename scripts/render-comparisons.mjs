import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
export const statuses=['verified-supported','verified-unsupported','partially-supported','not-applicable','unknown'];
const nonempty=x=>typeof x==='string'&&x.trim().length>0;
export function validate(c){
 const errors=[];const must=(ok,msg)=>{if(!ok)errors.push(msg)};
 must(c.schemaVersion===1,'schemaVersion must be 1');
 const sources=c.sources??{},pages=c.pages??[],slugs=new Set();
 const refs=(r,where)=>{must(Array.isArray(r)&&r.length>0,`${where}: missing sources`);for(const id of r??[])must(!!sources[id],`${where}: unknown source ${id}`)};
 const date=(v)=>/^\d{4}-\d{2}-\d{2}$/.test(v??'')&&!Number.isNaN(Date.parse(v))&&new Date(v).toISOString().slice(0,10)===v;
 for(const [id,s] of Object.entries(sources)){
  must(nonempty(s.label)&&nonempty(s.level)&&nonempty(s.version),`${id}: incomplete source`);
  must(/^https:\/\//.test(s.url??''),`${id}: source must use https`);must(date(s.verified),`${id}: invalid verification date`);
 }
 const fact=(f,where)=>{must(!!f,`${where}: missing fact`);if(!f)return;must(nonempty(f.text)&&nonempty(f.layer),`${where}: missing text or layer`);must(statuses.includes(f.status),`${where}: invalid status`);refs(f.sources,where)};
 for(const [id,f] of Object.entries(c.kujoFacts??{}))fact(f,id);
 for(const p of pages){
  must(/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(p.slug??''),`invalid slug ${p.slug}`);must(!slugs.has(p.slug),`duplicate slug ${p.slug}`);slugs.add(p.slug);
  for(const field of ['title','description','summary'])must(nonempty(p[field]),`${p.slug}: missing ${field}`);
  must(date(p.verified),`${p.slug}: invalid verified date`);must(['direct','discovery','guide'].includes(p.kind),`${p.slug}: invalid kind`);refs(p.sources,p.slug);
  must(Array.isArray(p.sections)&&p.sections.length>0,`${p.slug}: missing sections`);
  for(const s of p.sections??[])must(nonempty(s.heading)&&nonempty(s.body),`${p.slug}: incomplete section`);
  if(p.kind==='direct'){
   const t=p.technology??{};for(const f of ['name','website','documentation','version'])must(nonempty(t[f]),`${p.slug}: missing technology ${f}`);
   must(nonempty(t.repository)||nonempty(t.repositoryNote),`${p.slug}: missing repository provenance`);
   must(Array.isArray(t.aliases),`${p.slug}: missing aliases`);
   for(const h of ['Technical architecture','When to choose Kujo',`When to choose ${t.name}`,'Can you use both?','Honest limitations','Examples and benchmark evidence'])must(p.sections.some(s=>s.heading===h),`${p.slug}: missing ${h}`);
   must(p.dimensions?.length>0,`${p.slug}: missing matrix`);
   for(const [label,id,f] of p.dimensions??[]){must(!!c.kujoFacts[id],`${p.slug}: unknown Kujo fact ${id}`);fact(f,`${p.slug}: ${label}`)}
  }
  must(p.faq?.length>0,`${p.slug}: missing FAQ`);
  for(const q of p.faq??[])must(q.length===2&&q.every(nonempty),`${p.slug}: invalid FAQ`);
 }
 for(const p of pages)for(const r of p.related??[])must(slugs.has(r)&&r!==p.slug,`${p.slug}: broken related reference ${r}`);
 if(errors.length)throw new Error(errors.join('\n'));return c;
}
const esc=s=>String(s).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');
const inline=s=>esc(s).replace(/`([^`]+)`/g,'<code>$1</code>').replace(/\[([^\]]+)\]\(([^)]+)\)/g,(_,label,url)=>{if(!/^(https:\/\/|\/)/.test(url))throw new Error('Unsafe link');return `<a href="${url}">${label}</a>`});
const link=(u,t)=>`<a href="${esc(u)}">${esc(t)}</a>`;
const labels={'verified-supported':'Verified supported','verified-unsupported':'Verified unsupported','partially-supported':'Partially supported','not-applicable':'Not applicable',unknown:'Unknown / not verified'};
function sourceLinks(ids,c){return ids.map(id=>link(c.sources[id].url,c.sources[id].label)).join('; ')}
function cell(f,c){return `<p class="comparison-status">${labels[f.status]} · ${esc(f.layer)}</p><p>${esc(f.text)}</p><p class="comparison-sources">${sourceLinks(f.sources,c)}</p>`}
function body(p,c){
 let h=`<p class="comparison-answer">${esc(p.summary)}</p>\n<p class="comparison-review">Last reviewed: <time datetime="${p.verified}">${p.verified}</time>. Written from Kujo’s perspective. ${link('/compare/editorial-policy.md','Editorial policy')} · ${link(`/compare/text/${p.slug}.md`,'Read as Markdown')}</p>`;
 if(p.technology){const t=p.technology;h+=`<section aria-label="Technology identity"><h2>At a glance</h2><dl><dt>Compared project</dt><dd>${link(t.website,t.name)} · ${link(t.documentation,'Documentation')}</dd><dt>Reviewed version</dt><dd>${esc(t.version)}</dd><dt>Repository</dt><dd>${t.repository?link(t.repository,'Canonical source'):esc(t.repositoryNote)}</dd><dt>Kujo baseline</dt><dd>Kujo 1.8.1 runtime and pinned ecosystem sources; no universal proof or performance claim.</dd></dl></section>`;
 h+=`<h2>Capability matrix</h2><p>Statuses describe the evidence reviewed, not a score. “Partially supported” includes documentation-only support without local reproduction; “unknown” never means unsupported. Language and ecosystem layers are named separately.</p><div class="comparison-table" role="region" aria-label="Scrollable capability comparison" tabindex="0"><table><caption>Kujo and ${esc(t.name)}: scope, evidence and limitations</caption><thead><tr><th scope="col">Dimension</th><th scope="col">Kujo</th><th scope="col">${esc(t.name)}</th></tr></thead><tbody>`;
 for(const [label,id,f]of p.dimensions)h+=`<tr><th scope="row">${esc(label)}</th><td>${cell(c.kujoFacts[id],c)}</td><td>${cell(f,c)}</td></tr>`;h+='</tbody></table></div>';
 }
 for(const s of p.sections)h+=`\n<section><h2>${esc(s.heading)}</h2><p>${inline(s.body)}</p></section>`;
 h+='<section><h2>Frequently asked questions</h2>';for(const[q,a]of p.faq)h+=`<h3>${esc(q)}</h3><p>${esc(a)}</p>`;h+='</section>';
 h+='<section><h2>Primary sources and verification</h2><p>Source inspection is not a successful runtime test. Dates below are recorded review dates, not automatic freshness timestamps.</p><ul>';
 const used=new Set(p.sources);for(const[,id,f]of p.dimensions??[])for(const s of [...c.kujoFacts[id].sources,...f.sources])used.add(s);
 for(const id of used){const s=c.sources[id];h+=`<li>${link(s.url,s.label)} — ${esc(s.level)}; ${esc(s.version)}. Reviewed ${s.verified}.</li>`;}h+='</ul></section>';
 h+='<section><h2>Continue your evaluation</h2><ul>';for(const slug of p.related){const r=c.pages.find(x=>x.slug===slug);h+=`<li>${link('/compare/'+slug+'/',r.title)}</li>`;}h+='</ul><p>'+link('https://docs.kujolang.ai/','Read the Kujo documentation')+' · '+link('https://github.com/kujolang/kujo','Inspect Kujo on GitHub')+' · '+link('/ecosystem/','Explore ecosystem tools')+'</p><p>'+link('https://github.com/kujolang/kujolang.ai/issues/new','Report an inaccuracy')+' with the page URL, a source and the affected version.</p></section>';
 return h+'\n';
}
function markdown(p,c){let m=`# ${p.title}\n\n${p.summary}\n\nLast reviewed: ${p.verified}. Canonical page: https://kujolang.ai/compare/${p.slug}/\n\n`;
 if(p.technology){const t=p.technology;m+=`## At a glance\n\n${t.name}: ${t.website}\n\nDocumentation: ${t.documentation}\n\nVersion: ${t.version}\n\nRepository: ${t.repository??t.repositoryNote}\n\n## Capability matrix\n\n`;for(const[label,id,f]of p.dimensions){m+=`### ${label}\n\n`;for(const[n,v]of [['Kujo',c.kujoFacts[id]],[t.name,f]])m+=`${n} — ${labels[v.status]} (${v.layer}): ${v.text}\n\nSources: ${v.sources.map(s=>c.sources[s].url).join(', ')}\n\n`;}}
 for(const s of p.sections)m+=`## ${s.heading}\n\n${s.body}\n\n`;m+='## Frequently asked questions\n\n';for(const[q,a]of p.faq)m+=`### ${q}\n\n${a}\n\n`;
 m+='## References\n\n';for(const id of p.sources){const s=c.sources[id];m+=`- [${s.label}](${s.url}) — ${s.level}; ${s.version}; reviewed ${s.verified}.\n`;}
 m+='\n## Related pages\n\n'+p.related.map(s=>`- [${c.pages.find(p=>p.slug===s).title}](https://kujolang.ai/compare/${s}/)`).join('\n')+'\n\n[Editorial policy](https://kujolang.ai/compare/editorial-policy.md) · [Report inaccuracies](https://github.com/kujolang/kujolang.ai/issues/new)\n';return m;
}
export function outputs(c){validate(c);const out=new Map();for(const p of c.pages){
 const front={title:p.title,description:p.description,seo_title:p.title,custom_url:p.slug,date:p.verified,author:'1',social_image:`/assets/images/social/${p.slug}.jpg`};
 out.set(`content/compare/${p.slug}.md`,'---\n'+Object.entries(front).map(([k,v])=>`${k}: ${JSON.stringify(v)}`).join('\n')+'\n---\n\n'+markdown(p,c).replace(/^# [^\n]+\n\n/,''));
 out.set(`templates/compare-content/${p.slug}.html`,body(p,c));
 out.set(`public/compare/text/${p.slug}.md`,markdown(p,c));
 }return out;}
if(process.argv[1]===fileURLToPath(import.meta.url)){
 const c=JSON.parse(fs.readFileSync(path.join(root,'comparison/catalog.json'),'utf8'));const out=outputs(c);let stale=[];
 for(const [name,text]of out){const dest=path.join(root,name);if(process.argv.includes('--check')){if(!fs.existsSync(dest)||fs.readFileSync(dest,'utf8')!==text)stale.push(name);}else{fs.mkdirSync(path.dirname(dest),{recursive:true});fs.writeFileSync(dest,text)}}
 if(stale.length)throw new Error('Regenerate comparisons: '+stale.join(', '));console.log(`Validated ${c.pages.length} records and ${out.size} generated content files.`);
}
