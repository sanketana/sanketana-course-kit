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

# Kit files live in .kit/ so the course root shows only what a teacher or author needs.
# CLAUDE.md is the exception: Claude Code reads it from the root and nowhere else.
mkdir -p "$DEST/.kit/scripts" "$DEST/_drafts" "$DEST/.github/workflows" "$DEST/assessments"
cp "$KIT/core/CLAUDE.md" "$DEST/"
cp "$KIT/core/CONVENTION.md" "$KIT/core/pedagogy.md" "$DEST/.kit/"
cp "$KIT/core/scripts/validate.py" "$KIT/core/scripts/sync-kit.sh" "$DEST/.kit/scripts/"
cp "$KIT/core/.github-workflow-validate.yml" "$DEST/.github/workflows/validate.yml"
cp "$KIT/tracks/$TRACK/TRACK.md" "$DEST/.kit/"
cp -r "$KIT/tracks/$TRACK/_template" "$DEST/.kit/_template"
cp "$KIT/core/curriculum-template.md" "$DEST/curriculum.md"
echo "# KIT TODO — things to improve in sanketana-course-kit" > "$DEST/_drafts/KIT-TODO.md"

# Three assessments: two formative, one summative. Scaffolded from the kit template.
for A in formative-1:formative:10:15 formative-2:formative:10:15 summative:summative:20:45; do
  STEM="${A%%:*}"; REST="${A#*:}"; KIND="${REST%%:*}"; REST="${REST#*:}"
  NQ="${REST%%:*}"; MINS="${REST##*:}"
  cat > "$DEST/assessments/$STEM.yaml" << YAML
# $NQ questions, $MINS min. Write this once the lessons it covers exist.
# Worked examples and the full field list: CONVENTION.md §6 and the kit's assessment-template.yaml
id: $STEM
title:
kind: $KIND
after:                           # the lesson id this runs after
covers: []                       # the lesson ids it tests
duration_min: $MINS
questions: []
YAML
  cat > "$DEST/assessments/$STEM-solutions.md" << MD
# $STEM — marking notes

TEACHER-ONLY. Answers live in \`$STEM.yaml\`; this file holds what a machine can't mark —
what a short answer needs for full marks, what a wrong answer tells you, what to re-teach.
Number the sections to match the question ids.
MD
  echo "  assessments/$STEM.yaml — $NQ questions, $MINS min (stub)"
done

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


cat > "$DEST/.gitignore" << GI
_drafts/
__pycache__/
.DS_Store
GI

cd "$DEST" && git init -q && git add -A && git commit -qm "Scaffold from sanketana-course-kit $KIT_VERSION ($TRACK)"
echo "Created $DEST from kit $KIT_VERSION, track $TRACK."
echo "Next: fill course.yaml, replace curriculum.md with your baselined spine, then: git tag spine-v1"
echo "Kit files (convention, pedagogy, track rules, model lesson, scripts) are in .kit/"
echo "Validate with: python3 .kit/scripts/validate.py"
