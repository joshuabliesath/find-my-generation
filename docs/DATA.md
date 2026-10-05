# Data

_Filled in by T02, T03, T08._

## Generations
Source: Pew Research (URLs and date checked are inside the file). File: `data/generations.json`.

Format: top-level `source_urls`, `date_checked`, `notes`, and `generations` (list, oldest first). Each entry: `name`, `label` (short), `start_year`, `end_year`. Gen Alpha `end_year` is `null` (open-ended). Ranges are inclusive; next start = previous end + 1.

Caveat: Greatest start (1901) and Gen Alpha start (2013) came from secondary summaries of Pew, not the pages listed. See `notes` in file.

If Pew changes definitions: edit the years in the file, update `date_checked`, run `pytest tests/test_generations.py`, and log the change in `docs/DECISIONS.md`.

## Population
Source: US Census Bureau, NC-EST2025-AGESEX-RES (Vintage 2025), resident population by single year of age and sex, July 1, 2025 estimate.
URL: https://www2.census.gov/programs-surveys/popest/datasets/2020-2025/national/asrh/nc-est2025-agesex-res.csv
Raw file: `data/raw/nc-est2025-agesex-res.csv` (has 2020-2025; we use POPESTIMATE2025, SEX=0 = both sexes). Converted by `scripts/convert_population.py` (one-off; T08 builds on it) to `data/population_2025.json`.

Format: `dataset`, `vintage`, `estimate_date`, `source_url`, `sex`, `top_age_group`, `census_total` (Census's own total row), `ages` (list of `{age, count}`, ages 0-100).

Top age group: age 100 means "100 and older" (open-ended). Flagged in `top_age_group` (`open_ended: true`, label "100+").

## Updating
_(steps added in T08)_
