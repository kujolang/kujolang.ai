import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {execFileSync} from 'node:child_process';
test('guide templates stay in sync with authored content',()=>execFileSync(process.execPath,['scripts/render-language-guides.mjs','--check']));
test('performance evidence agrees with the published receipt',()=>{
 const receipt=JSON.parse(fs.readFileSync('public/samples/performance.json','utf8'));
 const page=fs.readFileSync('content/pages/performance.md','utf8');
 assert(page.includes(receipt.median_ms.toFixed(2)));
 for(const value of receipt.samples_ms)assert(page.includes(value.toFixed(2)+' ms'));
 assert(page.includes(receipt.cpu));assert(page.includes(receipt.os));
});
