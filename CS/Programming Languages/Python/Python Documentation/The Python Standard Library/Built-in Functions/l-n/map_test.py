"""map(function, iterable, ...)"""
# https://www.programiz.com/python-programming/methods/built-in/map

"""Return an iterator that applies 'function' to every item of 'iterable', yielding the results.
If additional iterable arguments are passed, function must take that many arguments and is applied to the items
from all iterables in parallel. With multiple iterables, the iterator stops when the shortest iterable is exhausted.
For cases where the function inputs are already arranged into argument tuples, see itertools.starmap().

The returned value from map() (map object) then can be passed to functions like list() (to create a list),
set() (to create a set) and so on."""

# Example 1: How map() works?
def calculateSquare(n):
  return n*n

numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
print(f"result: {result}")

# converting map object to set
numbersSquare = set(result)
print(f"numbersSquare: {numbersSquare}\n")



"""Since map() expects a function to be passed in, lambda functions are commonly used
while working with map() functions."""

# Example 2: How to use lambda function with map()?
# There is no difference in functionalities of this example and Example 1.
numbers = (1, 2, 3, 4)
result = map(lambda x: x*x, numbers)
print(f"result: {result}")

# converting map object to set
numbersSquare = set(result)
print(f"numbersSquare: {numbersSquare}\n")



# Example 3: Passing Multiple Iterators to map() Using Lambda
num1 = [4, 5, 6]
num2 = [5, 6, 7]

result = map(lambda n1, n2: n1+n2, num1, num2)
print(f"list(result): {list(result)}")
