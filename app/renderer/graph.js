// The graph: the chart's own layered DAG (build.py's render_dag), with zoom, pan, search and the tracker.
'use strict';

(function (A) {
  const host = A.$('#graph-host');
  const q = A.$('#graph-q');
  let svg = null;
  let base = null;          // the SVG's own width and height
  let zoom = 1;
  let loadedAt = null;

  try { zoom = Number(localStorage.getItem('atlas.zoom')) || 1; } catch (_) { /* default */ }

  async function ensure() {
    const s = A.state.summary;
    if (!s || (svg && loadedAt === s.loadedAt)) return;
    host.innerHTML = '<div class="loading">Laying out the graph…</div>';
    try {
      const g = await A.call('chart.graph');
      host.innerHTML = g.html;
      svg = host.querySelector('svg#dag');
      loadedAt = s.loadedAt;
      base = { w: Number(svg.getAttribute('width')), h: Number(svg.getAttribute('height')) };
      wire();
      applyZoom();
      shade();
      markCurrent(false);
      search();
    } catch (err) {
      host.innerHTML = `<div class="loading">The graph could not be drawn: ${A.esc(err.message)}</div>`;
    }
  }

  function wire() {
    const edges = A.$$('.edge', svg);
    const byNode = {};
    for (const e of edges) {
      (byNode[e.dataset.from] = byNode[e.dataset.from] || []).push(e);
      (byNode[e.dataset.to] = byNode[e.dataset.to] || []).push(e);
    }
    for (const g of A.$$('.gn', svg)) {
      const id = g.dataset.id;
      g.addEventListener('mouseenter', () => (byNode[id] || []).forEach((e) => e.classList.add('hl')));
      g.addEventListener('mouseleave', () => (byNode[id] || []).forEach((e) => e.classList.remove('hl')));
      g.addEventListener('click', (ev) => {
        ev.preventDefault();
        if (moved) return;
        A.go(id);
      });
    }
  }

  function applyZoom() {
    if (!svg) return;
    svg.setAttribute('width', String(Math.round(base.w * zoom)));
    svg.setAttribute('height', String(Math.round(base.h * zoom)));
    A.$('#graph-zoom').textContent = Math.round(zoom * 100) + '%';
    try { localStorage.setItem('atlas.zoom', String(zoom)); } catch (_) { /* fine */ }
  }

  function setZoom(z, cx, cy) {
    const old = zoom;
    zoom = Math.max(0.25, Math.min(2.5, z));
    if (!svg || old === zoom) return;
    // keep the point under the cursor where it is
    const r = host.getBoundingClientRect();
    const px = (cx ?? r.width / 2), py = (cy ?? r.height / 2);
    const gx = (host.scrollLeft + px) / old, gy = (host.scrollTop + py) / old;
    applyZoom();
    host.scrollLeft = gx * zoom - px;
    host.scrollTop = gy * zoom - py;
  }

  function shade() {
    if (!svg) return;
    host.classList.toggle('shade', A.$('#graph-und').checked);
    for (const g of A.$$('.gn', svg)) {
      const n = A.state.byId[g.dataset.id];
      g.classList.remove('u-no', 'u-partial', 'u-yes');
      if (n) g.classList.add('u-' + n.understood);
    }
  }

  function markCurrent(scroll) {
    if (!svg) return;
    A.$$('.gn.cur', svg).forEach((g) => g.classList.remove('cur'));
    const g = A.state.current && svg.querySelector(`.gn[data-id="${CSS.escape(A.state.current)}"]`);
    if (!g) return;
    g.classList.add('cur');
    if (scroll) centerOn(g);
  }

  function centerOn(g) {
    const rect = g.querySelector('rect');
    const x = Number(rect.getAttribute('x')) * zoom, y = Number(rect.getAttribute('y')) * zoom;
    host.scrollTo({ left: x - host.clientWidth / 2 + 85 * zoom, top: y - host.clientHeight / 2, behavior: 'smooth' });
  }

  function search() {
    if (!svg) return;
    const words = q.value.trim().toLowerCase().split(/\s+/).filter(Boolean);
    let first = null;
    for (const g of A.$$('.gn', svg)) {
      const n = A.state.byId[g.dataset.id];
      const hit = words.length > 0 && n && words.every((w) => n.search.includes(w));
      g.classList.toggle('hit', !!hit);
      if (hit && !first) first = g;
    }
    host.classList.toggle('searching', words.length > 0);
    return first;
  }

  // drag to pan
  let drag = null, moved = false;
  host.addEventListener('mousedown', (ev) => {
    if (ev.button !== 0) return;
    drag = { x: ev.clientX, y: ev.clientY, l: host.scrollLeft, t: host.scrollTop };
    moved = false;
  });
  window.addEventListener('mousemove', (ev) => {
    if (!drag) return;
    const dx = ev.clientX - drag.x, dy = ev.clientY - drag.y;
    if (Math.abs(dx) + Math.abs(dy) > 4) { moved = true; host.classList.add('dragging'); }
    host.scrollLeft = drag.l - dx;
    host.scrollTop = drag.t - dy;
  });
  window.addEventListener('mouseup', () => {
    drag = null;
    host.classList.remove('dragging');
    setTimeout(() => { moved = false; }, 0);
  });
  host.addEventListener('wheel', (ev) => {
    if (!ev.ctrlKey) return;
    ev.preventDefault();
    const r = host.getBoundingClientRect();
    setZoom(zoom * (ev.deltaY < 0 ? 1.12 : 1 / 1.12), ev.clientX - r.left, ev.clientY - r.top);
  }, { passive: false });

  A.$('#graph-in').addEventListener('click', () => setZoom(zoom * 1.2));
  A.$('#graph-out').addEventListener('click', () => setZoom(zoom / 1.2));
  A.$('#graph-center').addEventListener('click', () => markCurrent(true));
  A.$('#graph-und').addEventListener('change', shade);
  q.addEventListener('input', A.debounce(search, 120));
  q.addEventListener('keydown', (ev) => {
    if (ev.key === 'Enter') { const g = search(); if (g) centerOn(g); }
    else if (ev.key === 'Escape') { q.value = ''; search(); }
  });

  A.on('understood', shade);
  A.on('current', () => markCurrent(false));
  A.on('loaded', () => { if (A.state.view === 'graph') ensure(); });

  A.views.graph = {
    async shown() {
      await ensure();
      markCurrent(true);
    },
  };
})(window.A);
