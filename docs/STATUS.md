# Status

Statuses: todo / in progress / done / blocked

| # | Ticket | Model | Depends on | Status | Note |
|---|---|---|---|---|---|
| T01 | Project setup | haiku | – | done | Python 3.12, .venv, pytest passes, first commit made. |
| T02 | Generation definitions file | haiku | T01 | done | data/generations.json + tests pass. Greatest start (1901) and Alpha start (2013) from secondary sources; see DATA.md. |
| T03 | Population data file | sonnet | T01 | done | data/population_2025.json (Census Vintage 2025, ages 0-100+). Tests pass. |
| T04 | Decide B method (discussion) | opus | – | done | S-curve blend, max 2 gens, 8-yr fade from each Pew line. See B-METHOD.md. |
| T05 | Core math: A (rank) | sonnet | T02, T03 | done | core/rank.py + tests pass. Same-year = half older; 100+ bucket spread evenly 1901-1925 (approximate). |
| T06 | Core math: B (membership) | sonnet | T04, T05 | done | core/membership.py + tests pass (all B-METHOD examples). Input check moved to shared `check_birth_year` in rank.py. |
| T07 | Terminal front end | haiku | T05, T06 | done | tui/app.py; `python -m tui.app`. Tested by hand (valid, text, future year). |
| T08 | Data update script | sonnet | T03 | done | scripts/update_data.py (replaces convert_population.py); app uses newest population file; rerun reproduces 2025 JSON. |
| T09 | Final docs pass | haiku | all | done | Docs trimmed and checked against code; finished tickets in `tickets/done/`. |

Suggested order: T01 → T02 → T03 → T04 → T05 → T06 → T07 → T08 → T09
(T04 can happen anytime before T06.)

## Next up (not ticketed yet)
- HTML dashboard (Sonnet), with B as the main visual.
- iPhone app: rewrite the math in Swift and reuse the same JSON data (Sonnet; Opus only if it gets stuck).
