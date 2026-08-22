#!/usr/bin/env bash
# Pull the latest kit files into this course repo. Run from the course repo root.
# Usage: ./scripts/sync-kit.sh /path/to/sanketana-course-kit
set -euo pipefail
KIT="${1:?path to sanketana-course-kit required}"
[[ -f course.yaml ]] || { echo "run from a course repo root"; exit 1; }
TRACK="$(grep -m1 -E '^track:' course.yaml | awk '{print $2}')"
KIT_VERSION="$(grep -m1 -oE '^## [0-9.]+' "$KIT/CHANGELOG.md" | sed 's/## //')"

cp "$KIT/core/CONVENTION.md" "$KIT/core/pedagogy.md" .
cp "$KIT/core/scripts/validate.py" "$KIT/core/scripts/sync-kit.sh" scripts/
mkdir -p .github/workflows && cp "$KIT/core/.github-workflow-validate.yml" .github/workflows/validate.yml
cp "$KIT/tracks/$TRACK/TRACK.md" .
rm -rf _template && cp -r "$KIT/tracks/$TRACK/_template" _template
# CLAUDE.md is NOT overwritten: it holds course-specific context. Diff it by hand:
diff -u CLAUDE.md "$KIT/core/CLAUDE.md" > _drafts/CLAUDE.md.kit-diff || true
sed -i.bak -E "s/^kit_version:.*/kit_version: \"$KIT_VERSION\"/" course.yaml && rm -f course.yaml.bak

echo "Synced kit $KIT_VERSION (track $TRACK). CLAUDE.md left untouched; see _drafts/CLAUDE.md.kit-diff."
echo "Now run: python3 scripts/validate.py"
