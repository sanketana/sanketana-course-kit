# Sanketana Course Repo Convention

**Convention version: 1** (kit 0.1)

Every Sanketana course lives in its own GitHub repo and follows this layout. The repo is the
**content** source of truth only. Student state — progress, quiz attempts, submissions, notes
about a particular student — never goes in git.

- **MUST** rules are enforced by `scripts/validate.py` and will fail a frontend build.
- **SHOULD** rules produce warnings. They exist for consistency and can evolve freely.
- Track-specific rules live in `TRACK.md` and extend (never override) this file.

---

## 1. Repo layout

```
<course-slug>/
  course.yaml              MUST   course manifest (§2)
  curriculum.md            MUST   the baselined spine (shape: curriculum-template.md)
  overview.md              MUST   parent/student-facing description
  CONVENTION.md            kit    this file
  TRACK.md                 kit    track rules
  pedagogy.md              kit
  CLAUDE.md                kit    authoring instructions for Claude Code
  _template/               kit    one model lesson to copy from
  scripts/                 kit    validate.py, sync-kit.sh
  lesson-01-<slug>/               one folder per lesson (§3)
  lesson-02-<slug>/
  shared/                  opt    assets/ or code/ reused across lessons
  _drafts/                 opt    scratch; ignored by validator and view
```

- Course slug: lowercase, hyphens, no version suffix. `python-foundations`, not `python-foundations-v2`.
- MUST: no other files or folders at root (dotfiles like `.github/`, `.gitignore` are fine).

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
  classwork.md         MUST   student-facing
  homework.md          MUST   student-facing (may say "No homework this lesson")
  solutions.md         opt    TEACHER-ONLY
  teacher-notes.md     opt    TEACHER-ONLY
  practice.md          opt    student-facing extra projects
  quiz.yaml            opt    structured quiz (§6)
  code/                opt    see TRACK.md
  assets/              opt    images, project files, referenced relatively
```

- MUST: folder name matches `lesson-NN-<slug>`, NN two digits. NN is for humans browsing GitHub;
  the view uses `lesson.yaml: id`.
- MUST: **audience is decided by filename.** Only the `.md` names above are allowed in a lesson folder.
- MUST: one lesson is one folder. Don't split classwork across files.

## 4. `lesson.yaml`

```yaml
id: l03                          # MUST  lNN at creation; never reassigned
title: Making Decisions          # MUST
summary: >                       # MUST  1–2 sentences for lesson lists
  Programs that react: if/else, comparisons, and the assign-vs-compare bug.
duration_min: 60                 # MUST
tier: syntax                     # SHOULD matches a tier id in course.yaml
thinking_skills:                 # SHOULD from the fixed vocabulary
  - mental-modeling
video:                           # opt  list so recap + demo both fit
  - label: Class recording
    url: https://youtu.be/xxxx
prerequisites: [l02]             # opt  lesson ids
tags: [conditionals, boolean]    # opt  free text for search
```

**Thinking-skills vocabulary (fixed):** `mental-modeling`, `intentional-direction`,
`critical-evaluation`, `selective-judgment`, `ethical-reasoning`.

## 5. Markdown body rules

1. MUST: no YAML frontmatter in any `.md`. Metadata lives in `lesson.yaml`.
2. MUST: every H2 (`## `) comes from the allowlist. Any subset, any order, none required.
3. H3 and below are free.

**Core H2 allowlist**

| file | headings |
|---|---|
| classwork.md | `Lesson Theme` · `What You'll Build` · `Tools Used` · `What You'll Learn` · `Starter Materials` · `Predict the Output` · `In Class` · `Reflection` · `Key Takeaways` |
| homework.md | `Homework` · or numbered tasks `1. …`, `2. …` |
| solutions.md | mirrors homework numbering |
| practice.md | `Practice Projects` · numbered projects |
| teacher-notes.md | `Prep` · `Timing` · `Common Pitfalls` · `Differentiation` · `What to Watch For` |

Tracks add headings in `TRACK.md`. A new heading is justified only if the view would render it
differently from every existing one; otherwise reuse a core heading with different content.

SHOULD: inside `## In Class`, each timed activity is an H3 ending with the duration:
`### Recap and the bridge from Scratch (6 min)`.

## 6. `quiz.yaml`

```yaml
id: l03-quiz                     # MUST  <lesson-id>-quiz
title: Check your understanding
questions:
  - id: q1                       # MUST  unique within quiz
    type: single                 # MUST  single | multi | predict | short
    prompt: |
      What does `print(7 > 5)` show?
    options:                     # MUST for single/multi
      - { id: a, text: "7 > 5" }
      - { id: b, text: "True" }
      - { id: c, text: "1" }
    answer: b                    # MUST  id, or list of ids for multi
    explanation: A comparison produces a boolean and print shows it as text.
  - id: q2
    type: predict
    prompt: Before running, write down exactly what this prints.
    code_ref: code/predict_decisions.py   # MUST for predict; path relative to lesson
    answer: |
      True
      You qualified!
```

`predict` exists because Predict → Observe → Explain is the house method. Attempts are
stored by the view, never here.

## 7. Links and assets

- MUST: images and project files live in `assets/`, referenced relatively: `![Alt](assets/flow.png)`.
- MUST: cross-lesson links are relative: `[Lesson 2](../lesson-02-variables/classwork.md)`. Never absolute GitHub URLs.
- SHOULD: refer to code files in backticks with the exact filename.
- Don't rename code or asset files after a lesson is committed; markdown and quiz.yaml reference them.

## 8. Stability rules — the ones that future-proof you

1. `course.yaml: id` and `lesson.yaml: id` never change. They are join keys for student state later.
2. Filenames decide audience. Never put solutions inside homework.md.
3. Ordering lives only in `course.yaml: lessons`.
4. Structured things (quiz, video, skills, duration) live in YAML. Prose lives in markdown.
5. Nothing the view needs is implied by folder numbering, heading order, or file position.

## 9. Evolving this convention

- Adding an optional file, folder, field or heading: bump kit minor version. Nothing breaks.
- Renaming, removing, or making something required: bump `convention`, ship a migration script,
  upgrade courses one at a time. The view keeps rendering older conventions.

## 10. Out of scope (deliberately)

Student progress, grades, submissions, per-student notes → state store. Rendering, navigation → the view.
Scheduling, enrolment → Zoho.
