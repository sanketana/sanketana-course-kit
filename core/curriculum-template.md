# <Course Title> — Curriculum

<!-- This is the spine, and the single source for everything written about this course.
     Baseline it with `git tag spine-v1` before writing lessons.

     Decisions, not delivery. No clock times, no minute-by-minute breakdowns, no scripted wording —
     those are the lesson plan's job. A session's duration in the heading is as fine-grained as
     timing gets in this file. -->

**Everything else is derived from this file.** The course's front page in the view, and any brochure
copy handed to a designer, are *rendered* from the sections below. They are outputs, not documents —
there is no second file to keep in sync, and nothing in them is a fact this file doesn't already
hold. When the spine changes, they change with it.

**The file itself is internal.** Sections down to and including `## Questions parents ask` are
parent-safe and are what the derived views draw on. Everything from `## The <N> sessions` onward —
teacher risks, named cuts, open questions — is for whoever is building and teaching the course, and
is never shown to a parent as-is.

**Course id:** `<course-slug>`  ·  **Track:** text-code  ·  **Sessions:** 24 × 60 min  ·  **Ages:** 10–14

## Promise
One paragraph, written for a parent. What the student can do at the end that they could not at the start.

## Who this is for

**Comes from.** Where students typically arrive from and what we assume. Name it plainly; don't
assume a prior tool the course can't actually rely on.

**Suits a student who…** Three lines. Concrete enough that a parent can tell whether it's their child.

**Not the right course if…** Two lines, and write them honestly — this is the part that earns trust
with a parent who can tell depth from gamified ed-tech, and the part a derived brochure must not
quietly drop.

**What you need.** Tools and equipment, prior experience (or "none"), and anything a parent has to
set up, pay for, or agree to before the first session.

## Tiers
| id | title | lessons | what changes for the student |
|---|---|---|---|
| syntax | Tier 1 — Syntax | l01–l05 | can read and write basic programs |
| mental-model | Tier 2 — Mental Model | l06–l11 | can predict what code does before running it |

## Capstone
What is built at the end, and which tiers it draws on.

## What a parent sees

Four or five lines, no more. What reaches a parent and when: how progress is reported, the two short
checks partway through and the assessment at the end, what the final session looks like, and what the
student keeps afterwards. Be straight about what the checks are for — telling the teacher what to go
back over, not producing a grade.

Then: **what we ask of you.** The practical asks stated plainly — time between sessions, anything a
parent must be present for, accounts or keys they hold. A parent who discovers these later feels sold
to, which is the opposite of the positioning.

## Questions parents ask

Optional, five or six, two lines each. The objections actually received, including the awkward ones —
a missed session, whether the child needs to know something already, how much screen time this really
is, what happens when the course ends. A dodged question is worse than an omitted one.

<!-- Everything below this line is internal. -->

## The <N> sessions

> The table is the summary view. Where it and the per-session blocks under `## Sessions in detail`
> disagree, the blocks are correct.

One row per session, numbered 1 to <N>, grouped into blocks. **A block is a tier** — same grouping and
the same ids as the `## Tiers` table above and `course.yaml: tiers`. Don't invent a second scheme.

- **Focus** — the one idea of the session, in a few words. Not a sentence.
- **Ships** — what the student *leaves with*. Every session ships something: a working program, a
  project file, a filled log, a decision written down. If a session ships nothing, it is a lecture,
  and this course doesn't have lectures.
- **Bold** in Ships marks a flagship deliverable — the ones a parent would recognise and a student
  would show someone. Use it sparingly.
- ***Filler*** in the Session column marks a session left deliberately unassigned, for the teacher to
  fill from a bank of mini-projects. One or two in a long course absorbs the slippage that always
  happens; without them the last block gets eaten.

### Block 1 · <block title> (S1–S<n>)

| # | Session | Focus | Ships |
|---|---|---|---|
| 1 | <session title> | <the one idea> | <what they leave with> |
| 2 | … | … | … |

### Block 2 · <block title> (S<n+1>–S<m>)

| # | Session | Focus | Ships |
|---|---|---|---|
| 3 | … | … | … |
| 4 | *Filler* | Teacher's choice from the filler bank | One mini-project |

<!-- …one block per tier, covering every session through to the last. -->

**<N> working <artifacts>, <M> of them <what makes those ones different>.**

Close the table with one line like that — the course's claim in a sentence, countable and checkable.
If you can't write it, the spine isn't finished.

## Sessions in detail

<!-- One block per session, every session, in order. This is the part that gets reviewed and
     baselined — `git tag spine-v1` — before a single lesson is generated. -->

Blocks and their ranges match the table above and `course.yaml: tiers`.

Each session heading carries four things: the session number used throughout this file, the **permanent
lesson id**, the tier, and the duration — `#### S3 · <title>  (l03, <tier>, 60 min)`. The id is what
`lesson.yaml`, `course.yaml: lessons` and every later cross-reference use, and it is never reassigned
once written. Inside this file, refer to sessions by S-number; the heading carries the mapping.

**This is the brief, not the plan.** Each session's `lesson-plan.md` is generated from the block below
it, and the fields map straight across:

