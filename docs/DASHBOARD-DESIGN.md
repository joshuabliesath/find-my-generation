# Dashboard design (approved T10)

Reference mock: `site/mock.html` (hard-coded 1985). Same info as the TUI, nothing extra.

## Layout (single column, max 640px, works at phone width)
1. Title "Find my generation".
2. Birth-year input + Go button.
3. Error line (empty unless bad input).
4. B card: label "Born <year>", headline, split bar, legend.
5. A card: one row per generation.
6. Footer.

## B visual
Headline "82% Millennials + 18% Gen X" (each part in its generation color) + one horizontal split bar (width = %). Colors: own generation blue, neighbour orange.

## A visual
Per generation row: name, birth years, bar (gray = % older than you, blue = % younger), numbers "x.x% older than you" / "y.y% younger than you". `*` after the numbers if approximate; footnote "* approximate (people aged 100+ spread evenly over birth years)" shown only then.

## Theme / tone
Auto light/dark (`prefers-color-scheme`). Clean, neutral. Plain CSS, no libraries, no CDN, no age-distribution chart.

## Errors
Same messages as TUI: non-number → "Please enter a whole number, e.g. 1985."; out of range → message from the math (valid 1901–2025).

## Data each element needs
- B: list of {label, pct} (1–2 items).
- A: per generation {name, start_year, end_year, older_pct, younger_pct, approximate}.
- Footer: population `dataset`, `vintage`; "Generations: Pew Research Center".
