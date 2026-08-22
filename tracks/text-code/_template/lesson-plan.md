# Lesson 11 — Functions That Answer Back

Tier 2 Mental Model · Lesson 11 of 24 · 60 minutes

## 1. Lesson Theme

The student can already write a function. **Lesson 9** gave them `def` and a call; **Lesson 10** gave them
parameters, and they spent it happily printing things from inside functions. Everything worked, which is
the problem. Today the printing stops being enough.

The idea underneath is that `print` and `return` are not two ways of doing the same thing. `print` puts
marks on a screen for a human to read. `return` hands a value back to the line that called the function, so
the program itself can carry on with it. A function that prints has *done* something. A function that
returns has *produced* something. Only the second kind can be used to build anything larger, and every
function they write from here on will be judged on that.

The lesson turns on one error message. When a printing function's result gets stored and used, Python says
`TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'` — and `None` is the thing they
have never met. It is what a function hands back when you never told it to hand back anything. Seeing
`None` come out of a function that plainly worked is the moment the distinction becomes real.

- **Comes from:** l07 (the same three lines written out three times, and we said "we'll fix this later"),
  l09 (`def` and calling), l10 (parameters).
- **Sets up:** l13 (functions calling other functions — impossible without return values), l16 (returning
  a list), and the capstone, where anything not returnable can't be assembled.
- **Running threads:** **Predict → Observe → Explain** — today the prediction is about what comes *back*,
  not what appears. **Don't write it twice** — the extraction habit, opened in l07, closed here. **Errors
  are information** — `TypeError` is the teacher this lesson, not a failure.

## 2. Key Activity

**Extract the repetition, then find out the extracted function is useless.** `starter_temps.py` converts
three temperatures with the same arithmetic written out three times. The student pulls that line into
`to_celsius(f)` — a clean extraction, and it runs, and the output is identical. It looks finished.

Then they uncomment the two lines at the bottom that average the three results, and it breaks:
`TypeError: ... 'NoneType' and 'NoneType'`. The function printed the answer instead of handing it back, so
there was never a value to add. One word changes — `print` becomes `return` — and the averaging line works.

The protected takeaway: **a function that prints has done something; a function that returns has produced
something you can use. Only one of them is a building block.**

## 3. Tools & Materials

- **Tool:** VS Code with Python 3.12. Run files from the terminal today, not the REPL — see §8.
- **Code files:** `code/predict_return.py` (read and predict *before* running), `code/starter_temps.py`
  (the build). Reference solution in `solutions.md`, never in `code/` — students browse `code/`.
- **Concept page:** `concepts.md` in this folder — print versus return, what `None` is, and where a value
  goes when nothing catches it. It has no `Worked Example` section; the two traces inside `How It Works`
  are the worked examples, and a third would have repeated them. Set it as the read-after.
- **Board sketch — draw this before opening any file, and leave it up for the whole hour:**

  ```
      print                              return
      -----                              ------
      to_celsius(67)                     to_celsius(67)
           |                                  |
           v                                  v
      +-----------+                      +-----------+
      |   19.4    |                      |   19.4  ---+--> back to the line
      +-----------+                      +-----------+     that called it
           |
           v
        the screen                       x = to_celsius(67)
        (and nowhere else)               x is 19.4 — usable

      x = <a function that prints>  ->   x is None; nothing was handed back
  ```

## 4. Learning Outcomes

By the end of the session the student can:

1. Say what `return` does in terms of **where the value goes** — back to the caller — and what `print` does
   instead.
2. Predict what a variable holds after it is assigned the result of a function that only prints, and name
   that value as `None`.
3. Extract a repeated expression into a function and make it **usable** by returning rather than printing.
4. Read a `TypeError` mentioning `NoneType` and say which function is missing a `return`.
5. Decide, for a function they are about to write, whether it should print or return — and give a reason in
   terms of what the rest of the program needs.

## 5. Class Activities

A high-level map of the hour. Protect **the `TypeError` at the end of Build** — the whole lesson is that
error and the one-word fix. Everything before it is setup for that moment.

