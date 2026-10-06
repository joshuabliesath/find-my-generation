# T12 — Build dashboard + GitHub Pages

**Model:** sonnet
**Depends on:** T10, T11

## Goal
Working standalone dashboard in `site/`, published on GitHub Pages.

## Read
- docs/DASHBOARD-DESIGN.md, site/mock.html
- site/core.js (function signatures only)
- docs/DATA.md

## Do
- Create `site/index.html` from the approved mock: birth-year input, live results via `site/core.js`, bad-year message, footer with data source.
- Load generation and population JSON by `fetch` from files inside `site/data/`. Add a script (or extend `scripts/update_data.py`) that copies the newest `data/*.json` into `site/data/` so the site never goes stale; document it.
- Test locally with a simple static server (`python -m http.server` in `site/`) at phone and desktop width; check valid year, text, future year, very old year.
- Add GitHub Pages instructions to docs (repo Settings → Pages → deploy from branch, folder). If the Pages source must be `/docs` or root, report the options and let the user choose; do not move `docs/`.
- Do NOT push or change repo settings; give the user the exact steps.

## Don't
- Don't change `core/` Python or `core.js` math. Don't add libraries/CDNs unless T10 approved them.
- Don't include any data beyond the public Census and Pew-based files already in the repo.

## Done when
- Dashboard works locally and matches the approved design. Numbers match the TUI for 3 sample years. Git commit made.

## Update docs
- ARCHITECTURE.md (layout, how to run/publish), README.md (link to live site placeholder), DATA.md (update step), STATUS.md.

---
### HANDOFF.md format (write this when done)
"No ticket queued." (last ticket). Tell the user the Pages steps.
