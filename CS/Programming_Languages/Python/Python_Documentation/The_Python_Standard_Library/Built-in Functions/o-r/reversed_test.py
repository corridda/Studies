"""reversed(seq)"""
# https://www.programiz.com/python-programming/methods/built-in/reversed

"""Return a reverse iterator. seq must be an object which has a __reversed__() method
or supports the sequence protocol (the __len__() method and the __getitem__() method with integer arguments
starting at 0) such as tuple, string, list or range."""



# Example 1: How reversed works for a sequence: string, tuple, list and range?

# for string
seqString = 'python'
print(list(reversed(seqString)))

# for tuple
seqTuple = ('P', 'y', 't', 'h', 'o', 'n')
print(list(reversed(seqTuple)))

# for range
seqRange = range(5, 9)
print(list(reversed(seqRange)))

# for list
seqList = [1, 2, 4, 3, 5]
print(list(reversed(seqList)))
print()



# Example 2: How reversed works for custom objects by implementing __reversed__()?

class Vowels:
    vowels = ['a', 'e', 'i', 'o', 'u']

    def __reversed__(self):
        return reversed(self.vowels)

v = Vowels()
print(list(reversed(v)))