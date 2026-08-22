# Lesson 11 — Temperatures (starter)
# Three conversions, the same arithmetic written out three times.
# Your job: pull the repeated line into a function, then make that function
# usable by the code at the bottom.

boston = (67 - 32) * 5 / 9
print("Boston:", round(boston, 1))

nairobi = (81 - 32) * 5 / 9
print("Nairobi:", round(nairobi, 1))

reykjavik = (38 - 32) * 5 / 9
print("Reykjavik:", round(reykjavik, 1))

# Uncomment these two once your function exists. They are the test of whether
# your function hands the answer back, or only shows it.
# average = (boston + nairobi + reykjavik) / 3
# print("Average:", round(average, 1))
