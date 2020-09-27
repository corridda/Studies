"""max(iterable, *iterables[, key, default])
max(arg1, arg2, *args[, key])"""
# https://www.programiz.com/python-programming/methods/built-in/max

"""Return the largest item in an iterable or the largest of two or more arguments.

If one positional argument is provided, it should be an iterable. The largest item in the iterable is returned.
If two or more positional arguments are provided, the largest of the positional arguments is returned.
There are two optional keyword-only arguments. The key argument specifies a one-argument ordering function
like that used for list.sort(). The default argument specifies an object to return if the provided iterable is empty.
If the iterable is empty and default is not provided, a ValueError is raised.
If multiple items are maximal, the function returns the first one encountered.
This is consistent with other sort-stability preserving tools such as sorted(iterable, key=keyfunc, reverse=True)[0]
and heapq.nlargest(1, iterable, key=keyfunc)."""

# empty iterable
try:
    print(f"max([]): {max([])}")
except ValueError as e:
    print(repr(e))

print(f"max([]): {max([], default=0)}\n")


# Example 1: Find maximum among the given numbers
# using max(arg1, arg2, *args)
print(f'Maximum is: {max(1, 3, 2, 5, 4)}')

# using max(iterable)
num = [1, 3, 2, 8, 5, 10, 6]
print(f'Maximum is: {max(num)}\n')


# Example 2: Find number whose sum of digits is largest using key function
"""Here, each element in the passed argument (list or argument) is passed to the same function sumDigit().
Based on the return value of the sumDigit(), i.e. sum of the digits, the largest is returned."""
def sumDigit(num):
    sum = 0
    while(num):
        sum += num % 10
        num = int(num / 10)
    return sum

# using max(arg1, arg2, *args, key)
print(f'Maximum is: {max(100, 321, 267, 59, 40, key=sumDigit)}')

# using max(iterable, key)
num = [15, 300, 2700, 821, 52, 10, 6]
print(f'Maximum is: {max(num, key=sumDigit)}\n')


# Example 3: Find list with maximum length using key function
"""In this program, each iterable num, num1 and num2 is passed to the built-in method len().
Based on the result, i.e. length of each list, the list with maximum length is returned."""
num = [15, 300, 2700, 821]
num1 = [12, 2]
num2 = [34, 567, 78]

# using max(iterable, *iterables, key)
print(f'Maximum is: {max(num, num1, num2, key=len)}')
