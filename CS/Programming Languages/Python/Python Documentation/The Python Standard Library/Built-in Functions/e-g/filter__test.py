"""filter(function, iterable)"""
# https://www.programiz.com/python-programming/methods/built-in/filter

import numpy as np

"""Construct an iterator from those elements of 'iterable' for which 'function' returns true.
'iterable' may be either a sequence, a container which supports iteration, or an iterator.
If function is None, the identity function is assumed, that is, all elements of iterable that are false are removed."""
iterable = list(range(0, 10))
print(f"iterable: {iterable}")
iterable_filtered = list(filter(lambda x: x % 2 == 0, iterable))
iterable_filtered_2 = list(filter(None, iterable))
print(f"iterable_filtered: {iterable_filtered}")
print(f"iterable_filtered_2: {iterable_filtered_2}\n")


"""Note that filter(function, iterable) is equivalent to the generator expression
(item for item in iterable if function(item)) if function is not None
and (item for item in iterable if item) if function is None."""
print(f"list((item for item in iterable if item % 2 == 0)):"
      f"{list((item for item in iterable if item % 2 == 0))}\n")
print(f"list(item for item in iterable if item): {list(item for item in iterable if item)}\n")



array = np.arange(0, 10, dtype='int8')
print(f"array: {array}")
print(f"type(array[0]): {type(array[0])}")
print(f"array.size: {array.size}")
print(f"array[array % 2 == 0]: {array[array % 2 == 0]}")
print(f"array[array > 0]: {array[array > 0]}\n")


# How filter() works for iterable list?
# list of alphabets
alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# function that filters vowels
def filterVowels(alphabet):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if(alphabet in vowels):
        return True
    else:
        return False

filteredVowels = filter(filterVowels, alphabets)
print(f'The filtered vowels are: {list(filteredVowels)}\n')



# How filter() method works without the filter function?
# random list
randomList = [1, 'a', 0, False, True, '0']

"""When we loop through the final filteredList, we get the elements which are true: 1, a, True and '0'
('0' as a string is also true)."""
filteredList = filter(None, randomList)
print(f"randomList: {randomList}")
print(f'The filtered elements are: {list(filteredList)}')