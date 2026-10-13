// James Atlas — the main process: the window, the chart folder, Python, the bridge and the engine.

const { app, BrowserWindow, ipcMain, dialog, shell, Menu, session, clipboard } = require('electron');
const fs = require('fs');
const path = require('path');
const { Settings } = require('./settings');
const { findPython } = require('./python');
const { Bridge } = require('./bridge');
const { EngineRunner } = require('./engine');

if (process.env.ATLAS_USER_DATA) app.setPath('userData', path.resolve(process.env.ATLAS_USER_DATA));

const settings = new Settings(app.getPath('userData'));
const BRIDGE_METHODS = new Set([
  'ping', 'chart.summary', 'chart.card', 'chart.graph', 'chart.lists', 'chart.reload', 'chart.setUnderstood',
  'instrument.rules', 'instrument.law', 'instrument.inspect', 'instrument.apply',
]);
const NODE_ID = /^[A-Za-z0-9]+\.[A-Za-z0-9-]+$/;

let win = null;
let siteWin = null;
let python = null;          // { command, args, version, executable, label }
let pythonError = null;
let bridge = null;
let watcher = null;
let quietUntil = 0;         // the app's own writes do not count as outside changes

// ----------------------------------------------------------------------------- the chart folder

function isChart(dir) {
  try {
    return !!dir && fs.statSync(path.join(dir, 'nodes')).isDirectory() &&
      fs.existsSync(path.join(dir, 'tools', 'check.py')) && fs.existsSync(path.join(dir, 'tools', 'build.py'));
  } catch (_) {
    return false;
  }
}

function defaultChartRoot() {
  // Run from source, the app lives in <chart>/app; the chart is the folder above it.
  const above = path.resolve(__dirname, '..', '..');
  return isChart(above) ? above : null;
}

function chartRoot() {
  const env = process.env.ATLAS_CHART_ROOT && path.resolve(process.env.ATLAS_CHART_ROOT);
  if (env && isChart(env)) return env;
  const saved = settings.get('chartRoot');
  if (saved && isChart(saved)) return saved;
  return defaultChartRoot();
}

function bridgeFile(name) {
  return app.isPackaged
    ? path.join(process.resourcesPath, 'bridge', name)
    : path.join(__dirname, '..', 'bridge', name);
}

function bridgeScript() {
  return bridgeFile('atlas_bridge.py');
}

// ----------------------------------------------------------------------------- Python and the bridge

async function ensurePython() {
  if (python) return python;
  try {
    python = await findPython(process.env.ATLAS_PYTHON || settings.get('python'));
    pythonError = null;
  } catch (err) {
    pythonError = err.message;
    throw err;
  }
  return python;
}

async function ensureBridge() {
  const root = chartRoot();
  if (!root) throw new Error('No chart folder is open. Choose the Boundary Chart folder (the one with nodes/ and tools/ in it).');
  const py = await ensurePython();
  if (bridge && bridge.chartRoot === root && bridge.python === py) return bridge;
  if (bridge) bridge.stop();
  bridge = new Bridge({ python: py, script: bridgeScript(), chartRoot: root, log: (l) => console.log(l) });
  bridge.on('crash', (why) => send('atlas:bridge-crash', { message: why }));
  bridge.start();
  watchChart(root);
  return bridge;
}

function resetBridge() {
  if (bridge) bridge.stop();
  bridge = null;
}

// ----------------------------------------------------------------------------- watching for outside edits

function watchChart(root) {
  if (watcher && watcher.root === root) return;
  if (watcher) watcher.close();
  let timer = null;
  const fire = (what) => {
    if (Date.now() < quietUntil) return;
    clearTimeout(timer);
    timer = setTimeout(() => send('atlas:chart-changed', { what }), 600);
  };
  const ws = [];
  for (const sub of ['nodes', 'census']) {
    try {
      ws.push(fs.watch(path.join(root, sub), { persistent: false }, () => fire(sub)));
    } catch (_) { /* a folder that cannot be watched is simply not watched */ }
  }
  watcher = { root, close: () => ws.forEach((w) => w.close()) };
}

function send(channel, payload) {
  if (win && !win.isDestroyed()) win.webContents.send(channel, payload);
}

// ----------------------------------------------------------------------------- the engine

