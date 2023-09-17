""" tuple([iterable])
    class type(object)
    class type(name, bases, dict)"""
# https://www.programiz.com/python-programming/methods/built-in/tuple

"""Rather than being a function, tuple is actually an immutable sequence type, as documented
in Tuples and Sequence Types — list, tuple, range.

If an iterable is passed, corresponding tuple is created. If the iterable is omitted, empty tuple is created."""


# Example: How to creating tuples using tuple()?

t1 = tuple()
print('t1=', t1)

# creating a tuple from a list
t2 = tuple([1, 4, 6])
print('t2=', t2)

# creating a tuple from a string
t1 = tuple('python')
print('t1=',t1)

# creating a tuple from a dictionary
t1 = tuple({1: 'one', 2: 'two'})
print('t1=',t1)
