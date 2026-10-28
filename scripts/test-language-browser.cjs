const { chromium } = require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const fs=require('node:fs');const assert=require('node:assert/strict');
(async()=>{
 const browser=await chromium.launch({headless:true, ...(process.env.CHROME_BIN ? {executablePath:process.env.CHROME_BIN}: {})});const base=process.env.SITE_URL||'http://127.0.0.1:4178';
 const context=await browser.newContext({permissions:['clipboard-read','clipboard-write'],reducedMotion:'reduce'});
 const page=await context.newPage();page.setDefaultTimeout(15000);const errors=[];page.on('pageerror',e=>errors.push(e.message));page.on('console',m=>{if(m.type()==='error')errors.push(m.text())});
 const evidence=process.env.BROWSER_EVIDENCE_DIR||'.loop-engineering/evidence/browser';
 fs.mkdirSync(evidence,{recursive:true});
 for(const [name,width,height] of [['desktop',1440,1000],['tablet',768,1024],['mobile',390,844]]){
  await page.setViewportSize({width,height});await page.goto(base,{waitUntil:'domcontentloaded'});
  assert(await page.locator('.site-footer').isVisible(),'Homepage footer must be visible');
  assert(!/\bv?1\.9(?:\.0)?\b/.test(await page.locator('main').innerText()),'No release number in homepage copy');
  await page.locator('.example-selector').waitFor({state:'visible'});assert.equal(await page.locator('[data-example]:visible').count(),1);
  assert(await page.locator('[data-code-explorer]').evaluate(el=>el.getBoundingClientRect().top)<height,'Code explorer should start in first viewport');if(name==='desktop')assert(await page.locator('#example-hello-world pre').first().evaluate(el=>el.getBoundingClientRect().top)<height,'Actual code visible in first desktop viewport');
  await page.locator('#home-example').focus();await page.keyboard.press('f');await page.keyboard.press('Tab');assert.notEqual(await page.locator('#home-example').inputValue(),'hello-world');await page.selectOption('#home-example','request-hash');assert(await page.locator('#example-request-hash').isVisible());
  await page.locator('#example-request-hash [data-copy-code]').first().click();await page.waitForFunction(()=>document.querySelector('#example-request-hash [data-code-status]').textContent==='Copied!');
  assert.equal(await page.evaluate(()=>navigator.clipboard.readText()),fs.readFileSync('public/samples/request-hash.kujo','utf8'));
  await page.selectOption('#home-example','hello-world');
  assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),'horizontal overflow');
  await page.evaluate(()=>scrollTo(0,0));await page.screenshot({path:`${evidence}/home-${name}.png`,fullPage:true});await page.screenshot({path:`${evidence}/viewport-${name}.png`});
  if(name==='mobile'){await page.locator('[data-mobile-menu-toggle]').click();assert(await page.locator('#mobile-navigation').isVisible());await page.keyboard.press('Escape');assert(await page.locator('#mobile-navigation').isHidden());}
 }
 await page.goto(base+'/examples/',{waitUntil:'domcontentloaded'});await page.fill('#example-search','replay');assert(await page.locator('[data-example-card]:visible').count()>0);await page.fill('#example-search','no-such-feature');assert.equal(await page.locator('[data-example-card]:visible').count(),0);assert.equal(await page.locator('#example-count').textContent(),'0 examples found');await page.fill('#example-search','');await page.selectOption('#example-category','Concurrency');assert.equal(await page.locator('[data-example-card]:visible').count(),3);
 await page.screenshot({path:evidence+'/examples-mobile.png',fullPage:true});
 for(const route of ['/language/','/development-workflow/','/performance/','/examples/replay/','/ecosystem/','/compare/']){await page.goto(base+route,{waitUntil:'domcontentloaded'});assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),route+' overflow');assert.equal(await page.locator('main').count(),1);}
 if (process.env.AXE_SCRIPT) {
   for (const route of ['/', '/examples/', '/examples/hello-world/', '/language/', '/development-workflow/', '/performance/']) {
     await page.goto(base+route,{waitUntil:'domcontentloaded'});
     await page.addScriptTag({path:process.env.AXE_SCRIPT});
     const result=await page.evaluate(()=>axe.run(document,{runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21aa']}}));
     fs.writeFileSync(evidence+'/axe-'+(route.replaceAll('/','-')||'home')+'.json',JSON.stringify({url:route,violations:result.violations,passes:result.passes.length},null,2));
     assert.deepEqual(result.violations.map(x=>({id:x.id,nodes:x.nodes.map(n=>n.target)})),[],route+' accessibility');
   }
 }
 const nojs=await browser.newContext({javaScriptEnabled:false});const p=await nojs.newPage();await p.goto(base);assert.equal(await p.locator('[data-example]:visible').count(),6);await p.goto(base+'/examples/');assert.equal(await p.locator('[data-example-card]:visible').count(),21);
 assert.deepEqual(errors,[]);await browser.close();console.log('Browser: selection, exact clipboard, filter, no-JS, mobile menu, responsive layouts and console passed');
})().catch(e=>{console.error(e);process.exit(1)});
