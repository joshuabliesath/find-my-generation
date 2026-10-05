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
_(none yet)_

## How to run
From the project folder, in PowerShell:
```
.\.venv\Scripts\Activate.ps1      # activate virtual environment
pip install -r requirements.txt     # install (first time only)
pytest                              # run tests
```
If activation is blocked: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`.
_(app run command added in T07)_
