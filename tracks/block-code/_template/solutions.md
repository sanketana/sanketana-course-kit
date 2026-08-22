# Solutions — Lesson 3 (teacher only)

Reference project: `assets/solution_maze.sb3`.

## 1. Second wall colour

Expect `change x by -5` style bounces that only work for one direction. Good moment to ask: how would the
sprite know which way it was going? (Sets up variables next lesson.)

## 2. Predict first

The check runs once, at flag click, before the sprite has moved. Nothing happens on green. Most students
predict it works. The gap is the whole lesson.

## 3. Timer

`reset timer` on flag click; `say (round (timer))` at the exit. Bonus if they use `join` to add "seconds".
