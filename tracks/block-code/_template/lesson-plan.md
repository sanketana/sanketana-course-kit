# Lesson 3 — The Sprite Decides

Tier 1 React · Lesson 3 of 20 · 60 minutes

## 1. Lesson Theme

Two lessons of sequence and motion have produced sprites that do the same thing every time the flag is
clicked. In **Lesson 2** the student built a sprite that walked a fixed path and we noted, without dwelling
on it, that it walked straight through the wall. Today the sprite starts to **notice** — and the maze that
was decoration becomes something the program can actually react to.

The idea underneath is that the hexagon slot is a different shape for a reason. Scratch will not let a
number or a word drop into it; only a sensing block or a comparison fits, because only those answer
yes-or-no. Making the shape explicit — "what fits in this slot, and why won't `x position` go in?" — is
worth more here than any number of completed scripts.

The second idea is that a check has to keep happening. A `touching color` test placed outside the `forever`
loop asks once, at the start, and never again. Students consistently build this, run it, and watch the
sprite sail through the wall. That failure is the lesson: **`if` asks a question every time it runs, not
once.**

- **Comes from:** l01 (flag, motion blocks), l02 (a sprite following a fixed path; the wall it ignores).
- **Sets up:** l04 (variables and score — the same `if` now reacting to a value rather than the stage),
  l06 (broadcast and multiple sprites reacting to each other).
- **Running threads:** **Predict → Observe → Explain** — in this track prediction is about what the sprite
  will *do*. **The screenshot is the code** — students cannot read block stacks from prose. **Sensing is
  about right now** — the stage's current state, not what was true a second ago.

## 2. Key Activity

**Make the maze walls real, then find out how fragile the check is.** The student adds a `touching color`
test inside a `forever` loop so the sprite is pushed back at the black walls, and a second check on red for
the exit. It works, and it feels finished. Then the Remix Challenge breaks it twice: swap the order of the
two `if` blocks, and re-pick the wall colour with the eyedropper from the backdrop edge — where the black is
a near-black, not `#000000`. The sprite walks straight through.

The protected takeaway: **a sensing block only knows what is on the stage at this instant, and it matches
exactly — close is not touching. The check has to run inside `forever`, or it only ever asks once.**

## 3. Tools & Materials

- **Tool:** Scratch in the browser. No account needed for the lesson; one is needed to save.
- **Project files:** `assets/starter_maze.sb3` (the build), `assets/solution_maze.sb3` (reference — second
  tab, never on screen share until the end). Step screenshots `assets/step-01…04-*.png`.
- **Concept page:** `concepts.md` in this folder — the hexagon slot, why the check must live inside
  `forever`, and exact colour matching. Set it as the read-after; don't teach from it.
- **Board sketch — draw this before opening Scratch:**

  ```
      forever
        |
        +--> if <touching color [black]?> then
        |        go back to last safe spot         <- runs on EVERY loop pass
        |
        +--> if <touching color [red]?> then
                 say "Out!" / stop all
        |
        +----(loop round again, ask again)

      the same two questions, hundreds of times a second

      OUTSIDE the forever loop:  asked once, at the flag, then never again
  ```

## 4. Learning Outcomes

By the end of the session the student can:

1. Explain what fits in the **hexagon slot** and why a number or a word does not.
2. Place a check **inside** a `forever` loop and say what goes wrong when it sits outside.
3. Predict what a three-block script will make the sprite do, run it, and explain a wrong prediction.
4. Use `touching color` for a wall and an exit, and describe the block as asking about the stage **right
   now**.
5. Explain why a near-black wall breaks the check — colour matching is exact, not approximate.

## 5. Class Activities

A high-level map of the hour. Protect **the wall check running inside `forever`** — the sprite being
stopped by a wall it used to walk through is the moment the lesson lands. The near-black remix at the end
of Build is the second thing to protect.

