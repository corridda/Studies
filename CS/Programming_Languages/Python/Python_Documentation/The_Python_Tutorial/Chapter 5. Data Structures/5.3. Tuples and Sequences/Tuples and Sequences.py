# A tuple consists of a number of values separated by commas, for instance:
t = (156, 985, 'Hello!')
print(t)
print('t[0] =', t[0])
print('t[2] =', t[2])

# Tuples may be input with or without surrounding parentheses
t = 156, 985, 'Hello!'
print(t)

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u)

# Tuples are immutable:
try:
    t[0] = 8888
except TypeError as e:
    print(e)

# but they can contain mutable objects:
v = ([1, 2, 3], [4, 5, 6])
print('\nv = ', v)
v[1][0] = 15
print('v = ', v)


# Empty tuples are constructed by an empty pair of parentheses
empty = ()
print('empty =', empty, 'len(empty) = ', len(empty))

# turple with lone element, note trailing comma
lone = ('lone',)
print('lone =', lone, 'len(lone) = ', len(lone))

# this isn't a turple
lone = ('lone')
print('lone =', lone)

# tuple packing
t = (12345, 54321, 'hello!')

# sequence unpacking
x, y, z = t
print('x =', x, 'y =', y, 'z =', z)

# error
try:
    x, y = t
except ValueError as e:
    print(e)

# you can unpack any sequence
list = [10, 11, 12]
x, y, z = list
print('x =', x, 'y =', y, 'z =', z)
