# Lesson 3 — Making Decisions

## Lesson Theme

So far your programs run top to bottom and do the same thing every time. Today they start
to *react*: a robot that stops when the battery is low, a greeting that changes with the
time of day. Decisions are where programs begin to feel alive.

## What You'll Build

`battery_check.py` — a program that reads a battery percentage and prints one of three
messages: go, warn, or stop.

## Tools Used

- VS Code with Python 3.12
- `code/predict_decisions.py`, `code/starter_battery.py`

## What You'll Learn

- Comparisons produce a boolean: `7 > 5` is `True`, not "yes"
- `if` / `elif` / `else` and why indentation is not decoration
- The difference between `=` and `==`, and what happens when you mix them up

## In Class

### Recap and the bridge from Scratch (6 min)

You've used the orange `if` block in Scratch. Ask: what went inside the hexagon slot?
Something that was true or false. Same idea, now in text.

### Predict the Output (12 min)

Open `code/predict_decisions.py`. Don't run it. Write down what each of the four `print`
lines will show. Then run it and compare.

Most students get line 3 wrong. Talk about why: `5 > 5` is not true, and Python doesn't round up.

### Build: battery check (22 min)

Open `code/starter_battery.py`. It reads a number. Add the decision:

- 50 or above → `All good. Drive on.`
- 20 to 49 → `Low battery. Head back.`
- below 20 → `Stop. Charge now.`

Test with 75, 35, 10, and then 50 and 20 exactly. The boundaries are where bugs hide.

### Bug Hunt (8 min)

```python
battery = 35
if battery = 50:
    print("Half full")
```

Before running: what do you think happens? Run it. Read the error out loud.
`=` puts a value in; `==` asks a question. You will make this mistake again. Everyone does.

### Reflection and Key Takeaways (7 min)

See below.

## Reflection

- Explain to me, without looking at the code, how Python decides which branch to run.
- Where did your prediction go wrong, and what did you believe that wasn't true?
- A real robot using this code would stop at 19% but keep going at 20%. Is that the right line? Who decides?

## Key Takeaways

- A comparison is a question with a `True`/`False` answer.
- `if` runs its block only when the answer is `True`; `else` catches everything else.
- `=` assigns, `==` compares. Say it twice.
