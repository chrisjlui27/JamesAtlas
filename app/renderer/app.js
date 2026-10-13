// Starting up: find the chart and Python, load the walk, and keep it fresh.
'use strict';

(function (A) {
  const blocker = A.$('#blocker');
  const dlg = A.$('#settings-dlg');
  let loads = 0;

  // ------------------------------------------------------------------ theme: system → light → dark
  const THEMES = ['system', 'light', 'dark'];
  let theme = 'system';
  try { theme = localStorage.getItem('atlas.theme') || 'system'; } catch (_) { /* default */ }
  function applyTheme() {
    if (theme === 'system') delete document.documentElement.dataset.theme;
    else document.documentElement.dataset.theme = theme;
    const b = A.$('#theme-btn');
    b.innerHTML = {
      system: '<svg class="icon" viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="5.5"/><path d="M8 2.5v11a5.5 5.5 0 0 0 0-11z" fill="currentColor"/></svg>',
      light: '<svg class="icon" viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="3"/><path d="M8 1.5v1.6M8 12.9v1.6M1.5 8h1.6M12.9 8h1.6M3.4 3.4l1.1 1.1M11.5 11.5l1.1 1.1M3.4 12.6l1.1-1.1M11.5 4.5l1.1-1.1"/></svg>',
      dark: '<svg class="icon" viewBox="0 0 16 16" aria-hidden="true"><path d="M12.5 10.2A5.5 5.5 0 0 1 5.8 3.5a5.5 5.5 0 1 0 6.7 6.7z"/></svg>',
    }[theme];
    b.title = `Theme: ${theme === 'system' ? 'follow the system' : theme} (click to change)`;
  }
  A.$('#theme-btn').addEventListener('click', () => {
    theme = THEMES[(THEMES.indexOf(theme) + 1) % THEMES.length];
    try { localStorage.setItem('atlas.theme', theme); } catch (_) { /* fine */ }
    applyTheme();
  });
  applyTheme();
  A.$$('[data-mark]').forEach((b) => b.insertAdjacentHTML('afterbegin', A.mark(b.dataset.mark) + ' '));

  // ------------------------------------------------------------------ the blocker: no chart, no Python
  // primary: which way out comes first — 'chart' (choose the folder), 'python' (Python settings), 'retry' (try again)
  const PRIMARY = { chart: '#blocker-choose', python: '#blocker-settings', retry: '#blocker-retry' };
  function block(title, msg, primary = null, detail = '') {
    A.$('#blocker-title').textContent = title;
    A.$('#blocker-msg').textContent = msg || '';
    A.$('#blocker-detail').textContent = detail || '';
    A.$('#blocker-detail').hidden = !detail;
    A.$('#blocker-actions').hidden = !primary;
    for (const [k, sel] of Object.entries(PRIMARY)) A.$(sel).classList.toggle('primary', k === primary);
    A.$('main.views').inert = true;      // the views behind take no focus and no keys
    blocker.hidden = false;
    if (primary) A.$(PRIMARY[primary]).focus();
  }
  function unblock() {
    blocker.hidden = true;
    A.$('main.views').inert = false;
  }

  // ------------------------------------------------------------------ loading the chart
  async function load() {
    // chart.reload re-reads the node files and the ledgers (chart.summary would answer from what was read before)
    const s = await A.call('chart.reload', {}, { quiet: true });
    A.state.summary = s;
    A.state.byId = Object.fromEntries(s.nodes.map((n) => [n.id, n]));
    A.state.walk = s.nodes.map((n) => n.id);
    A.$('#chart-css').textContent = s.css;
    loads++;
    if (!A.isNode(A.state.current)) A.state.current = A.state.walk[0];
    A.emit('loaded', { first: loads === 1 });
    return s;
  }

  async function boot() {
    block('Opening the chart…', '');
    let info;
    try {
      info = await window.atlas.info();
    } catch (err) {
      block('James Atlas could not start', 'Something went wrong before the chart could be opened.', 'retry', A.cleanError(err));
      return;
    }
    A.state.info = info;
    fillSettings(info);
    if (!info.chartOk) {
      block('Where is the Boundary Chart?', 'Choose the folder that holds nodes and tools — the chart itself. James Atlas reads it there and writes back only your “understood” marks.', 'chart');
      return;
    }
    if (!info.python) {
      block('Python 3 is needed', 'The chart’s engine is Python 3 (standard library only), and James Atlas runs it. Install Python 3 from python.org — tick “Add python.exe to PATH” — then press Try again; or, if it is installed somewhere unusual, tell James Atlas where under Python settings.',
        'python', info.pythonError || '');
      return;
    }
    try {
      await load();
    } catch (err) {
      block('The chart could not be read', 'A file in the chart could not be read. Fix it (an editor will open it), then press Try again.', 'retry', err.message);
      return;
    }
    unblock();
    const start = A.isNode(info.lastNode) ? info.lastNode : A.state.walk[0];
    const view = ['walk', 'graph', 'lists', 'engine', 'instrument'].includes(info.view) ? info.view : 'walk';
    A.state.current = start;
    A.emit('current', start);
    A.showView(view);
  }

  // ------------------------------------------------------------------ outside changes: an editor, a check run, a pull
  const reload = A.debounce(async (what) => {
    if (!A.state.summary) return;
    try {
      await load();
      if (what !== 'nodes' || A.state.view !== 'engine') A.toast(what === 'nodes' ? 'The chart changed on disk — reloaded.' : 'Reloaded the chart and its ledgers.');
    } catch (err) {
      A.toast('The chart could not be reloaded: ' + err.message, true, 8000);
    }
  }, 500);
  window.atlas.onChartChanged(({ what }) => {
    if (A.state.running && A.state.running.tool === 'check' && what === 'census') return;   // mid-run ledger writes
    reload(what);
  });
  window.atlas.onBridgeCrash(({ message }) => {
    console.warn(message);
    A.toast('The Python bridge stopped; it will restart on the next request.', true, 6000);
  });
  window.atlas.onMenu((what) => { if (what === 'choose-chart') chooseChart(); });

  // ------------------------------------------------------------------ settings
  function fillSettings(info) {
    A.$('#set-chart').textContent = info.chartRoot || 'not chosen';
    A.$('#set-python').textContent = info.python ? `${info.python.label} — Python ${info.python.version} (${info.python.executable})` : (info.pythonError || 'not found');
    A.$('#set-python-in', dlg).value = info.pythonSetting || '';
    A.$('#set-version').textContent = `James Atlas ${info.appVersion} · ${info.platform}`;
  }

  async function chooseChart() {
    const r = await window.atlas.chooseChart();
    if (r.error) { A.toast(r.error, true, 7000); A.$('#set-err').textContent = r.error; return; }
    if (r.changed) {
      A.state.summary = null;
      if (dlg.open) dlg.close();
      await boot();
    }
  }

  A.$('#settings-btn').addEventListener('click', async () => {
    try { fillSettings(await window.atlas.info()); } catch (_) { /* keep what is shown */ }
    A.$('#set-err').textContent = '';
    dlg.showModal();
  });
  A.$('#set-choose').addEventListener('click', chooseChart);
  const pyIn = A.$('#set-python-in', dlg);
  async function usePython() {
    const err = A.$('#set-err', dlg);
    err.textContent = 'Trying it…';
    const r = await window.atlas.setPython(pyIn.value);
    if (r.ok) {
      fillSettings(await window.atlas.info());
      err.textContent = r.preferredFailed ? `What you entered did not run (${r.preferredFailed}); using ${r.python.label} — Python ${r.python.version} — instead.` : '';
      A.toast(`Using Python ${r.python.version}`);
      if (!A.state.summary) boot();
    } else {
      err.textContent = r.error;
    }
  }
  A.$('#set-python-btn', dlg).addEventListener('click', usePython);
  pyIn.addEventListener('keydown', (ev) => {
    // Enter would submit the dialog's form and close it, losing what was typed
    if (ev.key === 'Enter') { ev.preventDefault(); usePython(); }
  });
  A.$('#blocker-choose').addEventListener('click', chooseChart);
  A.$('#blocker-settings').addEventListener('click', () => { A.$('#settings-btn').click(); });
  A.$('#blocker-retry').addEventListener('click', async () => {
    await window.atlas.setPython(pyIn.value);   // forget what was found, look again
    boot();
  });

  // ------------------------------------------------------------------ tabs and keys
  A.$$('.tabs button').forEach((b) => b.addEventListener('click', () => A.showView(b.dataset.view)));
  document.addEventListener('keydown', (ev) => {
    if (A.typing(ev) || ev.ctrlKey || ev.metaKey || ev.altKey || dlg.open) return;
    const v = { 1: 'walk', 2: 'graph', 3: 'lists', 4: 'engine', 5: 'instrument' }[ev.key];
    if (v && blocker.hidden) { A.showView(v); ev.preventDefault(); }
  });

  boot();
})(window.A);
