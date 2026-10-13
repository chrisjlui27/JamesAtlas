// The live instrument (SPEC §13, v2): pick a law, write a form, apply the law and walk the result.
// Every rewrite offered is one the chart's derivation checker would license (tools/prover.py).
'use strict';

(function (A) {
  const list = A.$('#law-list');
  const q = A.$('#law-q');
  const input = A.$('#form-in');
  const readingSel = A.$('#reading-sel');
  let rules = null;         // instrument.rules, by walk order
  let byId = {};
  let law = null;           // instrument.law for the chosen law
  let seed = 0;
  let current = null;       // instrument.inspect of the form in the editor
  let trail = [];           // [{ sugar, canonical, svg, rule, dir, instance, value }]
  let inspectToken = 0;

  async function ensureRules() {
    if (rules) return rules;
    const r = await A.call('instrument.rules');
    rules = r.rules;
    byId = Object.fromEntries(rules.map((x) => [x.id, x]));
    renderList();
    return rules;
  }

  function renderList() {
    if (!rules) return;
    const words = q.value.trim().toLowerCase().split(/\s+/).filter(Boolean);
    const all = A.$('#law-all').checked;
    list.textContent = '';
    let rung = null, shown = 0;
    for (const r of rules) {
      if (!r.usable && !all) continue;
      const n = A.state.byId[r.id];
      const hay = ((n ? n.search : r.id) + ' ' + r.law).toLowerCase();
      if (words.length && !words.every((w) => hay.includes(w))) continue;
      if (r.rung !== rung) {
        rung = r.rung;
        const rr = A.state.summary.rungs.find((x) => x.id === rung);
        list.append(A.el('li', { class: 'rung-h' }, A.el('span', { class: 'rid', text: rung }), A.el('span', { text: rr ? rr.title : '' })));
      }
      const li = A.el('li', { class: 'wl-item' + (r.usable ? '' : ' unusable') + (law && law.id === r.id ? ' cur' : ''), dataset: { id: r.id }, title: r.law },
        A.el('span', { class: 'mk', text: r.usable ? '→' : '·' }),
        A.el('span', { class: 'wid' }, A.el('i', { class: `tdot td-${r.type}` }), r.id),
        A.el('span', { class: 'wt', text: n ? n.title : r.title }),
        r.usable ? null : A.el('span', { class: 'why', text: r.why }));
      li.addEventListener('click', () => choose(r.id));
      list.append(li);
      shown++;
    }
    if (!shown) list.append(A.el('li', { class: 'wl-empty', text: 'No law matches.' }));
  }

  async function choose(id, { prefill = false } = {}) {
    await ensureRules();
    const r = byId[id];
    if (!r) return;
    A.$$('.wl-item.cur', list).forEach((li) => li.classList.remove('cur'));
    const li = list.querySelector(`.wl-item[data-id="${CSS.escape(id)}"]`);
    if (li) { li.classList.add('cur'); li.scrollIntoView({ block: 'nearest' }); }
    const box = A.$('#inst-law');
    if (!r.usable) {
      law = null;
      box.innerHTML = `<div class="lawhead"><span class="id">${A.esc(id)}</span><h3>${A.esc(r.title)}</h3></div><p class="note">This law is not a rewrite the instrument can apply: ${A.esc(r.why)}.</p>`;
      updateButtons();
      return;
    }
    try {
      law = await A.call('instrument.law', { id });
    } catch (_) { return; }
    readingSel.value = law.reading;
    const notes = [];
    if (law.conditional) notes.push(`<p class="note warn">A conditional law: ${A.esc(law.units)}. The forms cannot state the premise, so each result says whether it holds there (read in ℍ).</p>`);
    if (law.oneWay) notes.push('<p class="note">One of this law’s sides is a bare variable or the void, which would match anything, so it is applied left to right only.</p>');
    if (law.instances.length) notes.push(`<p class="note">A law with ${law.rules} instances (${A.esc(law.instances.slice(0, 6).join('; '))}${law.instances.length > 6 ? '; …' : ''}); each result names the one it used.${law.instance ? ` The sides below are the instance its card draws, ${A.esc(law.instance)}.` : ''}</p>`);
    notes.push(`<p class="note">Values are read in ${A.esc(readingLabel(law.reading))} — the law’s own setting${law.domain ? `, with variables sampled from its domain (${A.esc(law.domain)})` : ''}.</p>`);
    box.innerHTML = `<div class="lawhead"><span class="id">${A.esc(law.id)}</span><h3>${A.esc(law.title)}</h3><span class="spacer"></span><a href="#${A.esc(law.id)}" class="nl">open its card</a></div>` + law.html + notes.join('');
    clearResults();
    if (prefill || !input.value.trim()) {
      if (law.lhs) setForm(law.lhs);
    }
    updateButtons();
  }

  // Results belong to the form they were computed from: any change to the form takes them away, so a step can
  // only ever be taken from the form shown.
  function clearResults() {
    A.$('#results').innerHTML = '';
    A.$('#apply-note').textContent = '';
  }

  function readingLabel(r) {
    return { C: 'ℂ', J1: '𝕁₁ (ω = 2πi)', H: 'ℍ' }[r] || (r && r.startsWith('p') ? `the place ${r.slice(1)}` : r);
  }

  function updateButtons() {
    A.$('#apply-btn').disabled = !(law && current && current.ok);
    A.$('#use-lhs').disabled = !(law && law.lhs);
    A.$('#use-rhs').disabled = !(law && law.rhs);
    A.$('#undo-btn').disabled = trail.length === 0;
    A.$('#copy-btn').disabled = trail.length < 2;
    A.$('#clear-btn').disabled = trail.length === 0;
  }

  function setForm(text) {
    input.value = text;
    inspect();
  }

  const inspectSoon = A.debounce(() => inspect(), 180);

  async function inspect() {
    const token = ++inspectToken;
    const text = input.value;
    const err = A.$('#form-err');
    const view = A.$('#form-view');
    if (!text.trim()) {
      current = null;
      err.textContent = '';
      input.classList.remove('bad');
      view.innerHTML = '<span class="muted">The void — write a form above, or start from a side of the law.</span>';
      updateButtons();
      return;
    }
    try {
      const r = await A.call('instrument.inspect', { form: text, seed, reading: readingSel.value, domain: law ? law.domain : 'positive' }, { quiet: true });
      if (token !== inspectToken) return;
      current = r;
      err.textContent = '';
      input.classList.remove('bad');
      view.innerHTML = `<div class="drawing">${r.svg}</div><div class="facts">` +
        `<span class="k">canonical</span><code>${A.esc(r.canonical || 'void')}</code>` +
        `<span class="k">with sugar</span><code>${A.esc(r.sugar)}</code>` +
        `<span class="k">size</span><span>${r.size} boundar${r.size === 1 ? 'y' : 'ies'}, ${r.depth} deep</span>` +
        `<span class="k">value in ${A.esc(readingLabel(r.reading))}</span><span><b>${A.esc(r.value)}</b>${r.valueNote ? ` <span class="muted">${A.esc(r.valueNote)}</span>` : ''}</span></div>`;
    } catch (e) {
      if (token !== inspectToken) return;
      current = null;
      err.textContent = e.message;
      input.classList.add('bad');
      view.innerHTML = '<span class="muted">—</span>';
    }
    updateButtons();
  }

  async function apply() {
    if (!law) return;
    await inspect();   // the drawing above must be of the form being rewritten, even straight after typing
    if (!current || !current.ok) return;
    const from = current;
    const ruleId = law.id;
    const btn = A.$('#apply-btn');
    btn.disabled = true;
    A.$('#apply-note').textContent = 'Applying…';
    const out = A.$('#results');
    try {
      const r = await A.call('instrument.apply', { rule: law.id, form: input.value, seed, reading: readingSel.value, domain: law.domain }, { quiet: true });
      const parts = [];
      if (!r.results.length) parts.push(`${law.id} does not apply anywhere in this form.`);
      else parts.push(`${r.distinct} distinct result${r.distinct === 1 ? '' : 's'}${r.shown < r.distinct ? `, the ${r.shown} smallest shown` : ''}. Click one to take the step.`);
      if (r.truncated) parts.push('Some matches were not enumerated — the form is wide; results may be incomplete.');
      parts.push(`Values in ${readingLabel(r.reading)}${r.valueNote ? ' ' + r.valueNote : ''}: this form is ${r.value}.`);
      A.$('#apply-note').textContent = parts.join(' ');
      out.textContent = '';
      for (const x of r.results) out.append(resultCard(x, r, from, ruleId));
    } catch (e) {
      A.$('#apply-note').textContent = '';
      out.innerHTML = `<p class="form-err">${A.esc(e.message)}</p>`;
    } finally {
      btn.disabled = false;
      updateButtons();
    }
  }

  function resultCard(x, r, from, ruleId) {
    const dir = x.direction === '→' ? '→ left to right' : '← right to left';
    const kept = x.kept === true ? `<span class="tag ok" title="the value in this reading is unchanged (${A.esc(r.symbol)})">value kept</span>`
      : x.kept === false ? `<span class="tag bad" title="the value in this reading changed — the step needs a guard, a receipt, or another reading">value changed</span>`
        : '<span class="tag mute">no value to compare</span>';
    const premise = x.premise === true ? '<span class="tag ok">premise holds</span>' : x.premise === false ? '<span class="tag bad" title="the law’s premise fails on these entries: the step is not licensed here">premise fails</span>' : '';
    const env = Object.entries(x.env).map(([k, v]) => `${k} = ${v}`).join(', ');
    const card = A.el('button', { class: 'res', type: 'button', title: 'Take this step' });
    card.innerHTML =
      `<div class="rtop"><span class="dir">${dir}</span><span>· ${A.esc(x.where)}</span>${x.instance ? `<span>· ${A.esc(x.instance)}</span>` : ''}</div>` +
      `<div class="drawing">${x.svg}</div><code>${A.esc(x.sugar)}</code>` +
      `<div class="step"><code>${A.esc(x.redex)}</code> becomes <code>${A.esc(x.into)}</code>${env ? ` <span>(${A.esc(env)})</span>` : ''}</div>` +
      `<div class="val">${kept}${premise}<span>${A.esc(x.value)}${x.readingLabel ? ` <span class="muted">in ${A.esc(x.readingLabel)}</span>` : ''}</span></div>`;
    card.addEventListener('click', () => take(x, from, ruleId));
    return card;
  }

  // A step is recorded only from the trail's last form: if the form was changed since (by hand, from a side of the
  // law, from another card), the derivation starts again from the form the step was taken from.
  function take(x, from, ruleId) {
    const last = trail[trail.length - 1];
    if (last && last.canonical !== from.canonical) {
      trail = [];
      A.toast('The form was changed since the last step, so a new derivation starts here.');
    }
    if (!trail.length) {
      trail.push({ sugar: from.sugar, canonical: from.canonical, svg: from.svg, rule: null, dir: '', instance: '', value: from.value });
    }
    trail.push({ sugar: x.sugar, canonical: x.canonical, svg: x.svg, rule: ruleId, dir: x.direction, instance: x.instance, value: x.value });
    renderTrail();
    setForm(x.sugar);
    A.$('#apply-note').textContent = `Took the step by ${ruleId}. Apply it again, or pick another law.`;
  }

  function renderTrail() {
    const body = A.$('#trail-body');
    body.textContent = '';
    if (!trail.length) {
      body.append(A.el('tr', { class: 'empty' }, A.el('td', { colspan: '3', text: 'Each step you take is written here, as a Given–Rule table like the chart’s own derivations.' })));
    }
    for (const t of trail) {
      const rule = t.rule ? `<a href="#${A.esc(t.rule)}" class="nl">${A.esc(t.rule)}</a> ${A.esc(t.dir)}${t.instance ? ` <span class="muted">${A.esc(t.instance)}</span>` : ''}` : 'given';
      body.append(A.el('tr', {},
        A.el('td', { class: 'f', html: `<span class="drawing">${t.svg.replace('form big', 'form sm')}</span><code>${A.esc(t.sugar)}</code>` }),
        A.el('td', { html: rule }),
        A.el('td', { text: t.value })));
    }
    updateButtons();
  }

  function asTable() {
    const rows = ['| form | rule | note |', '|---|---|---|'];
    for (const t of trail) {
      const note = t.rule ? [t.dir === '←' ? 'right to left' : '', t.instance].filter(Boolean).join('; ') || '—' : '—';
      rows.push(`| \`${t.sugar}\` | ${t.rule ? `[[${t.rule}]]` : 'given'} | ${note} |`);
    }
    return rows.join('\n') + '\n';
  }

  // ------------------------------------------------------------------ wiring
  input.addEventListener('input', () => { clearResults(); inspectSoon(); });
  input.addEventListener('keydown', (ev) => { if (ev.key === 'Enter') { ev.preventDefault(); apply(); } });
  readingSel.addEventListener('change', () => { clearResults(); inspect(); });
  A.$('#resample').addEventListener('click', () => { seed++; inspect(); if (A.$('#results').childElementCount) apply(); });
  A.$('#apply-btn').addEventListener('click', apply);
  A.$('#use-lhs').addEventListener('click', () => { if (law && law.lhs) { clearResults(); setForm(law.lhs); } });
  A.$('#use-rhs').addEventListener('click', () => { if (law && law.rhs) { clearResults(); setForm(law.rhs); } });
  A.$$('#palette > button[data-ins]').forEach((b) => b.addEventListener('click', () => {
    const ins = b.dataset.ins;
    const s = input.selectionStart ?? input.value.length, e = input.selectionEnd ?? s;
    const v = input.value;
    if (ins.length === 2 && '([<'.includes(ins[0])) {
      // a boundary wraps the selection, or opens empty at the cursor
      input.value = v.slice(0, s) + ins[0] + v.slice(s, e) + ins[1] + v.slice(e);
      input.setSelectionRange(s + 1, e + 1);
    } else {
      input.value = v.slice(0, s) + ins + v.slice(e);
      input.setSelectionRange(s + ins.length, s + ins.length);
    }
    input.focus();
    clearResults();
    inspectSoon();
  }));
  A.$('#undo-btn').addEventListener('click', () => {
    if (!trail.length) return;
    const first = trail[0];
    trail.pop();
    let last = trail[trail.length - 1];
    if (trail.length === 1) { trail = []; last = first; }   // undoing the first step leaves nothing to record
    renderTrail();
    clearResults();
    if (last) setForm(last.sugar);
  });
  A.$('#clear-btn').addEventListener('click', () => { trail = []; renderTrail(); });
  A.$('#copy-btn').addEventListener('click', async () => {
    await window.atlas.copyText(asTable());
    A.toast('Copied as a Given–Rule table — paste it into a node’s Derivation.');
  });
  q.addEventListener('input', A.debounce(renderList, 120));
  q.addEventListener('keydown', (ev) => {
    if (ev.key === 'Enter') {
      renderList();
      const first = A.$('.wl-item:not(.unusable)', list);
      if (first) { choose(first.dataset.id); input.focus(); }
    } else if (ev.key === 'Escape') { q.value = ''; renderList(); }
  });
  A.$('#law-all').addEventListener('change', renderList);
  A.followLinks(A.$('#inst-law'));
  A.followLinks(A.$('#trail-body'));

  A.on('loaded', ({ first }) => {
    if (first) return;
    rules = null;               // the laws may have changed on disk
    if (A.state.view === 'instrument') ensureRules();
  });

  A.views.instrument = {
    async shown() {
      await ensureRules();
      if (!input.value && !current) inspect();
      renderTrail();
    },
    usable(id) { return !rules || !byId[id] ? true : byId[id].usable; },
    async tryLaw(id) {
      A.showView('instrument');
      await choose(id, { prefill: true });
      input.focus();
    },
    rulesReady: ensureRules,
  };
})(window.A);
