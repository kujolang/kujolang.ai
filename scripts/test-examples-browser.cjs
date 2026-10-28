const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright');
const fs=require('node:fs');const assert=require('node:assert/strict');
(async()=>{
 const browser=await chromium.launch({headless:true,...(process.env.CHROME_BIN?{executablePath:process.env.CHROME_BIN}:{})});
 const base=process.env.SITE_URL||'http://127.0.0.1:4178';
 const evidence=process.env.EXAMPLES_EVIDENCE_DIR||'.loop-engineering/examples-visual-refinement/evidence/browser';fs.mkdirSync(evidence,{recursive:true});
 const catalog=JSON.parse(fs.readFileSync('examples/catalog.json','utf8'));
 const context=await browser.newContext({permissions:['clipboard-read','clipboard-write'],reducedMotion:'reduce'});
 const page=await context.newPage();const errors=[];page.on('pageerror',e=>errors.push(e.message));page.on('console',m=>{if(m.type()==='error')errors.push(m.text())});
 const fits=async()=>assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),'No horizontal page overflow: '+page.url());
 const icons=async()=>{for(const code of await page.locator('.sample-code pre code:visible').all())assert(!/departure/i.test(await code.evaluate(el=>getComputedStyle(el).fontFamily)),'Code uses a conventional monospace font');for(const button of await page.locator('[data-copy-code]:visible').all()){
  assert.equal(await button.evaluate(el=>getComputedStyle(el).position),'absolute','Copy controls must not occupy a code row');assert(await button.evaluate(el=>parseFloat(getComputedStyle(el.closest('.sample-code').querySelector('pre')).paddingTop)<=24),'Code has no extra top row for controls');assert.equal(await button.getAttribute('aria-label'),'Copy code');assert.equal(await button.locator('svg').count(),1);
  assert(await button.evaluate(b=>{const r=b.getBoundingClientRect(),p=b.closest('.sample-code').getBoundingClientRect();return r.top>=p.top&&r.bottom<=p.bottom&&r.right<=p.right+1&&p.right-r.right<16&&r.top-p.top<16;}),'Copy icon is inside top-right of code block');
 }};
 for(const [name,width,height] of [['desktop',1440,1000],['tablet',768,1024],['mobile',390,844]]){
  await page.setViewportSize({width,height});await page.goto(base+'/examples/',{waitUntil:'domcontentloaded'});
  await page.locator('.example-filter').waitFor({state:'visible'});await fits();assert.equal(await page.locator('[data-example-card]:visible').count(),21);
  assert(await page.locator('.site-footer').isVisible());assert.equal(await page.locator('h1').count(),1);
  await page.screenshot({path:`${evidence}/index-${name}.png`,fullPage:true});
  await page.fill('#example-search','no-such-example');assert.equal(await page.locator('.example-category-group:visible').count(),0);assert.equal(await page.locator('#example-count').textContent(),'0 examples found');
  await page.fill('#example-search','');await page.selectOption('#example-category','Concurrency');assert.equal(await page.locator('[data-example-card]:visible').count(),3);
  await page.goto(base,{waitUntil:'domcontentloaded'});await icons();await fits();
 }
 const axeReports=[];
 for(const x of catalog.items){
  for(const width of [1440,390]){
   await page.setViewportSize({width,height:1000});await page.goto(base+'/examples/'+x.slug+'/',{waitUntil:'domcontentloaded'});await fits();await icons();
   assert.equal(await page.locator('h1').textContent(),x.title);assert.equal(await page.locator('.example-source code').textContent(),fs.readFileSync('public/samples/'+x.slug+'.kujo','utf8'));
   assert(await page.locator('.site-footer').isVisible());
   if(['hello-world','replay','http'].includes(x.slug))await page.screenshot({path:`${evidence}/${x.slug}-${width}.png`,fullPage:true});
  }
  await page.locator('.example-source [data-copy-code]').click();await page.waitForFunction(()=>document.querySelector('.example-source [data-code-status]').textContent==='Copied!');
  assert.equal(await page.evaluate(()=>navigator.clipboard.readText()),fs.readFileSync('public/samples/'+x.slug+'.kujo','utf8'));
  if(x.slug==='hello-world'){assert.equal(await page.locator('.example-source [data-code-status]').evaluate(el=>getComputedStyle(el).backgroundColor),'rgba(0, 0, 0, 0)');await page.waitForFunction(()=>document.querySelector('.example-source [data-code-status]').textContent==='',{},{timeout:2200});}
  if(x.expected){await page.locator('.example-result [data-copy-code]').click();await page.waitForFunction(()=>document.querySelector('.example-result [data-code-status]').textContent==='Copied!');assert.equal(await page.evaluate(()=>navigator.clipboard.readText()),x.expected);}
  else assert((await page.locator('.example-scope').textContent()).includes('did not run the full application'));
  await page.locator('.example-provenance summary').click();assert((await page.locator('.example-provenance').textContent()).includes(x.sha256));await fits();
  if(process.env.AXE_SCRIPT){await page.addScriptTag({path:process.env.AXE_SCRIPT});const r=await page.evaluate(()=>axe.run(document,{runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21aa']}}));axeReports.push({slug:x.slug,violations:r.violations,passes:r.passes.length});assert.deepEqual(r.violations.map(v=>({id:v.id,nodes:v.nodes.map(n=>n.target)})),[],x.slug+' accessibility');}
 }
 fs.writeFileSync(evidence+'/accessibility.json',JSON.stringify(axeReports,null,2)+'\n');
 const nojs=await browser.newContext({javaScriptEnabled:false});const p=await nojs.newPage();await p.goto(base+'/examples/');assert.equal(await p.locator('[data-example-card]:visible').count(),21);await p.goto(base+'/examples/replay/');assert.equal(await p.locator('.example-source code').textContent(),fs.readFileSync('public/samples/replay.kujo','utf8'));assert.equal(await p.locator('[data-copy-code]:visible').count(),0);
 assert.deepEqual(errors,[]);await browser.close();console.log('Examples: all 21 pages, source/clipboard integrity, output copying, in-block icons, responsive layouts, filtering, no-JS and accessibility passed');
})().catch(e=>{console.error(e);process.exit(1)});
