"""range(stop)
    range(start, stop[, step])"""
# https://realpython.com/python-range/

import numpy as np

"""Rather than being a function, range is actually an immutable sequence type, as documented in
Ranges and Sequence Types — list, tuple, range."""

for i in range(3, 16, 3):
    quotient = i / 3
    print(f"{i} divided by 3 is {int(quotient)}.")
print()



"""range(stop)"""

"""When you call range() with one argument, you will get a series of numbers that starts at 0 and includes
every whole number up to, but not including, the number you have provided as the stop."""
print("range(stop)")
for i in range(3):
    print(i)
print()



"""range(start, stop)"""

"""When you call range() with two arguments, you get to decide not only where the series of numbers stops
but also where it starts, so you don’t have to start at 0 all the time. """
print("range(start, stop)")
for i in range(1, 8):
    print(i)
print()



"""range(start, stop, step)"""

"""When you call range() with three arguments, you can choose not only where the series of numbers
will start and stop but also how big the difference will be between one number and the next.
If you don’t provide a step, then range() will automatically behave as if the step is 1."""
print("range(start, stop, step)")
for i in range(1, 8):
    print(i)
print()

"""If your step is positive, then you move through a series of increasing numbers and are incrementing.
If your step is negative, then you move through a series of decreasing numbers and are decrementing."""
for i in range(10, -6, -2):
    print(i)
print()



# range() is a type in python:
print(f"type(range(3): {type(range(3))}")

# You can access items in a range() by index, just as you would with a list:
print(f"range(3)[1]: {range(3)[1]}")
print(f"range(3)[2]: {range(3)[2]}")

# You can even use slicing notation on a range(), but the output in a REPL may seem a little strange at first:
# (although that output may look odd, slicing a range() just returns another range().)
print(f"range(6)[2:5]: {range(6)[2:5]}\n")




"""Using NumPy"""

print("Using NumPy")
print(f"np.arange(0.3, 1.6, 0.3): {np.arange(0.3, 1.6, 0.3)}\n")

# If you want to print each number on its own line, you can do the following:
for i in np.arange(0.3, 1.6, 0.3):
    print(i)

