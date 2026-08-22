# Solutions — Lesson 3 (teacher only)

## 1. Speed limit

```python
speed = int(input("Speed: "))
if speed < 50:
    print("Fine")
elif speed < 70:
    print("Warning")
else:
    print("Too fast")
```

Watch for students who write `elif speed >= 50 and speed < 70` — correct but redundant. Ask
why the first condition already rules out below-50.

## 2. Predict first

Prints `A` then `B`. Common wrong answer: `A` only, from reading the two `if`s as one chain.
The second `if` is independent; only the `else` belongs to it.

## 3. Three-way greeting

Any consistent boundaries are fine. The point is the one-line justification — look for a reason,
not a shrug.
