"""class list([iterable])"""
# https://www.programiz.com/python-programming/methods/built-in/list

"""Rather than being a function, list is actually a mutable sequence type, as documented in Lists
and Sequence Types — list, tuple, range.
The list() constructor creates a list in python.

python list() constructor takes a single argument:
iterable (Optional) - an object that could be a sequence (string, tuples) or collection (set, dictionary)
or iterator object.

If no parameters are passed, it creates an empty list.
If iterable is passed as parameter, it creates a list of elements in the iterable."""


class PowTwo:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if (self.num >= self.max):
            raise StopIteration
        result = 2 ** self.num
        self.num += 1
        return result


# Example 1: Create list from sequence: string, tuple and list
# empty list
print(f"list(): {list()}")

# vowel string
vowelString = 'aeiou'
print(f"vowelString: {vowelString}")
print(f"list(vowelString): {list(vowelString)}\n")

# vowel tuple
vowelTuple = ('a', 'e', 'i', 'o', 'u')
print(f"vowelTuple: {vowelTuple}")
print(f"list(vowelTuple): {list(vowelTuple)}\n")

# vowel list
vowelList = ['a', 'e', 'i', 'o', 'u']
print(f"vowelList: {vowelList}")
print(f"list(vowelList): {list(vowelList)}\n")


# Example 2: Create list from collection: set and dictionary
# vowel set
vowelSet = {'a', 'e', 'i', 'o', 'u'}
print(f"vowelSet: {vowelSet}")
print(f"list(vowelSet): {list(vowelSet)}\n")

# vowel dictionary
vowelDictionary = {'a': 1, 'e': 2, 'i': 3, 'o':4, 'u':5}
print(f"vowelDictionary: {vowelDictionary}")
# Note: Keys in the dictionary are used as elements of the returned list.
print(f"list(vowelDictionary): {list(vowelDictionary)}\n")


# Example 3: Create list from custom iterator object
powTwo = PowTwo(5)
powTwoIter = iter(powTwo)
print(f"list(powTwoIter): {list(powTwoIter)}")


