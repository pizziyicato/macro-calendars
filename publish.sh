#!/usr/bin/env bash
set -euo pipefail
command -v gh >/dev/null || { echo "Install GitHub CLI: brew install gh && gh auth login"; exit 1; }
REPO="${1:-macro-calendars}"
git init -b main -q 2>/dev/null || true
git add -A
git commit -q -m "macro calendars $(date +%F)" || true
gh repo create "$REPO" --public --source=. --push 2>/dev/null || git push -u origin main || {
  echo "If push was rejected over workflow files: run  gh auth refresh -s workflow  and retry ./publish.sh"; exit 1; }
USER=$(gh api user -q .login)
gh workflow run mirror-feeds.yml 2>/dev/null || true
echo ""
echo "Repo: https://github.com/$USER/$REPO  (Actions tab should show mirror-upstream-feeds)"
echo ""
echo "Subscribe to these in Thunderbird (New Calendar -> On the Network -> iCalendar):"
for f in calendars/*.ics; do echo "  https://raw.githubusercontent.com/$USER/$REPO/main/$f"; done
echo "  https://raw.githubusercontent.com/$USER/$REPO/main/calendars/Feed-US-BLS-Official.ics"
echo "  https://raw.githubusercontent.com/$USER/$REPO/main/calendars/Feed-US-BEA-Official.ics"
echo "  https://raw.githubusercontent.com/$USER/$REPO/main/calendars/Feed-US-FOMC.ics"
echo "  https://raw.githubusercontent.com/$USER/$REPO/main/calendars/Feed-EU-ECB.ics"
echo "  https://raw.githubusercontent.com/$USER/$REPO/main/calendars/Feed-US-Macro-Combined.ics"
echo ""
echo "Refresh loop: ask Claude to update calendars/, then: git add -A && git commit -m refresh && git push"
