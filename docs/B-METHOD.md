# B method — membership % ("how much of each generation you are")

Decided in T04 (2026-10-05). T06 builds from this file alone.

## In plain words
- Generation lines are Pew's, from `data/generations.json`. They are not changed.
- Everyone is a blend of **at most 2 generations**: their own (Pew) generation plus the neighbour on the side of the **nearest** line.
- **Exactly at a line = 50/50.** The year just inside a line leans to its own side (1980 = 51% Gen X / 49% Millennial).
- Blending fades out over **8 years** from every line, the same at every line. Anyone 7.5+ years from every line is **100%** their own generation.
- The fade follows an **S-curve**: nearly pure near the core, steepest in the middle, biggest blends in the last ~3 years before a line.
- Shown as **whole percents**. Own share is never shown as 50 (no-tie rule).

## Formula
Constant: `FADE_YEARS = 8`. Must be ≤ half the shortest generation (16 yrs → 8), which guarantees at most 2 generations. Keep it as one named constant in the math code.

For birth year `y`:
1. `own` = the generation whose `start_year ≤ y ≤ end_year` (Pew). For the first generation (Greatest), treat any earlier year as Greatest. For the last generation (Alpha, `end_year = null`), treat it as having no end.
2. `m = y + 0.5` (count the birth year at its middle).
3. Distances to the lines of `own`:
   - start line (only if `own` is not the first generation): `u_start = m − own.start_year`, neighbour = previous generation
   - end line (only if `own.end_year` is not null): `u_end = (own.end_year + 1) − m`, neighbour = next generation
   - If neither line exists → 100% own.
4. `u` = the smaller distance; `partner` = the neighbour on that side. (A tie can only happen at a generation's exact centre, where the result is 100% anyway; pick either.)
5. `t = max(0, (FADE_YEARS − 0.5 − u) / (FADE_YEARS − 0.5))`  → 0 in the core, rising toward 1 at the line.
6. `partner_share = 0.5 × (3t² − 2t³)`  (S-curve, "smoothstep").
7. `own_pct = round_half_up(100 × (1 − partner_share))`. Use round-half-up, not Python's default `round()` (which rounds halves to even).
8. No-tie rule: if `own_pct == 50`, set it to 51.
9. `partner_pct = 100 − own_pct`. If `partner_pct == 0`, return only the own generation at 100.

Return plain data, e.g. a list of `(generation, pct)` with own first. All other generations are 0%.

## Worked examples (current data)

Gen X sample (1965–1980). Years 1965–71 blend with Boomers; 1974–80 with Millennials.

| Year | Gen X % | Partner % |
|---|---|---|
| 1965 / 1980 | 51 | 49 |
| 1966 / 1979 | 55 | 45 |
| 1967 / 1978 | 63 | 37 |
| 1968 / 1977 | 73 | 27 |
| 1969 / 1976 | 82 | 18 |
| 1970 / 1975 | 91 | 9 |
| 1971 / 1974 | 98 | 2 |
| 1972, 1973 | 100 | – |

Other checks (use as tests):

| Birth year | Result |
|---|---|
| 1920 | Greatest 100 |
| 1926 | Greatest 55 / Silent 45 |
| 1928 | Silent 51 / Greatest 49 |
| 1946 | Boomers 51 / Silent 49 |
| 1955 | Boomers 100 |
| 1960 | Boomers 82 / Gen X 18 |
| 1964 | Boomers 51 / Gen X 49 |
| 1981 | Millennials 51 / Gen X 49 |
| 1988 | Millennials 100 |
| 2012 | Gen Z 51 / Gen Alpha 49 |
| 2013 | Gen Alpha 51 / Gen Z 49 |
| 2020, 2025 | Gen Alpha 100 |

Pure cores that result: Greatest ≤1920, Silent 1935–38, Boomers 1953–57, Gen X 1972–73, Millennials 1988–89, Gen Z 2004–05, Gen Alpha 2020+.

## Edge cases
- **Boundary years:** always 51/49 toward the Pew side, never 50/50.
- **Greatest:** no older neighbour, so years before 1921 are 100% Greatest.
- **Gen Alpha:** open-ended; needs no assumed end year. 2020+ is 100% Alpha.
- **Invalid years** (future, or older than the data supports): rejected by the shared input check from T05, not here.
- **Generation lines change** (e.g. Pew adds an end year for Alpha or a new generation): no code change needed, as long as every generation stays ≥ 16 years long. If a shorter generation appears, a person could be near two lines at once; revisit `FADE_YEARS`.

## Why this method
- The user wants big, meaningful blends at the cusps (1979 = 55/45) and pure-looking cores.
- Max 2 generations: from birth year alone, a person's formative years can overlap one neighbouring generation, not both.
- Same fade width at every line: uneven Pew generation lengths don't change how a line behaves.
- S-curve over linear: quieter tails near the core and bigger blends near the line.
- Rejected: population-weighted, blending other sources' boundaries, a centre-based fade that leaks into 3 generations, a √ curve (cliff at the centre), a t² curve (cusp too mild), and equal-length generations (breaks the well-known Pew labels).
- Note: "% of a generation" is a framing, not a measurement. The display should say something like "Generation lines are fuzzy; this shows how close you are to one."
