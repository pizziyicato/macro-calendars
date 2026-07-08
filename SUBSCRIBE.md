# Phone-home — 100% through your GitHub repo

Every calendar, curated and mirrored, is subscribed from ONE place:
  https://raw.githubusercontent.com/<YOU>/macro-calendars/main/calendars/<Name>.ics

## How each part stays fresh
- 51 curated country calendars: Claude refresh loop (see CLAUDE.md) -> git push -> all devices update.
- 5 Feed-*.ics mirrors (BLS, BEA, FOMC, ECB, US-Macro): a GitHub Actions workflow
  (.github/workflows/mirror-feeds.yml) re-fetches the upstreams every 8 hours on GitHub's
  servers and commits changes. Zero involvement from you or Claude.

## Thunderbird
New Calendar -> On the Network -> iCalendar (ICS) -> paste raw URL -> username blank ->
Subscribe. Properties: refresh every 30 min, read-only. Same URLs work in Google Calendar
("From URL") and on phones.

## Health checks
- Actions tab green = mirrors fresh. A failed fetch keeps the previous copy (never blank).
- bls.gov occasionally bot-blocks; the workflow warns and retries next cycle.
- Do not rename files or edit Feed-*.ics by hand (bot-managed); curated files follow CLAUDE.md.