| this field | becomes |
|---|---|
| the heading | `lesson.yaml: id`, `tier`, `duration_min` |
| New concepts | `lesson.yaml: tags` |
| What this session is for | `lesson.yaml: summary`, condensed — and plan §1 Lesson Theme |
| Concepts introduced | plan §4 Learning Outcomes, and `concepts.md` |
| Predict-then-run | the POE row of plan §5 |
| Build | plan §2 Key Activity, and the Build row of §5 |
| Deliverable | the Ships cell above, and plan §2's protected takeaway |
| Homework | `homework.md` |
| Teacher risk | plan §6 Differentiation and §8 Teacher Prep Notes |

So write the decisions here and the wording there. If you find yourself drafting the sentences a
teacher will actually say, you are in the wrong file.

Nine fields per session, all of them. The last two are the ones that get skipped and the ones that
matter most at review time: **Depends on / Feeds** is how you catch a session that quietly requires
something no earlier session built, and **Teacher risk** is how you catch a session that cannot be
delivered in the time it has.

### Block 1 · <block title> (S1–S<n>)

One short paragraph: what this block is for, and — more usefully — what it deliberately is *not*.
Name anything unusual about it here rather than repeating it in every session below.

#### S1 · <Session title>  (l01, <tier>, 60 min)
**New concepts:** <concept> · <concept> · <concept>

**What this session is for.** One paragraph. The purpose, not the contents — what the student can do
afterwards that they could not before, and why this session sits at this point in the course.

**Concepts introduced.**
- <one line each, in the order they are met>
- <a concept met by doing rather than by explanation — say so>

**Predict-then-run.** The prediction moment, concretely: what the student commits to in writing before
anything runs, and what the gap teaches. Every session has one. A session where you cannot name it is
a session where the student is being shown rather than taught.

**Build.** What gets written, in what file, and how far it gets. Name the starter material that is
provided rather than built — providing plumbing is fine, and saying so here stops it being mistaken
for a shortcut later.

**Deliverable.** What the student leaves with. Matches the Ships cell in the table above. **Bold it**
when it is a flagship the student would show someone.

**Depends on / Feeds.** S<n> → S<m>. What must have worked for this to run, and what breaks later if
this one does not land. The left-hand side becomes `lesson.yaml: prerequisites`, as ids.

**Homework.** One line. One focused task, or one task plus a stretch.

**Teacher risk.** The specific way this session fails — not "it might run long", but which part
overruns, and **what gets cut when it does**. Decide the cut here, in advance; a named cut is the
difference between a session that ends early and one that ends badly. Where in the hour that call gets
made is the lesson plan's business, not the spine's.

#### S2 · <Session title>  (l02, <tier>, 60 min)
**New concepts:** <concept> · <concept>
**Project:** <project name> — *anchor*

<!-- The Project line appears only when the session builds a named thing. *anchor* marks a project
     that spans several sessions and is carried forward; a one-session build needs no marker. -->

**What this session is for.** …

<!-- Optional: a named callout for a decision that needs arguing rather than listing. Use a bold
     lead-in and keep it to a paragraph. Examples of when to use one: a technique chosen over an
     obvious alternative, a constraint imposed for safety, a term introduced early on purpose. -->

**<The one decision worth arguing>.** …

**Concepts introduced.** …

**Predict-then-run.** …

**Build.** …

**Deliverable.** …

**Depends on / Feeds.** S1 → S3, S<m>.

**Homework.** …

**Teacher risk.** …

Open question: … <!-- keep while iterating; remove at baseline -->

#### S<n> · *Filler*  (l<nn>, <tier>, 60 min)
**Drawn from the filler bank — see the appendix.**

One paragraph: why the slot is *here* rather than elsewhere, and which kind of pick suits it — a
consolidation win after two heavy sessions, or a second repetition of something worth repeating.

**Deliverable.** One more working <artifact>, built in a single session.

<!-- A session whose shape genuinely differs — a capstone build, a demo, an assessment — can replace
     Concepts introduced / Predict-then-run / Build with a single **Session shape.** field. Keep
     Deliverable, Depends on / Feeds and Teacher risk; those are the ones review depends on. -->

#### S<n> · <A session that is not a normal teaching session>  (l<nn>, <tier>, 60 min)
**What this session is for.** …

**Session shape.** …

**Deliverable.** …

**Depends on / Feeds.** …

**Teacher risk.** …

## Appendices

Optional, and worth having once a course has practices that recur:

- **Cross-cutting practices** — things true of every session that would otherwise be repeated in all
  of them: what the student does and does not get an account for, what is logged, what is never
  committed. Number them, then refer to them inline as *(cross-cutting practice 2)* rather than
  restating them.
- **The filler bank** — the mini-projects a *Filler* session may draw from, one paragraph each, with
  a note on which kind of batch each suits.
- **Recurring markers** — if you use inline bold markers on sessions (a review gate, a checkpoint,
  a session where something must be verified), define each one here, once.

## Known risks
Where the spine is most likely to bend once real students hit it.
