#!/bin/bash
# Registers the REA MCP server and skill for Claude Code in cloud sessions,
# whose containers start without the user-level config from earlier sessions.
# Also installs Ghidra so REA has an analysis engine.
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

GHIDRA_VERSION=12.1.4
GHIDRA_BUILD_DATE=20260921
GHIDRA_SHA256=ddac49f903da9d5bac833e5cc79395098b9c33cfd3279be5f31bd00387d2d4db
export GHIDRA_INSTALL_DIR="/opt/ghidra_${GHIDRA_VERSION}_PUBLIC"

if [ ! -x "$GHIDRA_INSTALL_DIR/support/analyzeHeadless" ]; then
  zip="$(mktemp --suffix=.zip)"
  curl -sSfL --retry 3 -o "$zip" \
    "https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_${GHIDRA_VERSION}_build/ghidra_${GHIDRA_VERSION}_PUBLIC_${GHIDRA_BUILD_DATE}.zip"
  echo "$GHIDRA_SHA256  $zip" | sha256sum -c --quiet
  unzip -q "$zip" -d /opt
  rm -f "$zip"
fi

npx --yes rea-agents@6.7.0 setup --client claude_code --yes < /dev/null > /dev/null
