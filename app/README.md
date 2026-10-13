# James Atlas

A desktop app for the Boundary Chart. It does three things:

1. **Walk the chart.** Every law, one card at a time, in walk order — the same cards `tools/build.py` draws for the site — with search, the graph of what uses what, and the collected lists (gaps, owed, refuted, concepts, open forms). For each law you mark how well you know it: *not yet*, *partly*, or *understood*. The mark is saved straight into that law's file (`understood:` in `nodes/<id>.md`).
2. **Run the engine.** `tools/check.py`, `tools/build.py` and `tools/census.py`, run on the chart with their output shown as it comes. A check shows which law it has reached, lists any failures with links to the laws, and keeps a history of the session's runs.
3. **Try a law on a form of your own** (the "live instrument" of SPEC §13). Pick a law, write a form, and see it drawn and valued. Apply the law to see every place it can rewrite the form, in either direction. Each step you take is written into a Given–Rule table you can copy into a node's Derivation. Every step offered is one the chart's derivation checker (`tools/prover.py`) would license. Each result also says whether the form's value stayed the same in the reading you chose (ℂ, 𝕁₁, ℍ, or a place p).

The chart is the folder above this one. The app reads it in place and writes back only your *understood* marks. Running check, build or census writes whatever those tools always write (`census/*.md`, `site/index.html`).

## On Windows

You need three things, once:

- **Python 3** (3.9 or newer; 3.12 or 3.13 recommended) from [python.org](https://www.python.org/downloads/windows/). In the installer, tick **"Add python.exe to PATH"**. The chart's engine uses only the standard library, so there is nothing else to install.
- **Node.js** (the LTS version) from [nodejs.org](https://nodejs.org/).
- **Git for Windows**, to clone and pull the repository.

Then, in a terminal (PowerShell or Command Prompt):

```
git clone https://github.com/chrisjlui27/JamesAtlas.git
cd JamesAtlas\app
npm install
npm start
```

`npm install` downloads Electron (about 100 MB) the first time. `npm start` opens the app on the chart in the folder above.

### An installer

```
npm run dist:win
```

This writes two files to `app\dist\`:

- `James-Atlas-Setup-0.1.0.exe`, an ordinary installer that adds James Atlas to the Start menu.
- `James-Atlas-0.1.0-portable.exe`, a single file that runs without installing.

The installed app is not inside the repository, so the first time it opens it asks you to **choose the chart folder**: the `JamesAtlas` folder, the one that holds `nodes` and `tools`. It remembers the folder.

The executables are not code-signed. The first time you run one, Windows SmartScreen may say it "protected your PC". Choose **More info → Run anyway**.

## Using it

| | |
|---|---|
| **1–5** | switch between Walk, Graph, Lists, Engine and Instrument |
| **← →** or **k j** | previous and next law in the walk |
| **n · p · u** | mark the law *not yet*, *partly*, or *understood* |
| **/** | search the walk |
| **Enter** in a search box | open the first match |
| **Enter** in the instrument's form box | apply the law |
| **Ctrl + mouse wheel** on the graph | zoom |

- **Walk.** The list on the left is the walk, grouped by rung. Click a rung's heading to fold it. The bar under the search box shows how much of the chart you have marked. *Try it in the instrument* takes the law you are on to the instrument with its left side ready to rewrite. *Open file* opens the node's Markdown file in your editor.
- **Graph.** Columns are depth: how many steps of `uses` lie below a law. Hover a law to light up its edges, click it to open it in the walk, drag to move around. *Shade by understood* colours the laws you have marked.
- **Engine.** *Run check* with no prefix is the full check: every law, every derivation, and the four ledgers. It takes several minutes. With a prefix such as `Z.` or `H.`, it checks just those laws, in seconds. *Stop* ends a run, including any witness scripts it started. A full check that is stopped part-way can leave a ledger half-written; run it again, or restore the ledgers with `git checkout census`.
- **Instrument.** The reading box (ℂ, 𝕁₁, ℍ, p = …) sets where values are read. It starts at the law's own setting. *New sample* reads the variables at other values. In a result, "value kept" means the step left the value unchanged in that reading. "Value changed" marks a step that needs a guard or a receipt there, or that holds only in another reading. A conditional law of rung H also says whether its premise holds. *Copy as table* puts the steps on the clipboard as a `| form | rule | note |` table.

The ⚙ button shows the chart folder and the Python the app found. You can point it at another chart, or at a particular Python: `py -3`, or a full path such as `C:\Users\Lui\AppData\Local\Programs\Python\Python313\python.exe`. Settings are kept in `%APPDATA%\James Atlas\settings.json`.

## When something goes wrong

- **"Python 3 is needed."** Install Python as above, then press *Try again*. If Python is installed somewhere unusual, enter its path under ⚙.
- **"… starts with a byte-order mark."** An editor, usually old Notepad, saved a node file as "UTF-8 with BOM". The chart's tools cannot read such a file. Re-save it as plain UTF-8; in VS Code, use the encoding item in the status bar.
- **Line endings.** The repository's `.gitattributes` keeps every text file LF. With it, a check run on Windows does not show the ledgers as changed in `git status`.

## For whoever works on the app

```
app/
  src/main.js          the main process: window, chart folder, Python, bridge, engine runs, file watching
  src/preload.js       the window's only API (contextBridge); the page itself is sandboxed
  src/python.js        finds Python (py -3, python, python3; a configured command first) and runs it in UTF-8 mode
  src/bridge.js        client for the Python bridge (JSON lines over stdin/stdout)
  src/engine.js        runs check / build / census, streamed; validates flags; stops the whole process tree
  src/settings.js      settings.json in userData
  bridge/atlas_bridge.py    imports the chart's tools: cards, graph, lists, the tracker, the instrument
  bridge/check_progress.py  runs tools/check.py unchanged and announces its progress on stderr
  renderer/            index.html, app.css and one script per view (walk, graph, lists, engine, instrument)
  test/e2e.js          drives the real app on a scratch copy of the chart (15 steps, screenshots in test/out/)
  bridge/test_bridge.py     unit tests for the bridge, also on a scratch copy
```

- `npm test` runs the bridge tests, then the end-to-end test. On Linux without a display, run the end-to-end test as `xvfb-run -a -s "-screen 0 1600x1000x24" npm run test:e2e`.
- The tests never write to the real chart: each one copies `nodes/`, `tools/`, `census/`, `concepts/` and `site/` to a temporary folder first. `ATLAS_CHART_ROOT`, `ATLAS_USER_DATA` and `ATLAS_PYTHON` point the app elsewhere.
- **Cards.** The bridge calls `build.render_node`. The app also takes the stylesheet from `site/index.html`, so a card in the app looks exactly as it does on the site.
- **Rewrites.** They come from `licences.rules_for` and `prover.rewrite_all`, with duplicates and empty matches removed. A pre-check refuses forms on which a law's pattern would try more than 300,000 splits.
- **Values.** They are read with the engine's own readings, set per request and always reset to ℂ afterwards. A law written over the place p is valued at its instance's own place and depth, as the checker reads it.
- **Security.** The window has no Node access. It reaches the machine only through the named calls in `preload.js`, which the main process validates: an allowlist of bridge methods and of engine flags, node ids matched against the chart, and only http(s) links sent to the browser. A strict content-security policy blocks every script except the app's own. All network requests are blocked, because the app needs none.