| Phase | Min | What happens | Purpose |
|---|---|---|---|
| Recap | 8 | Homework back. Then open l07's file and look at the three repeated lines we said we'd fix. They now know `def` and parameters — so today we finally fix it. | Reopen a thread left deliberately open four lessons ago. |
| New concept | 10 | Draw the board sketch. `print` sends a value to the screen; `return` sends it back to the caller. Introduce `None` by name before they meet it in an error. | Name the idea before the error arrives, so the error is recognisable. |
| Predict → Observe → Explain | 12 | ✏️ `code/predict_return.py` — write down every line it will print, **don't run it**. Then run. The `None` is the surprise; ask what they expected `stored_shout` to hold, and why. | The house method, aimed at what comes back rather than what appears. |
| Build | 20 | `code/starter_temps.py`: pull the repeated arithmetic into `to_celsius(f)`. It runs, output unchanged, looks done. Then uncomment the two averaging lines — `TypeError`. Read it together, find the missing `return`, change one word. | The extraction habit, and the error that proves why it wasn't finished. |
| Reflection | 5 | Explain to me what `None` is, without using the word "nothing". Then: name a function you'd *want* to print rather than return, and say why that's the right choice there. | Teach-back, plus the judgment that print isn't simply worse. |
| Homework brief | 5 | Walk `homework.md` together and start task 1 with them. Point at `concepts.md`. | They leave knowing exactly what to do, not guessing. |

## 6. Differentiation Notes

**If the student is flying:**

- Have them write `to_celsius` so it both returns the number *and* prints a friendly line, then argue about
  whether that is a good idea. It usually isn't — a function with two jobs is hard to reuse — but the
  argument is worth more than the rule.
- Ask what a function that hands back nothing useful is *for*. Push until they get to "it changes something
  else" — that's a side effect, and it's l14 arriving early.
- Give them `round()` and `len()` and ask which of Python's built-ins print and which return. Almost all
  return. Ask why that might be.
- If there is real time left, hand them `practice.md` project 2, *The receipt* — it forces the choice
  between printing and returning on a function that plausibly wants to do both. Project 1 if they'd rather
  keep going on numbers.

**If the student is struggling:**

- Cut: the averaging lines, and do the extraction only. A working `to_celsius` that returns is the lesson;
  the average is the proof, and the proof can be a demo you drive.
- Slow down on: **where the value goes.** Point at the board sketch every time, physically. "The screen, or
  back to this line?" is the whole question and it bears asking ten times.
- If `None` won't land, do it in three lines in front of them: a function that prints, a variable assigned
  its result, and a print of that variable. Nothing else on screen.
- If the extraction itself is the blocker rather than the return, hand them the function signature already
  written and let them fill in only the body.
- **Never cut:** the student seeing a value come back and get used. If time collapses entirely, run the
  averaging demo yourself and have them tell you which word to change.

## 7. Student Templates / Starter Materials

- **Pre-filled:** `starter_temps.py` has the three repeated conversions written out and working, plus the
  two averaging lines commented out at the bottom with a note saying they can't work yet. The file runs
  as-is.
- **Student writes:** the `to_celsius` function and the three rewritten calls, plus their ✏️ written
  prediction of everything `predict_return.py` prints.
- **Convention reminder:** ✏️ marks something the student writes down before running anything. A blank
  prediction is an incomplete exercise, the same as a blank code file — the prediction is the assessment,
  not the program.

## 8. Teacher Prep Notes

- **Before class:** run both files yourself and know `predict_return.py`'s output cold — `HELLO`, `AGAIN`,
  `None`, `quietly`. Note that `whisper("WORLD")` on line 12 prints nothing at all: its return value is
  handed back and nobody catches it. That silent line catches more students than the `None` does. Have the
  exact `TypeError` text in front of you so you can read it together rather than paraphrase it.
- **Known gotchas:**
  1. **The terminal hides the difference.** A printing `to_celsius` and a returning one whose result gets
     printed produce identical output. The distinction is invisible until something *uses* the result —
     which is why the averaging lines exist. Don't skip them, and don't demo the fix without them.
  2. **Don't teach this in the REPL.** A Python shell echoes return values automatically, so a returning
     function looks exactly like a printing one and the entire lesson evaporates. Run files from the
     terminal today.
  3. **Code after `return` never runs.** A student who adds a print *below* their new `return` will
     conclude the return is broken. It isn't; the function was already over.
- **Likely misconceptions:**
  1. *"`return` prints the answer."* It hands the value back; nothing appears on screen unless something
     later prints it. This is the most common one and it survives a whole lesson if unchallenged.
  2. *"Every function needs a `return`."* Plenty of good functions just do something. They hand back
     `None`, and that's fine as long as nobody tries to use it.
  3. *"`None` means it crashed."* `None` is a value, as real as `0` or an empty string. It is what "I was
     never told to hand anything back" looks like.
- **Language note:** say **"hands it back to the line that called it"**, never "outputs" — "output" is the
  word that makes print and return sound like the same thing. For `None`, say **"nothing was handed
  back"**, not "it's empty" or "it's null". At the error, ask **"which function was supposed to give us a
  number?"** rather than pointing at the missing word.
