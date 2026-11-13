const {chromium} = require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');

const slugs = ['factories', 'software-factory', 'videoops-factory', 'publishing-house-factory', 'webops-factory', 'product-launch-factory'];
const base = process.env.SITE_URL || 'http://127.0.0.1:4178';
const evidence = process.env.BROWSER_EVIDENCE_DIR || '.loop-engineering/evidence/factories-browser';
const receipt = {base, started: new Date().toISOString(), pages: [], links: [], media: [], accessibility: [], consoleErrors: []};

(async () => {
  fs.mkdirSync(evidence, {recursive: true});
  const browser = await chromium.launch({headless: true, ...(process.env.CHROME_BIN ? {executablePath: process.env.CHROME_BIN} : {})});
  try {
    const context = await browser.newContext({reducedMotion: 'reduce'});
    const page = await context.newPage();
    page.setDefaultTimeout(20000);
    page.on('pageerror', error => receipt.consoleErrors.push(error.message));
    page.on('console', message => { if (message.type() === 'error') receipt.consoleErrors.push(message.text()); });
    const internalLinks = new Set();
    for (const width of [1440, 390]) {
      await page.setViewportSize({width, height: 1000});
      for (const slug of slugs) {
        const route = `/ecosystem/${slug}/`;
        const response = await page.goto(base + route, {waitUntil: 'networkidle'});
        assert.equal(response.status(), 200, route);
        assert.equal(await page.locator('main').count(), 1, `${route}: one main`);
        assert.equal(await page.locator('h1').count(), 1, `${route}: one h1`);
        const breadcrumb = page.locator('main > nav[aria-label="Breadcrumb"]');
        if (await breadcrumb.count()) {
          const box = await breadcrumb.locator('a').first().boundingBox();
          const header = await page.locator('.site-header').boundingBox();
          assert(box.y >= header.y + header.height, `${route}: breadcrumb clears fixed navigation`);
        }
        const brokenAnchors = await page.locator('main a[href^="#"]').evaluateAll(links => links.filter(link => !document.getElementById(decodeURIComponent(link.hash.slice(1)))).map(link => link.hash));
        assert.deepEqual(brokenAnchors, [], `${route}: section links resolve`);
        assert(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1), `${route}: overflow at ${width}`);
        // Scroll through lazy images before checking dimensions and taking the full-page capture.
        await page.evaluate(async () => {
          for (const image of document.querySelectorAll('main img')) { image.loading = 'eager'; await image.decode().catch(() => {}); }
        });
        const images = await page.locator('main img').evaluateAll(images => images.map(image => ({src: image.currentSrc || image.src, loaded: image.complete && image.naturalWidth > 0, alt: image.getAttribute('alt')})));
        assert(images.length > 0, `${route}: images present`);
        for (const image of images) { assert(image.loaded, `${route}: ${image.src}`); assert.notEqual(image.alt, null, `${route}: image alt`); }
        for (const href of await page.locator('main a[href]').evaluateAll(links => links.map(link => link.href))) {
          const url = new URL(href);
          if (url.origin === new URL(base).origin) { url.hash = ''; internalLinks.add(url.href); }
        }
        if (slug === 'factories') {
          const design = await page.evaluate(() => {
            const cards = [...document.querySelectorAll('.factory-feature-grid > li')].map(e => { const r = e.getBoundingClientRect(); return {x:r.x,y:r.y,width:r.width}; });
            const stations = [...document.querySelectorAll('.factory-stations li')].map(e => ({height:e.getBoundingClientRect().height,background:getComputedStyle(e).backgroundColor,title:e.querySelector('strong').textContent,font:getComputedStyle(e.querySelector('strong')).fontFamily,overflow:e.scrollWidth > e.clientWidth}));
            return {cards,stations,fonts:[...document.querySelectorAll('.factory-comparison th, .factory-comparison caption')].map(e=>getComputedStyle(e).fontFamily),notes:[...document.querySelectorAll('.factory-note')].map(e=>({align:getComputedStyle(e).textAlign,size:parseFloat(getComputedStyle(e).fontSize)}))};
          });
          assert(design.fonts.every(font => font.includes('Departure Mono')));
          assert(design.notes.length === 2 && design.notes.every(note => note.align === 'center' && note.size <= 14));
          assert(design.stations.every(station => station.background === 'rgb(255, 255, 255)' && station.font.includes('Departure Mono') && !/^\d/.test(station.title) && !station.overflow));
          if (width === 1440) {
            assert(design.cards[0].width > design.cards[1].width * 1.9, 'Software spans two columns');
            assert(design.cards[0].y === design.cards[1].y && design.cards[2].y === design.cards[3].y && design.cards[3].y === design.cards[4].y, 'two cards then three');
            assert(Math.max(...design.stations.map(s=>s.height))-Math.min(...design.stations.map(s=>s.height)) < 1, 'equal station heights');
          }
        } else if (width === 1440) {
          await page.locator('.tool-body').scrollIntoViewIfNeeded();
          const panel = await page.locator('.tool-links').boundingBox();
          const header = await page.locator('.site-header').boundingBox();
          assert(panel.y >= header.y + header.height, `${route}: sticky source panel clears header`);
          await page.evaluate(() => scrollTo(0,0));
        }
        assert.equal(await page.locator('.site-footer').evaluate(e => getComputedStyle(e).marginBlockStart), '0px', 'footer adds no duplicate section gap');
        await page.screenshot({path: path.join(evidence, `${slug}-${width}.png`), fullPage: true});
        await page.screenshot({path: path.join(evidence, `${slug}-${width}-hero.png`)});
        if (width === 390) {
          await page.locator('[data-mobile-menu-toggle]').click();
          assert(await page.locator('#mobile-navigation').isVisible());
          assert(await page.locator('#mobile-navigation a[href$="ecosystem/factories/"]').count() > 0, 'mobile factory navigation');
          await page.keyboard.press('Escape');
          assert(await page.locator('#mobile-navigation').isHidden());
        }
        if (process.env.AXE_SCRIPT) {
          await page.addScriptTag({path: process.env.AXE_SCRIPT});
          const result = await page.evaluate(() => axe.run(document, {runOnly: {type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21aa']}}));
          const audit = {route, width, violations: result.violations, passes: result.passes.length};
          receipt.accessibility.push(audit);
          fs.writeFileSync(path.join(evidence, `axe-${slug}-${width}.json`), JSON.stringify(audit, null, 2));
          assert.deepEqual(result.violations.map(item => ({id: item.id, targets: item.nodes.map(node => node.target)})), [], `${route}: accessibility at ${width}`);
        }
        if (slug !== 'factories') {
          const video = page.locator('main video');
          assert.equal(await video.count(), 1);
          assert.equal(await video.getAttribute('preload'), 'none');
          assert.notEqual(await video.getAttribute('controls'), null);
          assert.equal(await video.getAttribute('autoplay'), null);
          if (width === 1440) {
            const media = await video.evaluate(async video => {
              video.muted = true;
              const loaded = new Promise((resolve, reject) => {
                const timer = setTimeout(() => reject(new Error(`Video metadata timeout: ${video.currentSrc}`)), 60000);
                video.addEventListener('loadedmetadata', () => { clearTimeout(timer); resolve(); }, {once: true});
                video.addEventListener('error', () => { clearTimeout(timer); reject(new Error(`Video error ${video.error?.code}: ${video.currentSrc}`)); }, {once: true});
              });
              video.load(); await loaded; await video.play();
              await new Promise((resolve, reject) => { const timer = setTimeout(() => reject(new Error('Playback did not advance within 30 seconds')), 30000); const check = () => { if (video.currentTime > 0.1) { clearTimeout(timer); video.removeEventListener('timeupdate', check); resolve(); } }; video.addEventListener('timeupdate', check); check(); }); video.pause();
              return {src: video.currentSrc, duration: video.duration, width: video.videoWidth, height: video.videoHeight, currentTime: video.currentTime};
            });
            assert(media.duration > 0 && media.width > 0 && media.currentTime > 0, `${route}: actual playback`);
            const download = await context.request.head(media.src, {timeout: 60000});
            assert(download.ok(), `${route}: public download ${download.status()}`);
            receipt.media.push({route, ...media, downloadStatus: download.status(), contentType: download.headers()['content-type'], verification: 'Metadata decoded, muted playback advanced and public download HEAD succeeded; this is not full listening or creative approval.'});
          }
        }
        receipt.pages.push({route, width, images: images.length, status: response.status()});
      }
      for (const route of ['/', '/ecosystem/', '/ecosystem/tooling/', '/ecosystem/primitives/', '/ecosystem/showcase/']) {
        assert.equal((await page.goto(base + route, {waitUntil: 'domcontentloaded'})).status(), 200);
        assert.equal(await page.locator('h1').count(), 1);
        if (route === '/ecosystem/') {
          const carousel = page.locator('[aria-labelledby="factories-title"][data-carousel]');
          assert.equal(await carousel.locator('[data-carousel-track] > li').count(), 5);
          assert.equal(await carousel.locator('#factories-title a').evaluate(e => getComputedStyle(e).textDecorationLine), 'none');
          await carousel.scrollIntoViewIfNeeded();
          await carousel.locator('[data-carousel-next]').click();
          await page.waitForFunction(() => document.querySelector('[aria-labelledby="factories-title"] [data-carousel-track]').scrollLeft > 0);
          await page.screenshot({path:path.join(evidence, `ecosystem-carousel-${width}.png`)});
        }
        assert(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1), `${route}: regression overflow`);
      }
    }
    for (const href of internalLinks) {
      const response = await context.request.get(href);
      receipt.links.push({url: href, status: response.status()});
      assert(response.ok(), `${href}: ${response.status()}`);
    }
    const index = await (await context.request.get(base + '/.well-known/kujo-site-index.json')).json();
    for (const slug of slugs) assert.equal(index.items.filter(item => new URL(item.url, base).pathname === `/ecosystem/${slug}/`).length, 1, `${slug}: discovery search record`);
    const nojs = await browser.newContext({javaScriptEnabled: false, viewport: {width: 390, height: 844}});
    const staticPage = await nojs.newPage();
    for (const slug of slugs) {
      await staticPage.goto(`${base}/ecosystem/${slug}/`);
      assert(await staticPage.locator('main h1').isVisible());
      assert(await staticPage.locator('main a').count() > 0, `${slug}: static links`);
      if (slug !== 'factories') assert(await staticPage.locator('main video[controls]').isVisible(), `${slug}: native no-JS player`);
    }
    await nojs.close();
    assert.deepEqual(receipt.consoleErrors, []);
    receipt.result = 'passed';
    receipt.accessibilityMode = process.env.AXE_SCRIPT ? 'axe WCAG A/AA' : 'Axe not configured; automated WCAG audit not performed';
    console.log('Factories browser checks passed: six pages, desktop/mobile, images, native video playback, links, no-JS, discovery, navigation and existing-route regressions.');
  } catch (error) {
    receipt.result = 'failed'; receipt.error = error.stack; throw error;
  } finally {
    receipt.finished = new Date().toISOString();
    fs.writeFileSync(path.join(evidence, 'receipt.json'), JSON.stringify(receipt, null, 2));
    await browser.close();
  }
})().catch(error => { console.error(error); process.exitCode = 1; });
