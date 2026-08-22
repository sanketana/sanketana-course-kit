# Sanketana Course Repo Convention

**Convention version: 1** (kit 0.1)

Every Sanketana course lives in its own GitHub repo and follows this layout. The repo is the
**content** source of truth only. Student state — progress, quiz attempts, submissions, notes
about a particular student — never goes in git.

- **MUST** rules are enforced by `.kit/scripts/validate.py` and will fail a frontend build.
- **SHOULD** rules produce warnings. They exist for consistency and can evolve freely.
- Track-specific rules live in `TRACK.md` and extend (never override) this file.

---

## 1. Repo layout

```
<course-slug>/
  course.yaml              MUST   course manifest (§2)
  curriculum.md            MUST   the baselined spine (shape: curriculum-template.md)
  CLAUDE.md                kit    authoring instructions for Claude Code
  lesson-01-<slug>/               one folder per lesson (§3)
  lesson-02-<slug>/
  assessments/             MUST   the course's three assessments (§6)
  shared/                  opt    assets/ or code/ reused across lessons
  _drafts/                 opt    scratch; ignored by validator and view
  .kit/                    kit    everything shared with every other course:
      CONVENTION.md               this file
      TRACK.md                    track rules
      pedagogy.md
      _template/                  one model lesson to copy from
      scripts/                    validate.py, sync-kit.sh
  .github/workflows/       kit    validate.yml
```

**The root is what somebody authored.** A teacher opening a course sees the spine, the lessons and the
assessments — not five files identical in every course. The kit lives in `.kit/`, hidden from `ls` and
from Finder, and the validator skips every dotted entry before it checks anything.

`CLAUDE.md` is the one exception and stays at the root: Claude Code reads it from there and nowhere
else. It also holds this course's own context, which is why `sync-kit.sh` never overwrites it.

- Course slug: lowercase, hyphens, no version suffix. `python-foundations`, not `python-foundations-v2`.
- MUST: no other files or folders at root (dotted entries like `.kit/`, `.github/`, `.gitignore`
  are skipped entirely).
- **`curriculum.md` is the single source for everything written about the course.** There is no
  separate parent-facing document. The course's front page in the view, and any brochure copy handed
  to a designer, are rendered from the spine's parent-safe sections — outputs, not files to maintain.
  If a fact belongs in a parent-facing view and isn't in `curriculum.md` yet, add a field there.

## 2. `course.yaml`

```yaml
convention: 1                   # MUST   which convention version this repo follows
kit_version: "0.1"              # SHOULD informational
track: text-code                # MUST   text-code | block-code | ai-fluency
language: python                # SHOULD free text, informational
id: python-foundations          # MUST   stable forever; matches repo name
title: Python Foundations       # MUST
subtitle: From first print() to a working project
audience:
  age_min: 10
  age_max: 14
  prerequisites: "None. Block coding helps but isn't required."
format:
  sessions: 24
  session_min: 60
  mode: "1:1 live"
tools:
  - VS Code
  - Python 3.12
tiers:                          # SHOULD navigation groups; lesson ids must exist
  - id: syntax
    title: "Tier 1 — Syntax"
    lessons: [l01, l02, l03, l04, l05]
lessons:                        # MUST   explicit order; the only source of ordering
  - l01
  - l02
```

Ordering is explicit so that inserting a lesson later is a one-line change plus a new folder.
Existing folders are never renumbered; their ids, links and any future student records stay valid.

## 3. Lesson folder

```
lesson-03-<slug>/
  lesson.yaml          MUST   lesson metadata (§4)
  lesson-plan.md       MUST   TEACHER-ONLY — the session plan (§5)
  concepts.md          MUST   student-facing — the textbook page for this lesson's idea
  homework.md          MUST   student-facing (may say "No homework this lesson")
  practice.md          MUST   student-facing extra projects for a fast student (§5)
  solutions.md         opt    TEACHER-ONLY
  code/                opt    see TRACK.md
  assets/              opt    images, project files, referenced relatively
```

- MUST: folder name matches `lesson-NN-<slug>`, NN two digits. NN is for humans browsing GitHub;
  the view uses `lesson.yaml: id`.
- MUST: **audience is decided by filename.** Only the `.md` names above are allowed in a lesson folder.
- MUST: one lesson is one folder. Don't split a lesson across files.

**The two halves of a lesson.** They are not two views of the same thing — they answer different
questions, and neither one restates the other.

`lesson-plan.md` is the **hour**: what happens, in what order, for how long, what to protect when time
runs short, what the answers are. It is the only place the class flow is written down. A teacher runs the
session from this file alone.

`concepts.md` is the **idea**: a page from a textbook, written to the student. What the concept is, how it
works, a worked example, the mistakes people make, what it's called. No timings, no steps, no "now open
your starter file" — a student who missed the class should still be able to read it and understand the
idea, and a student revising in three months should find it the fastest way back.

