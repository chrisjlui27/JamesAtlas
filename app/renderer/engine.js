// The engine: check, build and census, run on the chart folder with their output streamed here.
'use strict';

(function (A) {
  const con = A.$('#console');
  const stopBtn = A.$('#run-stop');
  const runBtns = ['#run-check', '#run-build', '#run-census'].map((s) => A.$(s));
  const MAX_LINES = 20000;
  const SUMMARY = /^(\d+) nodes · (\d+) checks passed · (\d+) warnings · (\d+) failures$/;
  const ENTRY = /^\s*(FAIL|warn): ([A-Za-z0-9]+\.[A-Za-z0-9-]+(@[^:]*)?|chart|census): /;
  let run = null;           // { runId, tool, args, lines, fails, warns, summary }
  const history = [];
  let pendingLines = [];
  const PHASES = {
    laws: 'Checking the laws',
    'j1-ledger': 'Writing the 𝕁₁ ledger',
    'place-ledger': 'Reading the trunk at the places (p = 2, 3, 5, 7, 13)',
    'h-ledger': 'Reading the trunk in ℍ',
    'h-place-ledger': 'Reading rung H at the places, and the places in ℍ',
    witnesses: 'Running the witnesses',
    census: 'Taking the census of small forms',
  };
  let flushQueued = false;

  function classify(text) {
    const t = text.trimStart();
    if (t.startsWith('FAIL:')) return 'fail';
    if (t.startsWith('warn:')) return 'warn';
    if (SUMMARY.test(text.trim())) return 'sum';
    if (/Traceback|Error\b/.test(text)) return 'err';
    return '';
  }

  function append(text, cls) {
    pendingLines.push([text, cls]);
    if (!flushQueued) {
      flushQueued = true;
      requestAnimationFrame(flush);
    }
  }

  function flush() {
    flushQueued = false;
    const atBottom = con.scrollTop + con.clientHeight >= con.scrollHeight - 30;
    const frag = document.createDocumentFragment();
    for (const [text, cls] of pendingLines) {
      const line = A.el('span', { class: cls || null }, text + '\n');
      frag.append(line);
    }
    pendingLines = [];
    con.append(frag);
    while (con.childNodes.length > MAX_LINES) con.removeChild(con.firstChild);
    if (atBottom) con.scrollTop = con.scrollHeight;
  }

  function nodeLinks(text) {
    // a failure line reads "<node id>: message" (a schema instance: "<id>@n = 2: …")
    const m = text.match(/^([A-Za-z0-9]+\.[A-Za-z0-9-]+)(@[^:]*)?: ([\s\S]*)$/);
    if (m && A.isNode(m[1])) {
      return `<a href="#${A.esc(m[1])}">${A.esc(m[1] + (m[2] || ''))}</a> — ${A.esc(m[3])}`;
    }
    return A.esc(text);
  }

  function renderFailures() {
    const box = A.$('#run-failures');
    if (!run || (!run.fails.length && !run.warns.length)) { box.hidden = true; box.innerHTML = ''; return; }
    let h = '';
    if (run.fails.length) h += `<h4>${run.fails.length} failure${run.fails.length === 1 ? '' : 's'}</h4>` + run.fails.map((f) => `<div class="fl">${nodeLinks(f)}</div>`).join('');
    if (run.warns.length) h += `<h4 class="w">${run.warns.length} warning${run.warns.length === 1 ? '' : 's'}</h4>` + run.warns.map((f) => `<div class="fl">${nodeLinks(f)}</div>`).join('');
    box.innerHTML = h;
    box.hidden = false;
  }

  function renderSummary(exit) {
    const box = A.$('#run-summary');
    if (!run) { box.hidden = true; return; }
    const s = run.summary;
    let h = '';
    if (s) {
      h += `<div class="st"><b>${s.nodes}</b><span>laws</span></div><div class="st"><b>${s.checks.toLocaleString()}</b><span>checks passed</span></div>` +
        `<div class="st"><b>${s.warnings}</b><span>warnings</span></div><div class="st"><b>${s.failures}</b><span>failures</span></div>`;
    }
    if (exit) {
      const secs = exit.seconds < 90 ? `${exit.seconds.toFixed(1)} s` : `${Math.floor(exit.seconds / 60)} min ${Math.round(exit.seconds % 60)} s`;
      if (exit.stopped) h += `<span class="verdict stop">stopped after ${secs}</span>`;
      else if (run.tool === 'check' && s && s.nodes === 0) h += `<span class="verdict stop">no law’s id starts with “${A.esc(run.only || '')}” — ids are case-sensitive, e.g. Z. or H.</span>`;
      else if (exit.code === 0) h += `<span class="verdict ok">${run.tool === 'check' ? '0 failures' : 'done'} · ${secs}</span>`;
      else h += `<span class="verdict bad">${run.tool === 'check' && s ? `${s.failures} failure${s.failures === 1 ? '' : 's'}` : 'exit code ' + exit.code} · ${secs}</span>`;
    } else if (!s) {
      const p = run.progress || {};
      let label = PHASES[p.phase] || (run.tool === 'check' ? 'Starting' : 'Running');
      // a full check goes through up to six steps; say which one this is
      const steps = run.tool === 'check' && !run.only ? ['laws', 'j1-ledger', 'place-ledger', 'h-ledger', 'h-place-ledger', 'witnesses', 'census'].filter((k) => run.phasesSeen.has(k) || !run.skips.has(k)) : null;
      if (steps && p.phase && steps.includes(p.phase)) label = `Step ${steps.indexOf(p.phase) + 1} of ${steps.length}: ${label}`;
      let frac = null, detail = '';
      if (p.phase === 'laws' && p.total) { frac = p.done / p.total; detail = `${p.done} of ${p.total}${p.id ? ' — ' + p.id : ''}`; }
      else if (p.phase === 'witnesses' && p.wTotal) { frac = p.wDone / p.wTotal; detail = `${p.wDone} of ${p.wTotal}${p.wId ? ' — ' + p.wId : ''}`; }
      h += `<div class="prog"><div class="prog-label"><b>${A.esc(label)}</b> ${A.esc(detail)}</div>` +
        (frac !== null ? `<div class="bar"><i class="y" style="width:${(100 * frac).toFixed(1)}%"></i></div>` : '<div class="bar indet"><i></i></div>') +
        `<div class="muted small">${A.esc(elapsed())}</div></div>`;
    }
    box.innerHTML = h;
    box.hidden = !h;
  }

  function elapsed() {
    if (!run || !run.started) return '';
    const s = Math.round((Date.now() - run.started) / 1000);
    return s < 60 ? `${s} s` : `${Math.floor(s / 60)} min ${s % 60} s`;
  }

  setInterval(() => { if (run && !run.done) renderSummary(null); }, 1000);

  function busy(on, label) {
    runBtns.forEach((b) => { b.disabled = on; });
    stopBtn.disabled = !on;
    const st = A.$('#status-run');
    st.hidden = !on;
    st.textContent = on ? label : '';
    A.state.running = on ? run : null;
  }

  async function start(tool, args) {
    if (run && !run.done) { A.toast('A run is already going — stop it first.', true); return; }
    con.textContent = '';
    const only = tool === 'check' && args.includes('--only') ? args[args.indexOf('--only') + 1] : '';
    const skips = new Set();
    if (args.includes('--no-licences')) ['j1-ledger', 'place-ledger', 'h-ledger', 'h-place-ledger'].forEach((k) => skips.add(k));
    if (args.includes('--no-places')) ['place-ledger', 'h-ledger', 'h-place-ledger'].forEach((k) => skips.add(k));
    if (args.includes('--no-census')) skips.add('census');
    run = { tool, args, only, skips, phasesSeen: new Set(), fails: [], warns: [], summary: null, done: false, runId: null, started: Date.now(), progress: {}, lastEntry: null };
    A.$('#run-title').textContent = 'Starting…';
    renderFailures();
    renderSummary(null);
    busy(true, `${tool} running`);
    try {
      const r = await window.atlas.run(tool, args);
      run.runId = r.runId;
    } catch (err) {
      append(A.cleanError(err), 'err');
      run.done = true;
      busy(false);
      A.$('#run-title').textContent = `${tool}: could not start`;
    }
  }

  window.atlas.onEngine((ev) => {
    if (!run) return;
    if (run.runId !== null && ev.runId !== run.runId) return;
    if (ev.type === 'start') {
      run.runId = ev.runId;
      A.$('#run-title').textContent = ev.command;
      append('$ ' + ev.command, 'cmd');
    } else if (ev.type === 'progress') {
      const p = run.progress;
      if (ev.event === 'start') Object.assign(p, { total: ev.total, wTotal: ev.witnesses });
      else if (ev.event === 'phase') { p.phase = ev.name; run.phasesSeen.add(ev.name); }
      else if (ev.event === 'node') Object.assign(p, { phase: 'laws', done: ev.done, total: ev.total || p.total, id: ev.id });
      else if (ev.event === 'witness') Object.assign(p, { phase: 'witnesses', wDone: ev.done, wTotal: ev.total || p.wTotal, wId: ev.id });
      const st = A.$('#status-run');
      if (p.phase === 'laws' && p.total) st.textContent = `check ${p.done}/${p.total}`;
      else if (p.phase) st.textContent = `check: ${p.phase.replace(/-/g, ' ')}`;
    } else if (ev.type === 'line') {
      const cls = ev.stream === 'err' ? 'err' : classify(ev.text);
      append(ev.text, cls);
      const t = ev.text.trim();
      const m = t.match(SUMMARY);
      if (m) { run.summary = { nodes: +m[1], checks: +m[2], warnings: +m[3], failures: +m[4] }; renderSummary(null); }
      else if (run.summary && ev.stream === 'out') {
        // after the summary, check.py prints "  warn: <id>: …" and "  FAIL: <id>: …"; a failing witness's message
        // runs on over several lines, some of which may themselves start with FAIL — they belong to the entry above
        const e = ev.text.match(ENTRY);
        if (e) {
          run.lastEntry = { list: e[1] === 'FAIL' ? run.fails : run.warns, i: (e[1] === 'FAIL' ? run.fails : run.warns).push(ev.text.trim().slice(e[1].length + 1).trim()) - 1 };
        } else if (run.lastEntry && t) {
          run.lastEntry.list[run.lastEntry.i] += '\n' + ev.text;
        }
        renderFailures();
      }
    } else if (ev.type === 'exit') {
      run.done = true;
      busy(false);
      renderSummary(ev);
      const ok = ev.code === 0 && !ev.stopped;
      history.unshift({ tool: run.tool, args: run.args, ok, stopped: ev.stopped, summary: run.summary, seconds: ev.seconds, at: new Date() });
      renderHistory();
      append(ev.stopped ? '— stopped —' : `— exit code ${ev.code} —`, ok ? 'cmd' : 'err');
      if (run.tool === 'build' && ok) A.$('#open-site').disabled = false;
      A.emit('engine-finished', { tool: run.tool, ok });
      if (A.state.view !== 'engine') {
        const f = run.summary ? run.summary.failures : null;
        A.toast(`${run.tool} finished: ${f !== null ? `${f} failure${f === 1 ? '' : 's'}` : ok ? 'done' : ev.stopped ? 'stopped' : 'failed'}`, !ok);
      }
    }
  });

  function renderHistory() {
    const ol = A.$('#run-history');
    ol.textContent = '';
    for (const h of history) {
      const what = [h.tool, ...h.args].join(' ');
      const res = h.stopped ? '<span class="stop">stopped</span>' : h.summary ? `<span class="${h.summary.failures ? 'bad' : 'ok'}">${h.summary.failures} failure${h.summary.failures === 1 ? '' : 's'}</span>` : `<span class="${h.ok ? 'ok' : 'bad'}">${h.ok ? 'done' : 'failed'}</span>`;
      ol.append(A.el('li', { title: h.at.toLocaleTimeString() },
        A.el('code', { text: what }),
        A.el('span', { class: 'hres', html: `${res} · ${h.seconds < 10 ? h.seconds.toFixed(1) : h.seconds.toFixed(0)} s` })));
    }
  }

  const view = A.$('#view-engine');
  function checkArgs() {
    const args = [];
    const only = A.$('#chk-only', view).value.trim();
    if (only) args.push('--only', only);
    if (A.$('#chk-nocensus', view).checked) args.push('--no-census');
    if (A.$('#chk-nolic', view).checked) args.push('--no-licences');
    if (A.$('#chk-noplaces', view).checked) args.push('--no-places');
    const trials = parseInt(A.$('#chk-trials', view).value.trim(), 10);
    if (Number.isFinite(trials) && trials > 0) args.push('--trials', String(trials));
    const seed = parseInt(A.$('#chk-seed', view).value.trim(), 10);
    if (Number.isFinite(seed)) args.push('--seed', String(seed));
    return args;
  }

  A.$('#run-check').addEventListener('click', () => start('check', checkArgs()));
  for (const id of ['#chk-only', '#chk-trials', '#chk-seed']) {
    A.$(id).addEventListener('keydown', (ev) => { if (ev.key === 'Enter') { ev.preventDefault(); if (!A.$('#run-check').disabled) start('check', checkArgs()); } });
  }
  A.$('#run-build').addEventListener('click', () => start('build', []));
  A.$('#run-census').addEventListener('click', () => start('census', []));
  stopBtn.addEventListener('click', () => { if (run && run.runId !== null) window.atlas.stop(run.runId); });
  A.$('#open-site').addEventListener('click', async () => {
    const r = await window.atlas.openSite();
    if (r && !r.ok) A.toast(r.error, true);
  });
  A.followLinks(A.$('#run-failures'));

  A.on('loaded', () => {
    const dl = A.$('#rung-prefixes');
    dl.textContent = '';
    for (const r of A.state.summary.rungs) dl.append(A.el('option', { value: r.id + '.', label: `${r.title} (${r.nodes.length})` }));
  });

  A.views.engine = { shown() {} };
})(window.A);
