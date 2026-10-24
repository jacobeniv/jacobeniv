#!/bin/bash
# Registers the REA MCP server and skill for Claude Code in cloud sessions,
# whose containers start without the user-level config from earlier sessions.
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

npx --yes rea-agents@6.7.0 setup --client claude_code --yes < /dev/null > /dev/null