The test: if a sentence only makes sense while sitting in the lesson, it belongs in the plan. If it would
still make sense a year later, it belongs in `concepts.md`.

Homework is in neither. It lives in `homework.md` (student) and `solutions.md` (teacher), once.

## 4. `lesson.yaml`

```yaml
id: l03                          # MUST  lNN at creation; never reassigned
title: Making Decisions          # MUST
summary: >                       # MUST  1–2 sentences for lesson lists
  Programs that react: if/else, comparisons, and the assign-vs-compare bug.
duration_min: 60                 # MUST
tier: syntax                     # SHOULD matches a tier id in course.yaml
video:                           # opt  list so recap + demo both fit
  - label: Class recording
    url: https://youtu.be/xxxx
prerequisites: [l02]             # opt  lesson ids
tags: [conditionals, boolean]    # opt  free text for search
```

Tracks may add optional fields in `TRACK.md`; `ai-fluency` adds `thinking_skills`.

## 5. Markdown body rules

1. MUST: no YAML frontmatter in any `.md`. Metadata lives in `lesson.yaml`.
2. MUST: every H2 (`## `) comes from the allowlist. Any subset, any order, none required —
   **except `lesson-plan.md`, whose spine is fixed** (below).
3. H3 and below are free.

### `lesson-plan.md` — a fixed spine

MUST: exactly these eight H2s, numbered, in this order, all present. A teacher opening any lesson in any
course finds the same section in the same place; that predictability is the point of the file.

```
## 1. Lesson Theme          where this sits in the arc — what it pays off, what it sets up, live threads
## 2. Key Activity          the one thing that must happen, and the protected takeaway in one sentence
## 3. Tools & Materials     tools, files, assets, and a board sketch to draw before any building
## 4. Learning Outcomes     numbered; "by the end the student can …"
## 5. Class Activities      the map of the hour (below)
## 6. Differentiation Notes if flying / if struggling / what is never cut
## 7. Student Templates / Starter Materials   pre-filled vs student-written
## 8. Teacher Prep Notes    before class, known gotchas, likely misconceptions, language note
```

**§5 Class Activities** is a table — `Phase | Min | What happens | Purpose` — preceded by one bolded line
naming what to **protect** if the hour runs short. This table is the whole class flow; there is nowhere
else it is written down. The `Min` column should account for the session length in `lesson.yaml`.

The phases are the same in every lesson of every track. A teacher should recognise the shape of the hour
before reading a word of the content:

| phase | ~min | what it is |
|---|---|---|
| `Recap` | 8 | Homework back, and the thread from last lesson that today pays off. |
| `New concept` | 10 | Teach the idea. Same ground as `concepts.md`, taught rather than read. |
| `Predict → Observe → Explain` | 12 | The house method. The student commits a prediction, runs it, explains the gap. |
| `Build` | 20 | They make the thing. Any second predict, remix or deliberate break belongs at the end of this phase, not as a phase of its own. |
| `Reflection` | 5 | Teach-back, and the ethics beat where the lesson has one. |
| `Homework brief` | 5 | Walk the new homework together and start task 1 with them. |

SHOULD, not MUST — a lesson may merge two or rename one where the content genuinely demands it, and the
minutes are a default, not a budget. But don't split a phase in two because the lesson has two interesting
moments; put the second one inside the phase it belongs to. What used to be a track heading — a Prompt
Lab, a Build Steps run, a Bug Hunt, a Tool Judgment — is a *way of running* one of these phases, not an
extra row.

**✏️ means the student writes something down, before anything is run.** Use it in the plan's §5 and §7. A
blank ✏️ is an incomplete exercise, exactly like a blank code file — the prediction is the assessment, not
the program.

### `concepts.md` — the textbook page

Written to the student, about the idea rather than the session. Any subset of these, any order, none
required — but `The Idea` and `Key Takeaways` earn their place in almost every lesson.

| heading | what goes in it |
|---|---|
| `The Idea` | The concept in plain words, from the problem it solves. Start here. |
| `How It Works` | The mechanics. Short examples, each one making a single point. |
| `Worked Example` | One case traced end to end, including the wrong turn. |
| `Vocabulary` | Terms introduced, as a table. What a student needs to say it out loud. |
| `Common Mistakes` | The errors people actually make, with what the error message means. |
| `Where This Shows Up` | Where the idea recurs — later lessons, other tools, outside the course. |
| `Key Takeaways` | The handful of sentences worth remembering. |

MUST NOT: timings, "in class we will…", references to the starter file as a set of steps. Those are the
plan's. `concepts.md` may show code, screenshots and diagrams freely — it is a textbook page, not a script.

### `practice.md` — for the student who finishes early

Every lesson has one. A 1:1 hour with a fast student runs out of lesson before it runs out of
time, and "just try something" is not a plan — this is the teacher's material for that moment.

MUST: `## Practice Projects`, then **two or three** projects as H3s. Independent of each other,
so the teacher can pick one by eye. Each project carries three things:

