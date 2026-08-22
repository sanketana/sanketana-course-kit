# Practice — The Sprite Decides

Extra projects for when the maze is working and there's time left. Pick one; they're
independent. Each is harder than the classwork on purpose.

## Practice Projects

### 1. The key that opens the door

Add a yellow key sprite to the maze. The exit only works once the sprite has touched the key.

**The stretch:** the exit check needs to ask two questions at once — touching red *and* has the
key. You'll need a variable to remember the key, because sensing blocks only know about right
now, and the key won't still be under the sprite when it reaches the door.

**Done when:** walking onto the exit without the key does nothing, and with the key it finishes.

### 2. The patrolling guard

Add a second sprite that moves back and forth across a corridor on its own. If the player
touches it, they go back to the start.

**The stretch:** the guard needs its own `forever` loop running at the same time as the
player's. Two scripts, both looping, both checking — and neither one waits for the other.

**Done when:** the guard patrols without you touching the keyboard, and catching the player
sends them home from anywhere in the maze.

### 3. Break it on purpose

Make three copies of your project. In the first, move the wall check outside the `forever`
loop. In the second, swap the order of the wall and exit checks. In the third, change the wall
colour to a black one shade off.

**The stretch:** before you run each one, write down what you think will go wrong. Then run it.

**Done when:** you have three broken projects and can explain, for each, exactly which of the
three ideas from today it breaks.
