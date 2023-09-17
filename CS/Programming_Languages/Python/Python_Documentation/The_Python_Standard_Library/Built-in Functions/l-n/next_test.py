"""next(iterator[, default])"""
# https://www.programiz.com/python-programming/methods/built-in/next

"""Retrieve the next item from the iterator by calling its __next__() method. If default is given,
it is returned if the iterator is exhausted, otherwise StopIteration is raised."""



# Example 1: How next() works?
random = [5, 9, 'cat']
print(f"random: {random}")

# converting list to iterator
# A list is an iterable and you can get iterator from it by using iter() function in python.
randomIterator = iter(random)
print(f"randomIterator: {randomIterator}")

# Output: 5
print(f"next(randomIterator): {next(randomIterator)}")

# Output: 9
print(f"next(randomIterator): {next(randomIterator)}")

# Output: 'cat'
print(f"next(randomIterator): {next(randomIterator)}")

# This will raise Error - iterator is exhausted
try:
    print(f"next(randomIterator): {next(randomIterator)}")
except StopIteration as e:
    print(repr(e))

# But this won't raise an error
print(f"next(randomIterator): {next(randomIterator, 'Iterator is exhausted')}\n")




# Example 2: Iterator With Default Value
random = [5, 9]
print(f"random: {random}")

# converting list to iterator
randomIterator = iter(random)

# Output: 5
print(f"next(randomIterator, '-1'): {next(randomIterator, '-1')}")

# Output: 9
print(f"next(randomIterator, '-1'): {next(randomIterator, '-1')}")

# randomIterator is exhausted
# Output: '-1'
print(f"next(randomIterator, '-1'): {next(randomIterator, '-1')}")
print(f"next(randomIterator, '-1'): {next(randomIterator, '-1')}")
print(f"next(randomIterator, '-1'): {next(randomIterator, '-1')}")
