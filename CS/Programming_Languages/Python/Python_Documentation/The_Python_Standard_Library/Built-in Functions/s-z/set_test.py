"""class set([iterable])"""
# https://www.programiz.com/python-programming/methods/built-in/set

"""Return a new set object, optionally with elements taken from iterable. set is a built-in class.
See set and Set Types — set, frozenset for documentation about this class.

For other containers see the built-in frozenset, list, tuple, and dict classes, as well as the collections module.
"""


# Example 1: How set() works for a sequence: string, tuple, list, range?

# empty set
# Note: Empty sets cannot be created using {}, use set()
print(f"set(): {set()}")

# from string
print(f"set('Python'): {set('Python')}")

# from tuple
print(f"set(('a', 'e', 'i', 'o', 'u')): {set(('a', 'e', 'i', 'o', 'u'))}")

# from list
print(f"set(['a', 'e', 'i', 'o', 'u']): {set(['a', 'e', 'i', 'o', 'u'])}")

# from range
print(f"set(range(5)): {set(range(5))}\n")



# Example 2: How set() works for a collection: set, dictionary and frozen set?

# from set
print(f"set({'a', 'e', 'i', 'o', 'u'}): {set({'a', 'e', 'i', 'o', 'u'})}")

# from dictionary
# Note: Dictionary keys are used for set creation. And, ordering of the elements may not be the same.
print('from dictionary: ')
print(f"{set({'a':1, 'e': 2, 'i':3, 'o':4, 'u':5})}")

# from frozen set
frozenSet = frozenset(('a', 'e', 'i', 'o', 'u'))
print(f"set(frozenSet): {set(frozenSet)}\n")



# Example 3: How set() works for custom iterable object?

class PrintNumber:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if(self.num >= self.max):
            raise StopIteration
        self.num += 1
        return self.num

printNum = PrintNumber(5)

# creating a set
print(f"set(printNum): {set(printNum)}")