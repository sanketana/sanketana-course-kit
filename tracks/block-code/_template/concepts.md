# The Sprite Decides

## The Idea

Your sprite has been following orders. Move ten steps, turn, say something — the same run every time you
click the flag. It walks straight through walls because nothing has ever asked it whether there was a
wall there.

A wall only becomes real when the program **checks**. That is what the `if` block does: it asks a
question about the world right now, and runs the blocks inside it only when the answer is yes.

Look at the shape of the slot in an `if` block. It's a hexagon, and Scratch won't let just anything drop
into it. A number block won't fit. A `x position` block won't fit. Only blocks that are already pointed
— sensing blocks, comparisons — will snap in, because those are the only ones that answer **yes or no**.

![Three blocks: when flag clicked, if touching color black then say Ouch](assets/predict-touching.png)

The shape is the rule, made visible. The hexagon takes questions.

## How It Works

An `if` block has two parts: the question in the hexagon, and the blocks stacked inside its mouth.

When the program reaches the `if`, it asks the question once, at that instant. Yes → run the inside
blocks. No → skip straight past them. Then it carries on to whatever comes next either way.

That word *once* is the trap. A check sitting on its own under `when flag clicked` asks its question
one single time, in the first fraction of a second after you click, and never again. The sprite could
sit on a wall for an hour and nothing would happen — the question already got its answer.

```
    when flag clicked                 when flag clicked
    if <touching black?> then         forever
        say "Ouch!"                       if <touching black?> then
                                              say "Ouch!"

    asked ONCE, at the click          asked again, and again, and again
    (sprite walks through walls)      (the wall is real)
```

Putting the check inside `forever` is what turns one question into a continuous one. The loop runs the
check dozens of times a second, so within a blink of the sprite touching black, the answer flips to yes
and the blocks inside fire.

**Two `if` blocks in a row are two separate questions.** Both get asked, both can fire on the same pass
through the loop. If the first one moves the sprite and the second one checks where the sprite is, then
the first one has already changed the answer to the second. That is why swapping their order can change
what the project does.

## Worked Example

The maze has black walls and a red exit, and the sprite is sitting on white when you click the flag.

The `forever` loop starts. First pass: is the sprite touching black? No — it's on white. Skip. Is it
touching red? No. Skip. Loop round.

You hold the right arrow. The sprite slides right, still on white, and the loop keeps asking and keeps
getting no. Then one pass happens where the sprite has just crossed onto a black pixel. *Now* the first
question answers yes, the blocks inside fire, and the sprite is pushed back to where it last stood
safely. Next pass it's on white again, and the answer goes back to no.

The wall never moved. What changed is that something was asking.

Now try this: pick the wall colour again with the eyedropper, but click on the very edge of the black,
where the paint has faded slightly against the backdrop. The project stops working. The sprite walks
through the wall as if the check weren't there.

It isn't broken. `touching color` matches **exactly**, and the colour you just picked is `#0A0A0A`
while the wall is `#000000`. To your eye they are both black. To Scratch they are two different colours,
and one of them is nowhere on the stage.

## Vocabulary

| term | what it means |
|---|---|
| condition | The question in the hexagon slot. Always answers yes or no. |
| hexagon slot | The pointed hole in an `if` block. Only yes/no blocks fit. |
| sensing block | A block that asks about the stage right now — `touching color`, `key pressed`, `mouse down`. |
| `forever` loop | Runs the blocks inside it over and over, without stopping. |
| branch | One path the project can take. An `if` / `else` has two. |

## Common Mistakes

**The check sits outside the `forever` loop.** The single most common one. It looks right, it runs
without error, and the sprite ignores every wall. Drag the `if` inside the loop and run it again — same
blocks, completely different project.

**Picking the colour off the sprite instead of the backdrop.** The eyedropper takes whatever pixel you
click. Click the sprite and the check becomes "am I touching myself?", which is always yes, so the
sprite freezes the instant you click the flag.

**Two blacks that aren't the same black.** Colours must match exactly. Close is not touching.

**`stop all` under the wrong question.** Put it inside the wall check instead of the exit check and the
whole project ends the first time the sprite brushes a wall.

**Expecting the sprite to remember.** Sensing blocks only know about this instant. There is no block for
"was touching black a second ago" — if the project needs to remember, you have to store it yourself.

## Where This Shows Up

Every game you have ever played is doing this, thousands of times a second: has the player hit
something, has the timer run out, is a key held down. The loop asks, the `if` decides.

Next lesson the same `if` block watches a **variable** instead of the stage — has the score passed 10?
— and the question stops being about pixels and starts being about anything you can measure.

And the `if` block is where "the sprite decided to stop" stops being true. It didn't decide. You wrote
the question, you chose which colour counted as a wall, and you picked what happens when the answer is
yes.

## Key Takeaways

- The hexagon slot only takes a question with a yes-or-no answer. That's what the shape is telling you.
- An `if` asks its question **every time it runs** — which is once, unless it's inside a loop.
- `forever` is what turns a single check into a continuous one.
- Sensing blocks know about right now, and nothing else.
- Colours match exactly. Close is not touching.
- Two `if` blocks in a row are two questions, and their order can change the answer.
