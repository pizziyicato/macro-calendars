# CLAUDE.md — maintaining these macro calendars

This folder is the single source of truth for a 51-calendar global macro event system.
`calendars/*.ics` are plain-text RFC 5545 files that Thunderbird mounts as file-backed
calendars (File -> Open -> Calendar File). Editing a file on disk updates the calendar
in Thunderbird after a restart/reload. Any Claude session with filesystem access
(Claude Code, Cowork, MCP filesystem, thunderbird-mcp environment) can maintain them.

## Refresh workflow (run whenever the user asks, or ~quarterly)
1. Web-search the newly published schedules: each central bank publishes next-year
   meeting dates in Q3-Q4 (Fed ~June, ECB ~mid-year, BOJ ~July, BOE ~September,
   Copom ~June, RBA ~February). Statistics agencies (BLS, BEA, Eurostat, ONS, NBS)
   publish full-year release calendars in autumn.
2. Append new VEVENTs to the matching country file, before END:VCALENDAR. Rules:
   - Title format: <flag emoji> <event name> (<local time>) [+ " · est" if not from a primary source]
   - DTSTART in UTC (Z), converted from local time WITH correct DST for that date
   - UID unique, pattern <slug>-<yyyymmdd>@ziyi-macro; DTSTAMP any fixed UTC stamp
   - Fold lines at 74 octets (continuation lines start with one space); CRLF endings
   - All-day events: DTSTART;VALUE=DATE + exclusive DTEND
3. Replace any "· est" event with the confirmed date once the institution publishes it
   (edit DTSTART + description; keep the UID so Thunderbird updates in place).
4. Delete nothing: past events stay as history.
5. Run `python3 validate.py` — it must print AUDIT PASS before you finish.
6. Recurring "rr-*" events project conventions to Aug 2031; when a real schedule is
   added for a year, the fixed events take precedence visually (rules stay as backdrop).

## Known auto-updating upstream feeds (subscribe in Thunderbird; zero maintenance)
- BLS: webcal://www.bls.gov/schedule/news_release/bls.ics
- BEA: https://www.bea.gov/news/schedule/ics/online-calendar-subscription.ics
- Smart Calendars AI FOMC/ECB: smartcalendars.ai/en/feeds

## Trust tiers
no suffix = primary-source verified · " · est" = convention/pattern-derived ·
"TBC/window" = institution has not fixed the date. Never invent a date without a tier label.

## Publishing (phone-home)
If this folder is a git repo published via publish.sh, finish every refresh with:
  git add -A && git commit -m "refresh $(date +%F)" && git push
All calendars subscribed via the raw.githubusercontent.com URLs update automatically
on every device. Never rename files or change UIDs of existing events — subscribers
rely on both for clean in-place updates.

## Mirrored feeds
calendars/Feed-*.ics are managed by .github/workflows/mirror-feeds.yml (8-hourly upstream
mirror on GitHub Actions). Never edit them manually; validate.py skips them. If a mirror
goes stale, check the Actions log — likely upstream bot-blocking; it self-heals next run.
