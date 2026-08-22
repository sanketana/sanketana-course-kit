# Track: ai-fluency

For courses about working *with* AI tools — AI Fluency Lab, GenAI Foundations — where the artifact is often a
prompt, a judgment, or a small tool rather than a program. Extends `CONVENTION.md`.

## `assets/` and `code/`
- `assets/` holds prompt logs as `.md` (`prompt-log-<topic>.md`), example AI outputs as screenshots, and any
  templates the student fills (`ethics-contract.md`).
- `code/` is allowed for courses that write code (GenAI Foundations). Rules from the text-code track apply there.
- Never commit real student conversations with AI tools. Example logs are written by us.

## Extra H2 headings (classwork.md)
- `Prompt Lab` — the student writes a prompt, predicts the output's quality, runs it, compares. POE for prompts.
- `Tool Judgment` — two or three candidate AI outputs; the student ranks them against a stated standard and says why.
- `Ethics Check` — one concrete situation from the lesson's build; who is affected, what would you change.

`Ethics Check` is optional per lesson; `Tool Judgment` should appear in most lessons — it is where
critical-evaluation and selective-judgment live.

## Prediction in this track
Prediction is about *quality*, not output. "Before running, say what this prompt will get wrong." `quiz.yaml`
`predict` questions reference a prompt file in `assets/`.

## Lesson shape that works
Recap (5 min) → Prompt Lab on the new idea (15 min) → build or refine a tool (20 min) → Tool Judgment (10 min)
→ Ethics Check or Reflection (10 min).

## Don't
- Don't present an AI output as correct without the student having judged it first.
- Don't use "AI-powered" or "unlock" anywhere. See pedagogy.md.
- Don't let the lesson become a tool tour. One idea, exercised hard.
