# Asking a Better Question

## The Idea

An AI tool answers the question you asked. Not the one you meant, not the one you would have asked if
you'd thought about it for another minute — the one you actually typed.

That sounds obvious until you watch what people do when an answer disappoints them. They add "please".
They add "be detailed". They add "this is really important". None of it helps much, because none of it
is **information the tool didn't already have**.

Here is the same request, three times:

> *"Make me a study plan."*

You get something. It's structured, it's confident, and it's for nobody in particular — three hours a
day, subjects it invented, a start date it guessed.

> *"Make me a study plan. I have Physics, Maths and Chemistry. The exam is on 14 March. I get about
> two hours on weekdays and nothing on Sunday."*

Now it's a plan for your actual week. The difference wasn't politeness. It was five facts the tool had
no way of knowing.

> *"…and a good plan for me means short sessions, one hard subject a day, and nothing that assumes I'll
> revise at 6am."*

Now it's a plan you might actually follow. The last addition wasn't more information about your
situation — it was what **good** means to you.

## How It Works

A prompt has three jobs, and most weak prompts only do the first.

**The task** — what you want done. "Make me a study plan." Almost everyone gets this right; it's the
easy part, and on its own it's why the first answer was generic.

**The context** — what the tool can't see. Your subjects, your date, your hours, the fact that you
share a room with a younger brother who practises drums. The tool has read a great deal about study
plans in general and knows nothing whatsoever about you. Every fact you leave out, it invents.

**The standard** — what a good answer looks like. This is the one people skip. Without it the tool
falls back on what *usually* counts as good: long, thorough, evenly spread, ambitious. Which may be
exactly wrong for you.

Once you've written a standard, something else becomes possible. You can **judge the answer**.

This is the part that matters more than the prompting. An output on its own can't be good or bad — it
can only be good or bad *against something*. If you decide whether you like a plan after you've read
it, you'll pick the one that looks the most impressive: the longest, the most formatted, the one with
a table. If you write down three lines first and rank against those, you'll pick the one that fits.

The order is the whole skill: **standard first, output second.**

## Worked Example

Three study plans, written for the same student. Rank them.

**Plan A** — five bullet points, plain text, one subject per weekday evening, forty-minute blocks,
Sundays left empty.

**Plan B** — a formatted table with colour-coded subjects, motivational headers, a daily reflection
prompt, and a reading list. Six hours a day, seven days a week.

**Plan C** — three lines. Physics Monday and Thursday, Maths Tuesday and Friday, Chemistry Wednesday.
No detail beyond that.

Most people rank B first. It looks like the most effort went into it. It is also the only one of the
three that cannot be done — nobody has six hours a day, and the student said they don't work Sundays.
It ignores the constraints while looking magnificent.

Now rank them against a written standard: *short sessions · one hard subject a day · nothing on
Sunday.* A is the only one that satisfies all three. C satisfies two and is too thin to act on. B
satisfies none.

Same three plans, different order — and the second order is defensible, because you can point at the
line each one broke. That's the difference between an opinion about an output and a judgment of it.

## Vocabulary

| term | what it means |
|---|---|
| prompt | Everything you send the tool: task, context and standard together. |
| context | The facts the tool has no way of knowing unless you say them. |
| constraint | A limit the answer has to respect — a date, an hour count, a rule. |
| standard | What *you* decided a good answer looks like, written down before you see one. |
| generic output | A plausible answer built for nobody, which is what you get when you supply no context. |

## Common Mistakes

**Adding politeness instead of information.** "Please could you make it really good" adds nothing the
tool can use. Ask yourself: *what does it not know?*

**Confusing longer with better.** A longer prompt full of vague enthusiasm is still a vague prompt.
Three concrete facts beat three paragraphs.

**Judging by presentation.** Formatting is cheap. A table is not evidence of thought, and neither is a
confident tone.

**Writing the standard after reading the answer.** By then it isn't a standard, it's a justification —
you'll write down whatever the answer you already liked happens to do.

**Assuming there's one right way to prompt.** There isn't. There is a right way to *judge*, and better
prompts follow from knowing what you'd accept.

**Forgetting where the words go.** Your prompt contains your subjects, your weak spots, your exam
dates. That is real information about you, typed into a service that keeps it.

## Where This Shows Up

Every time you ask a tool for anything — an explanation, a summary, a first draft, some code. The
question is never "is this good?" but "good against what?"

Next lesson you'll give the tool a **role** and see how much that changes an answer on its own, which
is really a shortcut for supplying a pile of context at once.

And the standard outlives the tool completely. Deciding what you'd accept before you see what you're
offered is how you read a review, choose a phone, or mark your own homework.

## Key Takeaways

- The tool answers the question you typed, not the one you meant.
- Detail beats politeness. Ask what the tool doesn't know, and tell it that.
- A prompt does three jobs: task, context, standard. Most weak prompts only do the first.
- Write your standard **before** you see any output, or it isn't a standard.
- An output is only ever good *against something*. Presentation is not that something.
- Whatever you typed, you gave away. Notice what that was.
