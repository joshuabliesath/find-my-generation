# Architecture

## Layout
```
data/            JSON data files (population_<year>.json, generations.json); raw/ = Census CSVs
core/            all math; no display code
tui/             terminal front end (Rich)
scripts/         helper scripts (data update)
tests/           automated tests (pytest), one test file per module
docs/            these docs
```

## Modules
- `core/rank.py` — A math. `rank_birth_year(year)` → list of `GenerationRank` (older %, younger %, approximate flag) per generation. Helpers: `load_data`, `births_by_year`, `latest_population_file` (newest `population_<year>.json`), `check_birth_year` (shared input check).
- `core/membership.py` — B math. `membership_birth_year(year)` → list of `Membership` (label, whole %), own generation first, then at most one neighbour. Constant `FADE_YEARS`.
- `tui/app.py` — terminal front end (Rich). Asks birth year, shows B headline then A table + source footer, loops until `q`. Display only; calls `core/`.
- `scripts/update_data.py` — converts a Census CSV in `data/raw/` to `data/population_<year>.json`, with checks. See `DATA.md`.

## How to run
From the project folder, in PowerShell:
```
.\.venv\Scripts\Activate.ps1      # activate virtual environment
pip install -r requirements.txt     # install (first time only)
pytest                              # run tests
python -m tui.app                   # run the app; enter a birth year; q to quit
```
If activation is blocked: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`.
