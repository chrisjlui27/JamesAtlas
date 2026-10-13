#!/usr/bin/env node
// Runs Python with the given arguments using the same interpreter search as the app
// (py -3 / python / python3 on Windows; python3 / python elsewhere; ATLAS_PYTHON overrides).
// Usage: node scripts/run-python.js -m unittest discover -s bridge

const { spawn } = require('child_process');
const path = require('path');
const { findPython, pythonEnv } = require('../src/python');

(async () => {
  let py;
  try {
    py = await findPython(process.env.ATLAS_PYTHON || '');
  } catch (err) {
    console.error(err.message);
    process.exit(2);
  }
  const child = spawn(py.command, [...py.args, ...process.argv.slice(2)], {
    cwd: path.join(__dirname, '..'),
    env: pythonEnv(),
    stdio: 'inherit',
    windowsHide: true,
  });
  child.on('exit', (code) => process.exit(code === null ? 1 : code));
})();
