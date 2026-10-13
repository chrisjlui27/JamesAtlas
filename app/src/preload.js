// The window's only door to the machine: a small, named API. The page itself runs sandboxed,
// with no Node access.

const { contextBridge, ipcRenderer } = require('electron');

function on(channel, cb) {
  const fn = (_e, payload) => cb(payload);
  ipcRenderer.on(channel, fn);
  return () => ipcRenderer.removeListener(channel, fn);
}

contextBridge.exposeInMainWorld('atlas', {
  info: () => ipcRenderer.invoke('atlas:info'),
  chooseChart: () => ipcRenderer.invoke('atlas:choose-chart'),
  setPython: (command) => ipcRenderer.invoke('atlas:set-python', command),
  setSetting: (key, value) => ipcRenderer.invoke('atlas:set-setting', key, value),

  // the Python bridge: the chart's own tools, imported
  call: (method, params) => ipcRenderer.invoke('atlas:bridge', method, params || {}),

  // the engine: check / build / census, streamed
  run: (tool, args) => ipcRenderer.invoke('atlas:run', tool, args || []),
  stop: (runId) => ipcRenderer.invoke('atlas:stop', runId),
  onEngine: (cb) => on('atlas:engine', cb),

  openSite: () => ipcRenderer.invoke('atlas:open-site'),
  openNodeFile: (id) => ipcRenderer.invoke('atlas:open-node-file', id),
  openExternal: (url) => ipcRenderer.invoke('atlas:open-external', url),
  copyText: (text) => ipcRenderer.invoke('atlas:copy', text),

  onChartChanged: (cb) => on('atlas:chart-changed', cb),
  onMenu: (cb) => on('atlas:menu', cb),
  onBridgeCrash: (cb) => on('atlas:bridge-crash', cb),
});
