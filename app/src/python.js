// Finding a Python 3 the chart's tools can run on, and the environment they run in.
//
// The chart's engine is Python 3, standard library only. On Windows the usual entry points
// are the `py` launcher (`py -3`) and `python`; `python` may also be the Microsoft Store
// stub, which prints a message instead of running — so every candidate is tried for real.

const { execFile } = require('child_process');
const fs = require('fs');

const MIN_VERSION = [3, 9];

// Node files and ledgers are UTF-8 and full of ≐ ω □ 𝕁; on Windows Python's default for
// open() and for a piped stdout is the ANSI code page, so the UTF-8 mode is forced.
function pythonEnv(extra = {}) {
  return {
    ...process.env,
    PYTHONUTF8: '1',
    PYTHONIOENCODING: 'utf-8',
    PYTHONUNBUFFERED: '1',
    ...extra,
  };
}

// What the user typed into "Use this Python": "py -3" → { command: "py", args: ["-3"] }. A path is kept whole even
// with spaces in it, with or without surrounding quotes (PowerShell's '…' or cmd's "…") and with or without .exe
// (Explorer hides it); a folder stands for the python.exe inside it.
function parseCommand(text) {
  let t = String(text || '').trim();
  if (!t) return null;
  const whole = t.match(/^(["'])(.*)\1$/);
  if (whole) t = whole[2].trim();
  const asPath = existingPython(t);
  if (asPath) return { command: asPath, args: [] };
  const quoted = t.match(/^(["'])(.+?)\1\s*(.*)$/);
  if (quoted) return { command: existingPython(quoted[2]) || quoted[2], args: quoted[3] ? quoted[3].split(/\s+/) : [] };
  if (/[\\/]/.test(t) && /\.exe$/i.test(t)) return { command: t, args: [] };
  const parts = t.split(/\s+/);
  return { command: parts[0], args: parts.slice(1) };
}

function existingPython(p) {
  try {
    if (!/[\\/]/.test(p)) return null;
    for (const cand of [p, p + '.exe']) {
      if (!fs.existsSync(cand)) continue;
      if (fs.statSync(cand).isDirectory()) {
        for (const name of ['python.exe', 'python3', 'python']) {
          const inner = require('path').join(cand, name);
          if (fs.existsSync(inner) && fs.statSync(inner).isFile()) return inner;
        }
        continue;
      }
      return cand;
    }
  } catch (_) { /* not a path */ }
  return null;
}

function candidates(preferred) {
  const list = [];
  const p = parseCommand(preferred);
  if (p) list.push(p);
  if (process.platform === 'win32') {
    list.push({ command: 'py', args: ['-3'] }, { command: 'python', args: [] }, { command: 'python3', args: [] });
  } else {
    list.push({ command: 'python3', args: [] }, { command: 'python', args: [] });
  }
  return list;
}

function probe(cand, timeoutMs = 15000) {
  return new Promise((resolve) => {
    const code = 'import sys, json; print(json.dumps({"v": list(sys.version_info[:3]), "exe": sys.executable}))';
    execFile(cand.command, [...cand.args, '-c', code], { timeout: timeoutMs, windowsHide: true, env: pythonEnv() }, (err, stdout) => {
      if (err) return resolve({ ok: false, reason: err.code === 'ENOENT' ? 'not found' : String(err.message || err).split('\n')[0] });
      try {
        const info = JSON.parse(String(stdout).trim().split(/\r?\n/).pop());
        const [maj, min] = info.v;
        if (maj < MIN_VERSION[0] || (maj === MIN_VERSION[0] && min < MIN_VERSION[1])) {
          return resolve({ ok: false, reason: `Python ${info.v.join('.')} is too old; ${MIN_VERSION.join('.')} or newer is needed` });
        }
        resolve({ ok: true, version: info.v.join('.'), executable: info.exe });
      } catch (e) {
        resolve({ ok: false, reason: 'did not run as Python 3' });
      }
    });
  });
}

// Returns { command, args, version, executable, label, preferredFailed? } or throws with every attempt listed.
// preferredFailed says why the interpreter the user named did not run, when another one was found instead.
async function findPython(preferred) {
  const tried = [];
  const wanted = parseCommand(preferred);
  for (const cand of candidates(preferred)) {
    const r = await probe(cand);
    const label = [cand.command, ...cand.args].join(' ');
    if (r.ok) {
      // Spawn the interpreter itself, not a launcher in front of it: `py -3` stays the label, python.exe runs.
      const direct = r.executable && fs.existsSync(r.executable) && !/\\WindowsApps\\/i.test(r.executable);
      const found = direct
        ? { command: r.executable, args: [], version: r.version, executable: r.executable, label }
        : { command: cand.command, args: cand.args, version: r.version, executable: r.executable, label };
      if (wanted && tried.length) found.preferredFailed = tried[0];
      return found;
    }
    tried.push(`${label}: ${r.reason}`);
  }
  const err = new Error('No usable Python 3 was found.\n' + tried.join('\n'));
  err.tried = tried;
  throw err;
}

module.exports = { findPython, pythonEnv, parseCommand, MIN_VERSION };
