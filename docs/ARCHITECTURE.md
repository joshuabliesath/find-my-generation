# Architecture

## Layout
```
data/            JSON data files (population_<year>.json, generations.json); raw/ = Census CSVs
core/            all math; no display code
tui/             terminal front end (Rich)
scripts/         helper scripts (data update)
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
