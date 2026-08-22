# Practice — Functions That Answer Back

Two projects for when the temperature file is working and there's time left. Take either one.

## Practice Projects

### 1. The converter set

Write `converters.py` with three functions: miles to kilometres, kilograms to pounds, and hours to minutes.
Every one of them returns; none of them prints.

**The stretch:** at the bottom of the file, print a small table of five conversions using those functions —
without adding a single `print` inside any of them. All the printing happens in one place, at the end.

**Done when:** the table appears, and you can delete the printing section entirely without touching the
three functions or breaking them.

### 2. The receipt

Write `receipt.py`. A function `receipt_line(item, price, quantity)` builds a line of text like
`3 x apples ......... 2.40` and hands it back. A second function adds up a basket total.

**The stretch:** this one genuinely wants to print — a receipt is a thing you look at. Build it so it
doesn't: the functions return text and numbers, and one loop at the bottom prints them. Then write two
sentences on which version you'd rather have if the receipt later needed saving to a file instead.

**Done when:** nothing inside either function prints, the receipt still appears on screen, and you can say
what changing it to print would have cost you.
