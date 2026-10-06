# T11 — Port core math to JavaScript

**Model:** sonnet
**Depends on:** T06 (T10 not required)

## Goal
Same A (rank) and B (membership) math in browser JavaScript, giving identical numbers to the Python code.

## Read
- core/rank.py, core/membership.py
- docs/B-METHOD.md, docs/ARCHITECTURE.md
- data/generations.json (structure only), newest data/population_*.json (structure only: first ~20 lines)

## Do
- Create `site/core.js` (plain JS, no libraries, no build step). Functions mirror Python: `checkBirthYear`, `rankBirthYear`, `membershipBirthYear`. Take loaded JSON as arguments (no file reading inside the math).
- Make it usable from the browser (`<script>`) and from Node for tests.
- Create `tests/js_parity/`: a Node script that runs the JS for a spread of birth years (every year in range plus edge cases: first/last valid year, generation boundaries, same-year, 100+ bucket) and compares against Python output saved as JSON. Add a small Python script to dump the Python expected values.
- Document how to run the parity check.

## Don't
- Don't change the Python math or its tests. If JS and Python disagree, the Python is the reference; report the mismatch.
- Don't build any page or styling (T12).

## Done when
- Parity check passes for all birth years (numbers match, incl. rounding and `approximate` flag). Existing pytest still passes. Git commit made.

## Update docs
- ARCHITECTURE.md (layout + modules + how to run parity check), STATUS.md.

---
### HANDOFF.md format (write this when done)
Point at T12 (sonnet).
