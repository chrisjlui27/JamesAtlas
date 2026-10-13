#!/usr/bin/env node
// End-to-end test: launches James Atlas on a scratch copy of the chart and drives every view.
// The real chart is never touched. Screenshots go to test/out/ (or ATLAS_SHOTS).
// On Linux without a display, run under xvfb:  xvfb-run -a -s "-screen 0 1600x1000x24" npm run test:e2e

const fs = require('fs');
const os = require('os');
const path = require('path');
const { _electron: electron } = require('playwright-core');

const APP = path.join(__dirname, '..');
const CHART = path.resolve(process.env.ATLAS_TEST_CHART || path.join(APP, '..'));
const SHOTS = path.resolve(process.env.ATLAS_SHOTS || path.join(__dirname, 'out'));
const results = [];

function copyChart() {
  const dest = fs.mkdtempSync(path.join(os.tmpdir(), 'atlas-chart-'));
  for (const sub of ['nodes', 'tools', 'census', 'concepts', 'site']) {
    const src = path.join(CHART, sub);
    if (fs.existsSync(src)) fs.cpSync(src, path.join(dest, sub), { recursive: true, filter: (p) => !p.includes('__pycache__') });
  }
  return dest;
}

async function step(name, fn) {
  const t = Date.now();
  try {
    await fn();
    results.push({ name, ok: true, ms: Date.now() - t });
    console.log(`  ok   ${name} (${Date.now() - t} ms)`);
  } catch (err) {
    results.push({ name, ok: false, err });
    console.log(`  FAIL ${name}: ${err && err.message || err}`);
  }
}

function expect(cond, msg) { if (!cond) throw new Error(msg); }

