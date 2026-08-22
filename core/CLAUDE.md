# CLAUDE.md

This repository is a **Sanketana School of Code course**. Content only — never student state.

## Before writing anything
Read, in this order:
1. `CONVENTION.md` — structural rules. MUST rules are non-negotiable.
2. `TRACK.md` — rules for this course's track.
3. `pedagogy.md` — what a Sanketana lesson is, the thinking skills, the voice.
4. `curriculum.md` — the baselined spine. Lessons follow it. If writing a lesson reveals a
   problem with the spine, **stop and say so**; do not silently diverge.
5. `_template/` — the model lesson. Copy its structure and depth. Do not copy its content.

## Working rules
- New lesson: copy `_template/` to `lesson-NN-<slug>/`, set `lesson.yaml: id` to the id from
  `curriculum.md`, add the id to `course.yaml: lessons` if missing.
- Never renumber or rename existing lesson folders, code files, or asset files.
- Keep `solutions.md` and `teacher-notes.md` strictly teacher-facing. Nothing student-facing refers to them.
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
