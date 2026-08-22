# Lesson 2 — Asking a Better Question

Tier 1 Judgment · Lesson 2 of 16 · 60 minutes

## 1. Lesson Theme

In **Lesson 1** the student watched a tool answer confidently and be wrong, and we left them with a
question rather than a rule: *how would you have known?* Today we start building the answer, and the first
move is counter-intuitive. Students assume a better answer comes from a politer, longer prompt. It comes
from **detail the tool does not have** — and from having a standard to judge the answer against before it
arrives.

The session runs the same task three times. *"Make me a study plan"* returns something plausible, generic,
and useless. Adding real subjects, a real exam date and real available hours changes the output more than
any amount of "please" and "be detailed". Adding what a *good* plan looks like to them changes it again.
Three rounds, one task, visibly different results.

The half that matters more is the second one. A student who can improve a prompt but cannot say why one
output is better than another has learned a trick, not a skill. So they write their own three-line standard
**before** ranking anything, and then rank outputs against it — including outputs that are polished and
wrong. The order is the lesson: **the standard comes first; the output is judged against it, never the
other way round.**

- **Comes from:** l01 (a confident tool being wrong; the unanswered "how would you know?").
- **Sets up:** l03 (giving the tool a role and constraints), l05 (checking claims against a source), and
  the standing habit that every output in this course gets ranked against something written down.
- **Running threads:** **Predict → Observe → Explain** — here the prediction is about *quality*: what will
  this prompt get wrong? **Your standard, not the tool's** — introduced today, used every lesson after.
  **What did you give away?** — the ethics beat, woven not bolted on.

## 2. Key Activity

**Three rounds, then judge — with the standard written first.** The student prompts for a study plan three
times, predicting the weak spot before each send and logging what actually came back. Between rounds two
and three they stop and write three lines: what makes a study plan good *for them*. That is their standard,
and it is theirs, not ours.

Then they rank `assets/sample-outputs.md` against it. Plan B is deliberately the most polished and the
least useful — it looks like effort and ignores the constraints. A student who ranks it first has just
learned something about themselves that no amount of telling would have taught. Finally they rank their own
three rounds the same way, and answer the sharp question: **did the best prompt actually produce the best
plan?**

The protected takeaway: **detail beats politeness, and an output can only be called good against a standard
you wrote down before you saw it.**

## 3. Tools & Materials

- **Tool:** any chat AI the family has approved; we use Claude in class. Check before the session which one
  this student is actually allowed to use — it changes what you can put on screen.
