# Architecture

## Layout
```
data/            JSON data files (population_<year>.json, generations.json); raw/ = Census CSVs
core/            all math; no display code
tui/             terminal front end (Rich)
scripts/         helper scripts (data update, sync_site_data)
tests/           automated tests (pytest), one test file per module
tests/js_parity/ checks that site/core.js matches Python (see below)
site/            web dashboard (core.js = JS copy of the math)
docs/            these docs
```

## Modules
- `core/rank.py` — A math. `rank_birth_year(year)` → list of `GenerationRank` (older %, younger %, approximate flag) per generation. Helpers: `load_data`, `births_by_year`, `latest_population_file` (newest `population_<year>.json`), `check_birth_year` (shared input check).
- `core/membership.py` — B math. `membership_birth_year(year)` → list of `Membership` (label, whole %), own generation first, then at most one neighbour. Constant `FADE_YEARS`.
- `tui/app.py` — terminal front end (Rich). Asks birth year, shows B headline then A table + source footer, loops until `q`. Display only; calls `core/`.
- `scripts/update_data.py` — converts a Census CSV in `data/raw/` to `data/population_<year>.json`, with checks. See `DATA.md`.
- `site/core.js` — JS port of A + B (plain JS, no libraries). `checkBirthYear`, `rankBirthYear`, `membershipBirthYear` take loaded JSON (`gens`, `pop`) as arguments; no file reading. Works in browser (`window.FMG`) and Node (`require`). Python is the reference.
- `tests/js_parity/` — `dump_expected.py` saves Python results for every valid year + bad inputs to `expected.json`; `check.js` runs the JS and compares (ints/strings exact, floats within 1e-9).

- `site/index.html` — dashboard (plain HTML/CSS/JS, no libraries). Loads `site/data/*.json` by `fetch`, calls `FMG` from `core.js`. Design: `DASHBOARD-DESIGN.md`. `site/mock.html` = the approved static mock.
- `site/data/` — copies of the data files; made by `scripts/sync_site_data.py` (fixed names `generations.json`, `population.json`). Don't edit by hand.

## Website: run locally
```
python scripts/sync_site_data.py     # refresh site/data (after any data change)
cd site
python -m http.server 8000           # then open http://localhost:8000
```
Must use a server; opening `index.html` directly (file://) can't load the data.

## Website: publish on GitHub Pages
Pages can only serve from repo root or `/docs`, not `/site`. Options (pick one; not done yet):
1. **GitHub Actions deploy (recommended):** Settings → Pages → Source = "GitHub Actions", plus a small workflow file that uploads `site/`. Keeps `site/` as is.
2. Move/copy `site/` contents to `/docs` — conflicts with the existing `docs/` folder; not recommended.
3. Branch `gh-pages` containing only `site/` contents (Settings → Pages → Deploy from branch → `gh-pages` / root).
Ask Claude to set up option 1 or 3 when ready. After publishing, fill in the URL in `docs/README.md`.

## How to run
From the project folder, in PowerShell:
```
.\.venv\Scripts\Activate.ps1      # activate virtual environment
pip install -r requirements.txt     # install (first time only)
pytest                              # run tests
python -m tui.app                   # run the app; enter a birth year; q to quit
python tests/js_parity/dump_expected.py   # JS parity: save Python answers
node tests/js_parity/check.js             # JS parity: compare JS to them (needs Node)
```
Rerun both parity lines after changing the math or the data files.
If activation is blocked: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`.
