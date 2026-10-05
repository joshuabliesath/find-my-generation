# T05 — Core math: A (rank)

**Model:** sonnet
**Depends on:** T02, T03

## Goal
Function: birth year → for each generation, the % of that generation that is older than you (and younger than you).

## Read
- docs/ARCHITECTURE.md, docs/DATA.md

## Do
- In `core/`: load the JSON data and turn birth year into age (age = estimate year − birth year).
- Rank inside a generation: the people in that generation born before you, as a share of the generation's total population. Pick one rule for how people born in the same year as you are counted (e.g. count half of them) and record it in DECISIONS.md.
- Generations entirely older or younger than you come out as 100% or 0%.
- Ages in the grouped top bucket (85+ or 100+): give an approximate answer and mark it as approximate in the output.
- Reject birth years in the future or older than the data covers, with a clear error message.
- Return plain data (dictionaries or dataclasses), not formatted text.
- Write tests: one birth year in the middle of a generation, one at a boundary, one in the top age bucket, one invalid input.

## Don't
- Write any display code. Don't work on B.

## Done when
- Tests pass, git commit made.

## Update docs
- ARCHITECTURE.md "Modules": one line per new file/function.
- DECISIONS.md: the same-birth-year rule, how the top age bucket is handled.