- **Assets:** `assets/prompt-log-study-plan.md` (the student's log for the hour),
  `assets/sample-outputs.md` (three plans written by us — B is the polished trap).
- **Concept page:** `concepts.md` in this folder — task/context/standard, and why the standard has to
  come first. Set it as the read-after; don't teach from it.
- **Board sketch — draw this before the first prompt:**

  ```
      "Make me a study plan"          -> generic, plausible, useless
                + what I KNOW
      "...Physics, Maths, Chem;        -> fits my week
        exam 14 March; 2h weekday"
                + what I WANT
      "...short sessions, one hard     -> a plan I would follow
        subject a day, no Sundays"

      and running alongside, written BEFORE any ranking:

      MY STANDARD  1. ______________
                   2. ______________     <- the output is judged against THIS
                   3. ______________
  ```

## 4. Learning Outcomes

By the end of the session the student can:

1. Predict a prompt's **weak spot before sending it**, and say whether the prediction held.
2. Improve a prompt by adding **detail the tool does not have** — context and constraints — rather than
   politeness or length.
3. Write a **three-line standard** for what a good output looks like, in their own terms.
4. Rank several outputs against that standard and justify each placing in one sentence, including rejecting
   an output that is well-presented but does not meet the constraints.
5. Name one thing they typed that they would not want stored, and say what they would change.

## 5. Class Activities

A high-level map of the hour. Protect **the ranking inside Build** — judging outputs against a written
standard is the skill the whole track is built on. If the clock is going, cut a prompt round from POE,
never the ranking.

| Phase | Min | What happens | Purpose |
|---|---|---|---|
| Recap | 8 | Homework back, then resurface l01: the tool was confident and wrong, and we never answered *how would you know?* | Cash in last week's open question. |
| New concept | 10 | Draw the board sketch. A prompt does three jobs — task, context, standard — and most weak prompts only do the first. The standard is the one people skip. | Teach the idea before any prompting. Same ground as `concepts.md`. |
| Predict → Observe → Explain | 12 | ✏️ Three rounds in `assets/prompt-log-study-plan.md`, predicting the weak spot before each send: *"Make me a study plan"*; then with real subjects, date and hours; then with what a good plan means to them. | The house method on prompt *quality*, not output. |
| Build | 20 | ✏️ Write the three-line standard and keep it on screen. Rank `assets/sample-outputs.md` against it, one sentence each — B is the polished trap, don't tip it. Then rank their own three rounds: did the best prompt make the best plan? Refine the best prompt once. | The flagship phase: judging against a standard, not using. |
| Reflection | 5 | ✏️ Subjects, dates, weak spots — who else can see what you typed, and what would you leave out? Then: the tool wrote the plan, but who decided what "good" meant? | Teach-back, plus the woven ethics beat. |
| Homework brief | 5 | Walk `homework.md` together and start task 1 with them. The standard comes first. Point at `concepts.md`. | They leave knowing exactly what to do, not guessing. |

## 6. Differentiation Notes

**If the student is flying:**

- Have them write the standard **first**, before round 1, and predict how many of their three lines each
  round will satisfy. A sharper version of the same exercise.
- Give them a fourth sample output that satisfies the standard but is plainly wrong on a fact. Does the
  standard catch it? Should it? That is l05 arriving early.
- Ask them to write the prompt that would produce Plan B — the polished useless one — on purpose.
  Reverse-engineering a bad output is harder than improving a good one.
- If there is real time left, hand them `practice.md` project 1, *The standard for something else* — it
  moves the habit off the study plan and onto something they actually want. Project 2 is the same
  Plan B exercise written up, if you'd rather they finish it properly than start something new.

**If the student is struggling:**

- Cut round 3 and the refine phase. Two rounds and a real ranking beats three rounds and a rushed one.
- Slow down on: **the standard.** Three lines is genuinely hard. Prompt with "what would make you actually
  open this plan on a Tuesday?" rather than accepting "it should be good".
- If they cannot rank the samples, do the first one together out loud, then hand back the second.
- **Never cut:** the student ranking at least two outputs against a standard they wrote themselves, and
  being able to say what the standard is.

## 7. Student Templates / Starter Materials

- **Pre-filled:** `prompt-log-study-plan.md` has a row per round — prediction, prompt, what came back, was
  the prediction right — and an empty three-line standard box. The log is the artifact of the lesson.
- **Student writes:** every prediction, the three-line standard, one sentence per ranked output, and the
  ethics answer.
- **Convention reminder:** ✏️ marks something written **before** the tool is asked. In this track that is
  the entire discipline — a prediction typed after reading the answer is not a prediction, and a log filled
  in at the end is not a log.

## 8. Teacher Prep Notes

- **Before class:** run round 1 yourself **today**. Models change weekly and last month's generic answer is
  not this month's — you need to know what "generic" looks like right now. Have `sample-outputs.md` open.
  Confirm which AI tool this family has approved.
- **Known gotchas:**
  1. **Plan B is the trap and it works.** It is the most formatted and the least useful. Do not tip it. If
     the student ranks it first, that is the lesson functioning — walk them back to their own three lines.
  2. **"Please" and "be detailed" instead of detail.** The most common round-2 rewrite. Ask: *what does the
     tool not know about you?* That question does the work.
  3. **Ranking by length or formatting.** Bring them back to the standard every single time. The standard
     is on the table for exactly this reason.
  4. **Skipping the prediction.** They will want to just send it. The prediction is the lesson; the output
     is the evidence.
  5. **Never paste a real student's AI conversation into course materials.** Our example logs are written
     by us. This holds for anything you keep after class.
- **Likely misconceptions:**
  1. *"A longer prompt is a better prompt."* Round 2 versus round 3 usually disproves this on its own.
  2. *"The tool knows what I mean."* It answers the question asked, not the one intended.
  3. *"A well-formatted answer is a good answer."* Plan B exists to kill this.
  4. *"There's a right way to prompt."* There is a right way to *judge*. The prompt follows from that.
- **Language note:** say **"what does it not know?"** rather than "add more context". Say **"your
  standard"** every time, never "the criteria". At the ranking, ask **"against what?"** whenever a student
  says an output is good — it is the one question that turns using a tool into judging one.
