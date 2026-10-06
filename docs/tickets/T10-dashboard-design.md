# T10 — Decide dashboard look (discussion + prototype)

**Model:** sonnet
**Depends on:** –

## Goal
Agree with the user on how the web dashboard looks. Same information as the TUI, made pretty. Output: an approved design doc + mock page.

## Read
- tui/app.py (what the TUI shows: B headline, A table, footer notes)
- docs/B-METHOD.md (only if needed to word B visuals)

## Do
- Ask the user at most 4 short questions (AskUserQuestion), e.g.: B visual style (split bar / ring / big text), light vs dark vs auto theme, tone (clean/neutral vs playful), whether to include a small age-distribution chart marking the user.
- Build `site/mock.html`: ONE static page, hard-coded sample data for one birth year (e.g. 1985), no JS math. Inline CSS, no build step, works on phone width.
- Content must match the TUI: B headline (e.g. "70% Millennial + 30% Gen X"), A table/cards per generation (name, birth years, % older, % younger, `*` approximate note), footer (Census source, vintage, Pew generations).
- Show it to the user; iterate until they approve.
- Write `docs/DASHBOARD-DESIGN.md`: layout, B visual, A visual, colors/theme, error message for bad year, what data fields each element needs.

## Don't
- Don't port any math (that is T11) or wire real data (T12).
- Don't add information the TUI doesn't show, beyond what the user approves.
- Don't use external libraries or CDNs unless the user approves (GitHub Pages hosting is plain static files).

## Done when
- User approved `site/mock.html`. `docs/DASHBOARD-DESIGN.md` written. Git commit made.

## Update docs
- DECISIONS.md (look and chart choices), STATUS.md.

---
### HANDOFF.md format (write this when done)
Point at T11 (sonnet).
