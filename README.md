# Sanketana Course Kit

The shared scaffolding every Sanketana School of Code course repo is built from.
One kit, many courses. Courses are **content only** — student state never lives in git.

**Kit version: 0.1** (pre-1.0: expected to change while the first course is built on it)

## What's in here

```
core/                      identical in every course, evolves in lockstep
  CONVENTION.md            the rules: layout, ids, YAML shapes, heading allowlist
  pedagogy.md              what a Sanketana course is — read by humans and Claude
  curriculum-template.md   the shape of a course spine (curriculum.md)

  CLAUDE.md                standing instructions for Claude Code in a course repo
  scripts/validate.py      enforces the MUST rules; warns on the SHOULD rules
  scripts/new-course.sh    creates a new course repo from this kit
  scripts/sync-kit.sh      pulls kit updates into an existing course repo
  assessment-template.yaml           shape of the three course assessments
  assessment-solutions-template.md   shape of a teacher-only marking file
tracks/                    one per lesson *shape*, not per language
  text-code/               Python, Java, JS — runnable code files, predict-the-output
  block-code/              Scratch, App Inventor — project files + screenshots
  ai-fluency/              prompt labs, tool judgment, ethics checks
  <track>/TRACK.md         track-specific rules and extra headings
  <track>/_template/       one fully-written model lesson — lesson-plan.md + concepts.md
CHANGELOG.md               what changed in each kit version
```

## Workflow

### 1. Think out the spine (Claude Desktop)
Start a Desktop chat. Give it `core/pedagogy.md` and `core/curriculum-template.md`
plus your own brief (who it's for, what they build, how many sessions).
Argue it out. End with a `curriculum.md` in the template's shape.

`curriculum.md` is the **single source for everything written about the course**. Its parent-safe
sections — Promise, Who this is for, Tiers, Capstone, the session table, What a parent sees,
Questions parents ask — are what every parent-facing view is rendered from: the course's front page,
and brochure copy for a designer. Those are outputs, produced when needed; there is no second
document to keep in sync. If a parent-facing view needs a fact, add a field to the spine.

### 2. Create the course repo
```bash
./core/scripts/new-course.sh python-foundations text-code ~/Documents/Sanketana/courses
cd ~/Documents/Sanketana/courses/python-foundations
cp ~/path/to/curriculum.md .
git add -A && git commit -m "Spine v1" && git tag spine-v1
```
`new-course.sh` writes a starter `course.yaml` and puts everything shared with other
courses into a hidden `.kit/` — convention, pedagogy, track rules, the model lesson and
the scripts. The course root stays as `course.yaml`, `curriculum.md`, `assessments/`,
the lesson folders and `CLAUDE.md`, so a teacher opening the repo sees only real content.

### 3. Generate content (Claude Code)
Open the course repo in Claude Code. It reads `CLAUDE.md` automatically, which
points it at `.kit/CONVENTION.md`, `.kit/TRACK.md`, `.kit/pedagogy.md`, `curriculum.md`,
and `.kit/_template/`.

Suggested first prompts:
- "Derive `course.yaml` lessons/tiers and a `lesson.yaml` for every lesson from `curriculum.md`. Run validate.py."
- "Using `.kit/_template/` as the model, write lessons l01–l04. Run validate.py and fix errors."
- Review each batch as a git diff. Push back on voice and depth; structure is handled.

### 4. Revising the spine
- Mechanical changes (split, swap, move) → do in Claude Code, commit, `git tag spine-v2`.
- Judgment changes → fresh Desktop chat with current `curriculum.md` + the lessons that triggered it.
- Ask Claude Code: "lessons 1–9 were written against spine-v1; diff against spine-v2 and list affected lessons before changing anything."

### 5. Improving the kit
Change the kit **in the kit repo**, never only inside a course. Then:
```bash
cd <course-repo>                      # the course is the current directory, never an argument
bash ~/path/to/sanketana-course-kit/core/scripts/sync-kit.sh
```
Mid-lesson niggles go in the course's `_drafts/KIT-TODO.md`; clear them in batches.
Don't tag `kit-v1.0` until the first course validates clean end to end. Until then the kit is
unreleased and can change freely — no migration scripts, no legacy paths.

## Validation
```bash
python3 .kit/scripts/validate.py            # from inside a course repo
python3 .kit/scripts/validate.py --strict   # treat warnings as errors
```
Requires `pip install pyyaml`. Claude Code runs this itself; GitHub Actions runs it as backstop
(see `core/.github-workflow-validate.yml` — copy to `.github/workflows/validate.yml` in a course).

## Core vs track — the test
*Would a web app render it differently?* If no, it's core. Folder names, ids, ordering,
audience-by-filename, `lesson.yaml` fields, the assessment schema and the three-assessment rule, the
eight-section `lesson-plan.md` spine, the `concepts.md` heading list — core. What `code/` or `assets/` contains, which phases show up in the plan's
§5 table, what a concepts page looks like in that track — track.

## Adding things later
- New optional file, folder, field or heading → add to kit, bump minor version, sync. Nothing breaks.
- Renaming, removing, or making something required → bump `convention`, write a migration, upgrade courses one at a time.
- A new track only when the *shape* of a lesson is different. Python vs Java is not a new track.
