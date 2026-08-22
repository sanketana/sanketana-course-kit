# What a Sanketana course is

Read this before writing a spine or a lesson. It is the part of the school that is not in the folder structure.

## Who we teach
Students aged 8–18, one-to-one, live, online, across nine countries. Parents are discerning: they can tell
depth from gamified ed-tech and are paying for the former. A course must survive a parent reading it cold.
Positioning is premium and understated. "Coding, taught like a craft." Coach, not curriculum.

## Two layers
**Code is the artifact; thinking is the skill.** Every course has a visible layer — the projects a student
builds — sitting above a hidden thinking curriculum. Lessons are written so the student experiences the visible
layer and the teacher steers the hidden one.

The five thinking skills (vocabulary is fixed; use these exact ids in `lesson.yaml`):

| id | what it looks like in a lesson |
|---|---|
| `mental-modeling` | the student can predict what the machine will do before it does it |
| `intentional-direction` | the student decides what to build and why before touching the tool |
| `critical-evaluation` | the student judges output — theirs, a peer's, an AI's — against a standard |
| `selective-judgment` | the student chooses between valid options and can say why |
| `ethical-reasoning` | the student notices who is affected by what they build |

Every lesson emphasises one or two, not all five. Name them in `lesson.yaml`; don't lecture them in the prose.

## How we teach
**Predict → Observe → Explain.** The default shape for any new concept: the student predicts what code will do,
runs it, and explains the gap. Lessons should contain at least one explicit prediction moment; `predict`-type
quiz questions and `predict_*` code files exist for this.

Other habits a lesson should embody:
- Struggle is designed in. A lesson that never lets the student be wrong teaches nothing.
- Teach-back. Ask the student to explain the idea to the teacher, a parent, a younger sibling.
- Real detail, honest imperfection. Show a bug, a wrong first attempt, a limitation.
- One-to-one means the teacher adapts. Teacher notes say where to speed up or slow down; they don't script every word.

## Lesson proportions (60-minute default)
Roughly: 5–10 min recap and bridge · 15–20 min new idea through POE · 20–25 min build · 5–10 min reflection
and takeaway. Homework is one focused task plus one stretch, never a worksheet.

## Voice
Specific over grand. Real detail with honest imperfection. Confident, not loud. Respects the reader.
Voice, not costume.

Never use: fun, exciting, future-ready, 21st-century, AI-powered, unlock, journey, empower, supercharge,
game-changer. Don't address students as "kids". Don't promise outcomes we can't see.

Write to the student directly in classwork ("you'll build…"), to the teacher in teacher-notes
("watch for students who…"), to the parent in overview.md.

## Ethics is woven, not bolted on
Where a lesson touches data, automation, AI output, or other people, add one question in the Reflection
section. Not a separate unit. Not every lesson.
