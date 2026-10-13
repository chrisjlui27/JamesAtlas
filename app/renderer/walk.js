// The walk: every law in walk order, one card at a time, with Lui's tracker.
'use strict';

(function (A) {
  const list = A.$('#walk-list');
  const host = A.$('#card-host');
  const q = A.$('#walk-q');
  const seg = A.$('#und-seg');
  let filterUnd = 'all';
  let collapsed = new Set();
  let cardToken = 0;

  try { collapsed = new Set(JSON.parse(localStorage.getItem('atlas.collapsed') || '[]')); } catch (_) { /* fresh */ }

  function renderList() {
    const s = A.state.summary;
    if (!s) return;
    list.textContent = '';
    for (const r of s.rungs) {
      const ids = r.nodes;
      const counts = { yes: 0, partial: 0, no: 0 };
      ids.forEach((id) => { counts[A.state.byId[id].understood]++; });
      const pct = (k) => (100 * counts[k] / ids.length).toFixed(1) + '%';
      const head = A.el('li', { class: 'rung-h' + (collapsed.has(r.id) ? ' collapsed' : ''), dataset: { rung: r.id }, title: `${counts.yes} understood · ${counts.partial} partly · ${counts.no} not yet` },
        A.el('span', { class: 'caret', text: collapsed.has(r.id) ? '▸' : '▾' }),
        A.el('span', { class: 'rid', text: r.id }),
        A.el('span', { text: r.title }),
        A.el('span', { class: 'rcount', text: String(ids.length) }),
        A.el('span', { class: 'rmini', html: `<i class="y" style="width:${pct('yes')};background:var(--ok)"></i><i style="width:${pct('partial')};background:var(--warn)"></i>` }));
      head.addEventListener('click', () => toggleRung(r.id));
      list.append(head);
      for (const id of ids) {
        const n = A.state.byId[id];
        const li = A.el('li', { class: 'wl-item', dataset: { id, rung: r.id }, title: `${id} — ${n.title}` },
          A.el('span', { class: `mk ${n.understood}`, html: A.mark(n.understood), title: A.UND_WORD[n.understood] }),
          A.el('span', { class: 'wid' }, A.el('i', { class: `tdot td-${n.type}`, title: n.type }), id),
          A.el('span', { class: 'wt', text: n.title }));
        li.addEventListener('click', () => A.go(id));
        list.append(li);
      }
    }
    applyFilter();
    markCurrent();
    renderProgress();
  }

  function toggleRung(r) {
    if (collapsed.has(r)) collapsed.delete(r); else collapsed.add(r);
    try { localStorage.setItem('atlas.collapsed', JSON.stringify([...collapsed])); } catch (_) { /* fine */ }
    const head = list.querySelector(`.rung-h[data-rung="${CSS.escape(r)}"]`);
    if (head) {
      head.classList.toggle('collapsed', collapsed.has(r));
      head.querySelector('.caret').textContent = collapsed.has(r) ? '▸' : '▾';
    }
    applyFilter();
  }

  function applyFilter() {
    const text = q.value.trim().toLowerCase();
    const words = text.split(/\s+/).filter(Boolean);
    let shown = 0;
    for (const li of A.$$('.wl-item', list)) {
      const n = A.state.byId[li.dataset.id];
      const hitText = !words.length || words.every((w) => n.search.includes(w) || n.law.toLowerCase().includes(w));
      const hitUnd = filterUnd === 'all' || n.understood === filterUnd;
      const folded = !words.length && filterUnd === 'all' && collapsed.has(li.dataset.rung);
      const on = hitText && hitUnd && !folded;
      li.classList.toggle('off', !on);
      if (on) shown++;
    }
    // a rung with nothing to show under a search keeps its heading out of the way
    for (const h of A.$$('.rung-h', list)) {
      const any = A.$$(`.wl-item[data-rung="${CSS.escape(h.dataset.rung)}"]`, list).some((li) => !li.classList.contains('off'));
      h.hidden = !any && (words.length > 0 || filterUnd !== 'all');
    }
    let empty = A.$('.wl-empty', list);
    if (!shown && (words.length || filterUnd !== 'all')) {
      if (!empty) list.append(A.el('li', { class: 'wl-empty', text: 'No law matches.' }));
    } else if (empty) empty.remove();
  }

  function renderProgress() {
    const u = A.state.summary.understood;
    const total = u.yes + u.partial + u.no;
    const pct = (k) => (100 * u[k] / total).toFixed(1) + '%';
    A.$('#walk-progress').innerHTML =
      `<div class="bar" title="${u.yes} understood · ${u.partial} partly · ${u.no} not yet"><i class="y" style="width:${pct('yes')}"></i><i class="p" style="width:${pct('partial')}"></i></div>` +
      `<span>${A.mark('yes')} ${u.yes} understood · ${A.mark('partial')} ${u.partial} partly · ${A.mark('no')} ${u.no} not yet — of ${total} laws</span>`;
  }

  function markCurrent() {
    const cur = A.state.current;
    for (const li of A.$$('.wl-item.cur', list)) li.classList.remove('cur');
    const li = cur && list.querySelector(`.wl-item[data-id="${CSS.escape(cur)}"]`);
    if (li) {
      li.classList.add('cur');
      if (li.classList.contains('off') && collapsed.has(li.dataset.rung) && !q.value.trim()) toggleRung(li.dataset.rung);
      li.scrollIntoView({ block: 'nearest' });
    }
  }

  async function showCard(id, { keepScroll = false } = {}) {
    const n = A.state.byId[id];
    if (!n) return;
    const token = ++cardToken;
    const i = A.state.walk.indexOf(id);
    const rung = A.state.summary.rungs.find((r) => r.id === n.rung);
    const k = rung ? rung.nodes.indexOf(id) + 1 : 0;
    A.$('#walk-where').innerHTML = `<b>${i + 1}</b> of ${A.state.walk.length} in the walk · rung <b>${A.esc(n.rung)}</b>, ${k} of ${rung ? rung.nodes.length : '?'}`;
    A.$('#prev-btn').disabled = i <= 0;
    A.$('#next-btn').disabled = i >= A.state.walk.length - 1;
    setSeg(n.understood);
    const scroll = host.scrollTop;
    if (!keepScroll) host.innerHTML = '<div class="loading">Drawing the card…</div>';
    try {
      const card = await A.call('chart.card', { id });
      if (token !== cardToken) return;
      host.innerHTML =
        `<div class="rung-banner"><span class="rid">${A.esc(n.rung)}</span>${A.esc(rung ? rung.title : '')}<span class="rmeta">${rung ? rung.nodes.length : ''} laws</span></div>` +
        card.html;
      if (keepScroll) host.scrollTop = scroll; else host.scrollTop = 0;
    } catch (err) {
      if (token === cardToken) host.innerHTML = `<div class="loading">This card could not be drawn: ${A.esc(err.message)}</div>`;
    }
    const usable = A.views.instrument && A.views.instrument.usable(id);
    A.$('#try-btn').disabled = !usable;
    A.$('#try-btn').title = usable ? 'Apply this law to a form of your own' : 'This law is not a rewrite the instrument can apply';
  }

  function setSeg(v) {
    A.$$('button', seg).forEach((b) => b.setAttribute('aria-checked', String(b.dataset.v === v)));
  }

  async function setUnderstood(v) {
    const id = A.state.current;
    if (!id || A.state.byId[id].understood === v) return;
    seg.classList.add('saving');
    try {
      const r = await A.call('chart.setUnderstood', { id, value: v });
      Object.assign(A.state.byId[id], r.node);
      A.state.summary.understood = r.understood;
      const li = list.querySelector(`.wl-item[data-id="${CSS.escape(id)}"] .mk`);
      if (li) { li.className = `mk ${v}`; li.innerHTML = A.mark(v); }
      setSeg(v);
      renderList();
      A.emit('understood', { id, value: v });
      A.toast(`${id}: marked “${A.UND_WORD[v]}” — saved to nodes/${id}.md`);
    } catch (_) {
      setSeg(A.state.byId[id].understood);
    } finally {
      seg.classList.remove('saving');
    }
  }

  function step(d) {
    const i = A.state.walk.indexOf(A.state.current);
    const j = Math.max(0, Math.min(A.state.walk.length - 1, i + d));
    if (j !== i) A.go(A.state.walk[j]);
  }

  // ------------------------------------------------------------------ wiring
  q.addEventListener('input', A.debounce(applyFilter, 120));
  q.addEventListener('keydown', (ev) => {
    if (ev.key === 'Enter') {
      applyFilter();   // the typing may not have been filtered yet
      const first = A.$$('.wl-item:not(.off)', list)[0];
      if (first) A.go(first.dataset.id);
    } else if (ev.key === 'Escape') { q.value = ''; applyFilter(); q.blur(); }
  });
  A.$$('.filters .chip').forEach((b) => b.addEventListener('click', () => {
    filterUnd = b.dataset.und;
    A.$$('.filters .chip').forEach((x) => x.classList.toggle('on', x === b));
    applyFilter();
  }));
  A.$$('button', seg).forEach((b) => b.addEventListener('click', () => setUnderstood(b.dataset.v)));
  A.$('#prev-btn').addEventListener('click', () => step(-1));
  A.$('#next-btn').addEventListener('click', () => step(1));
  A.$('#file-btn').addEventListener('click', async () => {
    const r = await window.atlas.openNodeFile(A.state.current);
    if (r && !r.ok) A.toast(r.error || 'Could not open the file', true);
  });
  A.$('#try-btn').addEventListener('click', () => {
    if (A.views.instrument) A.views.instrument.tryLaw(A.state.current);
  });
  A.followLinks(host);

  document.addEventListener('keydown', (ev) => {
    if (A.state.view !== 'walk' || A.typing(ev) || ev.ctrlKey || ev.metaKey || ev.altKey) return;
    if (ev.key === 'ArrowRight' || ev.key === 'j') { step(1); ev.preventDefault(); }
    else if (ev.key === 'ArrowLeft' || ev.key === 'k') { step(-1); ev.preventDefault(); }
    else if (ev.key === 'n') setUnderstood('no');
    else if (ev.key === 'p') setUnderstood('partial');
    else if (ev.key === 'u') setUnderstood('yes');
    else if (ev.key === '/') { q.focus(); q.select(); ev.preventDefault(); }
  });

  A.on('current', (id) => { markCurrent(); showCard(id); });
  A.on('loaded', ({ first }) => {
    renderList();
    // on a reload (a check run, an edit made outside the app) the card on screen is redrawn in place
    if (!first && A.state.current) showCard(A.state.current, { keepScroll: true });
  });

  A.views.walk = {
    shown() { markCurrent(); },
    refreshCard() { if (A.state.current) showCard(A.state.current, { keepScroll: true }); },
  };
})(window.A);
