# Lesson 3 — The Sprite Decides

## Lesson Theme

Until now your sprite did the same thing every time you clicked the green flag. Today it
starts to notice the world and choose: stop at a wall, speed up on green, say something
only when a key is pressed.

## What You'll Build

A maze runner that stops when it touches the black walls and celebrates when it reaches the red exit.

## Tools Used

- Scratch (browser)
- `assets/starter_maze.sb3`

## What You'll Learn

- The hexagon slot in `if` takes a question with a yes/no answer
- `if` / `else` chooses one of two paths, never both
- Sensing blocks (`touching color`) ask the stage what's happening *right now*

## Predict the Output

![Three blocks: when flag clicked, if touching color black then say Ouch](assets/predict-touching.png)

The sprite is sitting on white. You click the flag. Does it say "Ouch"? Write your answer, then run it.

Now drag the sprite onto black and click the flag again. Different? Why did the first run say nothing?

## Build Steps

### 1. Open the starter and find the walls (3 min)

Open `assets/starter_maze.sb3`. The maze is drawn on the backdrop; walls are pure black.

![Starter project open](assets/step-01-open.png)

### 2. Make the sprite move with arrow keys (8 min)

Four `when key pressed` hats, each changing x or y by 5. Why 5? Try 20 and see what goes wrong at the corners.

![Four key-press scripts](assets/step-02-arrows.png)

### 3. Add the wall check (10 min)

Inside a `forever` loop: `if touching color black then` → move back the way you came.
We'll use `go to x: y:` with the last safe position for now.

![Forever loop with touching-color check](assets/step-03-wall.png)

### 4. Add the exit (6 min)

Second `if`: touching red → `say "Out!"` and `stop all`.

![Exit check added](assets/step-04-exit.png)

## Remix Challenge

Before you try it: what happens if you swap the order of the two `if` blocks? Predict, then swap.

Now change the wall colour check to a slightly different black (use the picker on the backdrop edge). Why does it stop working?

## Reflection

- Explain the `forever` loop to me as if I've never seen Scratch. Why does the wall check need to be inside it?
- When did `touching color` give you a wrong answer? What was it actually checking?
- Your sprite "decides" to stop. Did it decide, or did you?

## Key Takeaways

- `if` asks a question every time it runs, not once.
- Sensing blocks only know what's on the stage at that moment.
- Colours in Scratch must match exactly — close is not touching.