const engine = new EngineRunner({
  getPython: ensurePython,
  getChartRoot: () => {
    const root = chartRoot();
    if (!root) throw new Error('No chart folder is open.');
    return root;
  },
  send: (ev) => {
    send('atlas:engine', ev);
    if (ev.type === 'exit') send('atlas:chart-changed', { what: ev.tool });
  },
  checkWrapper: bridgeFile('check_progress.py'),
});

// ----------------------------------------------------------------------------- IPC

ipcMain.handle('atlas:info', async () => {
  const root = chartRoot();
  let py = null;
  try { py = await ensurePython(); } catch (_) { /* reported below */ }
  return {
    appVersion: app.getVersion(),
    platform: process.platform,
    packaged: app.isPackaged,
    chartRoot: root,
    chartOk: !!root,
    python: py ? { label: py.label, version: py.version, executable: py.executable } : null,
    pythonError,
    pythonSetting: settings.get('python') || '',
    lastNode: settings.get('lastNode'),
    view: settings.get('view'),
  };
});

ipcMain.handle('atlas:choose-chart', async () => {
  const r = await dialog.showOpenDialog(win, {
    title: 'Choose the Boundary Chart folder',
    message: 'The folder that holds nodes/ and tools/',
    properties: ['openDirectory'],
    defaultPath: chartRoot() || undefined,
  });
  if (r.canceled || !r.filePaths.length) return { changed: false, chartRoot: chartRoot() };
  const dir = r.filePaths[0];
  if (!isChart(dir)) return { changed: false, chartRoot: chartRoot(), error: `${dir} is not a Boundary Chart folder: it needs nodes/, tools/check.py and tools/build.py.` };
  settings.set('chartRoot', dir);
  resetBridge();
  return { changed: true, chartRoot: chartRoot() };
});

ipcMain.handle('atlas:set-python', async (_e, command) => {
  settings.set('python', String(command || '').trim());
  python = null;
  pythonError = null;
  resetBridge();
  try {
    const py = await ensurePython();
    return { ok: true, python: { label: py.label, version: py.version, executable: py.executable } };
  } catch (err) {
    return { ok: false, error: err.message };
  }
});

ipcMain.handle('atlas:set-setting', (_e, key, value) => {
  if (!['lastNode', 'view'].includes(key)) throw new Error(`Not a setting the window may change: ${key}`);
  settings.set(key, value);
  return true;
});

ipcMain.handle('atlas:bridge', async (_e, method, params) => {
  if (!BRIDGE_METHODS.has(method)) throw new Error(`Unknown request: ${method}`);
  const b = await ensureBridge();
  if (method === 'chart.setUnderstood') quietUntil = Date.now() + 2000;
  const timeout = method.startsWith('instrument.') ? 60000 : 180000;
  try {
    return await b.call(method, params, timeout);
  } catch (err) {
    // a request that never came back leaves the bridge busy: start a fresh one for the next request
    if (/did not answer/.test(err.message)) resetBridge();
    throw err;
  }
});

ipcMain.handle('atlas:run', (_e, tool, args) => engine.run(tool, Array.isArray(args) ? args : []));
ipcMain.handle('atlas:stop', (_e, runId) => engine.stop(runId));

ipcMain.handle('atlas:open-site', async () => {
  const root = chartRoot();
  const file = root && path.join(root, 'site', 'index.html');
  if (!file || !fs.existsSync(file)) return { ok: false, error: 'site/index.html has not been built yet — run Build first.' };
  openSiteWindow(file);
  return { ok: true };
});

ipcMain.handle('atlas:open-node-file', async (_e, id) => {
  const root = chartRoot();
  if (!root || !NODE_ID.test(String(id))) return { ok: false, error: 'not a node id' };
  const file = path.join(root, 'nodes', `${id}.md`);
  if (!fs.existsSync(file)) return { ok: false, error: `${id}.md not found` };
  const err = await shell.openPath(file);
  return err ? { ok: false, error: err } : { ok: true };
});

ipcMain.handle('atlas:copy', (_e, text) => {
  clipboard.writeText(String(text ?? ''));
  return true;
});

