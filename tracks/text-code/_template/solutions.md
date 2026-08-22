# Solutions — Lesson 11 (teacher only)

## 1. The shopping list

```python
def line_total(price, quantity):
    return price * quantity

apples = line_total(0.80, 6)
bread = line_total(2.40, 1)
milk = line_total(1.15, 2)

print("Total:", round(apples + bread + milk, 2))
```

The deliberate break gives `TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'`.
Accept any wording of the reason that gets at *the function printed instead of handing the value back, so
the variables hold `None`*. A student who writes "because print doesn't work" has the observation without
the mechanism — ask them what `apples` is actually holding.

Watch for students who make it work by printing inside the function *and* keeping a running total in a
global variable. It runs, and it dodges the entire lesson. Ask them to compute the total without touching
anything outside the function.

## 2. Print or return?

1. `greet(name)` — print. Its whole job is the side effect; there's nothing to hand back.
2. `is_weekend(day)` — return. A question needs an answer the program can branch on.
3. `save_score(score)` — return is arguable; print is not. Most would say it returns nothing useful, though
   returning whether the save succeeded is defensible and better practice.
4. `average(numbers)` — return. This is the one they'll all get right.

**The arguable one is 3**, and a student who names 1 or 4 as arguable hasn't thought about it. Accept an
answer that spots 3 with any coherent reason. Full marks for noticing that a function can hand back
something about *how it went* even when it has no result of its own.
