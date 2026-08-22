# Lesson 11 — Predict the Output
# Six lines print. Write down all six BEFORE you run this.
# The ones to look at: the two that print a stored result.

def shout(word):
    print(word.upper())

def whisper(word):
    return word.lower()

shout("hello")
whisper("WORLD")

stored_shout = shout("again")
print(stored_shout)

stored_whisper = whisper("QUIETLY")
print(stored_whisper)
