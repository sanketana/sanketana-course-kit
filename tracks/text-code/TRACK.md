# Track: text-code

For courses taught in a text language — Python, Java, JavaScript. Extends `CONVENTION.md`.

## `code/`
- Every file in `code/` is runnable as-is with the course's declared tool. No fragments.
- One program per file. Naming follows the language: `snake_case.py`, `PascalCase.java`, `camelCase.js`.
- Files the student should run *before* being told what happens are prefixed `predict_` (e.g. `predict_return.py`,
  `PredictReturn.java`). An assessment's `predict` question references them by path from the repo root.
- Starter files the student completes are prefixed `starter_`. Finished reference versions live in `solutions.md`
  as code blocks, never in `code/` (students can browse `code/`).
- A 3–5 line header comment at the top of each file: what it shows, and the one line to look at.

## How the standard phases run in this track
The six §5 phases are fixed in `CONVENTION.md`. What is track-specific is how two of them are run:
- **Predict → Observe → Explain** — a `predict_` file the student reads and writes the output of before
  running. A *bug hunt* is the same phase pointed at a deliberately broken program: predict the error,
  run it, read the message. Use one or the other, not both as separate phases.
- **Build** — a `starter_` file completed and then tested at its boundaries. Any deliberate break belongs
  at the end of Build, not as its own row.

## What a practice project looks like here
A new program in `code/`, not an edit of the classwork file — the student should start from an empty
file often enough that it stops being frightening. Good stretches in this track: an extra branch that
changes where the others must go, a rewrite under a constraint (no `elif`, no variables), or a
specification with a trap in it. Reference solutions go in `solutions.md`, never in `code/`.

## What belongs on the concepts page
Code blocks, freely — but each one making a single point, not a program to copy. Show the wrong version
next to the right one under `Common Mistakes`, and say what the error message actually means; a beginner
cannot read `SyntaxError: invalid syntax` without help. `Vocabulary` should give the words for things
students point at rather than name (block, branch, argument, boundary).

## Don't
- Don't paste more than ~25 lines of code into `concepts.md` at once; put it in `code/` and reference it.
- Don't show the fix before the student has predicted the bug.
- Don't assume the student came from a block environment. Some did; most courses can't rely on it.
