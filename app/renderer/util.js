// Shared state and helpers for the window. Every view script adds itself to window.A.
'use strict';

window.A = (function () {
  const A = {
    state: {
      summary: null,     // chart.summary from the bridge
      byId: {},          // node summaries by id
      walk: [],          // ids in walk order
      current: null,     // the law the walk is on
      view: 'walk',
      info: null,        // atlas.info()
      running: null,     // the engine run in progress, if any
    },
    views: {},
  };

  // ------------------------------------------------------------------ DOM
  A.$ = (sel, root = document) => root.querySelector(sel);
  A.$$ = (sel, root = document) => Array.from(root.querySelectorAll(sel));
  A.esc = (s) => String(s ?? '').replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  A.el = (tag, attrs = {}, ...kids) => {
    const e = document.createElement(tag);
    for (const [k, v] of Object.entries(attrs || {})) {
      if (v === null || v === undefined || v === false) continue;
      if (k === 'class') e.className = v;
      else if (k === 'html') e.innerHTML = v;
      else if (k === 'text') e.textContent = v;
      else if (k.startsWith('on') && typeof v === 'function') e.addEventListener(k.slice(2), v);
      else if (k === 'dataset') Object.assign(e.dataset, v);
      else e.setAttribute(k, v === true ? '' : v);
    }
    for (const kid of kids.flat()) if (kid !== null && kid !== undefined && kid !== false) e.append(kid instanceof Node ? kid : document.createTextNode(String(kid)));
    return e;
  };
  A.debounce = (fn, ms) => { let t = null; return (...a) => { clearTimeout(t); t = setTimeout(() => fn(...a), ms); }; };
  A.typing = (ev) => {
    const t = ev.target;
    return t && (t.tagName === 'INPUT' || t.tagName === 'TEXTAREA' || t.tagName === 'SELECT' || t.isContentEditable);
  };

  // ------------------------------------------------------------------ messages
  let toastTimer = null;
  A.toast = (msg, bad = false, ms = 3200) => {
    const t = A.$('#toast');
    t.textContent = msg;
    t.classList.toggle('bad', !!bad);
    t.hidden = false;
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => { t.hidden = true; }, ms);
  };

  // A bridge call; errors become a toast unless the caller handles them (quiet).
  A.call = async (method, params, { quiet = false } = {}) => {
    try {
      return await window.atlas.call(method, params);
    } catch (err) {
      const msg = cleanError(err);
      if (!quiet) A.toast(msg, true, 6000);
      const e = new Error(msg);
      e.original = err;
      throw e;
    }
  };

  function cleanError(err) {
    // ipcRenderer.invoke wraps the main process's error: "Error invoking remote method 'x': Error: message"
    return String(err && err.message || err).replace(/^Error invoking remote method '[^']+': (Error: )?/, '');
  }
  A.cleanError = cleanError;

  // ------------------------------------------------------------------ a tiny event bus
  const handlers = {};
  A.on = (name, fn) => { (handlers[name] = handlers[name] || []).push(fn); };
  A.emit = (name, payload) => { (handlers[name] || []).forEach((fn) => { try { fn(payload); } catch (e) { console.error(e); } }); };

  // ------------------------------------------------------------------ the chart's vocabulary
  A.UND = { no: '○', partial: '◐', yes: '●' };
  // the understood mark as a small drawing: an empty, a half and a full circle
  A.mark = (v) => {
    const half = v === 'partial' ? '<path d="M8 2.2 A5.8 5.8 0 0 0 8 13.8 Z"/>' : '';
    return `<svg class="um ${A.esc(v)}" viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="5.8"/>${half}</svg>`;
  };
  A.UND_WORD = { no: 'not yet', partial: 'partly', yes: 'understood' };

  A.isNode = (id) => Object.prototype.hasOwnProperty.call(A.state.byId, id);

  // Links inside chart HTML are fragment links (#Z.collection, #concept-zero, #rung-Z): follow them in the app.
  A.followLinks = (root) => {
    root.addEventListener('click', (ev) => {
      const a = ev.target.closest('a[href]');
      if (!a || !root.contains(a)) return;
      const href = a.getAttribute('href') || '';
      if (href.startsWith('#')) {
        ev.preventDefault();
        const target = decodeURIComponent(href.slice(1));
        if (A.isNode(target)) { A.go(target); return; }
        if (target.startsWith('concept-')) { A.showView('lists'); A.emit('list', { tab: 'concepts', anchor: target }); return; }
        if (target.startsWith('rung-')) {
          const r = target.slice(5);
          const first = A.state.walk.find((id) => A.state.byId[id].rung === r);
          if (first) A.go(first);
          return;
        }
        if (['gaps', 'owed', 'refuted', 'concepts'].includes(target)) { A.showView('lists'); A.emit('list', { tab: target }); }
        return;
      }
      if (/^https?:\/\//i.test(href)) { ev.preventDefault(); window.atlas.openExternal(href); return; }
      ev.preventDefault();
    });
  };

  // Go to a law in the walk.
  A.go = (id, { view = 'walk' } = {}) => {
    if (!A.isNode(id)) return;
    A.state.current = id;
    window.atlas.setSetting('lastNode', id).catch(() => {});
    if (view) A.showView(view);
    A.emit('current', id);
  };

  A.showView = (view) => {
    if (!A.views[view]) return;
    A.state.view = view;
    A.$$('.tabs button').forEach((b) => b.setAttribute('aria-selected', String(b.dataset.view === view)));
    A.$$('.view').forEach((s) => { s.hidden = s.dataset.view !== view; });
    window.atlas.setSetting('view', view).catch(() => {});
    if (A.views[view].shown) A.views[view].shown();
  };

  return A;
})();
