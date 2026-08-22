# Track: text-code

For courses taught in a text language — Python, Java, JavaScript. Extends `CONVENTION.md`.

## `code/`
- Every file in `code/` is runnable as-is with the course's declared tool. No fragments.
- One program per file. Naming follows the language: `snake_case.py`, `PascalCase.java`, `camelCase.js`.
- Files the student should run *before* being told what happens are prefixed `predict_` (e.g. `predict_decisions.py`,
  `PredictDecisions.java`). The matching `quiz.yaml` `predict` question references them.
- Starter files the student completes are prefixed `starter_`. Finished reference versions live in `solutions.md`
  as code blocks, never in `code/` (students can browse `code/`).
- A 3–5 line header comment at the top of each file: what it shows, and the one line to look at.

## Extra H2 headings (classwork.md)
- `Bug Hunt` — a deliberately broken program; the student finds and explains the bug.

Optional. `Predict the Output` (core) should appear in most lessons.

## Lesson shape that works
Recap and bridge (5–8 min) → Predict the Output on the new idea (10–15 min) → build in `starter_` file (20–25 min)
→ Bug Hunt or second predict (5 min) → Reflection and Key Takeaways (5 min).

## Don't
- Don't paste more than ~25 lines of code into classwork.md at once; put it in `code/` and reference it.
- Don't show the fix before the student has predicted the bug.
