import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';
const base=process.env.AUDIT_WORKSPACE || process.cwd();
const names=process.argv.slice(2);
const auditDate=process.env.AUDIT_DATE;
if(!/^\d{4}-\d{2}-\d{2}$/.test(auditDate||'')) throw new Error('Set AUDIT_DATE to a new audit date.');
const configs={web:{origin:'https://kujolang.ai',root:'output',page:'/ecosystem/agent-city/',extra:['/ecosystem/','/ecosystem/showcase/','/robots.txt','/sitemap.xml','/llms.txt','/agent-city-audit-missing-20261008/']},docs:{origin:'https://docs.kujolang.ai',root:'output',page:'/showcases/agent-city/',extra:['/ecosystem/showcases/','/robots.txt','/sitemap.xml','/llms.txt','/agent-city-audit-missing-20261008/']},registry:{origin:'https://kennel.kujolang.ai',root:'registry',page:'/getting-started/',extra:['/','/watchdog','/watchdog/','/robots.txt','/sitemap.xml','/agent-city-audit-missing-20261008/']}};
async function walk(dir){let out=[];for(const e of await fs.readdir(dir,{withFileTypes:true})){const p=path.join(dir,e.name);if(e.isDirectory())out.push(...await walk(p));else out.push(p)}return out}
async function probe(url,ua='AgentCityReleaseAudit/1.0'){
 const start=performance.now();try{const r=await fetch(url,{headers:{'User-Agent':ua},signal:AbortSignal.timeout(25000),redirect:'manual'});const body=await r.text();return {url,userAgent:ua,status:r.status,location:r.headers.get('location'),contentType:r.headers.get('content-type'),robots:r.headers.get('x-robots-tag'),bytes:Buffer.byteLength(body),sha256:crypto.createHash('sha256').update(body).digest('hex'),elapsedMs:Math.round(performance.now()-start),body}}catch(e){return{url,userAgent:ua,error:String(e)}}
}
for(const name of names){const c=configs[name];const repo=path.join(base,'agent-city-sites-'+name);const audit=path.join(repo,'seo-audit/agent-city/'+auditDate);await fs.mkdir(path.join(audit,'raw'),{recursive:true}); try { await fs.access(path.join(audit,'production-after.json')); throw new Error('Refusing to overwrite an existing production receipt'); } catch(e) { if(e.code!=='ENOENT') throw e; } const files=await walk(path.join(repo,c.root));const routes=files.filter(f=>f.endsWith('/index.html')).map(f=>'/'+path.relative(path.join(repo,c.root),f).replace(/index.html$/,''));const urls=[...new Set([...routes,...c.extra].map(r=>c.origin+r))];let next=0,rows=[];
 await Promise.all(Array.from({length:8},async()=>{while(next<urls.length){const url=urls[next++];const row=await probe(url);if(url===c.origin+c.page)await fs.writeFile(path.join(audit,'raw/production-agent-city.html'),row.body||'');delete row.body;rows.push(row)}}));
 const crawler=[];for(const ua of ['Mozilla/5.0','Googlebot','bingbot','OAI-SearchBot','GPTBot']){const row=await probe(c.origin+c.page,ua);delete row.body;crawler.push(row)}
 const variants=[];for(const url of ['http://'+new URL(c.origin).host+c.page,'https://www.'+new URL(c.origin).host+c.page,c.origin+c.page.replace(/\/$/,'')+'?source=audit']){const row=await probe(url);delete row.body;variants.push(row)}
 await fs.writeFile(path.join(audit,'production-after.json'),JSON.stringify({observedAt:new Date().toISOString(),responses:rows.sort((a,b)=>a.url.localeCompare(b.url)),crawlerAccess:crawler,variants},null,2)+'\n');
 console.log(name,JSON.stringify({pages:rows.length,statuses:rows.reduce((a,r)=>(a[r.status||'error']=(a[r.status||'error']||0)+1,a),{}),crawler:crawler.map(r=>[r.userAgent,r.status])}));
}