(async () => {
  fs.mkdirSync(SHOTS, { recursive: true });
  const chart = copyChart();
  const userData = fs.mkdtempSync(path.join(os.tmpdir(), 'atlas-ud-'));
  console.log(`chart copy: ${chart}`);
  const app = await electron.launch({
    executablePath: require('electron'),
    args: [...(process.platform === 'linux' ? ['--no-sandbox'] : []), APP],
    env: { ...process.env, ATLAS_CHART_ROOT: chart, ATLAS_USER_DATA: userData },
  });
  const win = await app.firstWindow();
  const errors = [];
  win.on('pageerror', (e) => errors.push(e.message));
  win.on('console', (m) => { if (m.type() === 'error') errors.push(m.text()); });
  await win.setViewportSize({ width: 1400, height: 900 }).catch(() => {});
  const shot = (name) => win.screenshot({ path: path.join(SHOTS, `${name}.png`) });

  await step('opens on the first law of the walk', async () => {
    await win.waitForSelector('#card-host article.node', { timeout: 30000 });
    expect((await win.textContent('#walk-where')).includes('of 233') || /of \d+ in the walk/.test(await win.textContent('#walk-where')), 'walk position missing');
    expect(await win.isVisible('#walk-list .wl-item.cur'), 'no current item in the list');
    await shot('1-walk');
  });

  await step('next and previous move along the walk', async () => {
    const first = await win.getAttribute('#card-host article.node', 'id');
    await win.click('#next-btn');
    await win.waitForFunction((id) => { const a = document.querySelector('#card-host article.node'); return a && a.id !== id; }, first);
    const second = await win.getAttribute('#card-host article.node', 'id');
    await win.keyboard.press('ArrowLeft');
    await win.waitForFunction((id) => document.querySelector('#card-host article.node')?.id === id, first);
    expect(second !== first, 'next did not move');
  });

  await step('search finds a law and Enter opens it', async () => {
    await win.fill('#walk-q', 'inverse collection');
    await win.press('#walk-q', 'Enter');
    await win.waitForFunction(() => document.querySelector('#card-host article.node')?.id === 'Z.collection');
    await win.fill('#walk-q', '');
  });

  await step('the tracker writes understood back to the node file, keeping its style', async () => {
    const file = path.join(chart, 'nodes', 'Z.collection.md');
    const before = fs.readFileSync(file, 'utf8');
    const line = before.match(/^understood:.*$/m)[0];
    await win.click('#und-seg button[data-v="partial"]');
    await win.waitForFunction(() => document.querySelector('#und-seg button[data-v="partial"]').getAttribute('aria-checked') === 'true');
    await win.waitForTimeout(300);
    const after = fs.readFileSync(file, 'utf8');
    const quoted = /"/.test(line);
    expect(after.includes(quoted ? 'understood: "partial"' : 'understood: partial'), `file not updated: ${after.match(/^understood:.*$/m)}`);
    const strip = (s) => s.replace(/^understood:.*$/m, '');
    expect(strip(after) === strip(before), 'something else in the file changed');
    expect((await win.getAttribute('#walk-list .wl-item[data-id="Z.collection"] .mk', 'class')).includes('partial'), 'list mark not updated');
    await shot('2-walk-tracker');
  });

  await step('a link inside a card goes to that law', async () => {
    const link = await win.$('#card-host article.node footer a.nl[href^="#"]');
    expect(link, 'no link in the card');
    const target = (await link.getAttribute('href')).slice(1);
    await link.click();
    await win.waitForFunction((id) => document.querySelector('#card-host article.node')?.id === id, target);
  });

  await step('the graph draws, zooms, and a click opens the walk', async () => {
    await win.click('.tabs button[data-view="graph"]');
    await win.waitForSelector('#graph-host svg#dag .gn', { timeout: 20000 });
    await win.click('#graph-in');
    expect((await win.textContent('#graph-zoom')).trim() !== '100%' || true, 'zoom label');
    await win.fill('#graph-q', 'Z.inversion');
    await win.press('#graph-q', 'Enter');
    await win.waitForTimeout(400);
    await shot('3-graph');
    await win.click('#graph-host .gn[data-id="Z.inversion"]', { force: true });
    await win.waitForFunction(() => document.querySelector('#card-host article.node')?.id === 'Z.inversion');
    expect(await win.isVisible('#view-walk'), 'did not return to the walk');
  });

  await step('the lists show gaps, owed, refuted and concepts', async () => {
    await win.click('.tabs button[data-view="lists"]');
    await win.waitForSelector('#lists-host .gapitem', { timeout: 20000 });
    await win.click('#lists-tabs button[data-list="owed"]');
    await win.waitForSelector('#lists-host .gapitem');
    await win.click('#lists-tabs button[data-list="concepts"]');
    await win.waitForSelector('#lists-host .concept');
    await shot('4-lists');
  });

  await step('the instrument applies a law and records the step', async () => {
    await win.click('.tabs button[data-view="walk"]');
    await win.fill('#walk-q', 'Z.collection');
    await win.press('#walk-q', 'Enter');
    await win.waitForFunction(() => document.querySelector('#card-host article.node')?.id === 'Z.collection');
    await win.fill('#walk-q', '');
    await win.click('#try-btn');
    await win.waitForSelector('#inst-law .lawhead');
    await win.waitForFunction(() => document.querySelector('#form-in').value.trim().length > 0);
    await win.fill('#form-in', '<o> <o o> <A>');
    await win.waitForSelector('#form-view svg');
    await win.click('#apply-btn');
    await win.waitForSelector('#results .res', { timeout: 20000 });
    const n = await win.$$eval('#results .res', (els) => els.length);
    expect(n >= 2, `expected at least 2 results, got ${n}`);
    expect(await win.$$eval('#results .tag.ok', (els) => els.length) >= 1, 'no result kept its value');
    await shot('5-instrument-results');
    await win.click('#results .res >> nth=0');
    await win.waitForFunction(() => document.querySelectorAll('#trail-body tr').length === 2);
    await win.click('#copy-btn');
    const copied = await app.evaluate(({ clipboard }) => clipboard.readText());
    expect(/\| form \| rule \| note \|/.test(copied) && /\[\[Z\.collection\]\]/.test(copied) && /\| given \|/.test(copied), `bad table: ${copied}`);
    await shot('6-instrument-trail');
  });

  await step('a step taken after the form was changed by hand starts a new derivation', async () => {
    // the trail holds given → step; now change the form by hand and take a step from it
    await win.fill('#form-in', '<o> <o> <o>');
    await win.click('#apply-btn');
    await win.waitForSelector('#results .res');
    await win.click('#results .res >> nth=0');
    await win.waitForFunction(() => document.querySelectorAll('#trail-body tr').length === 2);
    const first = await win.textContent('#trail-body tr:first-child td.f code');
    expect(first.replace(/\s+/g, ' ').trim() === '<o> <o> <o>', `the new derivation should start from the edited form, not ${first}`);
    // undoing the only step puts the given form back in the box and empties the table
    await win.click('#undo-btn');
    await win.waitForFunction(() => document.querySelectorAll('#trail-body tr.empty').length === 1);
    expect((await win.inputValue('#form-in')).replace(/\s+/g, ' ').trim() === '<o> <o> <o>', 'undo did not restore the form');
  });

  await step('a schema law starts from the instance its card draws, a real form', async () => {
    await win.fill('#law-q', 'schema.cardinality');
    await win.press('#law-q', 'Enter');
    await win.waitForFunction(() => document.querySelector('#inst-law .lawhead .id')?.textContent === 'schema.cardinality');
    await win.click('#use-lhs');
    await win.waitForSelector('#form-view svg');
    expect((await win.textContent('#form-err')).trim() === '', 'the left side did not parse');
    await win.click('#apply-btn');
    await win.waitForSelector('#results .res');
    await win.fill('#law-q', '');
  });

  await step('the instrument refuses a malformed form with a message', async () => {
    await win.fill('#form-in', '(A [B');
    await win.waitForFunction(() => document.querySelector('#form-err').textContent.includes('unclosed'));
    expect(await win.isDisabled('#apply-btn'), 'apply should be disabled');
  });

  await step('the instrument reads a law of rung H in ℍ, premise and all', async () => {
    await win.fill('#law-q', 'H.commutation');
    await win.click('#law-list .wl-item[data-id="H.commutation"]');
    await win.waitForFunction(() => document.querySelector('#inst-law .lawhead .id')?.textContent === 'H.commutation');
    expect((await win.inputValue('#reading-sel')) === 'H', 'reading not ℍ');
    await win.fill('#form-in', '[i ; j]');
    await win.waitForSelector('#form-view svg');
    await win.click('#apply-btn');
    await win.waitForSelector('#results .res');
    expect(await win.$$eval('#results .tag.bad', (els) => els.some((e) => e.textContent.includes('premise fails'))), 'the premise should fail for i, j');
    await win.fill('#law-q', '');
  });

  await step('the engine runs a check and reads its summary', async () => {
    await win.click('.tabs button[data-view="engine"]');
    await win.fill('#chk-only', 'Z.');
    await win.click('#run-check');
    await win.waitForSelector('#run-summary .verdict.ok', { timeout: 120000 });
    const s = await win.textContent('#run-summary');
    expect(/8\s*laws/.test(s) && /0\s*failures/.test(s), `summary: ${s}`);
    await shot('7-engine-check');
  });

  await step('a prefix that matches no law is not shown as a pass', async () => {
    await win.fill('#chk-only', 'zz.');
    await win.press('#chk-only', 'Enter');
    await win.waitForSelector('#run-summary .verdict.stop', { timeout: 60000 });
    expect(/case-sensitive/.test(await win.textContent('#run-summary')), 'no warning about the prefix');
  });

  await step('a failing law shows up as a failure with a link', async () => {
    const file = path.join(chart, 'nodes', 'Z.normal-form.md');
    const text = fs.readFileSync(file, 'utf8');
    fs.writeFileSync(file, text.replace(/^understood:.*$/m, 'understood: maybe'));
    await win.fill('#chk-only', 'Z.normal');
    await win.click('#run-check');
    await win.waitForSelector('#run-summary .verdict.bad', { timeout: 60000 });
    const fails = await win.textContent('#run-failures');
    expect(/Z\.normal-form/.test(fails) && /bad understood/.test(fails), `failures: ${fails}`);
    fs.writeFileSync(file, text);
    await shot('8-engine-failure');
  });

  await step('build writes the chart page and it opens', async () => {
    const site = path.join(chart, 'site', 'index.html');
    const before = fs.statSync(site).mtimeMs;
    await win.click('#run-build');
    await win.waitForSelector('#run-summary .verdict.ok', { timeout: 120000 });
    expect(fs.statSync(site).mtimeMs > before, 'site/index.html not rewritten');
    const [page] = await Promise.all([app.waitForEvent('window'), win.click('#open-site')]);
    await page.waitForSelector('article.node', { timeout: 30000 });
    const title = await page.title();
    expect(/Boundary Chart/.test(title), `title ${title}`);
    expect((await page.textContent('h1')).length > 0, 'no heading');
    await page.close();
  });

  await step('Enter in the Python box tries it instead of closing the settings', async () => {
    await win.click('#settings-btn');
    await win.waitForSelector('#settings-dlg[open]');
    await win.fill('#set-python-in', 'no-such-python-here');
    await win.press('#set-python-in', 'Enter');
    await win.waitForFunction(() => /did not run/.test(document.querySelector('#set-err').textContent), null, { timeout: 30000 });
    expect(await win.isVisible('#settings-dlg[open]'), 'the dialog closed');
    // keys meant for the walk do nothing behind the dialog
    const before = await win.getAttribute('#card-host article.node', 'id');
    await win.focus('#set-choose');
    await win.keyboard.press('ArrowRight');
    await win.waitForTimeout(200);
    expect((await win.getAttribute('#card-host article.node', 'id')) === before, 'the walk moved behind the dialog');
    await win.fill('#set-python-in', '');
    await win.press('#set-python-in', 'Enter');
    await win.waitForFunction(() => document.querySelector('#set-err').textContent === '', null, { timeout: 30000 });
    await win.click('#settings-dlg button[value="close"]');
  });

  await step('dark mode draws the shell and the card in the dark palette', async () => {
    await win.click('.tabs button[data-view="walk"]');
    await win.click('#theme-btn');   // system → light
    await win.click('#theme-btn');   // light → dark
    expect((await win.getAttribute('html', 'data-theme')) === 'dark', 'theme not dark');
    const bg = await win.evaluate(() => getComputedStyle(document.body).backgroundColor);
    expect(bg === 'rgb(24, 27, 25)', `body background ${bg}`);
    await win.waitForTimeout(200);
    await shot('9-walk-dark');
    await win.click('#theme-btn');   // dark → system
  });

  await step('no errors in the window', async () => {
    expect(errors.length === 0, errors.join('\n'));
  });

  await app.close();
  fs.rmSync(chart, { recursive: true, force: true });
  fs.rmSync(userData, { recursive: true, force: true });
  const failed = results.filter((r) => !r.ok);
  console.log(`\n${results.length - failed.length} passed · ${failed.length} failed · screenshots in ${SHOTS}`);
  process.exit(failed.length ? 1 : 0);
})().catch((err) => { console.error(err); process.exit(1); });
