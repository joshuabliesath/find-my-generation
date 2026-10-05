# T07 — Terminal front end

**Model:** haiku
**Depends on:** T05, T06

## Goal
Run the app → enter birth year → see B (headline) then A (table).

## Read
- docs/ARCHITECTURE.md (function names for A and B)

## Do
- Create `tui/app.py` using Rich.
- Ask for a birth year. Invalid input gets a friendly message and the question again.
- Show B first and prominently (e.g. a big line or simple bar).
- Show A below as a table: generation, its birth years, % older than you, % younger than you.
- Footer: data source and data year.
- Ask again for another birth year, or quit.
- Make it runnable with `python -m tui.app`.

## Don't
- Put any math in this file. Call the `core/` functions only.

## Done when
- The app runs and handles invalid input. Git commit made.

## Update docs
- ARCHITECTURE.md "How to run" + "Modules".
