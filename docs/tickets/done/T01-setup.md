# T01 — Project setup

**Model:** haiku
**Depends on:** –

## Goal
Empty but working Python project skeleton.

## Read
- docs/ARCHITECTURE.md

## Do
- Check that Python 3.11 or newer is installed. If it isn't, stop and tell the user.
- `git init`. Add a `.gitignore` for Python files and the virtual environment folder.
- Create a virtual environment in `.venv` (a project-only Python install).
- Create `requirements.txt` listing `rich` and `pytest`, then install them.
- Create the empty folders from ARCHITECTURE.md, with `__init__.py` files where Python needs them.
- Add one placeholder test that passes.

## Don't
- Write any app logic.

## Done when
- `pytest` runs and passes.
- First git commit made.

## Update docs
- ARCHITECTURE.md "How to run": activate the virtual environment, install, run tests (exact PowerShell commands).
