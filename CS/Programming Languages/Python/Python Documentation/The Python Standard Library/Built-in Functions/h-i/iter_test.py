"""iter(object[, sentinel])"""
# https://www.programiz.com/python-programming/methods/built-in/iter

"""Return an iterator object. The first argument is interpreted very differently depending on the presence
of the second argument. Without a second argument, object must be a collection object which supports
the iteration protocol (the __iter__() method), or it must support the sequence protocol (the __getitem__() method
with integer arguments starting at 0). If it does not support either of those protocols, TypeError is raised.
If the second argument, 'sentinel', is given, then object must be a callable object.
The iterator created in this case will call object with no arguments for each call to its __next__() method;
if the value returned is equal to sentinel, StopIteration will be raised, otherwise the value will be returned."""


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



# Example 1: How iter() works in Python?

# list of vowels
vowels = ['a', 'e', 'i', 'o', 'u']

vowelsIter = iter(vowels)

# prints 'a'
print(next(vowelsIter))

# prints 'e'
print(next(vowelsIter))

# prints 'i'
print(next(vowelsIter))

# prints 'o'
print(next(vowelsIter))

# prints 'u'
print(next(vowelsIter))

# StopIteration
try:
    print(next(vowelsIter))
except StopIteration as e:
    print(f"{repr(e)}\n")



# Example 2: How iter() works for custom objects?
printNum = PrintNumber(3)

printNumIter = iter(printNum)

# prints '1'
print(next(printNumIter))

# prints '2'
print(next(printNumIter))

# prints '3'
print(next(printNumIter))

# raises StopIteration
try:
    print(next(printNumIter))
except StopIteration as e:
    print(f"{repr(e)}\n")



# Example 3: How iter() works for callable objects with sentinel?
with open('mydata.txt', 'r') as f:
    for line in iter(f.readline, ''):
        print(line.strip().upper())
