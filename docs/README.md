# Docs index

Start here. Reading this file + `STATUS.md` should be enough to know where the project stands.

| File | What's in it | Read when |
|---|---|---|
| `STATUS.md` | Ticket list, model, status, one-line notes | Always |
| `DECISIONS.md` | Every design decision and why | Changing behavior |
| `ARCHITECTURE.md` | How the code is organized and how pieces connect | Writing code |
| `DATA.md` | Data sources, file formats, how to update yearly | Touching data |
| `B-METHOD.md` | How membership % (B) is calculated: rule, formula, worked examples | Working on B |
| `tickets/` | One file per ticket (`done/` = finished); `_TEMPLATE.md` for new ones | Running that ticket |

## What the app does
Input: birth year. Output:
- **B (headline): Membership.** How much of each generation you are, e.g. "80% Millennial / 20% Gen X". Method: see `B-METHOD.md`.
- **A: Rank.** Where you fall inside each generation, by US population, e.g. "older than 62% of Millennials".

## Shape
- Python. Terminal front end first (Rich library), HTML dashboard and/or iPhone app later.
- Math code is kept separate from display code, so later front ends can reuse it.
- Data is saved as static JSON files in `data/`, labelled by year. The app never goes online.
- Data gets refreshed yearly or every 5 years by a helper script.

## Future
See "Next up" in `STATUS.md`.
