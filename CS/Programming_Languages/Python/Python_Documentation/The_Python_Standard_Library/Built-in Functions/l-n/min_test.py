"""min(iterable, *[, key, default])
    min(arg1, arg2, *args[, key])"""
# https://www.programiz.com/python-programming/methods/built-in/min

"""Return the smallest item in an iterable or the smallest of two or more arguments.
If one positional argument is provided, it should be an iterable. The smallest item in the iterable is returned.
If two or more positional arguments are provided, the smallest of the positional arguments is returned.
There are two optional keyword-only arguments. The key argument specifies a one-argument ordering function
like that used for list.sort(). The default argument specifies an object to return
if the provided iterable is empty. If the iterable is empty and default is not provided, a ValueError is raised.
If multiple items are minimal, the function returns the first one encountered.
This is consistent with other sort-stability preserving tools such as sorted(iterable, key=keyfunc)[0]
and heapq.nsmallest(1, iterable, key=keyfunc).
"""

try:
    print(f"min([]): {min([])}")
except ValueError as e:
    print(repr(e))
print(f"min([], default='empty sequance'): {min([], default='empty sequance')}\n")


# Example 1: Find minimum among the given numbers
# using min(arg1, arg2, *args)
print(f'Minimum is: {min(1, 3, 2, 5, 4)}')

# using min(iterable)
num = [3, 2, 8, 5, 10, 6]
print(f'Minimum is: {min(num)}\n')



# Example 2: Find number whose sum of digits is smallest using key function
def sum_of_digits(num: int) -> int:
    sum = 0
    while num > 0:
        temp = divmod(num, 10)
        sum += temp[1]
        num = temp[0]
    return sum

# using min(arg1, arg2, *args, key)
print(f'Minimum is: {min(100, 321, 267, 59, 40, key=sum_of_digits)}')

# using min(iterable, key)
num = [15, 300, 2700, 821, 52, 10, 6]
print(f'Minimum is: {min(num, key=sum_of_digits)}\n')

"""Here, each element in the passed argument (list or argument) is passed to the same function sumDigit().
Based on the return value of the sumDigit(), i.e. sum of the digits, the smallest is returned."""



# Example 3: Find list with minimum length using key function
num = [15, 300, 2700, 821]
num1 = [12, 2]
num2 = [34, 567, 78]

# using min(iterable, *iterables, key)
print(f'Minimum is: {min(num, num1, num2, key=len)}')

"""In this program, each iterable num, num1 and num2 is passed to the built-in method len().
Based on the result, i.e. length of each list, the list with minimum length is returned."""