# Track: block-code

For courses taught in block environments — Scratch, MIT App Inventor, micro:bit MakeCode. Extends `CONVENTION.md`.

## `assets/`
- Project files live here: `.sb3`, `.aia`, `.hex`. One starter per lesson, prefixed `starter_`.
  Finished reference projects are prefixed `solution_` and are referenced only from `solutions.md`.
- Every build step that places or changes blocks has a screenshot: `step-NN-<what>.png`. Students can't
  read block code from prose; the screenshot *is* the code.
- A screenshot of the finished stage or screen: `finished.png`.
- No `code/` folder in this track.

## Extra H2 headings (classwork.md)
- `Build Steps` — numbered H3s, each with a screenshot and one sentence of intent. Replaces a long `In Class` build.
- `Remix Challenge` — change one thing and predict the effect before trying it. This is POE for blocks.

## Prediction in blocks
"Predict the Output" still applies: show a small script as a screenshot, ask what the sprite will do,
then run. `quiz.yaml` `predict` questions use `code_ref` pointing at a screenshot in `assets/`.

## Lesson shape that works
Recap by showing last week's project (5 min) → predict on a tiny script (10 min) → Build Steps (25–30 min)
→ Remix Challenge (10 min) → Reflection (5 min).

## Don't
- Don't describe a block stack in prose when a screenshot would do.
- Don't give a Build Step without saying *why* this block, in one line.
