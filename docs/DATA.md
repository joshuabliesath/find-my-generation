# Data

_Filled in by T02, T03, T08._

## Generations
Source: Pew Research (URLs and date checked are inside the file). File: `data/generations.json`.

Format: top-level `source_urls`, `date_checked`, `notes`, and `generations` (list, oldest first). Each entry: `name`, `label` (short), `start_year`, `end_year`. Gen Alpha `end_year` is `null` (open-ended). Ranges are inclusive; next start = previous end + 1.

Caveat: Greatest start (1901) and Gen Alpha start (2013) came from secondary summaries of Pew, not the pages listed. See `notes` in file.

If Pew changes definitions: edit the years in the file, update `date_checked`, run `pytest tests/test_generations.py`, and log the change in `docs/DECISIONS.md`.

## Population
Source: US Census Bureau national population estimates by single year of age. _(exact dataset, vintage, format added in T03)_

## Updating
_(steps added in T08)_
