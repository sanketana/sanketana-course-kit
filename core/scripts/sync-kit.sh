#!/usr/bin/env bash
# Pull the latest kit files into this course repo.
#
# ALWAYS run from the course repo root — the course is the current directory,
# never an argument. The only argument is where to copy FROM.
#
#   from the kit:     bash /path/to/sanketana-course-kit/core/scripts/sync-kit.sh
#   from the course:  ./.kit/scripts/sync-kit.sh /path/to/sanketana-course-kit
#
# Invoked from inside the kit it works out the kit path itself. The copy that ends up
# in .kit/scripts/ can't — it lives in the course — so that one needs the argument.
set -euo pipefail

[[ -f course.yaml ]] || {
  echo "No course.yaml here. Run this from the root of the COURSE repo you want to update,"
  echo "not from the kit. The course is the current directory; the argument is the kit."
  exit 1
}

KIT="${1:-}"
if [[ -z "$KIT" ]]; then
  GUESS="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." 2>/dev/null && pwd)" || GUESS=""
  [[ -n "$GUESS" && -f "$GUESS/core/CONVENTION.md" ]] && KIT="$GUESS"
fi
[[ -n "$KIT" ]] || {
  echo "Can't tell where the kit is. Pass it:"
  echo "  ./.kit/scripts/sync-kit.sh /path/to/sanketana-course-kit"
  exit 1
}
[[ -f "$KIT/core/CONVENTION.md" ]] || { echo "Not a course kit: $KIT"; exit 1; }
TRACK="$(grep -m1 -E '^track:' course.yaml | awk '{print $2}')"
KIT_VERSION="$(grep -m1 -oE '^## [0-9.]+' "$KIT/CHANGELOG.md" | sed 's/## //')"

mkdir -p .kit/scripts
cp "$KIT/core/CONVENTION.md" "$KIT/core/pedagogy.md" .kit/
cp "$KIT/core/scripts/validate.py" "$KIT/core/scripts/sync-kit.sh" .kit/scripts/
mkdir -p .github/workflows && cp "$KIT/core/.github-workflow-validate.yml" .github/workflows/validate.yml
cp "$KIT/tracks/$TRACK/TRACK.md" .kit/
rm -rf .kit/_template && cp -r "$KIT/tracks/$TRACK/_template" .kit/_template
# CLAUDE.md is half kit, half course. Everything above `## Course-specific context` is the
# kit's and gets replaced; that heading and everything below it is the course's and is kept.
mkdir -p _drafts
MARK="## Course-specific context"
if [[ ! -f CLAUDE.md ]]; then
  cp "$KIT/core/CLAUDE.md" CLAUDE.md
  echo "CLAUDE.md: created from the kit — fill in the Course-specific context section."
elif grep -qxF "$MARK" CLAUDE.md && grep -qxF "$MARK" "$KIT/core/CLAUDE.md"; then
  awk -v m="$MARK" '$0==m{exit} {print}' "$KIT/core/CLAUDE.md"  > CLAUDE.md.new
  awk -v m="$MARK" '$0==m{f=1} f{print}'  CLAUDE.md            >> CLAUDE.md.new
  if cmp -s CLAUDE.md CLAUDE.md.new; then rm -f CLAUDE.md.new
  else mv CLAUDE.md.new CLAUDE.md; echo "CLAUDE.md: kit rules updated, your Course-specific context kept."; fi
else
  diff -u CLAUDE.md "$KIT/core/CLAUDE.md" > _drafts/CLAUDE.md.kit-diff || true
  echo "CLAUDE.md: no \"$MARK\" heading, so left untouched. Merge _drafts/CLAUDE.md.kit-diff by hand."
fi
sed -i.bak -E "s/^kit_version:.*/kit_version: \"$KIT_VERSION\"/" course.yaml && rm -f course.yaml.bak

echo "Synced kit $KIT_VERSION (track $TRACK)."
echo "Now run: python3 .kit/scripts/validate.py"
