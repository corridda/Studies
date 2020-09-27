"""sorted(iterable, *, key=None, reverse=False)"""
# https://www.programiz.com/python-programming/methods/built-in/sorted

"""Return a new sorted list from the items in iterable.
Has two optional arguments which must be specified as keyword arguments.
'key' specifies a function of one argument that is used to extract a comparison key
from each list element: key=str.lower. The default value is None (compare the elements directly).
'reverse' is a boolean value. If set to True, then the list elements are sorted as if each comparison were reversed.
Use functools.cmp_to_key() to convert an old-style cmp function to a key function.
The built-in sorted() function is guaranteed to be stable. A sort is stable if it guarantees
not to change the relative order of elements that compare equal — this is helpful for sorting in multiple passes
(for example, sort by department, then by salary grade).
"""


# Example 1: Sort a given sequence: string, list and tuple

# vowels list
pyList = ['e', 'a', 'u', 'o', 'i']
print(f"sorted(pyList): {sorted(pyList)}")

# string
pyString = 'Python'
print(f"sorted(pyString): {sorted(pyString)}")

# vowels tuple
pyTuple = ('e', 'a', 'u', 'o', 'i')
print(f"sorted(pyTuple): {sorted(pyTuple)}\n")


"""Note: A list also has sort() method which performs the same way as sorted().
Only difference being, sort() method doesn't return any value and changes the original list itself."""




# Example 2: Sort a given collection in descending order: set, dictionary and frozen set

# set
pySet = {'e', 'a', 'u', 'o', 'i'}
print(f"sorted(pySet, reverse=True): {sorted(pySet, reverse=True)}")

# dictionary
pyDict = {'e': 1, 'a': 2, 'u': 3, 'o': 4, 'i': 5}
print(f"sorted(pyDict, reverse=True): {sorted(pyDict, reverse=True)}")

# frozen set
pyFSet = frozenset(('e', 'a', 'u', 'o', 'i'))
print(f"sorted(pyFSet, reverse=True): {sorted(pyFSet, reverse=True)}\n")



# Example 3: Sort the list using sorted() having a key function

# take second element for sort
def takeSecond(elem):
    return elem[1]

# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# sort list with key
sortedList = sorted(random, key=takeSecond)

# print list
print(f'Sorted list: {sortedList}')