- the **brief** — what to build, in two or three sentences;
- **The stretch** — the one constraint that makes it harder than the classwork, named explicitly,
  so the teacher knows what the project is *for*;
- **Done when** — how the student knows they're finished, in terms of behaviour, not effort.

Harder than the classwork on purpose. A project that is just "the same thing again with different
numbers" is a worksheet. Reference solutions, where a project needs one, go in `solutions.md`.

`lesson-plan.md` §6 Differentiation Notes should name the project it would reach for first.

### Core H2 allowlist — the other files

| file | headings |
|---|---|
| homework.md | `Homework` · or numbered tasks `1. …`, `2. …` |
| solutions.md | mirrors homework numbering |
| practice.md | `Practice Projects` · numbered projects |

Convention 2 has no track-specific headings: what used to be an extra heading is now a phase in §5. Tracks
still say in `TRACK.md` what belongs on a concepts page for that track.

## 6. Assessments

A course has **exactly three**, at the repo root in `assessments/`. Not one per lesson — a quiz
after every session trains students to answer questions about the last hour, which is not what
this course claims to teach.

```
assessments/
  formative-1.yaml           MUST   ~a third of the way in   10 questions   15 min
  formative-1-solutions.md   MUST   TEACHER-ONLY  marking notes
  formative-2.yaml           MUST   ~two thirds in           10 questions   15 min
  formative-2-solutions.md   MUST
  summative.yaml             MUST   the end                  20 questions   45 min
  summative-solutions.md     MUST
```

**Formative** assessments are diagnostic and low stakes. They run inside a lesson's Recap slot,
and their job is to tell the teacher what to re-teach — not to produce a mark worth reporting.
**The summative** is its own session at the end of the course.

```yaml
id: formative-1                  # MUST  matches the filename stem
title: Where we are so far       # MUST  student-facing; not "Test 1"
kind: formative                  # MUST  formative | summative
after: l08                       # MUST  the lesson it runs after
covers: [l01, l02, l03, l04, l05, l06, l07, l08]   # MUST  lesson ids, all real
duration_min: 15                 # MUST
questions:
  - id: q1                       # MUST  unique within the assessment
    type: single                 # MUST  single | multi | predict | short
    lesson: l03                  # MUST  which lesson this tests; must be in `covers`
    prompt: What does `print(7 > 5)` show?
    options:                     # MUST for single/multi
      - { id: a, text: "7 > 5" }
      - { id: b, text: "True" }
    answer: b                    # MUST  option id, or a list of ids for multi
    explanation: A comparison produces a boolean and print shows it as text.
  - id: q2
    type: predict
    lesson: l03
    prompt: Before running, write down exactly what this prints.
    code_ref: lesson-03-decisions/code/predict_decisions.py   # MUST for predict; path from the repo root
    answer: |
      True
      You qualified!
```

- Every lesson in `covers` SHOULD be tested by at least one question. A lesson worth teaching is
  worth asking about.
- Weight towards `predict` and `short`. Multiple choice is cheap to mark and cheap to guess; the
  course claims to teach explanation, so assess explanation.
- `predict` exists because Predict → Observe → Explain is the house method. Attempts are stored
  by the view, never here.

**`<stem>-solutions.md`** is TEACHER-ONLY and holds what the YAML can't: what a `short` answer must
contain for full marks, what a specific wrong answer tells you about the student, and which lesson
to revisit because of it. Numbered to match the question ids; only questions needing judgment need
an entry. Shape: `assessment-solutions-template.md`.

## 7. Links and assets

- MUST: images and project files live in `assets/`, referenced relatively: `![Alt](assets/flow.png)`.
- MUST: cross-lesson links are relative: `[Lesson 2](../lesson-02-variables/concepts.md)`. Never absolute GitHub URLs.
- SHOULD: refer to code files in backticks with the exact filename.
- Don't rename code or asset files after a lesson is committed; markdown and assessments reference them.

## 8. Stability rules — the ones that future-proof you

1. `course.yaml: id` and `lesson.yaml: id` never change. They are join keys for student state later.
2. Filenames decide audience. `lesson-plan.md` and `solutions.md` are teacher-only and nothing
   student-facing may even name them; never put solutions inside homework.md.
3. Ordering lives only in `course.yaml: lessons`.
4. Structured things (assessments, video, duration) live in YAML. Prose lives in markdown.
5. Nothing the view needs is implied by folder numbering, heading order, or file position.

## 9. Evolving this convention

- Adding an optional file, folder, field or heading: bump kit minor version. Nothing breaks.
- Renaming, removing, or making something required: bump `convention`, ship a migration script,
  upgrade courses one at a time. The view keeps rendering older conventions.

## 10. Out of scope (deliberately)

Student progress, grades, submissions, per-student notes → state store. Rendering, navigation → the view.
Scheduling, enrolment → Zoho.
