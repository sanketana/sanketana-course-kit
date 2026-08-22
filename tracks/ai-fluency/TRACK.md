# Track: ai-fluency

For courses about working *with* AI tools — AI Fluency Lab, GenAI Foundations — where the artifact is often a
prompt, a judgment, or a small tool rather than a program. Extends `CONVENTION.md`.

## `assets/` and `code/`
- `assets/` holds prompt logs as `.md` (`prompt-log-<topic>.md`), example AI outputs as screenshots, and any
  templates the student fills (`ethics-contract.md`).
- `code/` is allowed for courses that write code (GenAI Foundations). Rules from the text-code track apply there.
- Never commit real student conversations with AI tools. Example logs are written by us.

## How the standard phases run in this track
The six §5 phases are fixed in `CONVENTION.md`. What is track-specific is how three of them are run:
- **Predict → Observe → Explain** — a *prompt lab*: the student writes a prompt, predicts what it will get
  wrong, sends it, compares. Prediction here is about *quality*, not output.
- **Build** — usually a *tool judgment*: two or three candidate outputs ranked against a standard the
  student wrote down first, each placing justified in a sentence. This should appear in most lessons; it is
  where critical-evaluation and selective-judgment live.
- **Reflection** — carries the *ethics check* where the lesson has one: a concrete situation from today's
  work, who is affected, what would you change. Optional per lesson, not a phase of its own.

## What a practice project looks like here
Something the student actually wants an answer to, judged against a standard they wrote — the habit only
transfers if it leaves the worked example. Good stretches in this track: the same prompt across two
tools, reverse-engineering a bad output, or sharpening a standard that turned out to be too easy to meet.
Never ask a student to paste a real conversation into the repo.

## What belongs on the concepts page
Real prompts and real outputs, quoted — the difference between a vague prompt and a specific one has to be
*shown*, not described. Include an output that is polished and wrong, and say what makes it wrong. Never
quote a real student's conversation; write the examples yourself. `Common Mistakes` in this track is about
judgment habits (ranking by formatting, writing the standard afterwards), not syntax.

## Thinking skills (this track only)
Working *with* AI is mostly judgment, so in this track we name the judgment explicitly. `lesson.yaml` takes an
optional `thinking_skills` list; the vocabulary is fixed, and these exact ids are the only ones the validator
accepts:

| id | what it looks like in a lesson |
|---|---|
| `mental-modeling` | the student can predict what the tool will do before it does it |
| `intentional-direction` | the student decides what to build and why before touching the tool |
| `critical-evaluation` | the student judges output — theirs, a peer's, an AI's — against a standard |
| `selective-judgment` | the student chooses between valid options and can say why |
| `ethical-reasoning` | the student notices who is affected by what they build |

Emphasise one or two per lesson, not all five. Name them in `lesson.yaml`; don't lecture them in the prose.
Other tracks don't use this field.

## Prediction in this track
Prediction is about *quality*, not output. "Before running, say what this prompt will get wrong." An
assessment's `predict` questions reference a prompt file in a lesson's `assets/`.

## Don't
- Don't present an AI output as correct without the student having judged it first.
- Don't use "AI-powered" or "unlock" anywhere. See pedagogy.md.
- Don't let the lesson become a tool tour. One idea, exercised hard.
