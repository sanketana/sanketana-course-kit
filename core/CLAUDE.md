# CLAUDE.md

This repository is a **Sanketana School of Code course**. Content only — never student state.

## Before writing anything
Read, in this order:
1. `CONVENTION.md` — structural rules. MUST rules are non-negotiable.
2. `TRACK.md` — rules for this course's track.
3. `pedagogy.md` — what a Sanketana lesson is, how we teach, the voice.
4. `curriculum.md` — the baselined spine. Lessons follow it. If writing a lesson reveals a
   problem with the spine, **stop and say so**; do not silently diverge.
5. `_template/` — the model lesson. Copy its structure and depth. Do not copy its content.

## Working rules
- New lesson: copy `_template/` to `lesson-NN-<slug>/`, set `lesson.yaml: id` to the id from
  `curriculum.md`, add the id to `course.yaml: lessons` if missing.
- Write `lesson-plan.md` first — the eight numbered sections are fixed and all required — then
  `concepts.md`, then `homework.md`, then `practice.md`.
- `practice.md` is required in every lesson: two or three projects, each harder than the classwork,
  each with a **The stretch** line and a **Done when** line. Name the first-choice project in the
  plan's §6.
- Assessments are course-level, not per-lesson: three files in `assessments/`, written once the
  lessons they cover exist. Never add a `quiz.yaml` to a lesson folder.
- `lesson-plan.md` is the only place the class flow lives; its §5 table is the whole hour.
  `concepts.md` is a textbook page about the idea — written to the student, no timings, no steps.
  If a sentence only makes sense during the lesson it belongs in the plan; if it still makes sense a
  year later it belongs in `concepts.md`.
- Never renumber or rename existing lesson folders, code files, or asset files.
- Keep `lesson-plan.md` and `solutions.md` strictly teacher-facing. Nothing student-facing may even
  name them — the validator errors on it.
- There is no separate parent-facing file. Anything written for a parent — the course's front page,
  brochure copy for a designer — is rendered on request from `curriculum.md`'s parent-safe sections
  (Promise through Questions parents ask). Draw only on facts already in `curriculum.md` or
  `course.yaml`; never invent a claim, a fee or an outcome. If a parent-facing view needs a fact the
  spine doesn't hold, add it to `curriculum.md` first.
- After any change, run `python3 scripts/validate.py` and fix every error before finishing.
  Warnings: fix if quick, otherwise list them in your final message.
- Don't edit `_template/`, `CONVENTION.md`, `TRACK.md`, or `pedagogy.md` here.
  Kit improvements go in `_drafts/KIT-TODO.md` for the kit repo.

## Course-specific context
<!-- Fill in when the course is created. Keep it short. -->
- Audience:
- Comes from:
- Tools:
- Anything opinionated about this course:
