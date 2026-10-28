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
  // The spacious hero supersedes the former first-viewport code constraint.
  assert(await page.locator('.home-hero .sk-hero__inner').evaluate(el=>{const s=getComputedStyle(el);return parseFloat(s.paddingBottom)>=64&&parseFloat(s.paddingTop)>=140;}),'Hero has breathing room');
  assert.equal(await page.locator('.home-hero a').count(),2,'Hero contains only its two primary actions');
  assert.equal(await page.locator('.home-build .eyebrow,.home-runtime header .eyebrow,.home-start .eyebrow,.home-ecosystem .eyebrow,.home-proof .eyebrow,.home-explorer-heading .eyebrow').count(),0);
  assert(await page.evaluate(()=>{
   const hero=document.querySelector('.home-hero .sk-hero__inner');
   const edges=el=>{const r=el.getBoundingClientRect(),s=getComputedStyle(el);return [r.left+parseFloat(s.paddingLeft),r.right-parseFloat(s.paddingRight)];};
   const [left,right]=edges(hero);
   return [...document.querySelectorAll('.language-home > .language-section:not(.language-final),.home-runtime-inner,.home-final-inner')].every(el=>{const [l,r]=edges(el);return Math.abs(l-left)<2&&Math.abs(r-right)<2;});
  }),'Homepage sections align with hero content');
  for(const selector of ['.home-explorer .example-panel h3','.home-card h3','.home-runtime-steps h3','.home-tool-grid strong'])assert(/Departure Mono/.test(await page.locator(selector).first().evaluate(el=>getComputedStyle(el).fontFamily)),selector+' display font');
  assert(await page.locator('.language-final').evaluate(el=>{const r=el.getBoundingClientRect(),s=getComputedStyle(el);return r.left===0&&Math.abs(r.width-innerWidth)<2&&s.backgroundColor==='rgb(17, 17, 17)'&&s.color==='rgb(255, 255, 255)';}),'Final CTA is full-width black with white text');
  assert.equal(await page.locator('.home-build .home-section-heading').evaluate(el=>getComputedStyle(el).textAlign),'center');
  assert.equal(await page.locator('.home-ecosystem .home-section-heading').evaluate(el=>getComputedStyle(el).textAlign),'center');
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
