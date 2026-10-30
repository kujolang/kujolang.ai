const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright');
const fs=require('node:fs');const assert=require('node:assert/strict');
(async()=>{
 const catalog=JSON.parse(fs.readFileSync('workflows/catalog.json','utf8'));
 const base=process.env.SITE_URL||'http://127.0.0.1:4178';
 const dir=process.env.WORKFLOW_EVIDENCE_DIR||'.loop-engineering/ai-workflows/evidence/browser';fs.mkdirSync(dir,{recursive:true});
 const browser=await chromium.launch({headless:true,...(process.env.CHROME_BIN?{executablePath:process.env.CHROME_BIN}:{})});
 const context=await browser.newContext({permissions:['clipboard-read','clipboard-write'],reducedMotion:'reduce'});
 const page=await context.newPage();const errors=[];page.on('pageerror',e=>errors.push(e.message));const reports=[];
 for(const width of [1440,390]){
  await page.setViewportSize({width,height:1000});await page.goto(base+'/examples/');
  assert.equal(await page.locator('.workflow-card').count(),catalog.items.length);assert.equal(await page.locator('[data-example-card]').count(),JSON.parse(fs.readFileSync('examples/catalog.json')).items.length);
  await page.locator('#build-something-useful').screenshot({path:dir+`/collection-${width}.png`});
  for(const x of catalog.items){
   await page.goto(base+'/examples/'+x.slug+'/',{waitUntil:'domcontentloaded'});
   assert.equal(await page.locator('h1').textContent(),x.title);
   assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),x.slug+' overflow');
   assert(await page.locator('.site-footer').isVisible());
   assert.equal(await page.locator('.example-source code').textContent(),fs.readFileSync(`public/workflows/${x.slug}/main.kujo`,'utf8'));
   for(const b of await page.locator('[data-copy-code]').all()){
    assert.equal(await b.evaluate(el=>getComputedStyle(el).position),'absolute');
    assert.equal(await b.locator('svg').count(),1);
    await b.click();await page.waitForFunction(()=>[...document.querySelectorAll('[data-code-status]')].some(el=>el.textContent==='Copied!'));
    const expected=await b.evaluate(el=>el.closest('.sample-code').querySelector('code').textContent);
    assert.equal(await page.evaluate(()=>navigator.clipboard.readText()),expected);
   }
   for(const code of await page.locator('.sample-code code').all())assert(!/departure/i.test(await code.evaluate(el=>getComputedStyle(el).fontFamily)));
   await page.screenshot({path:dir+`/${x.slug}-${width}.png`});
   if(width===390&&process.env.AXE_SCRIPT){await page.addScriptTag({path:process.env.AXE_SCRIPT});const result=await page.evaluate(()=>axe.run(document,{runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21aa']}}));reports.push({slug:x.slug,violations:result.violations});assert.deepEqual(result.violations.map(v=>({id:v.id,targets:v.nodes.map(n=>n.target)})),[],x.slug);}
   const zip=await context.request.get(base+'/workflows/'+x.slug+'.zip');assert(zip.ok());assert.deepEqual(await zip.body(),fs.readFileSync(`public/workflows/${x.slug}.zip`));
  }
 }
 const nojs=await browser.newContext({javaScriptEnabled:false});const p=await nojs.newPage();await p.goto(base+'/examples/');assert.equal(await p.locator('.workflow-card:visible').count(),catalog.items.length);await p.goto(base+'/examples/safe-editor/');assert.equal(await p.locator('[data-copy-code]:visible').count(),0);assert(await p.locator('.example-source code').isVisible());
 fs.writeFileSync(dir+'/accessibility.json',JSON.stringify(reports,null,2)+'\n');assert.deepEqual(errors,[]);await browser.close();console.log('All workflow pages passed desktop/mobile, exact clipboard, archive parity, no-JS and accessibility checks.');
})().catch(e=>{console.error(e);process.exit(1)});
