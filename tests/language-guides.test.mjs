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
test('runtime install instructions preserve the npm command and published compatibility links',()=>{
 const language=fs.readFileSync('templates/page-guide-language.html','utf8');
 const integrations=fs.readFileSync('templates/page-guide-integrations.html','utf8');
 assert.match(language,/<!--email_off--><pre><code class="language-sh">npm install --global @kujolang\/kujo-runtime@[0-9.]+\nkujo --version<\/code><\/pre><!--\/email_off-->/);
 assert.match(integrations,/<!--email_off--><code>@kujolang\/kujo-runtime@[0-9.]+<\/code><!--\/email_off-->/);
 assert(language.includes('https://docs.kujolang.ai/install/#npm-and-supported-platforms'));
 assert(language.includes('https://docs.kujolang.ai/install/#source-install'));
 assert.doesNotMatch(language,/Node\.js 18 or newer/);
});
