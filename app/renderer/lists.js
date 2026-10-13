// The chart's collected lists: gaps with their plans, owed items, refuted readings, concepts, open forms.
'use strict';

(function (A) {
  const host = A.$('#lists-host');
  const tabs = A.$('#lists-tabs');
  let data = null;
  let loadedAt = null;
  let tab = 'gaps';

  const INTRO = {
    gaps: 'What the chart cannot write yet — each gap carries a plan.',
    owed: 'Dated obligations the chart has not met, collected from every node’s <code>owed:</code> list.',
    refuted: 'Readings and derivations once believed and since refuted — kept, struck through, with the witness.',
    concepts: 'The second index: every concept, and the laws that name it.',
    openForms: 'Small forms the census found that no node reads yet.',
  };

  let pending = null;
  function ensure() {
    if (!pending) pending = load().finally(() => { pending = null; });
    return pending;
  }

  async function load() {
    const s = A.state.summary;
    if (!s) return;
    if (!data || loadedAt !== s.loadedAt) {
      host.innerHTML = '<div class="loading">Collecting…</div>';
      try {
        data = await A.call('chart.lists');
        loadedAt = s.loadedAt;
      } catch (err) {
        host.innerHTML = `<div class="loading">${A.esc(err.message)}</div>`;
        return;
      }
      const counts = { gaps: data.gapCount, owed: data.owedCount, refuted: data.refutedCount };
      for (const b of A.$$('button', tabs)) {
        const n = counts[b.dataset.list];
        const label = b.dataset.label || (b.dataset.label = b.textContent);
        b.innerHTML = A.esc(label) + (n !== undefined ? `<span class="n">${n}</span>` : '');
      }
    }
  }

  function render(anchor) {
    if (!data) return;
    A.$$('button', tabs).forEach((b) => b.classList.toggle('on', b.dataset.list === tab));
    host.innerHTML = `<p class="lede">${INTRO[tab]}</p>` + (data[tab] || '<p class="muted">Nothing here.</p>');
    host.scrollTop = 0;
    if (anchor) {
      const t = document.getElementById(anchor);
      if (t) t.scrollIntoView({ block: 'start' });
    }
  }

  for (const b of A.$$('button', tabs)) b.addEventListener('click', () => { tab = b.dataset.list; render(); });
  A.followLinks(host);

  A.on('list', async ({ tab: t, anchor }) => {
    if (t) tab = t;
    await ensure();
    render(anchor);
  });
  A.on('loaded', () => { if (A.state.view === 'lists') ensure().then(() => render()); });

  A.views.lists = { shown: () => ensure().then(() => render()) };
})(window.A);
