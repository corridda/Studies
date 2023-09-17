"""sum(iterable[, start])"""
# https://www.programiz.com/python-programming/methods/built-in/sum

"""Sums start and the items of an iterable from left to right and returns the total. 'start' defaults to 0.
The iterable’s items are normally numbers, and the start value is not allowed to be a string.
For some use cases, there are good alternatives to sum(). The preferred, fast way to concatenate
a sequence of strings is by calling ''.join(sequence). To add floating point values with extended precision,
see math.fsum(). To concatenate a series of iterables, consider using itertools.chain().
"""

# Example: How sum() function works in python?

numbers = [2.5, 3, 4, -5]

# start parameter is not provided
numbersSum = sum(numbers)
print(f"numbersSum: {numbersSum}")

# start = 10
numbersSum = sum(numbers, 10)
print(f"numbersSum: {numbersSum}")


