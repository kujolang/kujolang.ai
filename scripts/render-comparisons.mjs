import {renderGuide,validateGuide,guideMarkdown} from './render-comparison-guide.mjs';
import {renderDirect,validateDirect,directMarkdown} from './render-comparison-direct.mjs';
import {renderHub,validateHub} from './render-comparison-hub.mjs';
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
  must(p.socialCard===undefined||/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(p.socialCard),`${p.slug}: invalid social card id`);
  for(const field of ['title','description','summary'])must(nonempty(p[field]),`${p.slug}: missing ${field}`);
  must(date(p.verified),`${p.slug}: invalid verified date`);must(['direct','discovery','guide'].includes(p.kind),`${p.slug}: invalid kind`);refs(p.sources,p.slug);
  must(Array.isArray(p.sections)&&p.sections.length>0,`${p.slug}: missing sections`);
  for(const s of p.sections??[])must(nonempty(s.heading)&&nonempty(s.body),`${p.slug}: incomplete section`);
  if(p.kind==='direct'){
   validateDirect(p,c);
   const t=p.technology??{};for(const f of ['name','website','documentation','version'])must(nonempty(t[f]),`${p.slug}: missing technology ${f}`);
   must(nonempty(t.repository)||nonempty(t.repositoryNote),`${p.slug}: missing repository provenance`);
   must(Array.isArray(t.aliases),`${p.slug}: missing aliases`);
   for(const h of ['Technical architecture','When to choose Kujo',`When to choose ${t.name}`,'Can you use both?','Honest limitations','Examples and benchmark evidence'])must(p.sections.some(s=>s.heading===h),`${p.slug}: missing ${h}`);
   must(p.dimensions?.length>0,`${p.slug}: missing matrix`);
   for(const [label,id,f] of p.dimensions??[]){must(!!c.kujoFacts[id],`${p.slug}: unknown Kujo fact ${id}`);fact(f,`${p.slug}: ${label}`)}
  }
  if(p.kind==='guide'||p.kind==='discovery')validateGuide(p,c);
  must(p.faq?.length>0,`${p.slug}: missing FAQ`);
  for(const q of p.faq??[])must(q.length===2&&q.every(nonempty),`${p.slug}: invalid FAQ`);
 }
 for(const p of pages)for(const r of p.related??[])must(slugs.has(r)&&r!==p.slug,`${p.slug}: broken related reference ${r}`);
 validateHub(c);
 if(errors.length)throw new Error(errors.join('\n'));return c;
}
const labels={'verified-supported':'Verified supported','verified-unsupported':'Verified unsupported','partially-supported':'Partially supported','not-applicable':'Not applicable',unknown:'Unknown / not verified'};
function body(p,c){return p.kind==='direct'?renderDirect(p,c):renderGuide(p,c);}
function markdown(p,c){let m=`# ${p.title}\n\n${p.summary}\n\nLast reviewed: ${p.verified}. Canonical page: https://kujolang.ai/compare/${p.slug}/\n\n`;
 if(p.technology){const t=p.technology;m+=`## At a glance\n\n${t.name}: ${t.website}\n\nDocumentation: ${t.documentation}\n\nVersion: ${t.version}\n\nRepository: ${t.repository??t.repositoryNote}\n\n## Capability matrix\n\n`;for(const[label,id,f]of p.dimensions){m+=`### ${label}\n\n`;for(const[n,v]of [['Kujo',c.kujoFacts[id]],[t.name,f]])m+=`${n} — ${labels[v.status]} (${v.layer}): ${v.text}\n\nSources: ${v.sources.map(s=>c.sources[s].url).join(', ')}\n\n`;}}
 if(p.kind==='direct')m+=directMarkdown(p,c);else m+=guideMarkdown(p,c);
 for(const s of p.sections)m+=`## ${s.heading}\n\n${s.body}\n\n`;m+='## Frequently asked questions\n\n';for(const[q,a]of p.faq)m+=`### ${q}\n\n${a}\n\n`;
 m+='## References\n\n';for(const id of p.sources){const s=c.sources[id];m+=`- [${s.label}](${s.url}) — ${s.level}; ${s.version}; reviewed ${s.verified}.\n`;}
 m+='\n## Related pages\n\n'+p.related.map(s=>`- [${c.pages.find(p=>p.slug===s).title}](https://kujolang.ai/compare/${s}/)`).join('\n')+'\n\n[Editorial policy](https://kujolang.ai/compare/editorial-policy.md) · [Report inaccuracies](https://github.com/kujolang/kujolang.ai/issues/new)\n';return m;
}
export function outputs(c){validate(c);const out=new Map();for(const p of c.pages){
 const front={template:p.kind==='direct'?'comparison-direct':'comparison-guide',title:p.title,description:p.description,seo_title:p.title,custom_url:p.slug,date:p.verified,author:'1',social_image:`/assets/images/social/${p.socialCard??p.slug}.jpg`};
 out.set(`content/compare/${p.slug}.md`,'---\n'+Object.entries(front).map(([k,v])=>`${k}: ${JSON.stringify(v)}`).join('\n')+'\n---\n\n'+markdown(p,c).replace(/^# [^\n]+\n\n/,''));
 out.set(`templates/compare-content/${p.slug}.html`,body(p,c));
 out.set(`public/compare/text/${p.slug}.md`,markdown(p,c));
 }for(const [name,text] of renderHub(c))out.set(name,text);return out;}
if(process.argv[1]===fileURLToPath(import.meta.url)){
 const c=JSON.parse(fs.readFileSync(path.join(root,'comparison/catalog.json'),'utf8'));const out=outputs(c);let stale=[];
 for(const [name,text]of out){const dest=path.join(root,name);if(process.argv.includes('--check')){if(!fs.existsSync(dest)||fs.readFileSync(dest,'utf8')!==text)stale.push(name);}else{fs.mkdirSync(path.dirname(dest),{recursive:true});fs.writeFileSync(dest,text)}}
 if(stale.length)throw new Error('Regenerate comparisons: '+stale.join(', '));console.log(`Validated ${c.pages.length} records and ${out.size} generated content files.`);
}
