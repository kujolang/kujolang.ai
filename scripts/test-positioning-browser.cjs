const { chromium } = require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const assert = require('node:assert/strict');
(async () => {
  const browser = await chromium.launch({headless: true, ...(process.env.CHROME_BIN ? {executablePath: process.env.CHROME_BIN} : {})});
  const base = process.env.SITE_URL || 'http://127.0.0.1:4178';
  const providers = require('../assets/data/providers.json');
  for (const mode of ['enabled', 'disabled', 'failed-fetch']) {
    const context = await browser.newContext({javaScriptEnabled: mode !== 'disabled', reducedMotion: 'reduce'});
    if (mode === 'failed-fetch') await context.route('**/assets/data/providers.json', route => route.abort());
    const page = await context.newPage();
    await page.goto(base + '/providers/');
    assert.equal(await page.locator('[data-provider-record]').count(), providers.length);
    for (const p of providers) assert.equal(await page.locator(`a[href="${p.repo}"]`).count() > 0, true);
    if (mode === 'enabled') {
      await page.locator('[data-provider-search]').fill('ollama');
      assert.equal(await page.locator('[data-provider-record]:visible').count(), 1);
      await page.locator('[data-provider-id="ollama"]').click();
      assert(await page.getByRole('dialog').isVisible());
      await page.keyboard.press('Escape');
      assert.equal(await page.getByRole('dialog').count(), 0);
    } else assert.equal(await page.locator('[data-provider-record]:visible').count(), providers.length);
    for (const route of ['integrations', 'agent-accountability']) {
      for (const width of [390, 1440]) {
        await page.setViewportSize({width, height: 1000});
        await page.goto(`${base}/${route}/`);
        if (process.env.BROWSER_EVIDENCE_DIR && mode === 'enabled') await page.screenshot({path: `${process.env.BROWSER_EVIDENCE_DIR}/${route}-${width}.png`, fullPage: true});
        assert.equal(await page.locator('h1').count(), 1);
        assert(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1));
      }
    }
    await context.close();
  }
  await browser.close();
  console.log('Positioning browser checks passed: static links, no-JS, failed fetch, search, modal and responsive guides.');
})().catch(error => {console.error(error); process.exit(1);});
