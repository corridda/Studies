print((1, 2, 3) < (1, 2, 4))
print([1, 2, 3] == [1, 2, 4])
print('ABC' < 'C' < 'Pascal' < 'python')
print((1, 2, 3, 4) < (1, 2, 4))
print((1, 2) < (1, 2, -1))
print((1, 2, 3) == (1.0, 2.0, 3.0))
print((1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4))

# Comparing objects of different types with < or > is legal provided
# that the objects have appropriate comparison methods.
# Otherwise, rather than providing an arbitrary ordering,
# the interpreter will raise a TypeError exception.
try:
    print('string' < 5)
except TypeError as e:
    print(type(e), e)