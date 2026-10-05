# Status

Statuses: todo / in progress / done / blocked

| # | Ticket | Model | Depends on | Status | Note |
|---|---|---|---|---|---|
| T01 | Project setup | haiku | – | done | Python 3.12, .venv, pytest passes, first commit made. |
| T02 | Generation definitions file | haiku | T01 | done | data/generations.json + tests pass. Greatest start (1901) and Alpha start (2013) from secondary sources; see DATA.md. |
| T03 | Population data file | sonnet | T01 | done | data/population_2025.json (Census Vintage 2025, ages 0-100+). Tests pass. |
| T04 | Decide B method (discussion) | sonnet | – | todo | Headline stat. No code. |
| T05 | Core math: A (rank) | sonnet | T02, T03 | todo | |
| T06 | Core math: B (membership) | sonnet | T04, T05 | todo | |
| T07 | Terminal front end | haiku | T05, T06 | todo | |
| T08 | Data update script | sonnet | T03 | todo | |
| T09 | Final docs pass | haiku | all | todo | |

Suggested order: T01 → T02 → T03 → T04 → T05 → T06 → T07 → T08 → T09
(T04 can happen anytime before T06.)
