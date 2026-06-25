#!/bin/bash
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

# Restore ~/.claude/skills from repo
SKILLS_SRC="${CLAUDE_PROJECT_DIR}/.claude/skills"
SKILLS_DST="$HOME/.claude/skills"

if [ -d "$SKILLS_SRC" ]; then
  mkdir -p "$SKILLS_DST"
  cp -r "$SKILLS_SRC"/. "$SKILLS_DST/"
  echo "Skills restored from repo."
fi
