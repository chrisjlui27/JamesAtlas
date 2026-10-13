// The client side of the Python bridge (bridge/atlas_bridge.py): one long-lived process that
// imports the chart's tools and answers JSON requests, one per line, over stdin/stdout.

const { spawn } = require('child_process');
const readline = require('readline');
const { EventEmitter } = require('events');
const { pythonEnv } = require('./python');

class Bridge extends EventEmitter {
  constructor({ python, script, chartRoot, log = () => {} }) {
    super();
    this.python = python;
    this.script = script;
    this.chartRoot = chartRoot;
    this.log = log;
    this.proc = null;
    this.nextId = 1;
    this.pending = new Map();
    this.stderrTail = [];
    this.stopping = false;
  }

  start() {
    if (this.proc) return;
    this.stopping = false;
    const args = [...this.python.args, '-X', 'utf8', '-u', this.script, '--chart', this.chartRoot];
    const proc = spawn(this.python.command, args, {
      cwd: this.chartRoot,
      env: pythonEnv(),
      windowsHide: true,
      stdio: ['pipe', 'pipe', 'pipe'],
    });
    this.proc = proc;
    proc.stdout.setEncoding('utf8');
    proc.stderr.setEncoding('utf8');
    readline.createInterface({ input: proc.stdout }).on('line', (line) => this._onLine(line));
    readline.createInterface({ input: proc.stderr }).on('line', (line) => {
      this.stderrTail.push(line);
      if (this.stderrTail.length > 60) this.stderrTail.shift();
      this.log('[bridge] ' + line);
    });
    proc.on('error', (err) => this._fail(err));
    proc.on('exit', (code, signal) => {
      const was = this.proc === proc;
      if (was) this.proc = null;
      const why = `The Python bridge stopped (${signal || 'exit code ' + code}).` +
        (this.stderrTail.length ? '\n' + this.stderrTail.slice(-12).join('\n') : '');
      for (const [, p] of this.pending) p.reject(new Error(why));
      this.pending.clear();
      if (was && !this.stopping) this.emit('crash', why);
    });
  }

  _onLine(line) {
    let msg;
    try { msg = JSON.parse(line); } catch (_) { this.log('[bridge stdout] ' + line); return; }
    const p = this.pending.get(msg.id);
    if (!p) return;
    this.pending.delete(msg.id);
    clearTimeout(p.timer);
    if (msg.error) {
      const e = new Error(msg.error.message || 'bridge error');
      e.kind = msg.error.kind;
      e.detail = msg.error.detail;
      p.reject(e);
    } else {
      p.resolve(msg.result);
    }
  }

  _fail(err) {
    for (const [, p] of this.pending) p.reject(err);
    this.pending.clear();
    this.emit('crash', String(err && err.message || err));
  }

  call(method, params = {}, timeoutMs = 120000) {
    if (!this.proc) this.start();
    const id = this.nextId++;
    return new Promise((resolve, reject) => {
      const timer = setTimeout(() => {
        if (this.pending.delete(id)) reject(new Error(`The bridge did not answer "${method}" within ${Math.round(timeoutMs / 1000)} s.`));
      }, timeoutMs);
      this.pending.set(id, { resolve, reject, timer });
      try {
        this.proc.stdin.write(JSON.stringify({ id, method, params }) + '\n');
      } catch (err) {
        clearTimeout(timer);
        this.pending.delete(id);
        reject(err);
      }
    });
  }

  stop() {
    this.stopping = true;
    if (!this.proc) return;
    try { this.proc.stdin.end(); } catch (_) { /* already closed */ }
    const proc = this.proc;
    setTimeout(() => { try { proc.kill(); } catch (_) { /* gone */ } }, 1500);
    this.proc = null;
  }
}

module.exports = { Bridge };
