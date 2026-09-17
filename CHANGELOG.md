# Changelog

## 0.2 — what the view needs
Additive only. `convention:` stays **1**, no existing course breaks, no migration script: a course
written against 0.1 validates unchanged, and `sync-kit.sh` alone makes the new fields available.

**Five optional `lesson.yaml` fields.** `outcomes` (2–4 lines, written to the student, not plan §4
with the prefix stripped) · `project` (the named thing built in class — `name`, `brief`, and a
`starter` path that must exist) · `resources` (student-facing links; `label` and an http(s) `url`) ·
`interactive` (declared exercises) · and `thinking_skills`, see below. The validator enforces what is
required-when-present, and warns when `outcomes` falls outside 2–4.

**An optional per-lesson `check.yaml` — and it is never marked.** One to three questions the view
offers a student between sessions, weighted to `predict` and `short`. The state store may record that
it was attempted and nothing more; the three assessments in §6 remain the only marked instrument,
for the reason `pedagogy.md` gives. Reaching for `kind`, `covers` or `after` is an error, because
that is how a self-check quietly becomes an assessment.

**An optional `interactive/` folder, under a sandbox contract.** One exercise is one self-contained
`.html` file: inline CSS and JS, no network of any kind, embedded by the view in
`<iframe sandbox="allow-scripts">`. The validator names the line when it finds an external script,
stylesheet, `@import`, cross-origin `fetch`, `XMLHttpRequest` or remote iframe. Completion is
signalled by `postMessage` and stored by the view, never in the repo.

**Notebooks in `code/` on the text-code track.** `notebook_*.ipynb`, runnable top-to-bottom in Colab
with no local setup, committed with outputs cleared. The validator checks both.

**`thinking_skills` now applies to every track.** The five-id vocabulary moved from
`tracks/ai-fluency/TRACK.md` into `CONVENTION.md` §4; that TRACK.md keeps only which skills carry the
weight in that track. The id check no longer looks at `track`.

## 0.1 — initial
Unreleased. The kit changes freely until the first course is built on it; there are no legacy
paths and no migration scripts.

- Core convention, pedagogy, curriculum template, CLAUDE.md
- Validator (MUST rules as errors, SHOULD rules as warnings)
- Tracks: text-code, block-code, ai-fluency, each with a fully written model lesson
- `new-course.sh`, `sync-kit.sh`

**A lesson is two documents.** `lesson-plan.md` is teacher-only and owns the whole class flow, on a
fixed spine of eight numbered sections. `concepts.md` is the student's textbook page for the idea —
no timings, no steps. Plus `homework.md`, `practice.md`, and optional `solutions.md`.

**Six standard phases**, the same in every lesson of every track: Recap · New concept ·
Predict → Observe → Explain · Build · Reflection · Homework brief (8 · 10 · 12 · 20 · 5 · 5 min).
They live in the plan's §5 table — `Phase | Min | What happens | Purpose` — under a bolded line
naming what to protect when the hour runs short. A second predict, a remix or a deliberate break
goes at the end of Build rather than becoming a phase of its own. No track-specific headings: what
would have been one is a way of running one of the six.

**`practice.md` in every lesson** — two or three projects for the student who finishes early, each
with a **The stretch** line and a **Done when** line. The plan's §6 names the one to reach for first.

**Assessments are course-level**, not per-lesson: three in `assessments/` — two formative
(10 questions, 15 min, run in a Recap slot, diagnostic) and one summative (20 questions, 45 min, its
own session). Each pairs with a teacher-only `<stem>-solutions.md` of marking notes.

**`curriculum.md` is the single source for everything written about the course.** It carries the
session map (`# · Session · Focus · Ships`, grouped into blocks that are the course's tiers) and a
per-session detail block, so a spine can be reviewed before any lesson is generated. Sections down to
`## Questions parents ask` are parent-safe; every parent-facing view — the course front page,
brochure copy for a designer — is rendered from them on request. There is no second document.

**Kit files live in `.kit/` inside a course**, not at the root — convention, pedagogy, track rules,
the model lesson and the scripts. A course root is `course.yaml`, `curriculum.md`, `assessments/`,
the lesson folders and `CLAUDE.md`, which stays put because Claude Code reads it from there.

**`thinking_skills`** — the five-id vocabulary, introduced on the ai-fluency track and living in that
track's `TRACK.md`. (0.2 widens it to every track and moves the table into `CONVENTION.md` §4.)
