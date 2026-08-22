# Changelog

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

**`thinking_skills` is ai-fluency only.** The vocabulary lives in that track's `TRACK.md`; the
validator checks it there and warns if it appears elsewhere.
