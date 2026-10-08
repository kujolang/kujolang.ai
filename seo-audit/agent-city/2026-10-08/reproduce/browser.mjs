import { createRequire } from 'node:module';
import path from 'node:path';
const require=createRequire(path.resolve(process.env.PLAYWRIGHT_PACKAGE || 'agent-city/package.json'));
const { chromium }=require('playwright');
import fs from 'node:fs/promises';
const base=process.env.AUDIT_WORKSPACE || process.cwd();
const auditDate=process.env.AUDIT_DATE;
if(!/^\d{4}-\d{2}-\d{2}$/.test(auditDate||'')) throw new Error('Set AUDIT_DATE to a new audit date.');
const config={registry:'https://kennel.kujolang.ai/getting-started/',web:'https://kujolang.ai/ecosystem/agent-city/',docs:'https://docs.kujolang.ai/showcases/agent-city/'};
const browser=await chromium.launch({executablePath:process.env.CHROMIUM_PATH,headless:true});
try {
for(const name of process.argv.slice(2)){
 const results=[];const audit=base+'/agent-city-sites-'+name+'/seo-audit/agent-city/'+auditDate;
 await fs.mkdir(audit+'/raw',{recursive:true}); try { await fs.access(audit+'/browser-check.json'); throw new Error('Refusing to overwrite an existing browser receipt'); } catch(e) { if(e.code!=='ENOENT') throw e; }
 for(const width of [1440,320]){
  const context=await browser.newContext({viewport:{width,height:900},reducedMotion:'reduce'});const page=await context.newPage();const errors=[];page.on('pageerror',e=>errors.push(e.message));
  await page.addInitScript(()=>{window.__lcp=null;new PerformanceObserver(l=>{window.__lcp=l.getEntries().at(-1)?.startTime}).observe({type:'largest-contentful-paint',buffered:true})});
  const response=await page.goto(config[name],{waitUntil:'networkidle',timeout:60000});
  const metrics=await page.evaluate(()=>({title:document.title,h1:[...document.querySelectorAll('h1')].map(e=>e.textContent),canonical:document.querySelector('link[rel=canonical]')?.href,hasAgentCity:document.body.textContent.includes('Agent City'),overflow:document.documentElement.scrollWidth>innerWidth,images:[...document.images].map(i=>({src:i.currentSrc||i.src,alt:i.alt,width:i.naturalWidth,height:i.naturalHeight,loaded:i.complete&&i.naturalWidth>0})),navigation:performance.getEntriesByType('navigation').map(n=>({duration:n.duration,domContentLoaded:n.domContentLoadedEventEnd,ttfb:n.responseStart-n.requestStart,transferSize:n.transferSize,decodedBodySize:n.decodedBodySize})),lcpMs:window.__lcp,resources:performance.getEntriesByType('resource').map(r=>({name:r.name,transferSize:r.transferSize,decodedBodySize:r.decodedBodySize,duration:r.duration}))}));
  await page.keyboard.press('Tab');const focus=await page.evaluate(()=>({tag:document.activeElement.tagName,text:document.activeElement.textContent?.slice(0,100),outline:getComputedStyle(document.activeElement).outlineStyle}));
  if(name==='registry')await page.locator('#agent-city').scrollIntoViewIfNeeded();
  await page.screenshot({path:audit+'/raw/browser-'+width+'.png'});
  results.push({width,status:response.status(),metrics,firstKeyboardFocus:focus,errors});await context.close();
 }
 await fs.writeFile(audit+'/browser-check.json',JSON.stringify({date:new Date().toISOString(),browser:browser.version(),conditions:'Headless Chromium; reduced motion; one navigation per viewport; busy shared host; lab timing only, not field CWV',results},null,2)+'\n');console.log(name,results.map(r=>({width:r.width,status:r.status,overflow:r.metrics.overflow,errors:r.errors,agentCity:r.metrics.hasAgentCity})));}
} finally { await browser.close(); }
