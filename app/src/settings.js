// Per-user settings, kept as JSON in Electron's userData folder.

const fs = require('fs');
const path = require('path');

const DEFAULTS = {
  chartRoot: null,      // the Boundary Chart folder (holds nodes/ and tools/)
  python: '',           // an explicit interpreter, e.g. "py -3" or "C:\\Python313\\python.exe"; empty = find one
  lastNode: null,       // the card the walk was on
  view: 'walk',
  bounds: null,         // window position and size
};

class Settings {
  constructor(dir) {
    this.file = path.join(dir, 'settings.json');
    this.data = { ...DEFAULTS };
    try {
      const raw = JSON.parse(fs.readFileSync(this.file, 'utf8'));
      if (raw && typeof raw === 'object') Object.assign(this.data, raw);
    } catch (_) { /* first run, or an unreadable file: defaults */ }
  }

  get(key) { return this.data[key]; }

  set(key, value) {
    this.data[key] = value;
    this.save();
  }

  save() {
    try {
      fs.mkdirSync(path.dirname(this.file), { recursive: true });
      const tmp = this.file + '.tmp';
      fs.writeFileSync(tmp, JSON.stringify(this.data, null, 2), 'utf8');
      fs.renameSync(tmp, this.file);
    } catch (_) { /* settings are a convenience; never fail the app over them */ }
  }
}

module.exports = { Settings, DEFAULTS };
