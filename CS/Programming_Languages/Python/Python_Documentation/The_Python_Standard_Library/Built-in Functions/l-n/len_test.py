"""len(s)"""
# https://www.programiz.com/python-programming/methods/built-in/len

"""Return the length (the number of items) of an object. The argument may be a sequence (such as a string,
bytes, tuple, list, or range) or a collection (such as a dictionary, set, or frozen set).
Failing to pass an argument or passing an invalid argument will raise a TypeError exception."""


class Session:
    def __init__(self, number=0):
        self.number = number

    def __len__(self):
        return self.number


# Example 1: How len() works with tuples, lists and range?
testList = []
print(testList, 'length is', len(testList))

testList = [1, 2, 3]
print(testList, 'length is', len(testList))

testTuple = (1, 2, 3)
print(testTuple, 'length is', len(testTuple))

testRange = range(1, 10)
print('Length of', testRange, 'is', len(testRange))
print()



# Example 2: How len() works with strings and bytes?
testString = ''
print('Length of', testString, 'is', len(testString))

testString = 'Python'
print('Length of', testString, 'is', len(testString))

# byte object
testByte = b'Python'
print('Length of', testByte, 'is', len(testByte))

testList = [1, 2, 3]

# converting to bytes object
testByte = bytes(testList)
print('Length of', testByte, 'is', len(testByte))
print()



# Example 3: How len() works with dictionaries and sets?
testSet = {1, 2, 3}
print(testSet, 'length is', len(testSet))

# Empty Set
testSet = set()
print(testSet, 'length is', len(testSet))

testDict = {1: 'one', 2: 'two'}
print(testDict, 'length is', len(testDict))

testDict = {}
print(testDict, 'length is', len(testDict))

testSet = {1, 2}
# frozenSet
frozenTestSet = frozenset(testSet)
print(frozenTestSet, 'length is', len(frozenTestSet))
print()



# Example 4: How len() works for custom objects?
# default length is 0
s1 = Session()
print(f"len(s1): {len(s1)}")

# giving custom length
s2 = Session(6)
print(f"len(s1): {len(s2)}")
