# T02 — Generation definitions file

**Model:** haiku
**Depends on:** T01

## Goal
`data/generations.json` holding Pew Research's generation names and birth-year ranges.

## Read
- docs/DATA.md

## Do
- Look up Pew's current definitions (Silent, Boomers, Gen X, Millennials, Gen Z, Gen Alpha). Include Greatest Generation if Pew defines it.
- For each generation, store: name, short label, start year, end year. Gen Alpha's end year is `null` (not settled yet).
- Include the source URL and the date it was checked inside the file.
- Write a small test: the year ranges don't overlap and have no gaps.

## Don't
- Write any math beyond loading/checking this file.

## Done when
- File exists, test passes, git commit made.

## Update docs
- DATA.md "Generations": the file format, the source URL, and what to do if Pew changes its definitions.
