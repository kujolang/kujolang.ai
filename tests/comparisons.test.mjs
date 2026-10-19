import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {validate,outputs} from '../scripts/render-comparisons.mjs';
const catalog=JSON.parse(fs.readFileSync(new URL('../comparison/catalog.json',import.meta.url)));
test('published projections match the validated catalog',()=>{for(const [name,text]of outputs(catalog))assert.equal(fs.readFileSync(new URL('../'+name,import.meta.url),'utf8'),text,name)});
for(const [name,mutate]of [
 ['unknown status',c=>c.pages[0].dimensions[0][2].status='yes'],
 ['missing source',c=>c.pages[0].dimensions[0][2].sources=[]],
 ['broken source',c=>c.pages[0].dimensions[0][2].sources=['missing']],
 ['unknown Kujo fact',c=>c.pages[0].dimensions[0][1]='missing'],
 ['broken related page',c=>c.pages[0].related=['missing']],
 ['path traversal',c=>c.pages[0].slug='../escape'],
 ['missing competitor recommendation',c=>c.pages[0].sections=c.pages[0].sections.filter(s=>s.heading!=='When to choose Bend')],
 ['missing identity provenance',c=>{c.pages[2].technology.repository=null;delete c.pages[2].technology.repositoryNote}],
 ['duplicate route',c=>c.pages.push(c.pages[0])],
 ['invalid review date',c=>c.pages[0].verified='yesterday']
])test(`reject ${name}`,()=>{const c=structuredClone(catalog);mutate(c);assert.throws(()=>validate(c))});

test('hub rejects a stale fact reference before publication',()=>{
 const c=structuredClone(catalog);c.hub.rows[0].cells[1].refs=['kujo-vs-bend:99'];
 assert.throws(()=>validate(c),/Unknown hub fact/);
});
test('hub rejects a missing language cell rather than shifting columns',()=>{
 const c=structuredClone(catalog);c.hub.rows[0].cells.pop();
 assert.throws(()=>validate(c),/Invalid hub row/);
});

test('direct comparisons reject architecture claims without valid evidence',()=>{
 const c=structuredClone(catalog);c.pages[0].deepDive.architecture[0][4]=['missing'];
 assert.throws(()=>validate(c),/invalid architecture evidence/);
});
test('direct comparisons reject incomplete decision rows',()=>{
 const c=structuredClone(catalog);c.pages[1].deepDive.scenarios[0].pop();
 assert.throws(()=>validate(c),/invalid decision scenario/);
});
test('each technical comparison publishes its evaluation plan in HTML and Markdown',()=>{
 const out=outputs(catalog);
 for(const p of catalog.pages.filter(p=>p.kind==='direct')){
  const html=out.get(`templates/compare-content/${p.slug}.html`);
  const md=out.get(`public/compare/text/${p.slug}.md`);
  assert.equal((html.match(/<table>/g)||[]).length,2);
  for(const [title]of p.deepDive.trial){assert.ok(html.includes(title));assert.ok(md.includes(title));}
  assert.match(out.get(`content/compare/${p.slug}.md`),/template: "comparison-direct"/);
 }
});
