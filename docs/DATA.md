# Data

## Generations
Source: Pew Research (URLs and date checked are inside the file). File: `data/generations.json`.

Format: top-level `source_urls`, `date_checked`, `notes`, and `generations` (list, oldest first). Each entry: `name`, `label` (short), `start_year`, `end_year`. Gen Alpha `end_year` is `null` (open-ended). Ranges are inclusive; next start = previous end + 1.

Caveat: Greatest start (1901) and Gen Alpha start (2013) came from secondary summaries of Pew, not the pages listed. See `notes` in file.

If Pew changes definitions: edit the years in the file, update `date_checked`, run `pytest tests/test_generations.py`, and log the change in `docs/DECISIONS.md`.

## Population
Source: US Census Bureau, NC-EST2025-AGESEX-RES (Vintage 2025), resident population by single year of age and sex, July 1, 2025 estimate.
URL: https://www2.census.gov/programs-surveys/popest/datasets/2020-2025/national/asrh/nc-est2025-agesex-res.csv
Raw file: `data/raw/nc-est2025-agesex-res.csv` (has 2020-2025; we use POPESTIMATE2025, SEX=0 = both sexes). Converted by `scripts/update_data.py` to `data/population_2025.json`.

Format: `dataset`, `vintage`, `estimate_date`, `source_url`, `sex`, `top_age_group`, `census_total` (Census's own total row), `ages` (list of `{age, count}`, ages 0-100).

Top age group: age 100 means "100 and older" (open-ended). Flagged in `top_age_group` (`open_ended: true`, label "100+").

## Updating
1. Download the new NC-EST<vintage>-AGESEX-RES CSV from the Census Bureau (Population Estimates > National > by age and sex; same folder pattern as the URL above, e.g. `.../datasets/2020-2026/national/asrh/nc-est2026-agesex-res.csv`).
2. Save it in `data/raw/`, keeping its original name.
3. Run: `python scripts/update_data.py data/raw/<file>.csv` (uses the newest year in the file; add `--year 2026` to pick another).
4. Check: the script prints total and number of ages (expect ~335-350 million, 101 ages). It stops with an error if ages 0-100 are not all present, ages don't sum to Census's total (within 0.1%), or the total is implausible.
5. Run `python -m pytest`. Old `data/population_<year>.json` files are kept; the app automatically uses the newest.
6. Commit the new raw and JSON files. Note: `tests/test_population.py` still checks the 2025 file only.
