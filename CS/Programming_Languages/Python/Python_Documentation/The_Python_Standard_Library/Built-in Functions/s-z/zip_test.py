"""zip(*iterables)"""
# https://www.programiz.com/python-programming/methods/built-in/zip

"""Make an iterator that aggregates elements from each of the iterables.
Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences
or iterables. The iterator stops when the shortest input iterable is exhausted. With a single iterable argument,
it returns an iterator of 1-tuples. With no arguments, it returns an empty iterator.

The left-to-right evaluation order of the iterables is guaranteed. This makes possible an idiom for clustering
a data series into n-length groups using zip(*[iter(s)]*n). This repeats the same iterator n times so that
each output tuple has the result of n calls to the iterator. This has the effect of dividing the input
into n-length chunks.
zip() should only be used with unequal length input when you don’t care about trailing, unmatched values
from the longer iterables. If those values are important, use itertools.zip_longest() instead.
zip() in conjunction with the * operator can be used to unzip a list:
"""

x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
print(f"list(zipped): {list(zipped)}")
x2, y2 = zip(*zip(x, y))
print(f"x == list(x2) and y == list(y2): {x == list(x2) and y == list(y2)}\n")



# Example 1: How zip() works in python?

numberList = [1, 2, 3]
strList = ['one', 'two', 'three']

# No iterables are passed
result = zip()

# Converting itertor to list
resultList = list(result)
print(f"resultList: {resultList}")

# Two iterables are passed
result = zip(numberList, strList)

# Converting itertor to set
resultSet = set(result)
print(f"resultSet: {resultSet}\n")



# Example 2: Different Number of Elements in Iterables Passed to zip()

numbersList = [1, 2, 3]
strList = ['one', 'two']
numbersTuple = ('ONE', 'TWO', 'THREE', 'FOUR')

result = zip(numbersList, numbersTuple)

# Converting to set
resultSet = set(result)
print(f"resultSet: {resultSet}")

result = zip(numbersList, strList, numbersTuple)

# Converting to set
resultSet = set(result)
print(f"resultSet: {resultSet}\n")



# Example 3: Unzipping the Value Using zip()

coordinate = ['x', 'y', 'z']
value = [3, 4, 5, 0, 9]

result = zip(coordinate, value)
resultList = list(result)
print(f"resultList: {resultList}")

c, v =  zip(*resultList)
print(f'c = {c}, type(c): {type(c)}')
print('v =', v)

"""Notice that, elements 0 and 9 in variable value is not in variable v.
It's because the zipped iterables have different number of elements."""