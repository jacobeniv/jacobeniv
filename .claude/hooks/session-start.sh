#!/bin/bash
# Sets up the website-rebuilder skill's scripts and Python deps in cloud sessions.
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

REPO_URL="https://github.com/pantheonmarketing/claude-website-rebuilder.git"
# Pinned to the commit the vendored .claude/skills/website-rebuilder/SKILL.md came from.
REPO_REF="f8e1888"
TOOL_DIR="$(dirname "$CLAUDE_PROJECT_DIR")/claude-website-rebuilder"

if [ ! -d "$TOOL_DIR/.git" ]; then
  git clone --quiet "$REPO_URL" "$TOOL_DIR" >&2
fi
git -C "$TOOL_DIR" checkout --quiet "$REPO_REF" >&2

# Match Python Playwright to the preinstalled Node Playwright so it finds the
# bundled Chromium instead of needing `playwright install chromium`.
PW_VERSION="$(node -e "console.log(require('playwright/package.json').version)" 2>/dev/null || true)"
if [ -n "$PW_VERSION" ]; then
  pip install --quiet --root-user-action=ignore "playwright==$PW_VERSION" pillow >&2
else
  pip install --quiet --root-user-action=ignore playwright pillow >&2
  python3 -m playwright install chromium >&2
fi

echo "export WEBSITE_REBUILDER_DIR=\"$TOOL_DIR\"" >> "$CLAUDE_ENV_FILE"
echo "website-rebuilder scripts are at $TOOL_DIR (\$WEBSITE_REBUILDER_DIR); run its scripts/ commands from that folder."
