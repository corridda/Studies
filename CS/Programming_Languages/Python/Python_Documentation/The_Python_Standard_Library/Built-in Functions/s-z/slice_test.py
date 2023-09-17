"""class slice(stop)
    class slice(start, stop[, step])"""
# https://www.programiz.com/python-programming/methods/built-in/slice


"""Return a slice object representing the set of indices specified by range(start, stop, step).
The start and step arguments default to None. Slice objects have read-only data attributes start, stop
and step which merely return the argument values (or their default).
They have no other explicit functionality; however they are used by Numerical python
and other third party extensions. Slice objects are also generated when extended indexing syntax is used.
For example: a[start:stop:step] or a[start:stop, i]. See itertools.islice() for an alternate version
that returns an iterator.

The slice object is used to slice a given sequence (string, bytes, tuple, list or range)
or any object which supports sequence protocol (implements __getitem__() and __len__() method)."""



# Example 1: Create a slice object for slicing

# contains indices (0, 1, 2)
print(f"slice(3): {slice(3)}")

# contains indices (1, 3)
print(f"slice(1, 5, 2): {slice(1, 5, 2)}\n")



# Example 2: Get substring from a given string using slice object

pyString = 'python'

# contains indices (0, 1, 2)
# i.e. P, y and t
sObject = slice(3)
print(f"pyString: {pyString}\n")
print(f"sObject: {sObject}")
print(f"pyString[sObject]: {pyString[sObject]}")

# contains indices (1, 3)
# i.e. y and h
sObject = slice(1, 5, 2)
print(f"sObject: {sObject}")
print(f"pyString[sObject]: {pyString[sObject]}\n")



# Example 3: Get substring from a given string using negative index

# contains indices (-1, -2, -3)
# i.e. n, o and h
sObject = slice(-1, -4, -1)
print(f"sObject: {sObject}")
print(f"pyString[sObject]: {pyString[sObject]}\n")



# Example 4: Get sublist and sub-tuple from a given list and tuple respectively

pyList = ['P', 'y', 't', 'h', 'o', 'n']
pyTuple = ('P', 'y', 't', 'h', 'o', 'n')
print(f"pyList: {pyList}")
print(f"pyTuple: {pyTuple}")

# contains indices (0, 1, 2)
# i.e. P, y and t
sObject = slice(3)
print(f"sObject: {sObject}")

# slice a list
print(f"pyList[sObject]: {pyList[sObject]}")

# contains indices (1, 3)
# i.e. y and h
sObject = slice(1, 5, 2)
print(f"sObject: {sObject}")

# slice a tuple
print(f"pyTuple[sObject]: {pyTuple[sObject]}\n")



# Example 5: Get sublist and sub-tuple from a given list and tuple respectively using negative index

# contains indices (-1, -2, -3)
# i.e. n, o and h
sObject = slice(-1, -4, -1)
print(f"sObject: {sObject}")

# slice a list
print(f"pyList[sObject]: {pyList[sObject]}")

# contains indices (-1, -3)
# i.e. n and h
sObject = slice(-1, -5, -2)
print(f"sObject: {sObject}")

# slice a tuple
print(f"pyTuple[sObject]: {pyTuple[sObject]}\n")



# Example 6: Get substring from a given string by extending indexing syntax

"""The slice object can be substituted with the indexing syntax in python.
You can alternately use the following syntax for slicing:
obj[start:stop:step]"""

# contains indices (0, 1, 2)
# i.e. P, y and t
print(f"pyString[0:3]: {pyString[0:3]}")

# contains indices (1, 3)
# i.e. y and h
print(f"pyString[1:5:2]: {pyString[1:5:2]}")