ipcMain.handle('atlas:open-external', async (_e, url) => {
  const u = String(url || '');
  if (!/^https?:\/\//i.test(u)) return false;
  await shell.openExternal(u);
  return true;
});

// ----------------------------------------------------------------------------- windows

function lockDown(contents) {
  contents.setWindowOpenHandler(({ url }) => {
    if (/^https?:\/\//i.test(url)) shell.openExternal(url);
    return { action: 'deny' };
  });
  contents.on('will-navigate', (e, url) => {
    if (url !== contents.getURL()) {
      e.preventDefault();
      if (/^https?:\/\//i.test(url)) shell.openExternal(url);
    }
  });
}

function createWindow() {
  const b = settings.get('bounds') || {};
  win = new BrowserWindow({
    width: b.width || 1320,
    height: b.height || 880,
    x: b.x, y: b.y,
    minWidth: 860,
    minHeight: 560,
    title: 'James Atlas',
    icon: path.join(__dirname, '..', 'build', 'icon.png'),
    backgroundColor: '#f6f7f5',
    show: false,
    autoHideMenuBar: false,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      contextIsolation: true,
      nodeIntegration: false,
      sandbox: true,
      spellcheck: false,
    },
  });
  lockDown(win.webContents);
  win.once('ready-to-show', () => win.show());
  const saveBounds = () => { if (win && !win.isDestroyed() && !win.isMinimized() && !win.isMaximized()) settings.set('bounds', win.getBounds()); };
  win.on('resize', debounce(saveBounds, 400));
  win.on('move', debounce(saveBounds, 400));
  win.on('closed', () => { win = null; });
  win.loadFile(path.join(__dirname, '..', 'renderer', 'index.html'));
}

function openSiteWindow(file) {
  if (siteWin && !siteWin.isDestroyed()) {
    siteWin.loadFile(file);
    siteWin.focus();
    return;
  }
  siteWin = new BrowserWindow({
    width: 1180, height: 900, title: 'Boundary Chart — the chart page',
    // the page is a fragment with no <meta charset>: read it as the UTF-8 build.py writes
    webPreferences: { contextIsolation: true, nodeIntegration: false, sandbox: true, defaultEncoding: 'utf-8' },
  });
  lockDown(siteWin.webContents);
  siteWin.on('closed', () => { siteWin = null; });
  siteWin.loadFile(file);
}

function debounce(fn, ms) {
  let t = null;
  return (...a) => { clearTimeout(t); t = setTimeout(() => fn(...a), ms); };
}

function buildMenu() {
  const isMac = process.platform === 'darwin';
  const template = [
    ...(isMac ? [{ role: 'appMenu' }] : []),
    {
      label: 'File',
      submenu: [
        { label: 'Choose chart folder…', accelerator: 'CmdOrCtrl+O', click: () => send('atlas:menu', 'choose-chart') },
        { label: 'Open the chart page (site/index.html)', click: () => openSiteFromMenu() },
        { type: 'separator' },
        isMac ? { role: 'close' } : { role: 'quit' },
      ],
    },
    { role: 'editMenu' },
    {
      label: 'View',
      submenu: [
        { role: 'reload' }, { role: 'toggleDevTools' }, { type: 'separator' },
        { role: 'resetZoom' }, { role: 'zoomIn' }, { role: 'zoomOut' }, { type: 'separator' }, { role: 'togglefullscreen' },
      ],
    },
    { role: 'windowMenu' },
  ];
  Menu.setApplicationMenu(Menu.buildFromTemplate(template));
}

function openSiteFromMenu() {
  const root = chartRoot();
  const file = root && path.join(root, 'site', 'index.html');
  if (file && fs.existsSync(file)) openSiteWindow(file);
  else dialog.showMessageBox({ message: 'site/index.html has not been built yet — run Build in the Engine tab first.' });
}

// ----------------------------------------------------------------------------- lifecycle

app.whenReady().then(() => {
  // Nothing in the app needs the network: the chart page's web fonts fall back to local ones.
  session.defaultSession.webRequest.onBeforeRequest((details, cb) => {
    const ok = /^(file|devtools|data|blob|chrome-extension):/i.test(details.url);
    cb({ cancel: !ok });
  });
  buildMenu();
  createWindow();
  app.on('activate', () => { if (BrowserWindow.getAllWindows().length === 0) createWindow(); });
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit();
});

app.on('before-quit', () => {
  engine.stopAll();
  if (bridge) bridge.stop();
  if (watcher) watcher.close();
});
