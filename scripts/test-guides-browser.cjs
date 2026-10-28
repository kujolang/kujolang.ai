const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright');
const fs=require('node:fs');const assert=require('node:assert/strict');
(async()=>{
 const browser=await chromium.launch({headless:true,...(process.env.CHROME_BIN?{executablePath:process.env.CHROME_BIN}:{})});
 const context=await browser.newContext({permissions:['clipboard-read','clipboard-write'],reducedMotion:'reduce'});
 const page=await context.newPage();const base=process.env.SITE_URL||'http://127.0.0.1:4178';
 const dir=process.env.GUIDE_EVIDENCE_DIR||'/tmp/kujo-guide-browser';fs.mkdirSync(dir,{recursive:true});
 const errors=[];page.on('pageerror',e=>errors.push(e.message));
 const reports=[];
 const routes=['language','development-workflow','performance'];
 for(const width of [1440,768,390]) for(const route of routes){
  await page.setViewportSize({width,height:1000});await page.goto(base+'/'+route+'/',{waitUntil:'domcontentloaded'});
  assert.equal(await page.locator('main h1').count(),1);assert(await page.locator('.guide-overview').isVisible());
  assert(await page.locator('.guide-section').count()>=2);assert(await page.locator('.site-footer').isVisible());
  for(const block of await page.locator('.sample-code').all()){
   const code=await block.locator('code').textContent();const button=block.locator('[data-copy-code]');
   assert(!/departure/i.test(await block.locator('code').evaluate(el=>getComputedStyle(el).fontFamily)));
   assert.equal(await button.evaluate(el=>getComputedStyle(el).position),'absolute');
   await button.click();await page.waitForFunction(()=>[...document.querySelectorAll('[data-code-status]')].some(el=>el.textContent==='Copied!'));
   assert.equal(await page.evaluate(()=>navigator.clipboard.readText()),code);
   assert(await block.evaluate(el=>{const a=el.querySelector('button').getBoundingClientRect(),b=el.querySelector('[data-code-status]').getBoundingClientRect();return Math.abs((a.top+a.bottom)/2-(b.top+b.bottom)/2)<1;}),'Feedback centered with icon');
  }
  if(route==='development-workflow'){
   const yaml=await page.locator('code.language-yaml').textContent();
   assert(yaml.includes('  - id: project_tests\n    command: "npm test"\n    required: true'));
   assert(yaml.includes('commit:\n  enabled: false\n  push: false'));assert.equal(await page.locator('code.language-yaml ul').count(),0);
  }
  if(route==='performance'){
   const receipt=JSON.parse(fs.readFileSync('public/samples/performance.json','utf8'));
   assert((await page.locator('.measurement-card').textContent()).includes(receipt.median_ms.toFixed(2)));
   await page.locator('.measurement-runs summary').click();assert.equal(await page.locator('.measurement-runs li').count(),10);
  }
  assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),route+' overflow '+width);
  await page.screenshot({path:`${dir}/${route}-${width}.png`,fullPage:true});
  if(width===390&&process.env.AXE_SCRIPT){await page.addScriptTag({path:process.env.AXE_SCRIPT});const r=await page.evaluate(()=>axe.run(document,{runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21aa']}}));reports.push({route,violations:r.violations});assert.deepEqual(r.violations.map(x=>({id:x.id,targets:x.nodes.map(n=>n.target)})),[],route+' accessibility');}
 }
 // Review every internal destination linked from the redesigned homepage, including tool pages.
 await page.goto(base,{waitUntil:'domcontentloaded'});
 const links=await page.locator('main a[href^="/"]').evaluateAll(els=>[...new Set(els.map(a=>a.getAttribute('href')).filter(h=>h.endsWith('/')))]);
 for(const route of links){
  const response=await page.goto(base+route,{waitUntil:'domcontentloaded'});assert.equal(response.status(),200,route);
  assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),route+' mobile overflow');
  assert(await page.locator('.site-footer').isVisible(),route+' footer');
  const sample=page.locator('.sample-code [data-copy-code]:visible').first();
  if(await sample.count()){await sample.click();await page.waitForFunction(()=>[...document.querySelectorAll('.sample-code [data-code-status]')].some(el=>el.textContent==='Copied!'));}
  const install=page.locator('.tool-install-panel [data-copy-code]').first();
  if(await install.count()) {await install.click();await page.waitForFunction(()=>document.querySelector('.tool-install-panel [data-copy-status]').textContent==='Copied!');}
 }
 fs.writeFileSync(dir+'/review.json',JSON.stringify({routes,homepageDestinations:links,accessibility:reports},null,2));
 const nojs=await browser.newContext({javaScriptEnabled:false});const fallback=await nojs.newPage();
 for(const route of routes){await fallback.goto(base+'/'+route+'/');assert(await fallback.locator('.guide-section').count()>1);assert(await fallback.locator('pre code').count()>0);}
 assert.deepEqual(errors,[]);await browser.close();console.log('Guides: three responsive layouts, exact code/clipboard, aligned feedback, receipt details, accessibility, no-JS and all homepage destinations passed');
})().catch(e=>{console.error(e);process.exit(1)});
