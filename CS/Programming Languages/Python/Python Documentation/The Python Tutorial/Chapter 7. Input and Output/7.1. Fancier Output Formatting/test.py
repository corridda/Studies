import math

s = 'Hello, world.'
print(str(s))

# The repr() of a string adds string quotes and backslashes:
print(repr(s + '\n'))

print(str(1 / 7))
print(repr(1 / 7))

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)

# The argument to repr() may be any Python object:
print(repr((x, y, ('spam', 'eggs'))))
print(repr([1, 2, 3, 4, 5]), '\n')

# a table of squares and cubes
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), repr(x * x * x).rjust(4))
print()
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))

# str.zfill(), which pads a numeric string on the left with zeros. It understands about plus and minus signs:
print('\n'+'12'.zfill(5))
print('-3.14'.zfill(7))
print('3.14159265359'.zfill(5))

#  str.format()
print('\nWe are the {} who say "{}!"'.format('knights', 'Ni'))
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))
print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',other='Georg'))

# '!a' (apply ascii()), '!s' (apply str()) and '!r' (apply repr())
contents = 'eels'
print('My hovercraft is full of {!s}.'.format(contents))
print('My hovercraft is full of {!r}.'.format(contents))

# An optional ':' and format specifier can follow the field name
print('\nThe value of PI is approximately {0:.3f}'.format(math.pi))
print(f'The value of PI is approximately {math.pi:.3f}\n')

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print('{0:10} ==> {1:10}'.format(name, phone))

print('Sjoerd: {0[Sjoerd]:d}; Jack: {0[Jack]:d}; Dcab: {0[Dcab]:d}'.format(table))

# This could also be done by passing the table as keyword arguments with the ‘**’ notation.
print('Sjoerd: {Sjoerd:d}; Jack: {Jack:d}; Dcab: {Dcab:d}'.format(**table))

