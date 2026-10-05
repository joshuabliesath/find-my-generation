# Architecture

_Filled in as tickets complete. Keep it short: one line per file/module._

## Planned layout
```
data/            JSON data files (population_<year>.json, generations.json)
core/            all math; no display code
tui/             terminal front end (Rich)
scripts/         helper scripts (data update)
tests/           automated tests (pytest)
docs/            these docs
```

## Modules
- `core/rank.py` — A math. `rank_birth_year(year)` → list of `GenerationRank` (older %, younger %, approximate flag) per generation. Helpers: `load_data`, `births_by_year`.
- `tests/test_rank.py` — tests for rank (middle, boundary, top bucket, invalid input).

## How to run
From the project folder, in PowerShell:
```
.\.venv\Scripts\Activate.ps1      # activate virtual environment
pip install -r requirements.txt     # install (first time only)
pytest                              # run tests
```
If activation is blocked: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`.
_(app run command added in T07)_
