# Decisions

Newest at bottom. Format: date — decision — why.

- 2026-10-05 — Show both A (rank inside generation) and B (membership %) — both are interesting; B is the headline.
- 2026-10-05 — B method is undecided; settled in T04 — it drives the main visual, so it needs a deliberate choice.
- 2026-10-05 — Input is birth year, not age — age alone could mean either of two birth years.
- 2026-10-05 — Generation boundaries from Pew Research, kept in an editable data file — sources disagree; easy to swap.
- 2026-10-05 — Static JSON data, labelled by year, no internet use — simple, and works for future web/iPhone versions.
- 2026-10-05 — Math kept separate from display — so the dashboard/iPhone versions can reuse it.
- 2026-10-05 — Terminal front end uses Rich, not a full-screen framework — keep v1 simple.
- 2026-10-05 — Each ticket assigned the cheapest model that can do it — cost control.
- 2026-10-05 — Greatest Generation starts 1901 and Gen Alpha starts 2013, Alpha open-ended — Pew pages fetched did not state these; taken from secondary summaries, flagged in file notes.
- 2026-10-05 — Population = Census NC-EST2025-AGESEX-RES (Vintage 2025), single year of age 0-100+, both sexes — latest official national estimate with single-year ages; top age is open-ended 100+.
- 2026-10-05 — B method: population-weighted and other-sources options eliminated; want wide blends (e.g. 1979/1980 clearly part of both X and Millennial); choose between distance-from-center and boundary-blend variants in T04 — user priority is meaningful cusp blending.
- 2026-10-05 — B method: Pew lines kept; max 2 generations (own + nearest neighbour); 50/50 at each line; S-curve fade over a fixed 8 yrs from every line; whole %, own never shown as 50 (no-tie rule). Full spec in B-METHOD.md — big cusp blends (1979 = 55/45) with pure cores; 3-way blends judged unrealistic from birth year alone; equal-length generations rejected (breaks known Pew labels).
- 2026-10-05 — A rank: people born in your own birth year count half older / half younger — simple, symmetric, no tie.
- 2026-10-05 — A rank: age = 2025 − birth year (Census estimate year). Age 100+ bucket is spread evenly over birth years 1901–1925 and flagged `approximate` only when your birth year is ≤1925 — true spread unknown; only affects Greatest. Valid birth years: 1901–2025, else ValueError.
- 2026-10-05 — T06: moved birth-year validation out of rank_birth_year into shared check_birth_year() (core/rank.py) so A and B reject bad input identically.
- 2026-10-05 � T08: app picks the newest `population_<year>.json` by file name (`latest_population_file` in core/rank.py). update_data.py replaced convert_population.py; validates ages 0-100, sum vs Census total, plausible total.
