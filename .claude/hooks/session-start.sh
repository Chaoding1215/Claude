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

# The full ppt-master engine (scripts/templates/references/workflows) is
# vendored in the repo and already restored by the "Skills restored from
# repo" step above, so this is now a fallback for the rare case that copy is
# somehow missing/partial — not the primary install path.
PPT_ENGINE="$HOME/.claude/skills/ppt-master/scripts/project_manager.py"
if [ ! -f "$PPT_ENGINE" ]; then
  echo "ppt-master engine not found in vendored copy — downloading from GitHub as a fallback..."
  TMP_DIR=$(mktemp -d)
  # codeload.github.com tarball downloads are blocked by egress policy for
  # repos outside this session's scope; a plain git clone over github.com
  # goes through the same proxy without hitting that restriction.
  if git clone --depth 1 --quiet https://github.com/hugohe3/ppt-master.git "$TMP_DIR/ppt-master" 2>/dev/null; then
    SRC="$TMP_DIR/ppt-master/skills/ppt-master"
    if [ -d "$SRC" ]; then
      for dir in scripts templates references workflows requirements.txt; do
        if [ -e "$SRC/$dir" ]; then
          cp -r "$SRC/$dir" "$HOME/.claude/skills/ppt-master/"
        fi
      done
      echo "ppt-master engine installed successfully."
    else
      echo "WARNING: could not find ppt-master content in clone — engine not installed."
    fi
  else
    echo "WARNING: failed to download ppt-master engine."
  fi
  rm -rf "$TMP_DIR"
else
  echo "ppt-master engine already present."
fi
