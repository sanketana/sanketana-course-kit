# Functions That Answer Back

## The Idea

You already know how to write a function. This one works:

```python
def to_celsius(f):
    print((f - 32) * 5 / 9)

to_celsius(67)
```

Run it and `19.44...` appears. Job done, apparently.

Now try to *use* that number for something:

```python
boston = to_celsius(67)
nairobi = to_celsius(81)
print((boston + nairobi) / 2)
```

```
TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
```

The function printed the answer. It never *gave* it to you. `boston` and `nairobi` are holding nothing —
and Python can't add nothing to nothing.

That's the distinction the whole lesson is about. `print` puts marks on a screen for a person to read.
`return` hands a value back to the line that called the function, so the rest of the program can carry on
with it. A function that prints has **done** something. A function that returns has **produced** something.

Only the second kind can be used to build anything bigger.

## How It Works

Change one word:

```python
def to_celsius(f):
    return (f - 32) * 5 / 9
```

Now follow what happens, line by line:

```python
boston = to_celsius(67)
```

1. Python reaches `to_celsius(67)` and jumps into the function with `f` set to `67`.
2. It works out `(67 - 32) * 5 / 9`, which is `19.44...`.
3. `return` sends that value **back to the line that asked for it**.
4. Back in the original line, `to_celsius(67)` has become `19.44...`, and that gets stored in `boston`.

Nothing appeared on screen — and that's correct. Returning is not showing. If you want to see it, catch it
and print it:

```python
print(to_celsius(67))
```

Now trace the version that only prints:

```python
def shout(word):
    print(word.upper())

stored = shout("hello")
print(stored)
```

1. `shout("hello")` runs and prints `HELLO`. You see it.
2. The function ends without a `return`.
3. Python still has to give the calling line *something*, so it gives `None`.
4. `stored` is `None`, and the next line prints `None`.

**`None` is a value.** It's not an error and not an empty box — it's Python's way of saying "I was never
told to hand anything back". Every function that lacks a `return` hands back `None`, quietly, every time.

Two more things follow from this.

**A returned value that nobody catches just evaporates.** This line runs, works, and shows nothing:

```python
to_celsius(81)      # the answer came back and landed nowhere
```

That is not a bug. It's a function doing its job and no one being there to take the result.

**Code after `return` never runs.** `return` ends the function immediately:

```python
def to_celsius(f):
    return (f - 32) * 5 / 9
    print("converted!")       # never happens, not once
```

## Vocabulary

| term | what it means |
|---|---|
| return value | The value a function hands back to the line that called it. |
| `None` | What a function hands back when it has no `return`. A real value, not an error. |
| caller | The line that used the function and is waiting for an answer. |
| call | Using a function: `to_celsius(67)`. |
| side effect | Something a function does other than hand back a value — printing, saving a file. |

## Common Mistakes

**Printing when you needed to return.** The one this lesson is built on. It's invisible until something
tries to use the result, which is often several lessons later.

**Expecting `return` to show something.** It doesn't. If you want to see a returned value, print it at the
call site. A returning function producing no output on screen is working correctly.

**Assuming `None` means broken.** When you see `None` where you expected a number, don't hunt for a crash.
Go and look at the function: it's missing a `return`.

**Putting the print after the return.**

```python
return answer
print("done")     # unreachable
```

If a line below `return` never seems to run, that's why.

**Making a function do both, out of habit.**

```python
def to_celsius(f):
    result = (f - 32) * 5 / 9
    print("Converted:", result)
    return result
```

This isn't wrong, and sometimes it's what you want. But it means the function can never be used quietly —
every single call prints, whether you wanted it to or not. Decide which job the function has.

## Where This Shows Up

Almost every function you have already used returns rather than prints. `len("hello")` doesn't print `5` —
it hands `5` back, which is why `if len(name) > 3:` works. So do `round()`, `input()` and `int()`. That's
not a coincidence: they were written to be building blocks.

It's also the reason the next lessons are possible at all. A function that calls another function needs an
answer to work with, so the inner one has to return. Once you can pass values back, small functions start
to stack into large programs, and that stacking is most of what programming is.

The choice itself never goes away. Every function you write from here, you decide: does this hand something
back, or does it just do a job? Getting that decision right is worth more than the syntax.

## Key Takeaways

- `print` sends a value to the screen. `return` sends it back to the line that called the function.
- A function without a `return` hands back `None`, every time, quietly.
- `None` is a value, not an error. Seeing it means a `return` is missing somewhere.
- A returned value that nobody catches disappears. That's not a bug.
- `return` ends the function; nothing below it runs.
- Only functions that return can be used to build bigger things.
