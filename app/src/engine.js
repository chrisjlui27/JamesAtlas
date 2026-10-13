// Running the chart's own tools — check, build, census — as separate processes, with their
// output streamed to the window line by line.

const { spawn, execFile } = require('child_process');
const path = require('path');
const readline = require('readline');
const { pythonEnv } = require('./python');

const TOOLS = {
  check: 'tools/check.py',
  build: 'tools/build.py',
  census: 'tools/census.py',
};
const PROGRESS = '@@atlas ';

// The flags the app offers for each tool; anything else is refused before a process starts.
const FLAGS = {
  check: { '--only': 'value', '--seed': 'value', '--trials': 'value', '--no-census': 'bool', '--no-licences': 'bool', '--no-places': 'bool' },
  build: {},
  census: {},
};

function validateArgs(tool, args) {
  const allowed = Object.hasOwn(FLAGS, tool) ? FLAGS[tool] : null;
  if (!allowed) throw new Error(`Unknown tool: ${tool}`);
  const out = [];
  for (let i = 0; i < args.length; i++) {
    const a = String(args[i]);
    const kind = Object.hasOwn(allowed, a) ? allowed[a] : null;
    if (!kind) throw new Error(`${tool} does not take ${a}`);
    out.push(a);
    if (kind === 'value') {
      const v = String(args[++i] ?? '').trim();
      if (!v || v.startsWith('-') || /[\r\n\0]/.test(v)) throw new Error(`${a} needs a value`);
      out.push(v);
    }
  }
  return out;
}

class EngineRunner {
  // checkWrapper: bridge/check_progress.py, which runs tools/check.py unchanged and announces its progress
  constructor({ getPython, getChartRoot, send, checkWrapper }) {
    this.checkWrapper = checkWrapper;
    this.getPython = getPython;
    this.getChartRoot = getChartRoot;
    this.send = send;           // (event) => void, to the window
    this.runs = new Map();
    this.nextId = 1;
  }

  async run(tool, args = []) {
    const script = Object.hasOwn(TOOLS, tool) ? TOOLS[tool] : null;
    if (!script) throw new Error(`Unknown tool: ${tool}`);
    const clean = validateArgs(tool, args);
    const python = await this.getPython();
    const root = this.getChartRoot();
    const runId = this.nextId++;
    const viaWrapper = tool === 'check' && this.checkWrapper;
    const argv = viaWrapper
      ? [...python.args, '-X', 'utf8', '-u', this.checkWrapper, root, ...clean]
      : [...python.args, '-X', 'utf8', '-u', path.join(root, script), ...clean];
    const started = Date.now();
    // On macOS/Linux the run gets its own process group, so Stop reaches the witnesses too.
    const proc = spawn(python.command, argv, { cwd: root, env: pythonEnv(), windowsHide: true, detached: process.platform !== 'win32' });
    this.runs.set(runId, { proc, tool });
    this.send({ runId, type: 'start', tool, args: clean, command: [python.label, script, ...clean].join(' ') });
    for (const [name, stream] of [['out', proc.stdout], ['err', proc.stderr]]) {
      stream.setEncoding('utf8');
      readline.createInterface({ input: stream }).on('line', (text) => {
        if (name === 'err' && text.startsWith(PROGRESS)) {
          try { this.send({ runId, type: 'progress', ...JSON.parse(text.slice(PROGRESS.length)) }); } catch (_) { /* not ours */ }
          return;
        }
        this.send({ runId, type: 'line', stream: name, text });
      });
    }
    proc.on('error', (err) => {
      this.send({ runId, type: 'line', stream: 'err', text: String(err.message || err) });
    });
    proc.on('close', (code, signal) => {
      const r = this.runs.get(runId);
      this.runs.delete(runId);
      this.send({ runId, type: 'exit', tool, code, signal, stopped: !!(r && r.stopped), seconds: (Date.now() - started) / 1000 });
    });
    return { runId };
  }

  stop(runId) {
    const r = this.runs.get(runId);
    if (!r) return false;
    r.stopped = true;
    killTree(r.proc);
    return true;
  }

  stopAll() {
    for (const id of [...this.runs.keys()]) this.stop(id);
  }

  busy() {
    return this.runs.size > 0;
  }
}

// The checker starts witness scripts of its own; on Windows a plain kill would leave them running.
function killTree(proc) {
  if (!proc || proc.exitCode !== null) return;
  if (process.platform === 'win32') {
    execFile('taskkill', ['/pid', String(proc.pid), '/T', '/F'], { windowsHide: true }, () => {});
  } else {
    try { process.kill(-proc.pid, 'SIGTERM'); } catch (_) {
      try { proc.kill('SIGTERM'); } catch (__) { /* gone */ }
    }
  }
}

module.exports = { EngineRunner, validateArgs, TOOLS, FLAGS };
