#!/usr/bin/env bash
# Create a new Sanketana course repo from the kit.
# Usage: ./core/scripts/new-course.sh <course-slug> <track> [parent-dir]
#   track: text-code | block-code | ai-fluency
set -euo pipefail

SLUG="${1:?course slug required, e.g. python-foundations}"
TRACK="${2:?track required: text-code | block-code | ai-fluency}"
PARENT="${3:-.}"
KIT="$(cd "$(dirname "$0")/../.." && pwd)"
KIT_VERSION="$(grep -m1 -oE '^## [0-9.]+' "$KIT/CHANGELOG.md" | sed 's/## //')"

[[ -d "$KIT/tracks/$TRACK" ]] || { echo "unknown track: $TRACK"; exit 1; }
DEST="$PARENT/$SLUG"
[[ -e "$DEST" ]] && { echo "$DEST already exists"; exit 1; }

mkdir -p "$DEST/scripts" "$DEST/_drafts" "$DEST/.github/workflows"
cp "$KIT/core/CONVENTION.md" "$KIT/core/pedagogy.md" "$KIT/core/CLAUDE.md" "$DEST/"
cp "$KIT/core/scripts/validate.py" "$KIT/core/scripts/sync-kit.sh" "$DEST/scripts/"
cp "$KIT/core/.github-workflow-validate.yml" "$DEST/.github/workflows/validate.yml"
cp "$KIT/tracks/$TRACK/TRACK.md" "$DEST/"
cp -r "$KIT/tracks/$TRACK/_template" "$DEST/_template"
cp "$KIT/core/curriculum-template.md" "$DEST/curriculum.md"
echo "# KIT TODO — things to improve in sanketana-course-kit" > "$DEST/_drafts/KIT-TODO.md"

TITLE="$(echo "$SLUG" | sed -E 's/-/ /g; s/\b(.)/\u\1/g')"
cat > "$DEST/course.yaml" << YAML
convention: 1
kit_version: "$KIT_VERSION"
track: $TRACK
language:
id: $SLUG
title: $TITLE
subtitle:
audience:
  age_min:
  age_max:
  prerequisites:
format:
  sessions: 24
  session_min: 60
  mode: "1:1 live"
tools: []
tiers: []
lessons: []
YAML

cat > "$DEST/overview.md" << MD
# $TITLE

<!-- Parent-facing. What the student builds, what changes in how they think, who it's for. -->
MD

cat > "$DEST/.gitignore" << GI
_drafts/
__pycache__/
.DS_Store
GI

cd "$DEST" && git init -q && git add -A && git commit -qm "Scaffold from sanketana-course-kit $KIT_VERSION ($TRACK)"
echo "Created $DEST from kit $KIT_VERSION, track $TRACK."
echo "Next: fill course.yaml, replace curriculum.md with your baselined spine, then: git tag spine-v1"
