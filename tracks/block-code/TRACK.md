# Track: block-code

For courses taught in block environments — Scratch, MIT App Inventor, micro:bit MakeCode. Extends `CONVENTION.md`.

## `assets/`
- Project files live here: `.sb3`, `.aia`, `.hex`. One starter per lesson, prefixed `starter_`.
  Finished reference projects are prefixed `solution_` and are referenced only from `solutions.md`.
- Every build step that places or changes blocks has a screenshot: `step-NN-<what>.png`. Students can't
  read block code from prose; the screenshot *is* the code.
- A screenshot of the finished stage or screen: `finished.png`.
- No `code/` folder in this track.

## How the standard phases run in this track
The six §5 phases are fixed in `CONVENTION.md`. What is track-specific is how two of them are run:
- **Predict → Observe → Explain** — show a small script as a screenshot and ask what the sprite will *do*,
  then run it. Prediction here is about behaviour, not printed output.
- **Build** — the step screenshots (`step-NN-*.png`) belong to this one phase; name them in the row rather
  than giving each step a row. A *remix* — change one thing, predict the effect, try it — belongs at the
  end of Build.

## What a practice project looks like here
An addition to the lesson's project, not a new one from scratch — rebuilding the maze costs twenty
minutes of nothing. Good stretches in this track: a second sprite with its own loop, something the
project has to *remember* between frames, or three deliberately broken copies to predict and diagnose.
No new screenshots needed; a fast student can find blocks without them.

## What belongs on the concepts page
Screenshots that illustrate the **idea**, not the build — a two-block script showing what fits in the
hexagon slot, or the same check inside and outside a `forever` loop side by side. Step screenshots
(`step-NN-*.png`) belong to the plan's §5, not here. Students cannot read block stacks from prose, so a
concepts page in this track is mostly pictures with a paragraph each. ASCII sketches of block structure
work well where a screenshot would date quickly.

## Prediction in blocks
"Predict the Output" still applies: show a small script as a screenshot, ask what the sprite will do,
then run. An assessment's `predict` questions use `code_ref` pointing at a screenshot in a lesson's `assets/`.

## Don't
- Don't describe a block stack in prose when a screenshot would do.
- Don't give a Build Step without saying *why* this block, in one line.
