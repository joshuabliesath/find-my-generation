# T03 — Population data file

**Model:** sonnet
**Depends on:** T01

## Goal
`data/population_<year>.json`: US resident population for each single year of age, from the latest Census Bureau estimates.

## Read
- docs/DATA.md

## Do
- Find the latest US Census Bureau national population estimate by single year of age (both sexes, total US).
- Download the raw file into `data/raw/`.
- Convert it to JSON: the year the estimate describes (Census uses July 1), the source URL, the vintage, and a list of age → count.
- Record how the top age group works ("85+" or "100+") as a field in the file.
- Write a test: the counts add up to roughly the total US population that Census reports.

## Don't
- Build the reusable update script; that's T08. A one-off conversion is fine here, but save it in `scripts/` for T08 to build on.

## Done when
- JSON exists, test passes, git commit made.

## Update docs
- DATA.md "Population": the dataset name, vintage, URL, JSON format, how the top age group is handled.
- DECISIONS.md: which dataset was chosen and why.