| Phase | Min | What happens | Purpose |
|---|---|---|---|
| Recap | 8 | Homework back, then open last week's project and run it. Watch the sprite walk straight through the wall. "Today we fix that." | Make the gap visible before naming the tool that closes it. |
| New concept | 10 | Draw the board sketch. The hexagon slot only takes a yes-or-no question. A check asks **once** unless it sits inside `forever`. Sensing knows only this instant. | Teach the idea before any building. Same ground as `concepts.md`. |
| Predict → Observe → Explain | 12 | ✏️ Share `assets/predict-touching.png`: sprite on white, three blocks — does it say "Ouch"? Write it down, then run. Nothing happens. Drag the sprite onto black and run again. Why did the first run say nothing? | The house method; the gap between what they *want* and what the blocks *do*. |
| Build | 20 | `assets/starter_maze.sb3`: confirm the wall black, four `when key pressed` hats, then the wall check **inside** `forever`, then the exit check on red. Finish by breaking it — ✏️ predict, then swap the two `if` blocks, then re-pick a near-black with the eyedropper. | The flagship moment, then proof of how exact the check is. |
| Reflection | 5 | Explain the `forever` loop as if I've never seen it. When did `touching color` give a wrong answer? Your sprite "decided" to stop — did it? | Teach-back, plus the woven ethics beat. |
| Homework brief | 5 | Walk `homework.md` together and start task 1 with them. Close is not touching. Point at `concepts.md`. | They leave knowing exactly what to do, not guessing. |

## 6. Differentiation Notes

**If the student is flying:**

- Replace "go back to the last safe spot" with `if on edge, bounce` thinking: have them work out why the
  saved-position approach is needed for walls but not for edges.
- Add a third colour — a green square that speeds the sprite up. Where does that `if` go, and does its
  order matter relative to the other two?
- Ask: "the sprite checks hundreds of times a second. What would happen if it checked once a second?"
  Have them build it with a `wait 1 seconds` inside the loop and watch it tunnel through the wall.
- If there is real time left, hand them `practice.md` project 1, *The key that opens the door* — it forces
  a variable to carry what sensing can't remember. Project 3 is the quickest to start if only ten
  minutes remain.

**If the student is struggling:**

- Cut: the "try 20" experiment in *Move the sprite*, the third colour, and the order-swap remix. Keep the
  near-black remix — it is short and it is the memorable one.
- Slow down on: **inside versus outside the loop.** Build it wrong on purpose, run it, then drag the `if`
  into the loop and run it again. Two runs, thirty seconds, and the idea is theirs.
- If the four arrow-key scripts are eating the clock, hand them the movement pre-built. Movement is not
  today's skill; the wall check is.
- **Never cut:** the sprite being stopped by the wall, and the student saying in their own words that the
  check happens over and over.

## 7. Student Templates / Starter Materials

- **Pre-filled:** `starter_maze.sb3` ships with the maze backdrop drawn, the sprite placed at the start,
  and the last-safe-position variable already created. The project runs; the sprite just ignores walls.
- **Student writes:** the four movement scripts, both `if` blocks, and their ✏️ written predictions for the
  three-block script and for each remix.
- **Convention reminder:** ✏️ marks something written down before anything is run. In this track the
  prediction is about behaviour — "the sprite will say Ouch" — and a blank one is an incomplete exercise.

## 8. Teacher Prep Notes

- **Before class:** open `starter_maze.sb3` and **confirm the wall black is `#000000`**. A backdrop
  re-saved through a PNG editor can come back as `#010101` and Step 3 silently fails. Have
  `solution_maze.sb3` in a second tab. Know which corner of the maze the "change by 20" experiment breaks.
- **Known gotchas:**
  1. **The `if` outside the `forever` loop.** The single most common build error. Do not correct it on
     sight — let them run it and watch the sprite pass through the wall, then ask why.
  2. **Eyedropper on the sprite, not the backdrop.** Picks the sprite's own colour, so the check is true
     forever and the sprite freezes at the start. Looks like a different bug entirely.
  3. **`stop all` inside the wrong `if`.** Ends the project the moment it touches a wall. Ask which
     question it is sitting under.
  4. **Screenshots go stale.** If the Scratch UI has shifted since the step images were captured, say so
     out loud rather than letting the student hunt for a palette that moved.
- **Likely misconceptions:**
  1. *"The sprite decided to stop."* It ran a check you wrote. The Reflection question makes this explicit.
  2. *"`touching color` means near that colour."* Exact match only. The near-black remix is the cure.
  3. *"The check happens once when I click the flag."* The `forever` loop is what makes it continuous.
  4. *"Black is black."* Two blacks that look identical on screen are different values to Scratch.
- **Language note:** say **"the hexagon slot only takes a yes-or-no question"**. For the loop, say
  **"asking over and over"**, not "polling". At the remix, say **"close is not touching"** — it is the
  phrase students repeat back weeks later. Ask **"where is this `if` sitting?"** rather than pointing at
  the mistake.
