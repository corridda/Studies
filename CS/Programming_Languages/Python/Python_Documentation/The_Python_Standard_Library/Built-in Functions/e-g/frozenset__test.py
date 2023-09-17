"""class frozenset([iterable])"""
# https://www.programiz.com/python-programming/methods/built-in/frozenset

"""The frozenset() method returns an immutable frozenset object, optionally with elements taken from iterable."""

fz = frozenset([1, 2 ,3 ,4, 5])
print(f"{fz}")
print(f"type(fz): {type(fz)}")

"""Frozen set is just an immutable version of a python set object.
While elements of a set can be modified at any time, elements of frozen set remains the same after creation."""
try:
    fz.add([6, 7 , 8])
except AttributeError as e:
    print(repr(e))
print()

# Example 1: How frozenset() works in python?
# tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'u')

fSet = frozenset(vowels)
print('The frozen set is:', fSet)
print(f'The empty frozen set is: {frozenset()}\n')


# Example 2: frozenset() for Dictionary
"""When you use dictionary as an iterable for a frozen set, it only takes key of the dictionary to create the set:"""
# random dictionary
person = {"name": "John", "age": 23, "sex": "male"}
print(f"person: {person}")
fSet = frozenset(person)
print(f'The frozen set is: {fSet}')
