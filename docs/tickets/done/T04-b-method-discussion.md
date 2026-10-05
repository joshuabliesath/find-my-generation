# T04 — Decide B method (discussion)

**Model:** sonnet
**Depends on:** – (needs T02 + T03 done if a population-weighted method is chosen)

## Goal
With the user, choose how to calculate B ("how much of each generation you are"). B is the headline stat and will later be the main visual. **Discussion only, no code.**

## Read
- docs/DECISIONS.md
- data/generations.json (if it exists)

## Do
- Present the candidate methods below in plain language. For each one, give a worked example for 2–3 sample birth years (one in the middle of a generation, one near a boundary, one at the very edge).
- Point out the trade-offs: is it intuitive, does it add up to 100%, does it use population data, how would it look as a visual.
- Let the user decide. Suggest variations if useful.

Starting candidates:
1. **Distance from the center:** the closer you are to a generation's middle year, the more of that generation you are, fading off near the edges.
2. **Blended near the boundaries:** you're fully one generation unless you were born within a few years of a boundary. Inside that window you're split between the two.
3. **Weighted by population:** method 1 or 2, adjusted by how many people were born in each year.
4. **Other sources' definitions:** blend Pew with other sources' boundaries.

## Don't
- Write code.

## Done when
- The user has approved one method.
- `docs/B-METHOD.md` is written: the method in plain words, the formula, the worked examples, and the edge cases. T06 will build from this file alone.

## Update docs
- DECISIONS.md: the chosen method and why.
- README.md: link B-METHOD.md in the index table.
