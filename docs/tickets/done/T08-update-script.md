# T08 — Data update script

**Model:** sonnet
**Depends on:** T03

## Goal
A repeatable way to add a new year's Census data.

## Read
- docs/DATA.md
- The one-off conversion script T03 left in scripts/

## Do
- Turn it into `scripts/update_data.py`: it takes a downloaded Census file and writes `data/population_<year>.json`.
- Keep older population files. By default the app uses the newest one.
- Check the result is sensible: the total population is plausible and no ages are missing.
- If the app currently hard-codes which year's file to use, change it to use the newest file automatically.

## Don't
- Fetch data automatically from the internet; the user downloads the file by hand.

## Done when
- Re-running the script on T03's raw file reproduces the same JSON. Tests pass, git commit made.

## Update docs
- DATA.md "Updating": step-by-step instructions the user can follow alone (where to download, the command to run, how to check the result).
