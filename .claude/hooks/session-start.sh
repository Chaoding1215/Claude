#!/bin/bash
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

# Restore ~/.claude/skills (SKILL.md files) from repo
SKILLS_SRC="${CLAUDE_PROJECT_DIR}/.claude/skills"
SKILLS_DST="$HOME/.claude/skills"

if [ -d "$SKILLS_SRC" ]; then
  mkdir -p "$SKILLS_DST"
  cp -r "$SKILLS_SRC"/. "$SKILLS_DST/"
  echo "Skills restored from repo."
fi

# Install the full last30days engine (scripts/) if the Python engine is missing
ENGINE="$HOME/.claude/skills/last30days/scripts/last30days.py"
if [ ! -f "$ENGINE" ]; then
  echo "last30days engine not found — downloading from GitHub..."
  TMP_TAR=$(mktemp)
  TMP_DIR=$(mktemp -d)
  if curl -fsSL -o "$TMP_TAR" \
      "https://codeload.github.com/mvanhorn/last30days-skill/tar.gz/refs/heads/main"; then
    tar -xzf "$TMP_TAR" -C "$TMP_DIR" 2>/dev/null
    EXTRACTED=$(find "$TMP_DIR" -maxdepth 1 -type d -name "last30days-skill-*" | head -1)
    if [ -n "$EXTRACTED" ] && [ -d "$EXTRACTED/skills/last30days/scripts" ]; then
      cp -r "$EXTRACTED/skills/last30days/scripts" "$HOME/.claude/skills/last30days/"
      echo "last30days engine installed successfully."
    else
      echo "WARNING: could not find scripts/ in tarball — engine not installed."
    fi
  else
    echo "WARNING: failed to download last30days engine. Run: npx skills add mvanhorn/last30days-skill -g"
  fi
  rm -f "$TMP_TAR"
  rm -rf "$TMP_DIR"
else
  echo "last30days engine already present."
fi

# Install the full ppt-master engine if the core script is missing
PPT_ENGINE="$HOME/.claude/skills/ppt-master/scripts/project_manager.py"
if [ ! -f "$PPT_ENGINE" ]; then
  echo "ppt-master engine not found — downloading from GitHub..."
  TMP_TAR=$(mktemp)
  TMP_DIR=$(mktemp -d)
  if curl -fsSL -o "$TMP_TAR" \
      "https://codeload.github.com/hugohe3/ppt-master/tar.gz/refs/heads/main"; then
    tar -xzf "$TMP_TAR" -C "$TMP_DIR" 2>/dev/null
    EXTRACTED=$(find "$TMP_DIR" -maxdepth 1 -type d -name "ppt-master-*" | head -1)
    if [ -n "$EXTRACTED" ]; then
      for dir in scripts templates references workflows requirements.txt; do
        if [ -e "$EXTRACTED/$dir" ]; then
          cp -r "$EXTRACTED/$dir" "$HOME/.claude/skills/ppt-master/"
        fi
      done
      echo "ppt-master engine installed successfully."
    else
      echo "WARNING: could not find ppt-master content in tarball — engine not installed."
    fi
  else
    echo "WARNING: failed to download ppt-master engine."
  fi
  rm -f "$TMP_TAR"
  rm -rf "$TMP_DIR"
else
  echo "ppt-master engine already present."
fi
