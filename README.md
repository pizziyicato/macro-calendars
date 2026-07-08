# Global Macro Calendar System — final (8 Jul 2026)

51 flag-prefixed country calendars · 417 events · history from Jan 2026 ·
fixed future dates through 2026/27 · recurring convention rules projected to Aug 2031 ·
Claude-maintainable via CLAUDE.md.

## Setup (Thunderbird)
Keep this folder somewhere permanent. File -> Open -> Calendar File on each .ics in
calendars/ you want (each mounts as its own coloured, flag-named calendar, file-backed —
edits to the files on disk appear in Thunderbird after reload). Additionally SUBSCRIBE
(New Calendar -> On the Network) to the true auto-updating feeds:
- BLS: webcal://www.bls.gov/schedule/news_release/bls.ics
- BEA: https://www.bea.gov/news/schedule/ics/online-calendar-subscription.ics

## How "up to date for 5 years" works (honestly)
1. Fixed events: every schedule institutions have actually published (verified/est-tiered).
2. rr-* recurring events: deterministic conventions (NFP first Friday, LPR 20th, NBS PMI
   month-end, BCRP/NBS-Serbia 2nd Thursday, BI 3rd Wednesday, SG CPI/NODX, JP CPI, KR
   exports) auto-populate Jan 2027 - Aug 2031 inside the files themselves.
3. Claude refresh loop: banks publish next-year dates every autumn — point any Claude
   session (Claude Code / MCP filesystem / your thunderbird-mcp setup) at this folder and
   say "refresh the macro calendars"; CLAUDE.md tells it exactly what to fetch, how to
   edit, and to run validate.py. A static file can't update itself; this loop is the
   mechanism.

## Trust tiers
no suffix = primary-source verified · " · est" = pattern-derived (source named in each
event description) · "TBC/window" = not yet fixed by the institution.

## Corrections log (from cross-checking)
SNB Dec 10 (not 17) · BOK Jul 16 (not 9) · NBP Sep 2 / Dec 2 · SARB Sep 23 ·
Riksbank H2 = Aug 20 / Sep 24 / Nov 4 / Dec 16.

## Manifest
- calendars/Argentina.ics — 1 events
- calendars/Australia.ics — 16 events
- calendars/Bahrain.ics — 1 events
- calendars/Bosnia.ics — 1 events
- calendars/Brazil.ics — 10 events
- calendars/Canada.ics — 14 events
- calendars/CapeVerde.ics — 1 events
- calendars/Chile.ics — 4 events
- calendars/China.ics — 28 events
- calendars/Colombia.ics — 4 events
- calendars/Czechia.ics — 4 events
- calendars/Egypt.ics — 4 events
- calendars/Eurozone.ics — 30 events
- calendars/Gambia.ics — 1 events
- calendars/Ghana.ics — 3 events
- calendars/Global-Multilateral.ics — 5 events
- calendars/Haiti.ics — 1 events
- calendars/Hungary.ics — 6 events
- calendars/Iceland.ics — 3 events
- calendars/India.ics — 14 events
- calendars/Indonesia.ics — 7 events
- calendars/Israel.ics — 4 events
- calendars/Japan.ics — 19 events
- calendars/Kazakhstan.ics — 4 events
- calendars/Kenya.ics — 3 events
- calendars/Korea.ics — 14 events
- calendars/Latvia.ics — 1 events
- calendars/Malaysia.ics — 3 events
- calendars/Mexico.ics — 8 events
- calendars/Morocco.ics — 3 events
- calendars/NewZealand.ics — 8 events
- calendars/Nigeria.ics — 3 events
- calendars/Norway.ics — 8 events
- calendars/Peru.ics — 7 events
- calendars/Philippines.ics — 3 events
- calendars/Poland.ics — 4 events
- calendars/Romania.ics — 3 events
- calendars/Russia.ics — 4 events
- calendars/Serbia.ics — 7 events
- calendars/Singapore.ics — 20 events
- calendars/SouthAfrica.ics — 3 events
- calendars/SouthSudan.ics — 1 events
- calendars/Sweden.ics — 9 events
- calendars/Switzerland.ics — 4 events
- calendars/Taiwan.ics — 2 events
- calendars/Thailand.ics — 3 events
- calendars/Turkiye.ics — 8 events
- calendars/UK.ics — 14 events
- calendars/US.ics — 84 events
- calendars/Ukraine.ics — 4 events
- calendars/Zambia.ics — 1 events
